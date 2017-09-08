#!/usr/bin/env python3
import getpass, gifte_core, argparse

def main():
    args = parse_args()
    config = args.config if args.config \
        else input("Where would you like to pull your configuration from?: ")
    if config != "":
        title, people = gifte_core.load_preferences(config)
    else:
        title, people = manual_config()
    gifte_core.send_emails(gifte_core.gift_designation(people), title, get_credentials(args))
    
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Specify the configuration file to be used")
    parser.add_argument("-e", "--email", help="Specify the email to send from")
    parser.add_argument("-p", "--password", help="Specify the password of the email")
    return parser.parse_args()
    
def get_credentials(args):
    email = args.email if args.email \
        else input("Which email are you sending from?: ")
    password = args.password if args.password \
        else getpass.getpass("Enter your email password: ")
    return [ email, password ]

def manual_config():
    title = input("What is the title of your exchange?: ")
    people = [ ]
    for i in range(0, int(input("How many people are participating?: "))):
        person_details = input("Enter the person's Information: Name Pronoun Email Likes Dislikes ").split()
        people.append(gifte_core.Person(person_details[0], person_details[1], person_details[2],
            person_details[3], person_details[4]))
    return title, people

if __name__ == "__main__":
    main()
