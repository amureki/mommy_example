from django.test import TestCase
from model_mommy import mommy

from app.models import Post


class PostTest(TestCase):
    def setUp(self):
        self.post = mommy.make('app.Post')

    def test_something(self):
        print(self.post)
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), self.post.title)
