#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Tracker Analyser
By Nicholas Robinson

Main Class for Document Tracker Analyser System
"""

from Sorter import Sorter
from IDDictionary import IDDictionary as Dic
from DocAnalyser import DocAnalyser
from Visualizer import Visualizer

class DTA():

	def __init__(self, filename):
		self.filename = filename
		self.s = Sorter(filename)
		self.loadData()
		self.da = DocAnalyser(self.dd, self.ud, self.al)
		self.viz = Visualizer()

	def loadData(self):
		listSet = self.s.loadFile()
		self.dd = listSet[0]
		self.ud = listSet[1]
		self.al = listSet[2]

	def loadAnalyser(self):
		self.da = DocAnalyser(self.dd, self.ud, self.al)

	def task2a(self, docID):
		rawdata = self.da.docCountries(docID)
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["Countries","Views","Country","Top countries to view document"]
		self.viz.visualizeBar(data, datalabels, labels)
		return rawdata

	def task2b(self, docID):
		rawdata = self.da.docContinents(docID)
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["Continents","Views","Continent","Top continents to view document"]
		self.viz.visualizeBar(data, datalabels, labels)
		return rawdata

	def task3a(self):
		rawdata = self.da.userAgentsString()
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["Number of Users","User Agents","User Agents Document Views"]
		self.viz.visualizeSideBar(data, datalabels, labels, 0.3)
		return rawdata

	def task3b(self):
		rawdata = self.da.userAgentsStringBrowser()
		data = [x[1] for x in rawdata]
		datalabels = [x[0] for x in rawdata]
		labels = ["Number of Users","User Agents","Browser Document Views"]
		self.viz.visualizeSideBar(data, datalabels, labels, 0.3)
		return rawdata

	def task4(self):
		rawdata = self.da.topTenReaders()
		data = [x[1] for x in rawdata]
		datalabels = [x[0].id for x in rawdata]
		labels = ["Readers","Time Spent Reading","Top Readers Based on Reading Time"]
		self.viz.visualizeBar(data, datalabels, labels, 0.2)
		return rawdata

	def task5d(self, docID, userID=None):
		rawdata = self.da.alsoLiked(docID, self.s.readerProfileSort, userID)
		data = [x[1] for x in rawdata]
		datalabels = [x[0].id for x in rawdata]
		labels = ["Time Spent Reading","Documents","Task 5d"]
		self.viz.visualizeSideBar(data, datalabels, labels, 0.3)
		return rawdata

	def task5e(self, docID, userID=None):
		rawdata = self.da.alsoLiked(docID, self.s.readerNumberSort, userID)
		data = [x[1] for x in rawdata]
		datalabels = [x[0].id for x in rawdata]
		labels = ["Number of Readers","Documents","Task 5e"]
		self.viz.visualizeSideBar(data, datalabels, labels, 0.3)
		return rawdata
