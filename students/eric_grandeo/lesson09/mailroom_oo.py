#!/usr/bin/env python3

#class donor
#class report(sub of donor?)
#class thank_you(sub of donor?)

#hold all information about a single donor, including thank you letter, donation and donation history
class Donor():
    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName
        self.donations = []

    
    def add_donation(self, donation):
        self.donations.append(int(donation))  
        
    



    def thank_you():
        pass



#hold all of the donor objects, method to add a new donor, search for a donor, 
#save and reload data, generate reports
class DonorCollection:
    pass


