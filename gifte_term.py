#!/usr/bin/env python3
import getpass, gifte_core

def get_credentials():
    email = input("Which email are you sending from?: ")
    password = getpass.getpass("Enter your email password: ")
    return email, password

def main():
    config = input("Where would you like to pull your configuration from?: ")
    title, people = load_preferences(config)
    gifting = gift_designation(people)
    
    send_emails(gifting, title)

if __name__ == "__main__":
    main()
