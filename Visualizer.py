#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Visualizer
By Nicholas Robinson

Plot Graphs with data from Document Tracker Analyser System
"""

import numpy as np
import matplotlib.pyplot as plt

class Visualizer():

	""" Create Vertical Bar Chart Histogram
	"""
	def visualizeBar(self, data, datalabels, labels, padding=0.2, colour='#d61c1c'):
		xpos = np.arange(len(data))+.5
		fig, ax = plt.subplots()
		bars = ax.bar(xpos,data, align='center', color=colour)
		ax.set_xticks(xpos)
		ax.set_xticklabels(datalabels, rotation=30, ha='right')
		plt.xlabel(labels[0])
		plt.ylabel(labels[1])
		ax.set_title(labels[2])
		plt.subplots_adjust(bottom=padding)
		for bar in bars:
			height = bar.get_height()
			dataspace = min(10, height*0.01)
			ax.text(bar.get_x() + bar.get_width()/2., height+dataspace,
					'%d' % int(height),
					ha='center', va='bottom')
		plt.show()

	""" Create Horizontal Bar Chart Histogram
	"""
	def visualizeSideBar(self, data, datalabels, labels, padding=0.2, colour='#4868f0'):
		ypos = np.arange(len(data))+.5
		fig, ay = plt.subplots()
		bars = ay.barh(ypos,data, align='center', color=colour)
		ay.set_yticks(ypos)
		ay.set_yticklabels(datalabels,rotation=0, va='top')
		plt.xlabel(labels[0])
		plt.ylabel(labels[1])
		ay.set_title(labels[2])
		plt.subplots_adjust(left=padding)
		for bar in bars:
			width = bar.get_width()
			dataspace = min(10, width*0.01)
			ay.text(width+dataspace, bar.get_y() + bar.get_height()/2,
					'%d' % int(width),
					ha='left', va='center')
		plt.show()
