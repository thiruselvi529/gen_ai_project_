import random
from data.captions import *

def generate_caption(mood):

    if mood == "happy":
        return random.choice(happy_captions)

    elif mood == "sad":
        return random.choice(sad_captions)

    elif mood == "travel":
        return random.choice(travel_captions)

    else:
        return random.choice(motivational_captions)