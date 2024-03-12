from django.test import TestCase

from til.tag_utils import TagHelper


class TagTests(TestCase):
    def test_split_tags_gives_empty_list(self):
        helper = TagHelper(delim=",")
        self.assertEqual([], helper.split_tags(""))
        self.assertEqual([], helper.split_tags(" "))
        self.assertEqual([], helper.split_tags(", ,"))
        self.assertEqual([], helper.split_tags(", "))
        helper = TagHelper(delim="/")
        self.assertEqual([], helper.split_tags(""))
        self.assertEqual([], helper.split_tags("/"))
        self.assertEqual([], helper.split_tags("/ /"))
        self.assertEqual([], helper.split_tags("/ "))

    def test_returns_tags(self):
        helper = TagHelper(delim=",")
        result = helper.split_tags("One,Two")
        self.assertSetEqual(set(["one", "two"]), set(result))

    def test_not_dupe_tags(self):
        helper = TagHelper(delim=";")
        result = helper.split_tags("Guns; guns;butter;guns; butter;;")
        expected = set(["guns", "butter"])
        self.assertSetEqual(set(result), expected)
        self.assertEqual(len(result), len(expected))

    def test_misc_tags(self):
        helper = TagHelper(delim="-")
        result = helper.split_tags("-git")
        self.assertEqual(1, len(result))
        self.assertEqual("git", result[0])
        result = helper.split_tags("-git-")
        self.assertEqual(1, len(result))
        self.assertEqual("git", result[0])
        result = helper.split_tags("-Git-Got")
        self.assertEqual(2, len(result))
        self.assertIn("git", result)
        self.assertIn("got", result)

    def test_get_same_tag_twice_gets_same_id(self):
        helper = TagHelper(delim=",")
        result_foo = helper.get_new_or_existing_tag_id("foo")
        self.assertGreater(result_foo, 0)
        result_bar = helper.get_new_or_existing_tag_id("bar")
        self.assertNotEquals(result_foo, result_bar)
        result_foo_2 = helper.get_new_or_existing_tag_id("foo")
        self.assertEqual(result_foo, result_foo_2)

    def test_tags_as_delimited_string(self):
        helper = TagHelper(delim=",")
        from til.models import Learned

        learnt = Learned.objects.create(title="foo", tldr="foo", content="foo")
        # add tags to an object
        helper.set_tags_on_learnt("foo, fee, sup", learnt.id)
        # create the control list
        tags = helper.split_tags("foo, fee, sup")
        # get the list under test
        tags_from_learnt = helper.split_tags(helper.tags_as_delim_string(learnt.id))
        self.assertSetEqual(set(tags), set(tags_from_learnt))
