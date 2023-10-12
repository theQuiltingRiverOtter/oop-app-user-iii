from users.User import User


class FreeUser(User):
    def __init__(
        self, name: str, age: int, email: str = None, phone_number: str = None
    ):
        super().__init__(name, age, email, phone_number)

    def add_post(self, post):
        if len(self._user_posts) < 2:
            User.post_id += 1
            self._user_posts.append({"post_id": User.post_id, "text": post})
            User.all_user_posts[User.post_id] = post
        else:
            print("You need to upgrade")


if __name__ == "__main__":
    print(__name__)
