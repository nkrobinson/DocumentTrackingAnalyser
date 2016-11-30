#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
User
By Nicholas Robinson
"""

class User(object):

	def __init__(self,id):
		self.id = id
		self.docsRead = []
		self.docTotalTime = 0

	"""
	def __lt__(self, other):
		return self.docTotalTime < other.docTotalTime

	def __le__(self, other):
		return self.docTotalTime <= other.docTotalTime

	def __eq__(self, other):
		return self.docTotalTime == other.docTotalTime

	def __ne__(self, other):
		return self.docTotalTime != other.docTotalTime

	def __gt__(self, other):
		return self.docTotalTime > other.docTotalTime

	def __ge__(self, other):
		return self.docTotalTime >= other.docTotalTime
	"""

	def readDoc(self, doc, time=0):
		if not (doc in self.docsRead):
			self.docsRead.append((doc, time))
		self.docTotalTime += time

	def getDocs(self):
		return [doc[0] for doc in self.docsRead]

	def getDocTimes(self):
		return self.docsRead


"""
Document
By Nicholas Robinson
"""

class Document():

	def __init__(self,id):
		self.id = id
		self.usersRead = []
		self.countriesRead = []

	def userRead(self,user):
		if not (user in self.usersRead):
			self.usersRead.append(user)

	def countryRead(self, country):
		self.countriesRead.append(country)

	def getCountries(self):
		return self.countriesRead
