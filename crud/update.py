from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.EmployeeData

def update():
	try:
		criteria = input('\n Enter id to update\n')
		name = input('\n Enter name to update\n')
		age = input('\n Enter age to update \n')
		country = input('\n Enter country to update \n')
		db.Employees.update_one(
			{"id":criteria},
			{
				"$set":{
					"name" : name,
					"age" : age,
					"country" : country
				}
			}
		)
		print('\n Records updated successfully \n')
	except ImportError:
		platform_specific_module = None