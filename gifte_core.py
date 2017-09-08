#!/usr/bin/env python3
import random, smtplib, logging
from collections import namedtuple
from email.message import EmailMessage

Person = namedtuple('Person', 'name pronoun email likes dislikes')
EMAIL_MESSAGE = "Your {title} is {name}.\n{pronoun} like {likes}.\n{pronoun} dislike {dislikes}."
EMAIL_PORT = 587
NUM_PREFS = 5

logging.basicConfig(level=logging.INFO)

# Email Sending Function
def send_email(recipient, sender, subject, text, server):
    message = EmailMessage()
    message.set_content(text)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient
    server.send_message(message)
    logging.info("Sent email to " + recipient)
    
def infer_server_url(email):
    email_domain = email.split('@')[1]
    return "smtp." + email_domain

def load_preferences(filename):
    logging.info("Loading Preferences")
    title = ""
    people = [ ]
    # Open needed file
    config_file = open(filename)
    num_line = 0 # readlines  line positions
    lines = [line[:-1] for line in config_file.readlines()] # Truncate newlines
    config_file.close() # We're done with the file
    
    title = lines[0]
    for num_line in range(1, len(lines), NUM_PREFS): # Loop through lines
        people.append(Person(lines[num_line], lines[num_line + 1],
                            lines[num_line+2], lines[num_line + 3],
                            lines[num_line + 4]))
    logging.info("Preferences Loaded")
    return title, people

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
    
def send_emails(gifting, title, credentials):
    subject = "Welcome to " + title
    # Login to our SMTP server
    server = smtplib.SMTP(infer_server_url(credentials[0]), EMAIL_PORT)
    server.starttls()
    server.login(credentials[0], credentials[1])
    logging.info("Started email connection")
    for gifter in gifting.keys():
        giftee = gifting[gifter]
        send_email(gifter.email, credentials[0], subject, personalize_message(title, giftee), server)
        
    # Logout from the SMTP server when done with emails
    logging.info("Finished sending emails")
    server.quit()
    
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
