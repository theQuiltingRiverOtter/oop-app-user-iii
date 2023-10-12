# Import and create your users here

from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.User import User

if __name__ == "__main__":
    megan = PremiumUser("Megan", 38, "thequiltingriverotter@gmail.com", "123-456-7890")
    john = FreeUser("John", 25, "fakeemail@gmail.com", "978-456-1231")
    bob = FreeUser("Bob", 50)

    megan.add_post("This is a great app")
    megan.add_post("Code Platoon is the best bootcamp")
    megan.add_post("Hi there")
    megan.add_post("Coding is fun")
    megan.view_posts()
    print()
    john.add_post("Hi")
    john.add_post("There")
    john.view_posts()
    john.add_post("Can't post")
    john.add_post("because I'm cheap")

    john.view_posts()
