from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.User import User
import pytest


@pytest.fixture
def premium_user():
    megan = PremiumUser("Megan", 38, "thequiltingriverotter@gmail.com", "123-456-7890")
    return megan


def test_PremiumUser_getters(premium_user):
    assert premium_user.name == "Megan"
    assert premium_user.age == 38
    assert premium_user.email == "thequiltingriverotter@gmail.com"
    assert premium_user.phone_number == "123-456-7890"


def test_PremiumUser_setters(premium_user):
    premium_user.name = "Meg"
    premium_user.age = 39
    with pytest.raises(ValueError) as error:
        premium_user.email = "mishadoll48gmail.com"
    assert str(error.value) == "email must include an @ symbol"
    with pytest.raises(ValueError) as error2:
        premium_user.phone_number = "1234-456-7890"
    assert str(error2.value) == "Phone number should be 10 digits long"
    assert premium_user.name == "Meg"
    assert premium_user.age == 39
    assert premium_user.email == "thequiltingriverotter@gmail.com"
    assert premium_user.phone_number == "123-456-7890"


@pytest.fixture
def premium_user_posts():
    john = PremiumUser("John", 22)
    john.add_post("This is a great app")
    john.add_post("Code Platoon is the best bootcamp")
    john.add_post("Hi there")
    john.add_post("Coding is fun")
    return john


def test_PremiumUser_posts(premium_user_posts):
    assert len(premium_user_posts.get_posts) == 4
    assert premium_user_posts.get_posts == [
        {"post_id": 1, "text": "This is a great app"},
        {"post_id": 2, "text": "Code Platoon is the best bootcamp"},
        {"post_id": 3, "text": "Hi there"},
        {"post_id": 4, "text": "Coding is fun"},
    ]
    assert len(User.all_user_posts) == 4
    assert User.all_user_posts == {
        1: "This is a great app",
        2: "Code Platoon is the best bootcamp",
        3: "Hi there",
        4: "Coding is fun",
    }


def test_PremiumUser_delete_post(monkeypatch):
    sam = PremiumUser("Sam", 25)
    sam.add_post("I am Sam")
    sam.add_post("Sam I am")
    sam.add_post("I do not like green eggs and ham")
    sam.add_post("I do not like them Sam I am")
    monkeypatch.setattr("builtins.input", lambda _: "6")
    sam.delete_post()
    assert len(sam.get_posts) == 3
    assert sam.get_posts == [
        {"post_id": 5, "text": "I am Sam"},
        {"post_id": 7, "text": "I do not like green eggs and ham"},
        {"post_id": 8, "text": "I do not like them Sam I am"},
    ]
    assert len(User.all_user_posts) == 7
    assert User.all_user_posts == {
        1: "This is a great app",
        2: "Code Platoon is the best bootcamp",
        3: "Hi there",
        4: "Coding is fun",
        5: "I am Sam",
        7: "I do not like green eggs and ham",
        8: "I do not like them Sam I am",
    }


def test_FreeUser_post_without_delete(monkeypatch):
    jane = FreeUser("John", 25, "fakeemail@gmail.com", "978-456-1231")
    jane.add_post("Hi")
    jane.add_post("There")
    inputs = iter(["n", "n"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    jane.add_post("I can't post")
    jane.add_post("because I'm cheap")
    assert len(jane.get_posts) == 2


def test_FreeUser_post_with_delete(monkeypatch):
    mary = FreeUser("Mary", 30)
    mary.add_post("I'm a little teapot")
    mary.add_post("short and stout")
    inputs = iter(["y", "11", "y", "12"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    mary.add_post("Here is my handle")
    mary.add_post("Here is my spout")
    assert len(mary.get_posts) == 2
    assert mary.get_posts == [
        {"post_id": 13, "text": "Here is my handle"},
        {"post_id": 14, "text": "Here is my spout"},
    ]
    assert len(User.all_user_posts) == 11
    assert User.all_user_posts == {
        1: "This is a great app",
        2: "Code Platoon is the best bootcamp",
        3: "Hi there",
        4: "Coding is fun",
        5: "I am Sam",
        7: "I do not like green eggs and ham",
        8: "I do not like them Sam I am",
        9: "Hi",
        10: "There",
        13: "Here is my handle",
        14: "Here is my spout",
    }
