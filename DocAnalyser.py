#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Instance List
By Nicholas Robinson
"""

import Document
import User
import DocList
import UserList

from collections import Counter

class Sorter():

	def __init__(self, dl, ul):
		self.dl = dl
		self.ul = ul

	"""
	Task 4
	"""
	def topTenReaders(self):
		topten = []
		for user in ul:
			if len(topten) < 10 or user.docTotalTime > topten[0]:
				topten.append(user)
			topten.sort()
		return topten

	"""
	Task 2a
	"""
	def docCountries(self, docID):
		doc = dl.contains(docID)
		return Counter(doc.countriesRead).most_common()

"""
	def docContinents(self, docID):
		doc = dl.contains(docID)
		return doc.countriesRead
"""


	"""
	Task 5a
	"""
	def docReaders(self, docID):
		doc = dl.get(docID)
		return doc.usersRead

	"""
	Task 5b
	"""
	def readDocs(self, userID):
		user = ul.get(userID)
		return user.docsRead

	"""
	Task 5d & 5e
	"""
	def alsoLiked(self, docID, userID=None, sortingFun="readerNum"):
		totalUsers = self.docReaders(docID)

		if not (userID is None):
			if sortingFun == "readerNum":
				doclist = []
				for user in totalUsers:
					for doc in user.docsRead
						if doc.id == docID:
							doclist = doclist + user.docsRead

				counterlist =  Counter(doclist).most_common(11) #docID still in sorted list
				doclist = []
				for doc in counterlist:
					if not (doc[0].id == docID):
						doclist.append(doc[0])
				return doclist

			if sortingFun == "readerProfile":
				totalDocs = self.readDocs(userID)
				users = []
				for user in totalUsers:
					for doc in user.docsRead
						if doc.id == docID:
							users.append(user)

				userFitnessList = []
				for user in users:
					sameDocs = 0
					for doc in totalDocs:
						if doc in user.readDocs:
							sameDocs = sameDocs + 1
					userFitnessList.append((user,sameDocs))
				userFitnessList.sort(key=lambda tup: tup[1], reverse=True)
				"""
				TO DO
					Use userFitnessList to return list of other documents
					that user has not read
				"""
		else:
			if sortingFun == "readerProfile":
				totalDocs = self.readDocs(userID)
				users = []
				for user in totalUsers:
					for doc in user.docsRead
						if doc.id == docID:
							users.append(user)

				userFitnessList = []
				for user in users:
					sameDocs = 0
					for doc in totalDocs:
						if doc in user.readDocs:
							sameDocs = sameDocs + 1
					userFitnessList.append((user,sameDocs))
				userFitnessList.sort(key=lambda tup: tup[1], reverse=True)
				doclist = userFitnessList[0][0].docsRead
				doclist.remove(dl.get(docID))
				return doclist
			else:
				print("ERROR")
				return []
