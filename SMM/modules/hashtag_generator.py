import random
from data.captions import *

def generate_hashtags(mood):

    if mood == "happy":
        tags = random.sample(happy_tags, 3)

    elif mood == "sad":
        tags = random.sample(sad_tags, 3)

    elif mood == "travel":
        tags = random.sample(travel_tags, 3)

    else:
        tags = random.sample(motivation_tags, 3)

    return " ".join(tags)