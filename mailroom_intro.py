#------------------------------------------#
# Title: mailroom.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# KKauffman, 2 Nov 2020, Created File, wrote psuedocode, added functions for thank you note menu choice
# KKauffman, 4 Nov 2020, added more function to thank you note menu choice, 
# KKauffman, 4 Nov 2020, added all functions to second menu choice
#------------------------------------------#
# ----- Data ----- #

donors = [("Oprah", [70432.60, 16700.00]), ("Tom Hanks", [50555.50, 13999.99, 44200.00]), ("Wallace Kauffman", [250.00, 412.00, 175.00]), 
    ("Cameron James", [0.34]), ("Lady Gaga", [127000.12])]

# ----- Processing ----- #
#main function
def main(donor_lst):
    print('Welcome to the Mailroom Program!')
    while True:
        print_menu()
        menu_choice = int(input('\nPlease enter your menu choice. '))
        #Menu choice 1 is send a thank you
        if menu_choice == 1:
            while True:
                #ask for donor name or list
                user_input_1 = (input('\nEnter a donor name. Type "list" to see previous donors. ')).title()
                #User choose list, show donor list
                if user_input_1 == 'list':
                    print()
                    print(previous_donors(donor_lst))
                else:
                    #Check if donor name is already on list, if not add it
                    donor_name = donor_check(donor_lst, user_input_1)
                    if donor_name:
                        print('\nGreat! This name is already on the donor list.')
                        donor_info = donor_index(donor_lst, user_input_1)
                        donor_name, donor_indx = donor_info
                        #Ask for donation amount and add it to the main donor/donation list
                        donation_amnt = input('\nEnter how much money the donor contributed. ')
                        donation_add(donor_lst, donation_amnt, donor_indx)
                        thank_you_note(user_input_1, donation_amnt)
                        break
                    elif donor_name == None:
                        print('\nThis is a new name. Adding to the donor list now.')
                        donor_lst = donor_add(donor_lst, user_input_1)
                        #Ask for donation amount and add it to the main donor/donation list
                        donation_amnt = input('\nEnter how much money the donor contributed. ')
                        donation_add(donor_lst, donation_amnt)
                        thank_you_note(user_input_1, donation_amnt)
                        break
            
        elif menu_choice == 2:
            report_lst = report_data(donor_lst)
            sort_donations_report(report_lst)
            
        elif menu_choice == 3:
            break
        else:
            "Error"


#function to show menu (Send a thank you, Show report, quit)
def print_menu():
    ''' Print the mailroom menu.
        Args: none
        Returns: none
    '''
    print('\nPlease choose from the following menu:\n')
    print(''''Mailroom Menu\n\t1: Send a thank you\n\t2: Show Report\n\t3: Quit''')
    return None


#function to show current list of donors when user types 'list'. 
def previous_donors(lst):
    '''Prints a list of previous donors.
       Args:           
           lst - list of donors and donations
       Returns: 
           just_donors - list of only donors
    '''
    just_donors = []
    for item in lst:
        just_donors.append(item[0])
    return just_donors


#function to check if name is already in donor list
def donor_check(lst, input):
    '''Check if a donor's name is already on the donor/donation list.
       Args: 
           lst - list of donors
           input - the name of the donor the user entered
       Returns: input
    '''
    for tpl in lst:
        if input in tpl:
            return input
        else:
            None


#function to return the index of name on the donor list
def donor_index (lst, input):
    '''Determines the index of a donor's name in the donor/donation list
       Args:            
           lst - list of donors
           input - the name of the donor the user entered
       Returns: the input and the index of the input
    '''
    for idx, item in enumerate(lst):
        if input in item:
            return input, idx
        #return the input and the index of the input
        else: None
        

#function to add name to list of donors
def donor_add(lst, input):
    '''Adds a new donor name to the donor list.
       Args: 
           lst - list of donors and donations
           input - the name of the donor the user entered
       Returns: 
           new_lst - list of donors with the new donor added
    '''
    new_donor_tpl = (input, [])
    lst.append(new_donor_tpl)
    return lst
    

#function to add integer amount of donation to list of donors
def donation_add (lst, amount, indx = -1):

    '''Adds a donor's donation to the donor/donation list.
       Args: 
           lst - list of donors and donations
           amount - the amount of the donation
           indx - the index of the name of the donor; if the donor
                  was not already on the list then the index is -1
       Returns:
           lst - the updated list of donors/donations with the newest donation
    '''
    #can override the index if it is not the last entry in the donor/donation list
    amount = float(amount.strip('$'))
    name, donation = lst[indx]
    donation.append(amount)
    return lst


#function to write a thank you


def thank_you_note(name, amount):
    '''A thank you note that includes the name of the donor and how much they donated
       Args: 
           name - name of donor
           amount - the donor's donation amount
       Returns: none
    '''
    amount = float(amount.strip('$'))
    print('''
          Dear {:s},

          Thank you for your generous donation of ${:.2f}. We could not
          reach our goal without donors like you.

          Sincerely,

          Learners of Python Foundation'''.format(name, amount))
    print()
    return None

#function to create list of donors, total donated, number of donations, average of donations


def report_data(lst):
    '''Creates a new list with the donors names and the total donated, number of donations,
       and average of donations.
       Args:
          lst - list of donors and their donations
       Returns:          
          report_lst - list with donor names, total donated, number of donations,
          and average of donations
    '''
    report_lst = []
    for tpl in lst:
        name = tpl[0]
        sum_donations = sum(tpl[1])
        num_donations = len(tpl[1])
        avrg_donation = (sum_donations / num_donations)
        donor_tpl = (name, sum_donations, num_donations, avrg_donation)
        report_lst.append(donor_tpl)
    return report_lst


#function to create a sort key
def sort_key(item):
    '''Creates and return a key that will be used to sort the list of donors and their donation info
       Args:
            item - each tuple in the list of donors and their donation info (sum, number, average)
       Return:
            item[1] - the total donation amount in each tuple
    '''
    return item[1]

#function to sort the list of donors by total donated
def sort_donations_report(lst):
    '''Sorts the list with donors and their donation data by total donations.
       This sorted donation list is printed nicely in a report.
       Args:
            lst - the list of donors and their donation data
            sortkey - the sort key to sort the list by total donations
       Returns: none
    '''

    report_data_sorted = sorted(lst, key=sort_key, reverse = True)
    #print(report_data_sorted)
    print('\nDonor Name          |  Total Given  | Num Gifts | Average Gift ')
    print('-' * 63)
    for tpl in report_data_sorted:
      print('{:<20}| ${:>13.2f}| {:>10d}| ${:>11.2f}'.format(*tpl))
    return None

# ----- Input ----#

if __name__ == '__main__':

    main(donors)



