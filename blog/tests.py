from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
# Create your tests here.

from .models import Post

class PostTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testerman", email="tester@email.com", password="password"
        )

        self.post = Post.objects.create(
            title="test title",
            slug="test",
            author=self.user,
            content="test content",
            created_on = timezone.now(),
            status = 1
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), 'test title')

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "test title")
        self.assertEqual(f"{self.post.slug}", "test")
        self.assertEqual(f"{self.post.author}", self.user.email)
        self.assertEqual(f"{self.post.content}", "test content")

    # def test_post_list_view(self):
    #     response = self.client.get(reverse("blog_post_list_view"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "test title")
        # self.assertTemplateUsed(response, "blog/post-list-view.html")

    # def test_post_detail_view(self):
    #     response = self.client.get(reverse("blog_post_detail_view", args="1"))
    #     no_response = self.client.get("/100000/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "testerman")
    #     self.assertTemplateUsed(response, "blog/post-detail-view.html")
    #
    # def test_post_create_view(self):
    #     response = self.client.post(
    #         reverse("blog_post_create_view"),
    #         {
    #             "title": "test title",
    #             "content": "test content",
    #             "author": self.user.id,
    #         }, follow=True
    #     )
    #
    #     self.assertRedirects(response, reverse("blog_post_detail_view", args="2"))
    #     self.assertContains(response, "test title")
    #
    # def test_post_update_view_redirect(self):
    #     response = self.client.post(
    #         reverse("blog_post_update_view", args="1"),
    #         {"title": "Updated title", "content": "new content", "author":self.user.id}
    #     )
    #     self.assertRedirects(response, reverse("blog_post_detail_view", args="1"))
    #
    # def test_post_delete_view(self):
    #     response = self.client.get(reverse("blog_post_delete_view", args="1"))
    #     self.assertEqual(response.status_code, 200)