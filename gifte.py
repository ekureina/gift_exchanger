#!/usr/bin/env python3
import random, smtplib, getpass

# Email Sending Function
def send_email(to, subject, text, email, password, server='smtp.gmail.com', port=587):
        server = smtplib.SMTP(server, port)
        server.ehlo()
        server.starttls()
        server.login(email, password)

        BODY = '\r\n'.join(['To: ' + to,
                            'From: ' + email,
                            'Subject: ' + subject,
                            '', text])

        try:
            server.sendmail(email, [to], BODY)
            print('email sent to ' + gifter)
        except BaseException as e:
            print('error sending mail')
            print(e)

        server.quit()

# Set up needed variables
title = ""
gifter = ""
sender = ""
# Email values
names = []
senders = {}
recievers = []
likes = {}
dislikes = {}
gift = {} # Who gifts to who?
# Open the file we read from
config_file = open("geconf.txt")
num_line = 0 # readlines  line positions
lines = config_file.readlines()
config_file.close() # We're done with the file
for line in lines: # Loop through lines
    if num_line == 0: # First line is title
        title = line
    elif (num_line % 4)  == 1: # First lines are names
        names.append(line)
        recievers.append(line)
    elif (num_line % 4) == 2: # Second lines are emails
        senders[names[int((num_line-2)/4)]] = line
    elif (num_line % 4) == 3: # Third lines are likes
        likes[names[int((num_line-3)/4)]] = line
    elif (num_line % 4) == 0: # Fourth lines are dislikes
        dislikes[names[int((num_line-4)/4)]] = line
    num_line += 1 # Increment counter of line

# Set Subject
subject = 'Welcome to ' + title

# Get email and password
email = input("Which email are you sending from?: ")
password = getpass.getpass("Enter your email password: ")

while len(senders) > 0: # While people will still give gifts
    gifter = random.choice(names)
    if gifter in senders: # Gifter hasn't sent yet
        giftee = gifter
        while giftee == gifter or giftee not in recievers: # Gifter can't gift themselves and giftee can't get two gifts
            giftee = random.choice(names)
        # Start emailing
        to = senders[gifter] # Send email to gifter
        text = 'Your gift exchange recipiant is ' + giftee + \
            '\nAnd they like ' + likes[giftee] + \
            '\nAnd dislike ' + dislikes[giftee]
        send_email(to, subject, text, email, password)
        
        # Remove people from search
        del senders[gifter]
        recievers.remove(giftee)
