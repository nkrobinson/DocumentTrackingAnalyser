#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
User List
By Nicholas Robinson
"""


class ListContainer(object):

	def __init__(self):
		self.list = []
		self._index = -1

	def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.list):
            raise StopIteration
        self.index = self.index + 1
        return self.list[self.index]

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
