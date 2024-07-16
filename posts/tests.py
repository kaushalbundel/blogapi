from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        testuser1 = User.objects.create_user(username="test_user", password="123456")
        testuser1.save()

        test_post = Post.objects.create(
            author=testuser1, title="Blog_Title", body="Body Content ..."
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "test_user")
        self.assertEqual(title, "Blog_Title")
        self.assertEqual(body, "Body Content ...")
