from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData

def delete():
	try:
		criteria = input('\n Enter id to update\n')
		db.Employees.delete_many({"id":criteria})
		print('\n Deletion successfully \n')
	except ImportError:
		platform_specific_module = None