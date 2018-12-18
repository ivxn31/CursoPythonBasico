import insert
import read
import update
import delete

class Main:
	def __init__(self):
		self.dato = 1

	def menu(self):
		while self.dato:
			selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete \n')
			if selection == '1':
				insert.insert()
			elif selection == '2':
				update.update()
			elif selection == '3':
				read.read()
			elif selection == '4':
				delete.delete()
			else:
				print('\n Invalid selection \n')

persona1 = Main()
persona1.menu()