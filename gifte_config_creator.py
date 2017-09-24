#!/usr/bin/env python3
from gifte_core_io import write_config_file

def main():
    write_config_file(get_config_name(), get_title(),
        get_people_info())
    
def get_title():
    return input("What is the name of your exchange?: ") + "\n"

def get_config_name():
    return input("What would you like to name your config file?: ")

def get_people_info():
    people_info = [ ]
    for x in range(0, int(input("How many People are in your exchange?: "))):
        people_info.append(input("What is the person's name?: ") + "\n")
        people_info.append(input("What is the person's pronoun?: ") + "\n")
        people_info.append(input("What is the person's email?: ") + "\n")
        people_info.append(input("What is the person's likes?: ") + "\n")
        people_info.append(input("What is the person's dislikes?: ") + "\n")
    return people_info
    
if __name__ == "__main__":
    main()
