#!/usr/bin/env python3
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

def write_config_file(config_name, title, people_info):
    config_file = open(config_name, 'w')
    config_file.write(title)
    config_file.writelines(people_info)
    config_file.close()
    
if __name__ == "__main__":
    main()
