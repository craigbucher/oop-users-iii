# Your User class goes here
from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime
import re

@dataclass
class Post:
    _id: str = field(default_factory=lambda: uuid4().hex)
    created_at: datetime = field(default_factory=datetime.now)
    content: str = ""

@dataclass
class User:
    name: str
    email: str
    dl_number: str
    posts: dict[str, Post] = field(default_factory=dict)

    def create_post(self, content):
        post = Post(content=content)
        self.posts[post._id] = post

    def delete_post(self, post_id):
        del self.posts[post_id]

    def update_post(self, post_id, content):
        self.posts[post_id].content = content

    def get_posts(self):
        return self.posts.values()

    def get_post(self, post_id):
        return self.posts[post_id]

    def find_posts_with_string(self, string):
        for post in self.posts.values():
            if string in post.content:
                yield post

    def find_posts_matching_regex(self, regex):
        for post in self.posts.values():
            if regex.search(post.content):
                yield post