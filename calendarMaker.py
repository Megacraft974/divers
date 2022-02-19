from tkinter import *

def viewer(calendar):
	fen = Tk()
	weekdays = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi']
	for x, day in enumerate(calendar.items()):
		day, hours = day
		fen.grid_columnconfigure(x, weight=1)
		for y, hour in enumerate(hours):
			if x == 0:
				fen.grid_rowconfigure(y, weight=1)
			if y == 0:
				text=weekdays[x]
			else:
				text=str(x)+"/"+str(y)+"-"+hour
			Label(fen,text=text,borderwidth=1, relief="solid").grid(column=x,row=y,sticky="nsew")
	fen.mainloop()

class Calendar():
	def __init__(self):
		# Useless
		self.calendar = self.empty()

	def empty(self):
		calendar = {}
		week = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi']
		hours = ['M'+str(x+1) for x in range(4)]+['S'+str(x+1) for x in range(4)]
		for day in week:
			calendar[day] = []
			for hour in hours:
				calendar[day].append(hour)
		return calendar

columns, rows = 6,9
#calendar = [["yo"]*rows]*columns
calendar = Calendar().empty()
for day,hours in calendar.items():
	print(day,hours)
viewer(calendar)
