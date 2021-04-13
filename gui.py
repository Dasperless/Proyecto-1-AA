import tkinter as tk
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
from tkinter import ttk
# from main import *


class Application(tk.Frame):
	bfArray = []
	btArray = []
	output = None
	restrictions = None
	timeLabels = []
	mainInst = None
	answerLabels = []

	def __init__(self, main, master=None):
		super().__init__(master)
		self.master = master
		self.mainInst = main
		self.master.resizable(0,0)
		self.grid()
		self.showAnswer()
		self.showRestrictions()
		self.showBrutalForceSolution()
		self.showBacktrackinSolution()
		self.testControls()

	def showAnswer(self):
		tk.Label(self, text="Solución").grid(row=0, column=0, columnspan=4)

		keys = list(self.mainInst.cards.keys())
		for i in range(len(keys)):
			tk.Label(self, text=keys[i], borderwidth=1).grid(row=1, column=i)

		for i in range(len(keys)):
			self.answerLabels += [tk.Button(self, borderwidth=1, height=5, width=20)]
			self.answerLabels[i].grid(row=2, column=i, padx=5)

	def updateAnswer(self, answer):
		for i in range(len(answer)):
			self.answerLabels[i]['text'] = answer[i]

	def showRestrictions(self):
		tk.Label(self, text = "Restricciones").grid(row=0, column=6)
		self.restrictions = tkscrolled.ScrolledText(self, height=36, width=40)
		self.restrictions.grid(row=1, column=6, rowspan=10)
		self.restrictions.config(state=tk.DISABLED)


	def updateRestrictions(self, restrictions):
		self.restrictions.config(state=tk.NORMAL)
		self.restrictions.delete(1.0,tk.END)
		for i in range(len(restrictions)):
			self.restrictions.insert(tk.INSERT,str(restrictions[i]) + "\n")
		self.restrictions.config(state=tk.DISABLED)

	def showBrutalForceSolution(self):
		tk.Label(self, text="Solución (Algoritmo fuerza bruta)").grid(
			row=3, column=0, columnspan=4, pady=20)

		for i in range(5):
			btn = tk.Button(self, borderwidth=1, height=5, width=20)
			self.bfArray += [btn]

		for i in range(len(self.bfArray)):
			self.bfArray[i].grid(row=4, column=i, padx=5)

	def showBacktrackinSolution(self):
		tk.Label(self, text="Solución (Backtracking)").grid(
			row=5, column=0, columnspan=4, pady=20)

		for i in range(5):
			btn = tk.Button(self, borderwidth=1, height=5, width=20)
			self.btArray += [btn]

		for i in range(len(self.btArray)):
			self.btArray[i].grid(row=6, column=i, padx=5)

	def testControls(self):
		#Entry con las restricciones
		tk.Label(self, text="Restricciones").grid(row=7, column=0, pady=15)
		numRest = ttk.Entry(self)
		numRest.grid(row=7, column=1)
		tk.Label(self, text="Repeticiones").grid(row=8, column=0, pady=15)
		numRep = ttk.Entry(self)
		numRep.grid(row=8, column=1)

		#Tiempo de los algoritmos
		tk.Label(self, text="Algoritmo Fuerza Bruta (ns)").grid(row=7, column=2)
		tk.Label(self, text="Backtracking (ns) ").grid(row=8, column=2)

		self.bfTime = tk.Label(self, text="0")
		self.bfTime.grid(row=7, column=3)
		self.btTime = tk.Label(self, text="0")
		self.btTime.grid(row=8, column=3)

		#Output con los pasos del algoritmo
		self.output = tkscrolled.ScrolledText(self, height=10,  width=100, state="disable")
		self.output.grid(row=10, column=0, columnspan=5 )
		tk.Button(self, text="Iniciar", height=2, width=10, command= lambda:self.startTest(numRest.get(), numRep.get())).grid(row=11, column=0, columnspan=4)

	def setBfTime(self, time):
		self.bfTime['text'] = time

	def setBtTime(self, time):
		self.btTime['text'] = time

	def updateBfAnswer(self, arr):
		for i in range(len(arr)):
			self.bfArray[i]['text'] = arr[i]

	def updateBtAnswer(self, arr):
		for i in range(len(arr)):
			self.btArray[i]['text']  = arr[i]
		
	def updateOutput(self, str):
		self.output.config(state=tk.NORMAL)
		self.output.delete(1.0,tk.END)
		self.output.insert(tk.INSERT, str)
		self.output.config(state=tk.DISABLED)

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

		self.mainInst.startTest(numRest,numRep)
			

