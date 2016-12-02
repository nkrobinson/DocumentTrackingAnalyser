#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sorter
By Nicholas Robinson
"""

import json
import sys
from user_agents import parse
from collections import Counter

from DataTypes import Document as Doc
from DataTypes import User
from IDDictionary import IDDictionary as Dic

class Sorter(object):

	def __init__(self, filename):
		self.filename = filename
		self.dd = Dic()
		self.ud = Dic()
		self.al = []

	def loadFile(self):
		try:
			file_ = open(self.filename, 'r')
			for line in file_:
				self._sortJson(line)
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		except NameError as e:
			print("Name error({0}): {1}".format(e.errno, e.strerror))
		return (self.dd,self.ud, self.al)

	def _sortJson(self,_json):
		data = json.loads(_json)
		try:
			if (data['event_type'] != "pageread") and (data['event_type'] != "pagereadtime"):
				return

			""" Store Document Information """
			self._docAdd(data)
			doc = self.dd.get(data['subject_doc_id'])

			""" Store User Information """
			self._userAdd(data)
			user = self.ud.get(data['visitor_uuid'])

			""" Store Document Viewing Information """
			if 'event_readtime' in data:
				user.readDoc(doc, data['event_readtime'])
			else:
				user.readDoc(doc)
			doc.userRead(user)
			doc.countryRead(data['visitor_country'])

			""" Store User Agent Information """
			self.al.append(data['visitor_useragent'])
		except KeyError:
			print(_json)
			print("Bad JSON")
			sys.exit(1)

	def _docAdd(self, jsondata):
		doc = Doc(jsondata['subject_doc_id'])
		self.dd.add(doc)

	def _userAdd(self, jsondata):
		user = User(jsondata['visitor_uuid'])
		self.ud.add(user)

	def readerNumberSort(self, docTimeList):
		returnlist = [doc[0] for doc in docTimeList]
		returnlist = Counter(returnlist).most_common(10)
		return returnlist

	def readerProfileSort(self, docTimeListFull):
		dicDocs = {}
		for doc in docTimeListFull:
			if not doc[0] in dicDocs:
				dicDocs[doc[0]] = doc[1]
			else:
				dicDocs[doc[0]] += doc[1]
		returnlist = []
		for doc in dicDocs:
			returnlist.append((doc, dicDocs[doc]))
		returnlist.sort(key=lambda tup: tup[1], reverse=True)
		return returnlist
