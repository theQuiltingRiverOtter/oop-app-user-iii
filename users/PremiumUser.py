# Your PremiumUser class goes here
from users.User import User


class PremiumUser(User):
    def __init__(
        self, name: str, age: int, email: str = None, phone_number: str = None
    ):
        super().__init__(name, age, email, phone_number)
