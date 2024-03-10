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

    def test_gets_a_tag(self):
        helper = TagHelper(delim=",")
        result = helper.get_new_or_existing_tag_id("foo")
        self.assertGreater(result, 0)
