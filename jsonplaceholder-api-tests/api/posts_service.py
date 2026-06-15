import requests
from framework.api.posts.posts_client import PostsClient
from framework.config.config import BASE_URL

class PostsService:
    def __init__(self):
        self.client = PostsClient()

    def get_posts(self):
        response = self.client.get_posts()
        return requests.get(f"{BASE_URL}/posts")

    def create_post(self, data):
        response = self.client.create_post(data)
        return response