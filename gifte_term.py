#!/usr/bin/env python3
import getpass, gifte_core

def get_credentials():
    email = input("Which email are you sending from?: ")
    password = getpass.getpass("Enter your email password: ")
    return [ email, password ]

def main():
    config = input("Where would you like to pull your configuration from?: ")
    title, people = gifte_core.load_preferences(config)
    gift_core.send_emails(gifte_core.gift_designation(people), title, get_credentials())

if __name__ == "__main__":
    main()
