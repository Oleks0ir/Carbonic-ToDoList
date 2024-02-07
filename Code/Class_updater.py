
#---Import Area---------------------
import datetime

#---Test Area-----------------------
#Testing function for checking the connection between Library and Main code
def Hello_World():
	print("Hello World")


#---Class Area-----------------------

# Class 'Item' is created to store information of tasks. It stores: Title, Date of creation,
# Discription of the file and its importance level

class Item:
	
	def __init__(self, title, discription, importance):
		self.title = title
		self.discription = discription
		self.importance = importance

#		Date is being stored separatly, without users involved
		self.date = datetime.datetime.now()
		
#	The output function
	def __str__(self):
		return f"{self.title}({self.importance}) created on {self.date.strftime('%x  %X')}: \n {self.discription} "




