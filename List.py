#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
User List
By Nicholas Robinson
"""

class ListContainer(object):

	def __init__(self):
		self.list = []

	def __iter__(self):
		self._index = -1
		return self

	def __next__(self):
		if self._index == (len(self.list) - 1):
			raise StopIteration
		self._index += 1
		return self.list[self._index]

	def add(self, item):
		if not (self.contains(item)):
			self.list.append(item)

	def contains(self, ID):
		for item in self.list:
			if item.id == ID:
				return True
		return False

	def get(self, ID):
		for item in self.list:
			if item.id == ID:
				return item
		return None
