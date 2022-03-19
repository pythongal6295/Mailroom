#-------------------------------------#
#Title: <test_mailroom_dict.py
#Desc: tests the mailroom program
#Change Log: (Who, When, What)
#KKauffman, 8 Nov 2020, Created File
#KKauffman, 9 Nov 2020, Added tests for first menu option functions
#KKauffman, 11 Nove 2020, Added tests for second menu option functions
#KKauffman, 17 Nov 2020, Added tests for donor_check and previous_donors, 
#                        updated data to feature a dictionary of donors/donations
#KKauffman, 12 Dec 2020, Added tests for init methods for Donor and Donor Collections classes
#KKauffman, 13 Dec 2020, Added tests for str and repr methods for both classes
#KKauffman, 14 Dec 2020, Added tests for methods that add new donations/donors, 
#                        Check for previous donors, make a list of new donors
#kKauffman, 16 Dec 2020, Added tests for creating a report of donor data
#-------------------------------------#

from mailroom import mailroom_logic as ml


def get_donor_collection_obj():
    '''
    creates a DonorCollection object to use in testing methods
    '''
    d1 = ml.Donor('Tasha')
    d1.add_donation(300)
    d1.add_donation(900)

    d2 = ml.Donor('Eric')
    d2.add_donation(4000)
    
    d3 = ml.Donor('Danny')
    d3.add_donation(1050)

    d4 = ml.Donor('Bill')
    d4.add_donation(45)
    d4.add_donation(20)

    donor_tpl = (d1, d2, d3, d4)

    collection = ml.DonorCollection(*donor_tpl)

    return collection


def test_init_donor():
    '''
    test to ensure name attribute can be accessed
    '''
    d = ml.Donor('Jeff')
    
    assert d._name == 'Jeff'

def test_str_donor():
    '''
    test to check string representation for __str__ of a Donor object
    '''
    d = ml.Donor('Matt')
    d.add_donation(900)

    assert str(d) == 'Donor object: includes donor name (Matt) and list of donations ([900])'


def test_repr_donor():
    '''
    test to check string representation for __repr__ of a Donor object
    '''
    d = ml.Donor('Matt')

    assert repr(d) == 'Donor object: Matt'


def test_add_donation():
    '''
    checks a donation amount is added to the donation list
    '''
    d = ml.Donor('Jeff')
    d.add_donation(200)

    assert d._donations[-1] == 200 


def test_sum_donations():
    '''
    checks the sum of the donor's donations are totaled correctly
    '''
    d = ml.Donor('Jeff')
    d.add_donation(200)
    d.add_donation(400)
    d.add_donation(550)

    assert d.sum_donations == 1150


def test_num_donations():
    '''
    checks the number of donations are counted correctly
    '''
    d = ml.Donor('Jeff')
    d.add_donation(200)
    d.add_donation(400)
    d.add_donation(550)
    
    assert d.num_donations == 3


def test_avrg_donation():
    '''
    checks the average of the donor's donations are calculated correctly
    '''
    d = ml.Donor('Jeff')
    d.add_donation(200)
    d.add_donation(400)
    d.add_donation(550)

    assert d.avrg_donation == 383.33


def test_init_donorcollection():
    '''
    checks a tuple of donors gets turned into a dictionary of donor objects
    '''
    d = ml.Donor('Julie')
    d.add_donation(300)
    
    dict_compare = {d._name: d}
    
    donors_tpl = (d)
    collection = ml.DonorCollection(donors_tpl)

    assert collection._donors == dict_compare


def test_str_donorcollection():
    '''
    test to check string representation for __str__ of a Donor Collection object
    '''
    collection = get_donor_collection_obj()

    assert str(collection) == 'Donor dictionary'


def test_repr_donorcollection():
    '''
    test to check string representation for __repr__ of a Donor Collection object
    '''
    collection = get_donor_collection_obj()

    assert repr(collection) == 'Collection of donation objects'


def test_previous_donors():
    '''
    tests a list of previous donors is created from the keys in the dictionary of donors
    '''
    collection = get_donor_collection_obj()

    assert collection.previous_donors() == ['Tasha', 'Eric', 'Danny', 'Bill']


def test_donor_check_yesdonor():
    '''
    test that a inputted donor name already in the DonorCollection dictionary can 
    actually be found in the DonorCollection dictionary
    '''
    collection = get_donor_collection_obj()

    assert collection.donor_check('Bill') == True


def test_donor_check_nodonor():
    '''
    test that an inputted donor name not in the dictionary is not found in 
    the DonorCollection dictionary
    '''
    collection = get_donor_collection_obj()

    assert collection.donor_check('Cameron') == False


def test_donation_add_only():
    '''
    test that a new donation is added to an existing donor object
    '''
    collection = get_donor_collection_obj()
    collection.donation_add_only('Eric', 12)
    
    d = collection._donors['Eric']
    
    assert d._donations[-1] == 12 


def test_donor_donation_add():
    '''
    tests a new donor object is created and donation amounts are added 
    '''
    collection = get_donor_collection_obj()
    collection.donor_donation_add('Wallace', 110)

    assert 'Wallace' in collection._donors


def test_report_data():
    '''
    tests a list of tuples with the data for the report is created. 
    A tuple is created for each object with the name of the donor,
    sum of donations, number of donations, and the average of the donations
    '''
    collection = get_donor_collection_obj()
    
    report_data = collection.report_data()
    
    assert report_data == [('Tasha', 1200, 2, 600), ('Eric', 4000, 1, 4000), 
                           ('Danny', 1050, 1, 1050), ('Bill', 65, 2, 32.5)]


def test_create_report():
    '''
    tests that the report is correctly formatted and has the right data
    '''
    collection = get_donor_collection_obj()
    
    report_data = collection.report_data()
    report_rows = collection.create_report(report_data)
    assert report_rows[0] == 'Eric                | $      4000.00|          1| $    4000.00'

