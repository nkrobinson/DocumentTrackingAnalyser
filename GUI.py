#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TKinter GUI
By Nicholas Robinson
"""

# Example from: http://www.tkdocs.com/tutorial/firstexample.html

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

		for child in mainframe.winfo_children(): child.grid_configure(padx=20, pady=10)

		root.mainloop()

	def openFile(self):
		self.filename = filedialog.askopenfile(filetypes=(('JSON files', '*.json'), ('All Files', '*.*'))).name
		print(self.filename)
		self.loadDocTracker()

	def verifyFileName(self):
		return self.filename != ""

	def verifyDocID(self):
		return self._doc.get() != ""

	def verifyUserID(self):
		return self._user.get() != ""


	def task2a(self):
		if self.verifyDocID():
			return self.dt.task2a(self._doc.get())
		return

	def task2b(self):
		if self.verifyDocID():
			return self.dt.task2b(self._doc.get())
		return

	def task3a(self):
		return self.dt.task3a()

	def task3b(self):
		return self.dt.task3b()

	def task4(self):
		return self.dt.task4()

	def task5d(self):
		if self.verifyDocID():
			if self.verifyUserID():
				print("5d with User & Doc")
				return self.dt.task5d(self._doc.get(), self._user.get())
			print("5e with Doc")
			print(self.dt.task5d(self._doc.get()))
			return
		return

	def task5e(self):
		if self.verifyDocID():
			if self.verifyUserID():
				print("5e with User & Doc")
				return self.dt.task5e(self._doc.get(), self._user.get())
			print("5e with Doc")
			print(self.dt.task5e(self._doc.get()))
			return
		return

def __main__():
	gui = GUI()

__main__()
