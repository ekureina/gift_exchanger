#!/usr/bin/env python3
import smtplib, logging
from email.message import EmailMessage
EMAIL_PORT = 587

###########
#  EMAIL  #
###########

def _send_email(recipient: str, sender: str, subject: str, text: str, server: smtplib.SMTP) -> None:
    message = EmailMessage()
    message.set_content(text)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient
    server.send_message(message)
    logging.info('Sent email to ' + recipient)

def infer_server_url(email_address: str) -> str:
    email_domain = email_address.split('@')[1]
    return 'smtp.' + email_domain

def send_emails(gifting: dict, title: str, credentials: [str, str]) -> None:
    subject = 'Welcome to ' + title
    # Login to our SMTP server
    server = smtplib.SMTP(infer_server_url(credentials[0]), EMAIL_PORT)
    server.starttls()
    server.login(credentials[0], credentials[1])
    logging.info('Started email connection')
    for gifter in gifting.keys():
        giftee = gifting[gifter]
        _send_email(gifter.email, credentials[0], subject, personalize_message(title, giftee), server)
        
    logging.info('Finished sending emails')
    # Logout from the SMTP server when done with emails
    server.quit()

def create_message(exchanger_name: str, person: dict) -> str:
    message = f'Your {exchanger_name} is {person[\'name\']}
    for attribute in person.keys():
        if attribute not in ('name', 'email', 'pronoun'):
            message += f'{person[\'pronoun\']} {attribute} is/are {person[{attribute}]}.\n'

    return message

###################
#  CONFIGURATION  #
###################

def load_preferences(filename: str) -> [dict]:
    logging.info('Loading Preferences')
    # Open needed file
    config_file = open(filename)
    configuration_json = json.loads(config_file.read())
    
    logging.info('Preferences Loaded')
    return configuration

def write_config_file(config_name: str, exchanges: [dict]) -> None:
    config_file = None
    json_string = json.dumps(exchanges)
    
    try:
        config_file = open(config_name, 'w')
        config_file.write(json_string)
        
    finally:
        if config_file != None:
            config_file.close()

