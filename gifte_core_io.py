import smtplib
from email.message import EmailMessage
EMAIL_PORT = 587

## Email ##

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

## Preferences Config ##

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

def write_config_file(config_name, title, people_info):
    config_file = open(config_name, 'w')
    config_file.write(title)
    config_file.writelines(people_info)
    config_file.close()

