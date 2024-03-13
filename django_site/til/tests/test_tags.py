from django.test import TestCase, RequestFactory

from til.tag_utils import TagHelper

from til.views import landing_page

from til.models import Learned


class TagTests(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

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
        self.assertEqual([], helper.split_tags(None))

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

    def test_get_learned_items_with_a_tag(self):
        helper = TagHelper(delim=",")
        from til.models import Learned

        first_obj_feefoosup = Learned.objects.create(
            title="foo", tldr="foo", content="foo"
        )
        helper.set_tags_on_learnt("foo, fee, sup", first_obj_feefoosup.id)
        second_obj_feefoo = Learned.objects.create(
            title="foo", tldr="foo", content="foo"
        )
        helper.set_tags_on_learnt("foo, fee", second_obj_feefoo.id)
        matches = helper.get_learnt_items_with_tag("foo")
        self.assertTrue(matches.contains(first_obj_feefoosup))
        self.assertTrue(
            matches.contains(first_obj_feefoosup)
            and matches.contains(second_obj_feefoo)
        )
        matches = helper.get_learnt_items_with_tag("sup")
        self.assertTrue(matches.contains(first_obj_feefoosup))
        self.assertFalse(matches.contains(second_obj_feefoo))
        self.assertEqual(1, len(matches))
        matches = helper.get_learnt_items_with_tag("NOMATCH_UN1T_T3$T")
        self.assertEqual(0, len(matches))

    def test_get_multi_hit_fuzzy_returns_distincting_learned_items(self):
        """
        If you search for 'ex' and an item has tag 'exact'  and 'sexy'
        the item should only appear in the results one time
        """
        helper = TagHelper(delim=",")
        from til.models import Learned

        first_obj_feefoosup = Learned.objects.create(
            title="foo", tldr="foo", content="foo"
        )
        helper.set_tags_on_learnt("food, catfood", first_obj_feefoosup.id)
        matches = helper.get_fuzzy_learnt_items_by_tag("foo")
        self.assertTrue(matches.contains(first_obj_feefoosup))
        self.assertEqual(1, len(matches))

    def test_landingpage_view_contains_filtered_flag(self):
        helper = TagHelper(delim=",")
        earth_water_obj = Learned.objects.create(
            title="titleEarthWater", tldr="foo", content="foo"
        )
        air_fireobj = Learned.objects.create(
            title="titleAirFire", tldr="foo", content="foo"
        )
        helper.set_tags_on_learnt("earth, water", earth_water_obj.id)
        helper.set_tags_on_learnt("air, Fire,", air_fireobj.id)
        request = self.request_factory.get("/")
        match_earth = "ear"
        match_fire = "fir"
        match_water = "er"
        result = landing_page(request, tagstring=match_fire)
        self.assertContains(result, "titleAirFire")
        self.assertNotContains(result, "titleEarthWater")
        result = landing_page(request, tagstring=match_earth)
        self.assertNotContains(result, "titleAirFire")
        self.assertContains(result, "titleEarthWater")
