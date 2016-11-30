#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Analyser
By Nicholas Robinson
"""

from DataTypes import Document as Doc
from DataTypes import User as User
from List import ListContainer as List

from collections import Counter

class DocAnalyser():

	def __init__(self, dl, ul):
		self.dl = dl
		self.ul = ul

	"""
	Task 2a
	"""
	def docCountries(self, docID):
		if self.dl.contains(docID):
			doc = self.dl.get(docID)
			return Counter(doc.getCountries()).most_common()
		else:
			return []

	"""
	Task 2b
	"""
	"""
	def docContinents(self, docID):
		if self.dl.contains(docID):
			doc = self.dl.get(docID)
			return Counter(doc.getCountries()).most_common()
		else:
			return []
	"""

	"""
	Task 4
	"""
	def topTenReaders(self):
		topten = []
		for user in self.ul:
			if len(topten) < 10 or user.docTotalTime > topten[0][1]:
				topten.append((user,user.docTotalTime))
			topten.sort(key=lambda tup: tup[1], reverse=True)
		return [user[0] for user in topten]

	"""
	Task 5a
	"""
	def docReaders(self, docID):
		doc = self.dl.get(docID)
		return doc.usersRead

	"""
	Task 5b
	"""
	def readDocs(self, userID):
		user = self.ul.get(userID)
		return user.getDocs()

	"""
	Task 5d & 5e
	Parameters
		docID
		sortingFun
			Input tuple list of (Document, Time)
			Output Document list
		userID

	Output
		List of sorted documents
	"""
	def alsoLiked(self, docID, sortingFun="readerNum", userID=None):
		totalUsers = self.docReaders(docID)

		if not (userID is None):
			if sortingFun == "readerNum":
				doclist = []
				""" Get list of all documents read by similar users """
				for user in totalUsers:
					if user.id == userID: # Remove searching user from temp user list
						continue
					for doc in user.getDocs():
						if doc.id == docID:
							doclist = doclist + user.getDocs()
							break

				""" Sort list into most frequent doc items """
				counterlist =  Counter(doclist).most_common(10)
				doclist = []
				""" Edit list of sorted top documents to only save doc """
				for doc in counterlist:
					doclist.append(doc[0])
				return doclist

			if sortingFun == "readerProfile":
				totalDocs = self.readDocs(userID)
				users = []
				docTimeListFull = []
				for user in totalUsers:
					if user.id == userID: # Remove searching user from temp user list
						continue
					for doc in user.getDocs():
						if doc[0].id == docID:
							docTimeListFull += user.getDocTimes()

				docTimeList = []
				for doctime in docTimeListFull:
					"""templist = (x[0] for x in docTimeList)""" #TO DO GENERATOR
					templist = [x[0] for x in docTimeList]
					if not (doctime[0] in templist):
						docTimeList.append(doctime)
					else:
						for item in docTimeList:
							if item[0] == doctime[0]:
								item[1] += doctime[1]
				docTimeList.sort(key=lambda tup: tup[1], reverse=True)
				return docTimeList[:10]


			if sortingFun == "closestReader":
				totalDocs = self.readDocs(userID)
				users = []
				for user in totalUsers:
					if user.id == userID: # Remove searching user from temp user list
						continue
					for doc in user.getDocs():
						if doc.id == docID:
							users.append(user)

				userFitnessList = []
				for user in users:
					sameDocs = 0
					for doc in totalDocs:
						if doc in user.docsRead:
							sameDocs += 1
					userFitnessList.append((user,sameDocs))
				userFitnessList.sort(key=lambda tup: tup[1], reverse=True)

				docslist = []
				index = 0
				while len(docslist) < 10:
					for doc in userFitnessList[index][0].docsRead:
						if not (doc in totalDocs):
							docslist.append(doc)
					index += 1
				return docslist[:10]

		else:
			if sortingFun == "closestReader":
				totalDocs = self.readDocs(userID)
				users = []
				for user in totalUsers:
					for doc in user.getDocs():
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
				doclist.remove(self.dl.get(docID))
				return doclist
			else:
				print("ERROR")
				return []
