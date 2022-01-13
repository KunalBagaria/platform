import random


def get_random_avatar():
    base_url = "https://res.cloudinary.com/f22/image/upload/v1638256420/NodeAir/"
    options = ("1a", "2a", "3a", "4a", "5a")
    return base_url + random.choice(options) + ".png"

def get_random_banner():
    base_url = "https://res.cloudinary.com/f22/image/upload/v1638256420/NodeAir/"
    options = ("1b", "2b", "3b", "4b", "5b")
    return base_url + random.choice(options) + ".png"