#!/usr/bin/env python3
"""
MAIL ROOM PART 4
this script has a data structure that holds a list of  donors and a history of the amounts they have donated. 
This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
 data structure stored in the global namespace.
The script prompts the user (you) to choose from a menu of 3 actions: 
        "1 - Send a Thank You to a single donor.",
        "2 - Create a Report.",
        "3 - Send letters to all donors.",
   or   "4 - Quit".
"""

from operator import itemgetter
import sys  # imports go at the top of the file

#initial donations amount and givers names.
donor_list = {
    "Jan Balard": [600.00,250.00],
    "Joe McHennry": [1500.00,1500.00],
    "Scott Newman": [100.00,5000.00],
    "Rabi Das": [500.00,950.00],
    "Jeff Hansen": [600.0, 2, 300]
    }
# main menue prompt
def main_menu():
    print("\n".join(("Welcome to the MailRoom!",
        "Please Choose an action:",
        "1 - Send a Thank You to a single donor.",
        "2 - Create a Report.",
        "3 - Send letters to all donors.",
        "4 - Quit",
        ">>> ")))
    return input()


def get_amount(fullname):
    try:    
    # Prompt for the amount
        amount = input("please enter donation amounts : \n >>")
        amount = int(amount)
        #break
        add_amount(fullname,amount) 
    except ValueError:
        print("please enter an Integer Number...")
    return amount


def add_amount(fullname,amount):
    #add the integer number to the list
    donor_list[fullname].append(amount)


def prompt_name():
    #prompt for the donor name or return all names if list is requested
    try:
        fullname = input("please enter full name : ")
        if fullname == 'list':
            for key in donor_list:
                print(key)
            prompt_name()
        elif fullname == "": # if no name entered
            raise TypeError
        else:
            add_name(fullname)
    except TypeError:
            print("\nenter a name please\n>>>")
    return fullname

def add_name(fullname):
    #add the names to the list or just update it
    for donor in donor_list:
        if fullname == donor:
            break
    else:
        donor_list[fullname] = []


def thank_you_text(fullname,amount):
    #thank you letter text format
    print ("\n\nDear {}:\n Thank you for your donation of ${:2d}, we appriciate your support to our service. \n MailRoom Team\n".format(fullname,amount))

#thank you Email formating
def thank_you_email():
    fullname = prompt_name()
    amount = get_amount(fullname)
    thank_you_text(fullname, amount)
    main()


#create a report that calculate Donor Name, Total Given, Number of donatons, and the avarage amount of thier donations
def create_report():
    report = []
    print("\n{:<18}{:<6}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)
    for donor, value in sorted(donor_list.items(), key=lambda elem: sum(elem[1]), reverse=True):
        if len(value) != 0:
            report.append((donor, round(sum(value),2), len(value),round(sum(value)/len(value))))
            print ("{:<20} {:>2} {:>12} {:>17}{:>17}{:>12}".format(*(donor, '$', round(sum(value),2)), len(value), '$',round(sum(value)/len(value),1)))
    print (report)
    return report


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

#send letter to all givers
def letter_to_all():
    for name , value in donor_list.items():
        amount = str(value[-1:])
        filename = name.replace(' ', '_').replace(',', '') + ".txt"
        filename = filename.lower()
        filetext = "Dear {},\n\tThank you for your very kind donation of ${}\n\tIt will be put to very good use.\n\t\t\tSincerely,\n\t\t\t- The Team".format(name,amount)
        with open(filename,'w+') as output:
            output.write(filetext)
            print("\nLetters {} have been printed and are saved in the current directory".format(filename))


def main():
    #dict with the user options and the functions
    options = {
        '1': thank_you_email,
        '2': create_report,
        '3': letter_to_all,
        '4': exit_program
    }
    while True:
        #if response in options:
        try:
            response = main_menu()
            options[response]()
            #menu_function()
        except KeyError:
            print("\n'{}'  is not a valid answer, please select option from 1-4 !. \n >> ".format(response))


if __name__ == "__main__":
   main()