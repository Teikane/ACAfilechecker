# Author Kiet Nguyen
#
# Iteration Verison 1.0
#
# Desription: Just performs a quick parse and check of an ACA csv file.
# Mainly checking for FEIN, SSN length, and if CI flag is ticked apporiately.
# 
# Definitely more debug/testing needed.
#
# How to use (Windows): 
# shift right-click folder containing aca_filechecker.exe or aca_filechecker.py
# select open command prompt here
# drag and drop the exe or py file
# add a space
# drag and drop csv file into command prompt
# example of what command prompt at this point:
# C:\...\Desktop\ aca_filecheck.exe.lnk \...\filename.csv

import sys
import tkinter as tk

# INPUT: Entire list of each line in aca csv.
# Func: Checks if company FEIN has 9 char.
# OUTPUT: Throws error (0) otherwise pass (1).
def checkFEIN(aca):
	no_error = 1
	for line in aca:
		if 'CMP' in line[0]:
			print ('\n'+line[3]+'\n'+line[1]+'\n')
			#checks length of FEIN
			if "'" in line[4]:
				fein = line[4][1::]
			else:
				fein = line[4]
			if len(fein) != 9:
				print ("FEIN: not 9char")
				no_error = 0
			else:
				print("FEIN: OK")
	return no_error

# INPUT: Entire list of each line in aca csv.
# Func: Checks if EMP SSN has 9 char.
# OUTPUT: Throws error (0) otherwise pass (1).
def checkSSN(aca):
	no_error = 1
	for line in aca:
		if 'EMP' in line[0]:
			#checks length of SSN
			if "'" in line[7]:
				ssn = line[7][1::]
			else:
				ssn = line[7]
			if len(ssn) != 9:
				print ("EMP SSN: {} not 9char".format(ssn))
				no_error = 0
	if no_error:
		print("EMP SSN: OK")
	return no_error

# INPUT: Entire list of each line in aca csv.
# Func: Checks if EMP is marked for CI and checks CI under EMP.
# OUTPUT: Throws error (0) otherwise pass (1).
def checkCI(aca):
	currEMP = []
	ciFlag = False
	no_error = 1
	for line in aca:
		if "EMP" in line[0]:

			# sets current employee and checks CI directly below if any
			# index 17 has CI for EMP record

			currEMP = line
			if 'Y' in currEMP[17]:
				ciFlag = True
			else:
				ciFlag = False

			# if CI exist check EMP was set with CI flag
		if "CI" in line[0] and "CIMON" not in line[0]:
			if ciFlag is True:

				#check CI SSN length
				if "'" in line[5]:
					cissn = line[5][1::]
				else:
					cissn = line[5]
				if len(cissn) == 9 or len(cissn) == 0:
					pass
				else:
					print (line)
					print ("CI SSN: {} not 9char".format(cissn))
					no_error = 0
			else:
				print ("EMP SSN: {} for CI not marked".format(currEMP[7]))
				no_error = 0
	if no_error:
		print("CI: OK")
	return no_error

# GUI?
'''
class Checker(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()
		self.filetype = None
		self.filepath = ""

	def create_widgets(self):
		self.csv_filetype = tk.Button(self)
		self.csv_filetype["text"] = ".csv"
		self.csv_filetype["command"] = self.set_csv_type
		self.csv_filetype.pack(side="top")

		self.txt_filetype = tk.Button(self)
		self.txt_filetype["text"] = ".txt"
		self.txt_filetype["command"] = self.set_txt_type
		self.txt_filetype.pack(side="top")

		self.pathentry = tk.Entry(self)
		self.pathentry.pack()

		# tell the entry widget to watch this variable
		self.pathentry["textvariable"] = self.filepath

		self.scan = tk.Button(self)
		self.scan["text"] = "scan"
		self.scan["command"] = self.scanner
		self.scan.pack(side="top")

		self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
		self.quit.pack(side="bottom")


	def set_csv_type(self):
		self.filetype = 'csv'
	def set_txt_type(self):
		self.filetype = 'txt'

	def scanner(self):
		print (self.filetype)
'''
if __name__ == '__main__':
	file = sys.argv[1]
	aca = []

	with open (file, 'r') as acaFile:
		for line in acaFile:
			aca.append(line.split(','))
		acaFile.close()

	if checkFEIN(aca) and checkSSN(aca) and checkCI(aca):
		print ("All green")

# for gui things
'''
	root = tk.Tk()
	app = Checker(master=root)

	app.mainloop()
'''
