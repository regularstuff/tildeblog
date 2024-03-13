from django.test import TestCase
from django.test.client import RequestFactory, Client

from til.models import Learned


class TagLandingPage(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.client = Client()

    def test_landing_page_uses_correct_template(self):
        expected_template = "til/landing.html"
        c = self.client
        response = c.get(path="/", follow=True)
        self.assertTemplateUsed(response=response, template_name=expected_template)

    def test_headline_in_response(self):
        """
        If we add a headline to website we can see it in context of landing page
        """
        item = Learned.objects.create(
            title="xxfooxx", tldr="read_tldr_foo", content="foo_content"
        )
        response = self.client.get(path="/til", follow=True)
        self.assertInHTML("xxfooxx", response.content.decode("utf-8"))

        def test_headline_shows_in_response_when_emtpy_search(self):
            """
            Searching for an empty tag should render the page as if no tag were pased
            """
            item = Learned.objects.create(
                title="xxfooxx", tldr="read_tldr_foo", content="foo_content"
            )
            response = self.client.get(path="/til/show_tagged/", follow=True)
            self.assertInHTML("xxfooxx", response.content.decode("utf-8"))
