#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Tracker
By Nicholas Robinson
"""

import argparse

from Sorter import Sorter
from List import ListContainer as List
from DocAnalyser import DocAnalyser
from Visualizer import Visualizer

class DocTracker():

	def __init__(self, filename="data/issuu_cw2.json"):
		self.filename = filename
		self.s = Sorter()
		self.loadData()
		self.da = DocAnalyser(self.dl, self.ul, self.al)
		self.viz = Visualizer()

	def loadData(self):
		listSet = self.s.loadFile()
		self.dl = listSet[0]
		self.ul = listSet[1]
		self.al = listSet[2]

	def loadAnalyser(self):
		self.da = DocAnalyser(self.dl, self.ul, self.al)

	def docCountries(self, docID):
		rawdata = self.da.docCountries(docID)
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["Countries","Views","Country","Top countries to view document"]
		self.viz.visualizeBar(data, datalabels, labels)

	def docContinents(self, docID):
		rawdata = self.da.docContinents(docID)
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["Continents","Views","Continent","Top continents to view document"]
		self.viz.visualizeBar(data, datalabels, labels)

	def userAgentsString(self):
		rawdata = self.da.userAgentsString()
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["User Agents","Number of Users","User Agent","Top user agents to view documents"]
		self.viz.visualizeSideBar(data, datalabels, labels)

	def userAgentsStringShort(self):
		rawdata = self.da.userAgentsStringShort()
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["User Agents","Number of Users","User Agent","Top user agents to view documents"]
		self.viz.visualizeSideBar(data, datalabels, labels)

	def alsoLikedReaderNumber(self, docID, userID=None):
		return self.da.alsoLiked(docID, self.s.readerNumberSort, userID)

	def alsoLikedReaderProfile(self, docID, userID=None):
		return self.da.alsoLiked(docID, self.s.readerProfileSort, userID)

	def argumentHandler(self):
		"""
		TO DO
		Argument Handling
		"""
		return


def __main__():
	dt = DocTracker("data/sample_100k_lines.json")
	dt.loadAnalyser()
	da = dt.da

	print("TASK 2")
	print("DOCUMENT ANALYSER COUNTRIES")
	print(dt.docCountries("140206010823-b14c9d966be950314215c17923a04af7"))

	print("DOCUMENT ANALYSER CONTINENTS")
	print(dt.docContinents("140206010823-b14c9d966be950314215c17923a04af7"))

	print("TASK 3")
	print("USER AGENTS")
	print(da.userAgents())

	print("USER AGENTS STRING")
	print(dt.userAgentsString())

	print("USER AGENTS STRING SHORT")
	print(dt.userAgentsStringShort())

	print("TASK 4")
	print("TOP TEN READERS")
	print(da.topTenReaders())

	print("TASK 5")
	print("DOCUMENT READERS")
	print(da.docReaders("140206010823-b14c9d966be950314215c17923a04af7"))

	print("READ DOCUMENTS")
	print(da.readDocs("ade7e1f63bc83c66"))

	print("ALSO LIKED READER NUMBER SORT")
	print(dt.alsoLikedReaderNumber("140206010823-b14c9d966be950314215c17923a04af7"))

	print("ALSO LIKED READER PROFILE SORT")
	print(dt.alsoLikedReaderProfile("140206010823-b14c9d966be950314215c17923a04af7"))

__main__()
