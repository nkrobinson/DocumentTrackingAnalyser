#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TKinter GUI
By Nicholas Robinson

Graphical User interface for the Document Tracker Analyser system.
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog


from DTA import DTA

class GUI():

	def __init__(self):
		self.createSystem()

	def loadDocTracker(self):
		if self.verifyFileName():
			self.dta = DTA(self.filename)
			self.dta.loadAnalyser()

	def createSystem(self):
		root = Tk()
		root.title("Document Tracking Analyser")

		mainframe = ttk.Frame(root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)

		self.filename = ""
		self._user = StringVar()
		self._doc = StringVar()

		ttk.Button(mainframe, text="Open File", command=self.openFile).grid(column=1, row=1, columnspan=2, sticky=(W, E))

		ttk.Label(mainframe, text="User UUID").grid(column=1, row=2)
		user_entry = ttk.Entry(mainframe, width=7, textvariable=self._user)
		user_entry.grid(column=1, row=3, sticky=(W, E))

		ttk.Label(mainframe, text="Document UUID").grid(column=2, row=2)
		doc_entry = ttk.Entry(mainframe, width=7, textvariable=self._doc)
		doc_entry.grid(column=2, row=3, sticky=(W, E))

		ttk.Button(mainframe, text="Task 2a", command=self.task2a).grid(column=1, row=4, sticky=(W, E))
		ttk.Button(mainframe, text="Task 2b", command=self.task2b).grid(column=2, row=4, sticky=(W, E))
		ttk.Button(mainframe, text="Task 3a", command=self.task3a).grid(column=1, row=5, sticky=(W, E))
		ttk.Button(mainframe, text="Task 3b", command=self.task3b).grid(column=2, row=5, sticky=(W, E))
		ttk.Button(mainframe, text="Task 4", command=self.task4).grid(column=1, row=6, columnspan=2, sticky=(W, E))
		ttk.Button(mainframe, text="Task 5d", command=self.task5d).grid(column=1, row=7, sticky=(W, E))
		ttk.Button(mainframe, text="Task 5e", command=self.task5e).grid(column=2, row=7, sticky=(W, E))

		self.errorLabel = ttk.Label(mainframe, text="")
		self.errorLabel.grid(column=1, row=8, columnspan=2, sticky=(W, E))

		for child in mainframe.winfo_children(): child.grid_configure(padx=20, pady=10)

		root.mainloop()

	def openFile(self):
		self.errorLabel['text'] = "Opening File"
		self.filename = filedialog.askopenfile(filetypes=(('JSON files', '*.json'), ('All Files', '*.*'))).name
		self.loadDocTracker()
		self.errorLabel['text'] = "Opened File"

	def verifyFileName(self):
		return self.filename != ""

	def verifyDocID(self):
		return self._doc.get() != ""

	def verifyUserID(self):
		return self._user.get() != ""

	def taskFileMissingCheck(self, taskName):
		self.errorLabel['text'] = "Running Task %s" % (taskName)
		if not self.verifyFileName():
			self.errorLabel['text'] = "Task %s Failed: No File Selected" % (taskName)
			return True
		return False

	def tryTask(self, taskName, task, arg1=None, arg2=None):
			try:
				if arg1 is None:
					task()
				elif arg2 is None:
					task(arg1)
				else:
					task(arg1, arg2)
			except AssertionError as e:
				self.errorLabel['text'] = "Task %s Failed: No Document UUID" % (taskName)
			except Exception as e:
				self.errorLabel['text'] = "Task %s Failed: %s" % (taskName, e.message)
			else:
				self.errorLabel['text'] = "Task %s Completed" % (taskName)

	def tryTask5(self, taskName, task):
		assert(self.verifyDocID())
		if self.verifyUserID():
			task(self._doc.get(), self._user.get())
			self.errorLabel['text'] = "Task %s Completed" % (taskName)
			return
		task(self._doc.get())
		self.errorLabel['text'] = "Task %s Completed" % (taskName)

	def task2a(self):
		if self.taskFileMissingCheck("2a"):
			return
		if self.verifyDocID():
			self.tryTask("2a", self.dta.task2a, self._doc.get())
			return
		self.errorLabel['text'] = "Task 2a Failed: No Document UUID"

	def task2b(self):
		if self.taskFileMissingCheck("2b"):
			return
		if self.verifyDocID():
			self.tryTask("2b", self.dta.task2b, self._doc.get())
			return
		self.errorLabel['text'] = "Task 2a Failed: No Document UUID"

	def task3a(self):
		if self.taskFileMissingCheck("3a"):
			return
		self.tryTask("3a", self.dta.task3a)

	def task3b(self):
		if self.taskFileMissingCheck("3b"):
			return
		self.tryTask("3b", self.dta.task3b)

	def task4(self):
		if self.taskFileMissingCheck("4"):
			return
		self.tryTask("4", self.dta.task4)

	def task5d(self):
		if self.taskFileMissingCheck("5d"):
			return
		self.tryTask("5d",self.tryTask5, "5d", self.dta.task5d)

	def task5e(self):
		if self.taskFileMissingCheck("5e"):
			return
		self.tryTask("5e",self.tryTask5, "5e", self.dta.task5e)

def __main__():
	gui = GUI()

__main__()
