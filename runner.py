# Import and create your users here
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
import re

#################################
def main():
    print("Creating new user John")
    user = PremiumUser(name="John", email="john@gmail.com", dl_number="123456789")

    print("\nAdding a few posts")
    user.create_post("Hello, World!")
    user.create_post("Goodbye, World!")
    user.create_post("Goodbye, Heaven!")

    print("\nGetting all posts")
    print(user.get_posts())

    print("\nGetting all posts with string 'World'")
    for post in user.find_posts_with_string("World"):
        print(post)

    print("\nGetting all posts matching regex '^Goodbye'")
    for post in user.find_posts_matching_regex(regex=re.compile("^Goodbye")):
        print(post)

    print("\nDeleting the first post with the string 'Goodbye'")
    user.delete_post(next(iter(user.get_posts()))._id)

    print("\nGetting all posts")
    print(user.get_posts())

    print("Creating new free user John")
    user = FreeUser(name="John", email="john@gmail.com", dl_number="123456789")

    print("\nAdding a few posts")
    user.create_post("Hello, World!")
    user.create_post("Goodbye, World!")
    user.create_post("Goodbye, Heaven!")

if __name__ == '__main__':
    main()