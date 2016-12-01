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
from IDDictionary import IDDictionary as Dic

class Visualizer():

	def __init__(self):
		self.something = 0

	def visualizeBar(self, data, datalabels, labels, padding=0.2, colour='#d61c1c'):
		pos = np.arange(len(data))+.5
		fig, ax = plt.subplots()
		bars = ax.bar(pos,data, align='center', color=colour)
		ax.set_xticks(pos)
		ax.set_xticklabels(datalabels, rotation=30, ha='right')
		plt.xlabel(labels[0])
		plt.ylabel(labels[1])
		ax.set_title(labels[2])
		plt.subplots_adjust(bottom=padding)
		#plt.grid(True)
		for bar in bars:
			height = bar.get_height()
			dataspace = min(10, height*0.01)
			ax.text(bar.get_x() + bar.get_width()/2., height+dataspace,
					'%d' % int(height),
					ha='center', va='bottom')
		plt.show()

	def visualizeSideBar(self, data, datalabels, labels, padding=0.2, colour='#4868f0'):
		pos = np.arange(len(data))+.5    # the bar centers on the y axis
		fig, ay = plt.subplots()
		bars = ay.barh(pos,data, align='center', color=colour)
		ay.set_yticks(pos)
		ay.set_yticklabels(datalabels,rotation=0, va='top')
		plt.xlabel(labels[0])
		plt.ylabel(labels[1])
		ay.set_title(labels[2])
		plt.subplots_adjust(left=padding)
		#plt.grid(True)
		for bar in bars:
			width = bar.get_width()
			dataspace = min(10, width*0.01)
			ay.text(width+dataspace, bar.get_y() + bar.get_height()/2,
					'%d' % int(width),
					ha='left', va='center')
		plt.show()
