from .User import User, Post

class FreeUser(User):
    def __init__(self, name, email, dl_number):
        super().__init__(name, email, dl_number)
        
    def create_post(self, content):
        if len(self.posts) >= 2:
            raise ValueError('Free users may only post twice')
        post = Post(content=content)
        self.posts[post._id] = post