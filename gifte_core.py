#!/usr/bin/env python3
import random, smtplib
from collections import namedtuple

Person = namedtuple('Person', 'name email likes dislikes')
EMAIL_MESSAGE = "Your TITLE is NAME.\nThey like LIKES.\nThey dislike DISLIKES."

# Email Sending Function
def send_email(to, subject, text, credentials, port=587):
    server = smtplib.SMTP(infer_server_url(credentials[0]), port)
    server.ehlo()
    server.starttls()
    server.login(credentials[0], credentials[1])

    BODY = '\r\n'.join(['To: ' + to,
                        'From: ' + credentials[0],
                        'Subject: ' + subject,
                        '', text])

    try:
        server.sendmail(email, [to], BODY)
        print('email sent to ' + to)
    except BaseException as e:
        print('error sending mail')
        print(e)

    server.quit()
    
def infer_server_url(email):
    email_domain = email.split('@')[1]
    return "smtp." + email_domain

def load_preferences(filename):
    title = ""
    people = [ ]
    NUM_PREFS = 4
    # Open needed file
    config_file = open(filename)
    num_line = 0 # readlines  line positions
    lines = [line[:-1] for line in config_file.readlines()] # Truncate newlines
    config_file.close() # We're done with the file
    
    title = lines[0]
    for num_line in range(1, len(lines), NUM_PREFS): # Loop through lines
        people.append(Person(lines[num_line], lines[num_line + 1],
                            lines[num_line+2], lines[num_line + 3]))
    return title, people

def gift_designation(people):
    gifter = None
    giftee = None
    
    gifting = { }
    
    while len(gifting) < len(people): # While people will still give gifts
        gifter = random.choice(people)
        if gifter not in gifting.keys(): # Gifter hasn't sent yet
            giftee = gifter
            while giftee == gifter or giftee not in gifting.values(): # No duplicates
                giftee = random.choice(names)
        gifting[gifter] = giftee
    
def send_emails(gifting, title, credentials):
    subject = "Welcome to " + title
    for gifter in gifting.keys():
        giftee = gifting[gifter]
        send_email(gifter.email, subject, personalize_message(title, giftee),
            credentials)
        
def personalize_message(title, person):
    message = EMAIL_MESSAGE.replace("TITLE", title)
    message = message.replace("NAME", person.name)
    message = message.replace("LIKES", person.likes)
    message = message.replace("DISLIKES", person.dislikes)
    return message
