#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sorter
By Nicholas Robinson
"""

import json
import Document as doc
import DocList
import UserList

class Sorter():

	def __init__(self, filename="data/issuu_cw2.json"):
		self.filename = filename
		self.dl = DocList()
		self.ul = UserList()

	def loadFile(self):
        file_ = open(self.filename, 'r')
        for line in file_:
            self._sortJson(line)
		return (self.ul,self.dl)

	def _sortJson(self,_json):
		data = json.load(_json)
		try:
			if (data['visitor_uuid'] != "pageread") and (data['visitor_uuid'] != "pagereadtime"):
				return

			if not (ul.contains(data['subject_doc_id'])):
				self._docAdd(_json)
			doc = self.dl.get(data['subject_doc_id'])

			if not (ul.contains(data['visitor_uuid'])):
				self._userAdd(_json)
			user = self.ul.get(data['visitor_uuid'])

			if 'event_readtime' in data:
				user.readDoc(doc, data['event_readtime'])
			else:
				user.readDoc(doc)
			doc.userRead(user)
			doc.countryRead(data['visitor_country'])
		except KeyError:
			print("Bad JSON")

	def _docAdd(self, _json):
		docData = [data['subject_doc_id']]
		self.dl.add(docData)

	def _userAdd(self, _json):
		userData = [data['visitor_uuid'], data['username'], data[]]
		self.ul.add(userData)
