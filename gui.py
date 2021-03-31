import tkinter as tk
from tkinter import ttk
from main import *

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.grid()
		self.showAnswer()
		self.showBrutalForceSolution()
		self.showBacktrackinSolution()
		self.testControls()

	def showAnswer(self):
		tk.Label(self, text = "Solución").grid(row=0,column=0, columnspan=4)\

		keys = list(cards.keys())
		for i in range(len(keys)):
			tk.Label(self, text= keys[i], borderwidth=1 ).grid(row=1,column=i)

		for i in range(len(answer)):
			tk.Button(self, text= answer[i], borderwidth=1, height=5, width=20 ).grid(row=2,column=i, padx=5)

	def showBrutalForceSolution(self):
		tk.Label(self, text = "Solución (Algoritmo fuerza bruta)").grid(row=3,column=0, columnspan=4, pady=20)
		global bfArray 
		bfArray =[]
		for i in range(4):
			btn = tk.Button(self, borderwidth=1, height=5, width=20 )
			bfArray += [btn]

		for i in range(len(bfArray)):
			bfArray[i].grid(row=4,column=i, padx=5)
		print (bfArray)

	def showBacktrackinSolution(self):
		tk.Label(self, text = "Solución (Backtracking)").grid(row=5,column=0, columnspan=4, pady=20)
		global bfArray 
		bfArray =[]
		for i in range(4):
			btn = tk.Button(self, borderwidth=1, height=5, width=20 )
			bfArray += [btn]

		for i in range(len(bfArray)):
			bfArray[i].grid(row=6,column=i, padx=5)
		print (bfArray)		

	def testControls(self ):
		tk.Label(self, text = "Restricciones").grid(row = 7, column = 0, pady=20)
		ttk.Entry(self).grid(row=7,)

root = tk.Tk()
app = Application(master=root)
# app.printAnswer()
app.mainloop()