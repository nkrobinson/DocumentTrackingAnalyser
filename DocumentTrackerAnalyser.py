#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Tracker Analyser
By Nicholas Robinson

Run this script to run the DocumentTrackerAnalyser program.
"""

import getopt
import sys

from DocTracker import DocTracker

argv = sys.argv[1:]

def argumentHandler(self):
	"""
	TO DO
	Argument Handling
	"""
	return


def __main__(argv):
	dt = DocTracker("data/sample_100k_lines.json")
	dt.loadAnalyser()
	#da = dt.da

	print("TASK 2")
	print("DOCUMENT ANALYSER COUNTRIES")
	print(dt.task2a("140206010823-b14c9d966be950314215c17923a04af7"))

	print("DOCUMENT ANALYSER CONTINENTS")
	print(dt.task2b("140206010823-b14c9d966be950314215c17923a04af7"))

	"""
	print("TASK 3")
	print("USER AGENTS")
	print(da.userAgents())
	"""

	print("USER AGENTS STRING")
	print(dt.task3a())

	print("USER AGENTS STRING SHORT")
	print(dt.task3b())

	print("TASK 4")
	print("TOP TEN READERS")
	print(dt.task4())

	print("TASK 5")
	"""
	print("DOCUMENT READERS")
	print(da.docReaders("140206010823-b14c9d966be950314215c17923a04af7"))

	print("READ DOCUMENTS")
	print(da.readDocs("ade7e1f63bc83c66"))
	"""

	print("ALSO LIKED READER PROFILE SORT")
	print(dt.task5d("140206010823-b14c9d966be950314215c17923a04af7"))

	print("ALSO LIKED READER NUMBER SORT")
	print(dt.task5e("140206010823-b14c9d966be950314215c17923a04af7"))

__main__(argv)
