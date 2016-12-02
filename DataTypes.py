#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Data Types
By Nicholas Robinson

This file holds classes of each data type that can be held in the ID Dictionary Class.
"""

"""
ID Object
By Nicholas Robinson
"""

class IDObject(object):

	def __init__(self,id):
		self.id = id

"""
User
By Nicholas Robinson
"""

class User(IDObject):

	def __init__(self,id):
		IDObject.__init__(self,id)
		self.docsRead = {}
		self.docTotalTime = 0

	def readDoc(self, doc, time=0):
		if not doc in self.docsRead:
			self.docsRead[doc] = time
		else:
			self.docsRead[doc] += time
		self.docTotalTime += time

	def getDocs(self):
		return [self.docsRead[doc] for doc in self.docsRead]

	def getDocTimes(self):
		return self.docsRead


"""
Document
By Nicholas Robinson
"""

class Document(IDObject):

	def __init__(self,id):
		IDObject.__init__(self,id)
		self.usersRead = []
		self.countriesRead = []

	def userRead(self,user):
		if not (user in self.usersRead):
			self.usersRead.append(user)

	def countryRead(self, country):
		self.countriesRead.append(country)

	def getReaders(self):
		return self.usersRead

	def getCountries(self):
		return self.countriesRead
