#------------------------------------------#
# Title: mailroom_main.py
# Desc: main script for mailroom package
# Change Log: (Who, When, What)
# KKauffman, 2 Nov 2020, Created File, wrote psuedocode, added functions for thank you note menu choice
# KKauffman, 4 Nov 2020, added more function to thank you note menu choice, 
# KKauffman, 4 Nov 2020, added all functions to second menu choice
# KKauffman, 7 Nov 2020, added exception for all user inputs
# KKauffman, 8 Nov 2020, refactored some functions in first menu option
# KKauffman, 11 Nov 2020, refactored more first and second menu functions
# KKauffman, 15 Nove 2020 refactored so functions returned and used donor tuples instead of donor_lst
# KKauffman, 16 Nov 2020 added switch dictionary
# KKauffman, 17 Nov 2020 updated formatting, docstrings, and removed thank you note printing function
# KKauffman, 21 Nov 2020 added new menu option to write thank you for all donors
# KKauffman, 22 Nov 2020 broke up mailroom into logic/ui modules, put everything into "mailroom" package
# KKauffman, 16 Dec 2020 took out donor_dict as an argument to work with new class structure in mailroom_logic.py
#------------------------------------------#


from mailroom import mailroom_ui as mu

def main():
    mu.main(mu.menu_switcher_dict)

if __name__ == '__main__':

    main()

    



