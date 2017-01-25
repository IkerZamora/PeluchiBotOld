# -*- coding: utf-8 -*-

from datetime import datetime

EE = 'EE'
AE = 'AE'
GE = 'GE'

# Next encounter dates
next_ee_date = datetime(2017, 7, 21, 16, 0)
next_ae_date = datetime(2016, 10, 6, 16, 0)
next_ge_date = datetime(2016, 4, 14, 16, 0)

# First encounter years
first_ee_year = 1993  
first_ge_year = 2007
first_ae_year = 2014

class Encounter:

    def __init__(self, acronym):
        self.acronym = acronym
        if self.acronym == EE:
            self.date = next_ee_date
	    self.edition = self.date.year - first_ee_year + 1
        elif self.acronym == AE:
	    self.date = next_ae_date
	    self.edition = self.date.year - first_ae_year + 1
        elif self.acronym == GE:
	    self.date = next_ge_date
	    self.edition = self.date.year - first_ge_year + 1


    def time_left(self):
        '''
        Return: days, hours, minutes and seconds
                remaining for the next LAN party
        '''
        now = datetime.now()
        td = self.date - now
        days = td.days
        hours = td.seconds // 3600
        minutes = (td.seconds // 60) % 60
        seconds = (td.seconds % 3600) % 60
        return days, hours, minutes, seconds
