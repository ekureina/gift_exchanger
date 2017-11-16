#!/usr/bin/env python3
import random, logging
from collections import namedtuple
from email.message import EmailMessage

Person = namedtuple('Person', 'name pronoun email likes dislikes')
EMAIL_MESSAGE = "Your {title} is {name}.\n{pronoun} like {likes}.\n{pronoun} dislike {dislikes}."
NUM_PREFS = 5

logging.basicConfig(level=logging.INFO)

def gift_designation(people):
    gifter = None
    giftee = None
    
    gifting = { }
    while len(gifting) < len(people): # While people will still give gifts
        gifter = random.choice(people)
        if gifter not in gifting.keys(): # Gifter hasn't sent yet
            giftee = gifter
            while giftee == gifter or giftee in gifting.values(): # No duplicates
                giftee = random.choice(people)
        gifting[gifter] = giftee
    logging.info("Gifts designated.")
    return gifting
    
def personalize_message(title, giftee):
    return EMAIL_MESSAGE.format(title = title, name = giftee.name,
        pronoun = giftee.pronoun, likes = giftee.likes, dislikes = giftee.dislikes)
        
if __name__ == "__main__": # Testing functions work
    people = [ ]
    title = "Testing"
    print(infer_server_url("jdoe@gmail.com"))
    print(infer_server_url("jdoe@example.com"))
    people.append(Person("John Doe", "He", "jdoe@example.com", "Penguins", "Windows"))
    people.append(Person("Edith Example", "She", "eexample@example.com", "Dogs", "Cats"))
    people.append(Person("Ed Morrison", "They", "emorrison@example.com", "Othello", "Iago"))
    for person in people:
        print(personalize_message(title, person))
    print(gift_designation(people))
