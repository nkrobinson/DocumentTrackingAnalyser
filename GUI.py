#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TKinter GUI
By Nicholas Robinson
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog


from DocTracker import DocTracker as DT

class GUI():

	def __init__(self):
		self.createSystem()

	def loadDocTracker(self):
		if self.verifyFileName():
			self.dt = DT(self.filename)
			self.dt.loadAnalyser()

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


	def task2a(self):
		self.errorLabel['text'] = "Running Task 2a"
		if self.verifyDocID():
			try:
				self.dt.task2a(self._doc.get())
			except Exception as e:
				self.errorLabel['text'] = "Task 2a Failed: %s" % (e.message)
			self.errorLabel['text'] = "Task 2a Completed"
			return
		self.errorLabel['text'] = "Task 2a Failed: No Document UUID"
		return

	def task2b(self):
		self.errorLabel['text'] = "Running Task 2b"
		if self.verifyDocID():
			try:
				self.dt.task2b(self._doc.get())
			except Exception as e:
				self.errorLabel['text'] = "Task 2b Failed: %s" % (e.message)
			self.errorLabel['text'] = "Task 2b Completed"
			return
		self.errorLabel['text'] = "Task 2a Failed: No Document UUID"
		return

	def task3a(self):
		self.errorLabel['text'] = "Running Task 3a"
		try:
			self.dt.task3a()
		except Exception as e:
			self.errorLabel['text'] = "Task 3a Failed: %s" % (e.message)
		self.errorLabel['text'] = "Task 3a Completed"
		return

	def task3b(self):
		self.errorLabel['text'] = "Running Task 3b"
		try:
			self.dt.task3b()
		except Exception as e:
			self.errorLabel['text'] = "Task 3b Failed: %s" % (e.message)
		self.errorLabel['text'] = "Task 3b Completed"
		return

	def task4(self):
		self.errorLabel['text'] = "Running Task 4"
		try:
			self.dt.task4()
		except Exception as e:
			self.errorLabel['text'] = "Task 4 Failed: %s" % (e.message)
		self.errorLabel['text'] = "Task 4 Completed"
		return

	def task5d(self):
		self.errorLabel['text'] = "Running Task 5d"
		try:
			if self.verifyDocID():
				if self.verifyUserID():
					self.dt.task5d(self._doc.get(), self._user.get())
					self.errorLabel['text'] = "Task 5d Completed"
					return
				self.dt.task5d(self._doc.get())
				self.errorLabel['text'] = "Task 5d Completed"
				return
			self.errorLabel['text'] = "Task 2a Failed: No Document UUID"
		except Exception as e:
			self.errorLabel['text'] = "Task 5d Failed: %s" % (e.message)
		return

	def task5e(self):
		self.errorLabel['text'] = "Running Task 5e"
		try:
			if self.verifyDocID():
				if self.verifyUserID():
					self.dt.task5e(self._doc.get(), self._user.get())
					self.errorLabel['text'] = "Task 5e Completed"
					return
				self.dt.task5e(self._doc.get())
				self.errorLabel['text'] = "Task 5e Completed"
				return
			self.errorLabel['text'] = "Task 2a Failed: No Document UUID"
		except Exception as e:
			self.errorLabel['text'] = "Task 5e Failed: %s" % (e.message)
		return

def __main__():
	gui = GUI()

__main__()
