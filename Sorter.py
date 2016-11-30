#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sorter
By Nicholas Robinson
"""

import json
import sys

from DataTypes import Document as Doc
from DataTypes import User
from List import ListContainer as List

class Sorter(object):

	def __init__(self, filename="data/issuu_cw2.json"):
		self.filename = filename
		self.dl = List()
		self.ul = List()

	def loadFile(self):
		file_ = open(self.filename, 'r')
		for line in file_:
			#print(line)
			self._sortJson(line)
		return (self.dl,self.ul)

	def _sortJson(self,_json):
		data = json.loads(_json)
		try:
			if (data['event_type'] != "pageread") and (data['event_type'] != "pagereadtime"):
				return

			if not (self.ul.contains(data['subject_doc_id'])):
				self._docAdd(data)
			doc = self.dl.get(data['subject_doc_id'])

			if not (self.ul.contains(data['visitor_uuid'])):
				self._userAdd(data)
			user = self.ul.get(data['visitor_uuid'])

			if 'event_readtime' in data:
				user.readDoc(doc, data['event_readtime'])
			else:
				user.readDoc(doc)
			doc.userRead(user)
			doc.countryRead(data['visitor_country'])
		except KeyError:
			print(_json)
			print("Bad JSON")
			#sys.exit(1)

	def _docAdd(self, jsondata):
		doc = Doc(jsondata['subject_doc_id'])
		self.dl.add(doc)

	def _userAdd(self, jsondata):
		user = User(jsondata['visitor_uuid'])
		self.ul.add(user)
