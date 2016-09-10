# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

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
		Return: days, hours, minutes and seconds remaining for the given date
		'''
		now = datetime.now()
		td = self.date - now
		return td.days, td.seconds//3600, (td.seconds//60)%60, (td.seconds%3600)%60