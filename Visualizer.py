#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Visualizer
By Nicholas Robinson
"""

import numpy as np
import matplotlib.pyplot as plt

from DataTypes import Document as Doc
from DataTypes import User as User
from List import ListContainer as List

class Visualizer():

	def __init__(self):
		self.something = 0

	def visualizeBar(self, data, datalabels, labels):
		ind = np.arange(len(data))  # the x locations for the groups
		width = 0.15       # the width of the bars

		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, data, width, color='b')

		# add some text for labels, title and axes ticks
		plt.xlabel(labels[0])
		plt.ylabel(labels[1])
		ax.set_title(labels[3])
		ax.set_xticks(ind + width)
		ax.set_xticklabels(datalabels)

		ax.legend((rects1[0],), (labels[2]))
		def autolabel(rects):
		    # attach some text labels
		    for rect in rects:
		        height = rect.get_height()
		        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
		                '%d' % int(height),
		                ha='center', va='bottom')

		autolabel(rects1)
		plt.show()

	def visualizeSideBar(self, data, datalabels, labels):
		ind = np.arange(len(data))  # the x locations for the groups
		height = 0.15       # the width of the bars

		fig, ay = plt.subplots()
		rects1 = ay.bar(ind, data, height, color='b')

		# add some text for labels, title and axes ticks
		plt.xlabel(labels[0])
		plt.ylabel(labels[1])
		ay.set_title(labels[3])
		ay.set_yticks(ind + height)
		ay.set_yticklabels(datalabels)

		ay.legend((rects1[0],), (labels[2]))
		def autolabel(rects):
		    # attach some text labels
		    for rect in rects:
		        width = rect.get_width()
		        ay.text(1.01*width, rect.get_y() + rect.get_height()/2.,
		                '%d' % int(width),
		                ha='center', va='bottom')

		autolabel(rects1)
		plt.show()
