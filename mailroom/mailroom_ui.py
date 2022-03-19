#-------------------------------------#
#Title: mailroom_ui.py
#Desc: module for mailroom with menu structure, print and input functions
#Change Log: (Who, When, What)
#KKauffman, 22 Nov 2020, Created File
#KKauffman, 16 December 2020, updated code to work with Donor and DonorCollection classes
#-------------------------------------#


# ----- Data ----- #
import sys

from mailroom import mailroom_logic as ml 

Oprah = ml.Donor('Oprah')
Oprah.add_donation(450)
Oprah.add_donation(1000)

Gaga = ml.Donor('Lady Gaga')
Gaga.add_donation(1200)
Gaga.add_donation(250)
Gaga.add_donation(345)

Bill = ml.Donor('Bill Gates')
Bill.add_donation(500)

donors = (Oprah, Gaga, Bill)

donor_dict_obj = ml.DonorCollection(*donors)

# ----- Processing ----- #
def menu_one():
    '''First menu option code. Adds donors/donations and prints a thank you note.
       Args:
           none
       Returns:
           none
    '''

    while True:
        #ask for donor name or list
        user_input_1 = name_input()
            #User choose list, show donor list
        if user_input_1.lower() == 'list':
            print()
            print(donor_dict_obj.previous_donors())
            break
        else:
            user_input_1 = user_input_1.title()
            #Check if donor name is already on list
            donor_exist = donor_dict_obj.donor_check(user_input_1)
            if donor_exist:
                print('\nGreat! This name is already on the donor list.')
                #Ask for donation amount and add it to the donor object's list of donations
                donation_amnt = donation_input()
                donor_dict_obj.donation_add_only(user_input_1, donation_amnt)
                #Write thank you note
                print(ml.thank_you_note(user_input_1, donation_amnt))
                break
            else:
                print('\nThis is a new donor. Adding to the donor list now.')
                #Ask for donation amount and add it to the donor object's list of donations
                donation_amnt = donation_input()
                donor_dict_obj.donor_donation_add(user_input_1, donation_amnt)
                #Write thank you note
                print(ml.thank_you_note(user_input_1, donation_amnt))
                break


def menu_two():
    '''Second menu option code. Prints a report of all donors and donations.
       Args:
           none
       Returns:
           none
    '''
    report_lst = donor_dict_obj.report_data()
    formatted_lst = donor_dict_obj.create_report(report_lst)
    print_report(formatted_lst)


def menu_three():
    '''Third menu option. Writes a thank you note to all donors to a file.
       Args:
           none
       Returns: 
           none
    '''
    donor_dict_obj.multiple_thanks()
    print('\nYour thank you notes have been written.')
    
def menu_four():
    '''Fourth menu option. Exits the program.
    Args:
        none
    Returns:
        none
    '''
    print("Exiting the program.")
    sys.exit()


#Dictionary for switching between menu option functions
menu_switcher_dict = {1: menu_one, 2: menu_two, 3: menu_three, 4: menu_four}


#main function
def main(menu_switcher_dict):
    '''Main program function. Prints the menu, asks for user's menu option, and calls
       the three menu option functions.
       Args:
           menu_switcher_dict - dictionary that stores the three menu option functions
       Returns:
           none
    '''
    print('\nWelcome to the Mailroom Program!')
    while True:
        print_menu()
        menu_choice = menu_input()
        menu_switcher_dict.get(menu_choice)()


def print_menu():
    ''' Print the mailroom menu (Send a thank you, Show report, quit).
        Args: none
        Returns: none
    '''
    print('\nPlease choose from the following menu:\n')
    print('Mailroom Menu\n\t1: Send a thank you\n\t2: Show Report\n\t3: ' +  
          'Send letter to all donors\n\t4: Quit')
    return None


def menu_input():
    '''takes a user's input for the menu option.
       Args: 
           none
       Returns:
           choice - the user's menu choice
    '''
    while True:
        try:
            choice = int(input('\nPlease enter your menu choice. '))
        except (ValueError):
            print('Can only enter one of the following integers: 1, 2, 3, or 4.')
            continue
        else:
            break
    return choice


def name_input():
    '''takes a user's input for the donor's name.
       Args: 
           none
       Returns:
           user_input - the user's menu choice
    '''
    while True:
        try:
            user_input = input('\nEnter a donor name. Type "list" to see previous donors. ')
            if not user_input:
                raise ValueError
        except ValueError:
            print('Input cannot empty. Try again.')
            continue
        else:
            break
    return user_input


def donation_input():
    '''Asks user for donor's donation amount.
       Args: 
           none
       Returns:
           amount - the amount of the donation
    '''

    while True:
        amount = input('\nEnter how much money the donor contributed. ')
        try:
            amount = float(amount.strip('$'))
        except ValueError:
            print('Please enter a dollar amount in integer form ("$" optional).')
        else:
            if amount < 0:
                print('\nThe donation amount cannot be negative. Please try again.')
            else:
                break
    return amount


def print_report(report_lst):
    '''prints the formatted data in a report
       Args:
           report_lst - list of the formatted data
       Returns: 
           none
    '''
    
    print('\nDonor Name          |  Total Given  | Num Gifts | Average Gift ')
    print('-' * 63)
    for row in report_lst:
        print(row)