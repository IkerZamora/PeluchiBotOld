# -*- coding: utf-8 -*-

from datetime import datetime

EE = 'EE'
AE = 'AE'
GE = 'GE'


class Encounter:

    def __init__(self, date, acronym, edition):
        self.date = date
        self.acronym = acronym
        self.edition = edition

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
