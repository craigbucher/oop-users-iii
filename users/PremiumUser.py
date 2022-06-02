# Your PremiumUser class goes here
from .User import User

class PremiumUser(User):
    def __init__(self, name, email, dl_number):
        super().__init__(name, email, dl_number)