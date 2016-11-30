#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document
By Nicholas Robinson
"""

class Document():

	#	Parameters
	#ID

	def __init__(self,id):
		self.id = id
		self.usersRead = []
		self.countriesRead = []

	def userRead(self,user):
		if not (user in usersRead):
			self.usersRead.append(user)

	def countryRead(self, country):
		self.countriesRead.append(country)
