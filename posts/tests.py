from django.test import TestCase

# Create your tests here.

from .models import Post

from django.urls import reverse


class Postmodeltest(TestCase):
    def setUp(self):
        Post.objects.create(text = "just a test of boni's code")

    def test_text_contenx(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, "just a test of boni's code")




class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)


    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
