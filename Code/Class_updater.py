import datetime

def Hello_World():
	print("Hello World")


class Item:
	def __init__(self, title, discription, importance):
		self.title = title
		self.date = datetime.datetime.now()
		self.discription = discription
		self.importance = importance
	
	def __str__(self):
		return f"{self.title}({self.importance}) created on {self.date.strftime('%x  %X')}: \n {self.discription} "




