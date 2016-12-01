#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ID Dictionary
By Nicholas Robinson
"""

class IDDictionary(object):

	def __init__(self):
		self.dic = {}

	def __iter__(self):
		self._index = -1
		return self

	def __next__(self):
		if self._index == (len(self.dic) - 1):
			raise StopIteration
		self._index += 1
		return self.dic[self._index]

	def add(self, item):
		if not self.contains(item.id):
			self.dic[item.id] = item

	def contains(self, ID):
		return ID in self.dic

	def get(self, ID):
		return self.dic[ID]

	def getList(self):
		return [self.dic[item] for item in self.dic]
