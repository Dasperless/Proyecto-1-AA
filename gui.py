import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkscrolled

from tkinter import ttk
# from main import *


class Application(tk.Frame):
	bfArray = []
	output = None
	timeLabels = []
	mainInst = None
	def __init__(self, main, master=None):
		super().__init__(master)
		self.master = master
		self.mainInst = main
		self.master.resizable(0,0)
		self.grid()
		self.showBrutalForceSolution()
		self.showBacktrackinSolution()
		self.testControls()

	def showAnswer(self, answer):
		tk.Label(self, text="Solución").grid(row=0, column=0, columnspan=4)

		keys = list(self.mainInst.cards.keys())
		for i in range(len(keys)):
			tk.Label(self, text=keys[i], borderwidth=1).grid(row=1, column=i)

		for i in range(len(answer)):
			tk.Button(self, text=answer[i], borderwidth=1, height=5, width=20).grid(row=2, column=i, padx=5)

	def showRestrictions(self, restrictions):
		tk.Label(self, text = "Restricciones").grid(row=0, column=4)
		restictionList = tkscrolled.ScrolledText(self, width=20, state="disable").grid(row=1, column=4, rowspan=6)
		print(restrictions)
		for i in restrictions:
			print(i)
			# restrictions.insert(tk.INSERT,i)

	def showBrutalForceSolution(self):
		tk.Label(self, text="Solución (Algoritmo fuerza bruta)").grid(
			row=3, column=0, columnspan=4, pady=20)
		for i in range(4):
			btn = tk.Button(self, borderwidth=1, height=5, width=20)
			self.bfArray += [btn]

		for i in range(len(self.bfArray)):
			self.bfArray[i].grid(row=4, column=i, padx=5)

	def showBacktrackinSolution(self):
		tk.Label(self, text="Solución (Backtracking)").grid(
			row=5, column=0, columnspan=4, pady=20)
		global bfArray
		bfArray = []
		for i in range(4):
			btn = tk.Button(self, borderwidth=1, height=5, width=20)
			bfArray += [btn]

		for i in range(len(bfArray)):
			bfArray[i].grid(row=6, column=i, padx=5)

	def testControls(self):
		tk.Label(self, text="Restricciones").grid(row=7, column=0, pady=15)
		numRest = ttk.Entry(self)
		numRest.grid(row=7, column=1)
		tk.Label(self, text="Repeticiones").grid(row=8, column=0, pady=15)
		numRep = ttk.Entry(self)
		numRep.grid(row=8, column=1)
		tk.Label(self, text="Backtracking (ms)").grid(row=7, column=2)
		tk.Label(self, text="Algoritmo Fuerza Bruta (ms)").grid(row=8, column=2)
		tk.Label(self, text="0").grid(row=7, column=3)
		tk.Label(self, text="0").grid(row=8, column=3)

		self.output = tkscrolled.ScrolledText(self, height=5, state="disable")
		self.output.grid(row=10, column=0, columnspan=4)
		tk.Button(self, text="Iniciar", height=2, width=10, command= lambda:self.startTest(numRest.get(), numRep.get())).grid(row=11, column=0, columnspan=4)
		
	def startTest(self, numRest, numRep):
		if(numRest == ""):
			return messagebox.showinfo(message="No se ha ingresado el número de restricciones")
		elif(numRep == ""):
			return messagebox.showinfo(message="No se ha ingresado el número de repeticiones del algoritmo")
		try:
			numRest = int(numRest)
			numRep = int(numRep)
		except:
			messagebox.showerror(message= "La entrada no es válida")		
			
		# for i in range(numRep):
		self.mainInst.setAnswer()
		answer = self.mainInst.answer
		restrictions = self.mainInst.restrictions
		self.showAnswer(answer)
		self.showRestrictions(restrictions)
			# setRestrictions(numRest)
			# bruteForceSolution(cards,answer)
		# bruteForceSolution(cards, answer)

