#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Tracker
By Nicholas Robinson
"""

from Sorter import Sorter
from List import ListContainer as List
from DocAnalyser import DocAnalyser

class DocTracker():

	def __init__(self, filename="data/issuu_cw2.json"):
		self.filename = filename
		self.s = Sorter()
		self.loadData()

	def loadData(self):
		listSet = self.s.loadFile()
		self.dl = listSet[0]
		self.ul = listSet[1]
		self.al = listSet[2]

	def loadAnalyser(self):
		self.da = DocAnalyser(self.dl, self.ul, self.al)

	def argumentHandler(self):
		"""
		TO DO
		Argument Handling
		"""
		return


def __main__():
	dc = DocTracker("data/sample_100k_lines.json")
	dc.loadAnalyser()
	da = dc.da

	print("DOCUMENT ANALYSER COUNTRIES")
	print(da.docCountries("140206010823-b14c9d966be950314215c17923a04af7"))

	print("DOCUMENT ANALYSER CONTINENTS")
	print(da.docContinents("140206010823-b14c9d966be950314215c17923a04af7"))

	print("USER AGENTS")
	print(da.userAgents())

	print("USER AGENTS STRING")
	print(da.userAgentsString())

	print("USER AGENTS STRING SHORT")
	print(da.userAgentsStringShort())

	print("TOP TEN READERS")
	print(da.topTenReaders())

	print("DOCUMENT READERS")
	print(da.docReaders("140206010823-b14c9d966be950314215c17923a04af7"))

	print("READ DOCUMENTS")
	print(da.readDocs("ade7e1f63bc83c66"))

__main__()
