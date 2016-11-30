#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Tracker
By Nicholas Robinson
"""

import Sorter
import userList
import DocList
import DocAnalyser

class DocTracker():

	def __init__(self, filename="data/issuu_cw2.json"):
		self.filename = filename
		self.s = Sorter()
		self.loadData()

	def loadData(filename):
		listSet = s.loadFile(filename)
		self.ul = listSet[0]
		self.dl = listSet[1]

	def argumentHandler(self):
		"""
		TO DO
		Argument Handling
		"""
		return
