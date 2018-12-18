from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData

def insert():
	try:
		employeedid = input('Enter Employeed id : ')
		employeedname = input('Enter Employeed name : ')
		employeedage = input('Enter Employeed age : ')
		employeedcountry = input('Enter Employeed country : ')
		db.Employees.insert_one(
			{
				"id" : employeedid,
				"name" : employeedname,
				"age" : employeedage,
				"country" : employeedcountry
			}
		)
		print('Inserted data successfully')
	except ImportError:
		platform_specific_module = None