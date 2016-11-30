#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
User
By Nicholas Robinson
"""

class User(object):

	def __init__(self,id,username):
		self.id = id
		self.docsRead = []
		self.docTotalTime = 0

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

	def readDoc(self, doc, time=0):
		if not (doc in docsRead):
			self.docsRead.append(doc, time)
		self.docTotalTime += time

	def getDocs(self):
		return [doc[0] for doc in self.docsRead]

	def getDocTimes(self):
		return self.docsRead
