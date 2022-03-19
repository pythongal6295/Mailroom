#-------------------------------------#
#Title: mailroom_logic.py
#Desc: module for mailroom with logic functions
#Change Log: (Who, When, What)
#KKauffman, 22 Nov 2020, Created File
#KKauffman, 12 Dec 2020, created Donor and Donor Collections classes with init, str, and repr methods
#KKauffman, 13 Dec 2020, added more properties to Donor and methods to DonorCollection that work with 
#                        donor data (i.e. adding new donors/donations, creating a list of donors)
#KKauffman, 14 Dec 2020, added methods in DonorCollection that format and sort donor data
#KKauffman, 16 Dec 2020, added a method that formats thank yous for all donors and saves the data to a file
#-------------------------------------#

#initialize donor objects in mailroom_ui
class Donor:
    '''
    class for a single donor
    '''
    
    def __init__(self, name):
        '''
        initializer for Donor class
        '''
        self._name = name
        self._donations = []
    
    
    def __str__(self):
        '''
        string method for Donor class
        '''
        return f'Donor object: includes donor name ({self._name}) and list of donations ({self._donations})'
    
    
    def __repr__(self):
        '''
        repr method for Donor class
        '''
        return f'Donor object: {self._name}'
    
    
    def add_donation(self, donation_amt):
        '''
        method to add a donation to the list of donations
        Parameters:
            donation_amt - the donor's donation
        Returns:
            None
        '''
        self._donations.append(donation_amt)


    @property
    def sum_donations(self):
        '''
        computes the sum of all the donor's donations
        '''
        return round(float(sum(self._donations)), 2)


    @property
    def num_donations(self):
        '''
        computes the number of the donor's donations
        '''
        return len(self._donations)


    @property
    def avrg_donation(self):
        '''
        computes the average of all the donor's donations
        '''
        return round((self.sum_donations / self.num_donations), 2)


class DonorCollection:
    '''
    class for a dictionary of multiple donors
    '''
    
    def __init__(self, *donors):
        '''
        initializer for DonorCollection class
        '''
        self._donors = {obj._name: obj for obj in donors}


    def __str__(self):
        '''
        string method for Donor class
        '''
        return 'Donor dictionary'


    def __repr__(self):
        '''
        repr method for Donor class
        '''
        return 'Collection of donation objects'


    def previous_donors(self):
        '''Prints a list of previous donors.
           Args:           
               none
           Returns: 
               just_donors - list of only donors
        '''
        print('Previous donors:\n') #maybe move to the main loop
        just_donors = []
        for key in self._donors:
            just_donors.append(key)
        return just_donors


    def donor_check(self, name):
        '''Checks to see if the inputted donor is already in the donor dictionary.
           Args:
               name - the name of the donor the user entered
           Returns:
               True - if donor is already in dictionary
               False - if donor was not previously in the dictionary
        '''
        if name in self._donors:
            return True
        else:
            return False
    
    
    def donation_add_only(self, name, amount):
        '''Adds a new donation amount to the donor object's list of donations. 
           Donor object is already added to DonorCollection dictionary.
           Args: 
               name - the name of the donor the user entered
               amount - the amount of the donation
           Returns: 
               none
        '''
        donor = self._donors[name]
        donor.add_donation(amount)
            
            
    def donor_donation_add(self, name, amount):
        '''Adds a new donor name and donation amount to the DonorCollection dict.
           If donor is already in dictionary, then just the donation is added.
           Args: 
               name - the name of the donor the user entered
               amount - the amount of the donation
           Returns: 
               none
        '''
        new_donor = Donor(name)
        new_donor.add_donation(amount)
        self._donors[new_donor._name] = new_donor


    def report_data(self):
        '''Creates a new list with the donors' names and the total donated, number of donations,
           and average of donations.
           Args:
           Returns:          
              report_lst - list with donor names, total donated, number of donations,
              and average of donations
        '''
        report_lst = []
        for name in self._donors:
            donor_obj = self._donors[name]
            print(type(donor_obj))
            report_tpl = (name, donor_obj.sum_donations, donor_obj.num_donations, donor_obj.avrg_donation)
            report_lst.append(report_tpl)
        return report_lst


    def sort_key(self, item):
        '''Creates and return a key that will be used to sort the list of donors and their donation info
           Args:
                item - each tuple in the list of donors and their donation info (sum, number, average)
           Return:
                item[1] - the total donation amount in each tuple
        '''
        return item[1]


    def create_report(self, donor_lst):
        '''formats the rows in the report with the sum, number of donations, and average
           Args:
               donor_lst = list of donors and the calculated data for those donors
           Returns:
               report_lst - list of the formated data
        '''
        report_lst = []
        for donor_info in sorted(donor_lst, key=self.sort_key, reverse = True):
          report_row = ('{:<20}| ${:>13.2f}| {:>10d}| ${:>11.2f}'.format(*donor_info))
          report_lst.append(report_row)
        return report_lst


    def multiple_thanks(self):
        '''
        Writes a thank you note to all donors to a file.
        Args:
            none
        Returns:
            none
        '''
        for name, donor_obj in self._donors.items():
            last_donation = donor_obj._donations[len(donor_obj._donations)-1]
            name_together = name.replace(' ', '')
            note = thank_you_note(name, last_donation)
            file_name = f'{name_together}.txt'
            with open(file_name, 'w') as ty_file:
                ty_file.write(note)
                ty_file.close()


def thank_you_note(name, amount):
    '''A thank you note that includes the name of the donor and how much they donated
       Args: 
           name - name of donor
           amount - the donor's donation amount
       Returns: 
           note_string = thank you note string
    '''

    note_string = ('''
          Dear {:s},

          Thank you for your generous donation of ${:.2f}. We could not
          reach our goal without donors like you.

          Sincerely,

          Learners of Python Foundation'''.format(name.title(), amount))

    return note_string

