#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Document Tracker Analyser
By Nicholas Robinson

Run this script to run the DocumentTrackerAnalyser program.
"""

import argparse
import sys
import time

from DocTracker import DocTracker

def argumentHandler():
	"""
	TO DO
	Argument Handling
	"""
	parser = argparse.ArgumentParser(prog='DocumentTrackerAnalyser', usage='%(prog)s [options]')
	parser = argparse.ArgumentParser(description='Analyse Document Tracking Data')
	parser.add_argument('-f', '--file', nargs='?', help='document tracking data file',
						default="data/sample_100k_lines.json")
	parser.add_argument('-t', '--task', nargs='+', help='task(s) to execute',
						choices=["task2a","task2b","task3a","task3b","task4",
						"task5d","task5e"])
	parser.add_argument('-u', '--user_uuid', nargs='?', help='user id')
	parser.add_argument('-d', '--doc_uuid', nargs='?', help='document id')
	parser.print_help()
	args=parser.parse_args()
	print(args.file)
	print(args.task)
	return args

def runDocTracker(args):
	dt = DocTracker(args.file)
	print("Loading Data")
	start = time.time()
	dt.loadAnalyser()
	end = time.time()
	print(end - start)

	print("Analysing Data")
	if args.task is None:
		return
	for task in args.task:
		if task == "task2a":
			if args.doc_uuid is not None:
				print(dt.task2a(args.doc_uuid))
			else:
				print("ERROR: NEED DOC ID")
		elif task == "task2b":
			if args.doc_uuid is not None:
				print(dt.task2b(args.doc_uuid))
			else:
				print("ERROR: NEED DOC ID")
		elif task == "task3a":
			print(dt.task3a())
		elif task == "task3b":
			print(dt.task3b())
		elif task == "task4":
			print(dt.task4())
		elif task == "task5d":
			if args.doc_uuid is not None:
				if args.user_uuid is not None:
					print(dt.task5d(doc_uuid, user_uuid))
				else:
					print(dt.task5d(doc_uuid))
			else:
				print("ERROR: NEED DOC ID")
		elif task == "task5e":
			if args.doc_uuid is not None:
				if args.user_uuid is not None:
					print(dt.task5e(doc_uuid, user_uuid))
				else:
					print(dt.task5e(doc_uuid))
			else:
				print("ERROR: NEED DOC ID")


def testingFun():
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

def __main__():
	#testingFun()
	args = argumentHandler()
	runDocTracker(args)

__main__()
