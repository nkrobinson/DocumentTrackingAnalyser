#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File View Instance
By Nicholas Robinson
"""

import json
import UserList as ul
import DocList as dl

class FileViewInstance():

	#	Parameters
	#timestamp
	#userID
	#userip
	#userlocation
	#userreferrer

	#subjectype
	#subjectID
	#subjectpage

	#cause

	#timeRead

	def __init__(self, userID, docID, country, time=0):
		self.__user = UserList.GetUser(userID)
		self.__doc = DocList.GetDoc(docID)
		self.__time = time

	@property
	def doc(self):
		return self.__doc

	@property
	def user(self):
		return self.__user
