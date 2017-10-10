# Code written by : Hem Raj Regmi (sangamsyabil@gmail.com) http://hemrajregmi.com
# github repository: https://github.com/sangamsyabil/Learn_python_byExamples
""" this program is an example of key json methods like json.load(f), json.loads(f), json.dump(j,f) and json.dumps(j) """

import json

json_file = open("C:\\Users\\sanga\\PycharmProjects\\pythonExamplesEff\\jsonColor.json", "r", encoding="utf-8")
# the file path may be different, encoding = utf-8 is for mon ASCII characters
person_car = json.load(json_file) #loding the json data
#person_cars = json.loads(json_file) # this we can use when the JSON arrives in the form of string
json_file.close() #closing the json file

#python will purse all the json data into dictionary format
print(type(person_car))

print("Age = ",person_car["age"]) #testing

person_car_s = json.dumps(person_car, ensure_ascii = False) #Output JSON object as string also ensuring ASCII character into False

print(type(person_car_s)) #Testing type of person_car_string

#to demonstrate an example of json.dump(str), let's create a python dictionary
my_dict = {'name':'Hem Raj', 'age': 26}

# update value
my_dict['age'] = 27

# add item
my_dict['address'] = 'Canada'

print(my_dict)

new_json_file = open("C:\\Users\\sanga\\PycharmProjects\\pythonExamplesEff\\my_dict.json", "w", encoding="utf-8")
json.dump(my_dict, new_json_file, ensure_ascii=False) #Now we wrote JSON object to the file

new_json_file.close()

# Happy coding!!!