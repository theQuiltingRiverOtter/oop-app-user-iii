from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.User import User
import pytest


@pytest.fixture
def premium_user():
    megan = PremiumUser("Megan", 38, "thequiltingriverotter@gmail.com", "123-456-7890")
    megan.add_post("This is a great app")
    megan.add_post("Code Platoon is the best bootcamp")
    megan.add_post("Hi there")
    megan.add_post("Coding is fun")
    return megan


def test_PremiumUser_getters(premium_user):
    assert premium_user.name == "Megan"
    assert premium_user.age == 38
    assert premium_user.email == "thequiltingriverotter@gmail.com"
    assert premium_user.phone_number == "123-456-7890"


def test_PremiumUser_posts(premium_user):
    assert len(premium_user.get_posts) == 4


def test_FreeUser():
    john = FreeUser("John", 25, "fakeemail@gmail.com", "978-456-1231")
    john.add_post("Hi")
    john.add_post("There")
    john.add_post("Can't post")
    john.add_post("because I'm cheap")
    assert len(john.get_posts) == 2
