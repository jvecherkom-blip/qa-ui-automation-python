from framework.api.clients.posts_client import PostsClient


class PostsService:
    def __init__(self):
        self.client = PostsClient()

    def get_posts(self):
        response = self.client.get_posts()
        return response.json()

    def create_post(self, data):
        response = self.client.create_post(data)
        return response