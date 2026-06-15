from .base_client import BaseClient


class PostsClient(BaseClient):

    def get_posts(self):
        return self.get("/posts")

    def create_post(self, data):
        return self.post("/posts", data)