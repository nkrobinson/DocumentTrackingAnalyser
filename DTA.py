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
						choices=["2a","2b","3a","3b","4","5d","5e"], required=True)
	parser.add_argument('-u', '--user_uuid', nargs='?', help='user id')
	parser.add_argument('-d', '--doc_uuid', nargs='?', help='document id')
	parser.print_help()
	args=parser.parse_args()
	return args

def runDocTracker(args):
	print("Loading Data")
	start = time.time()
	dt = DocTracker(args.file)
	end = time.time()
	print("Time to load data: %f" % (end - start))
	dt.loadAnalyser()

	print("Analysing Data")
	if args.task is None:
		return
	for task in args.task:
		try:
			runTask(task, args, dt)
		except AssertionError as e:
			print("Error: %s is blank" % (e.args[0]))

def runTask(task, args, dt):
	if task == "2a":
		assert(args.doc_uuid is not None), "-d"
		print(dt.task2a(args.doc_uuid))
	elif task == "2b":
		assert(args.doc_uuid is not None), "-d"
		print(dt.task2b(args.doc_uuid))
	elif task == "3a":
		print(dt.task3a())
	elif task == "3b":
		print(dt.task3b())
	elif task == "4":
		print(dt.task4())
	elif task == "5d":
		assert(args.doc_uuid is not None), "-d"
		if args.user_uuid is not None:
			print(dt.task5d(args.doc_uuid, args.user_uuid))
		else:
			print(dt.task5d(args.doc_uuid))
	elif task == "5e":
		assert(args.doc_uuid is not None), "-d"
		if args.user_uuid is not None:
			print(dt.task5e(args.doc_uuid, args.user_uuid))
		else:
			print(dt.task5e(args.doc_uuid))

def __main__():
	#testingFun()
	args = argumentHandler()
	runDocTracker(args)

__main__()
