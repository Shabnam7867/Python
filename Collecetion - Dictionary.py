# Collections - Dictionary (basics)

# Create a new dictionary
new_employee = {'first_name' : 'David' , 'salary' : 10000 , 'company' : 'Google'}

# Print the dictionary
print("Print the dictionary : " +str(new_employee))

# Get cell 'value' - first way
print("Get 'value' of 'first_name' key : " +str(new_employee['first_name']))

# Get cell 'value' - second way
print("Get 'value' of 'salary' key : " +str(new_employee.get('salary')))

# Remove dictionary cell by using '.pop()
new_employee.pop('salary')
print("Remove dictionary cell by using '.pop()' :" +str(new_employee))

# Print out all 'keys' of the dictionary
print("Get all 'keys' out of the dictionary : " +str(new_employee.keys()))

# Print out all 'values' of the dictionary
print("Get all 'values' out of the dictionary : " +str(new_employee.values()))

# Use a variable and place it inside a dictionary cell
job_title_value = "developer"
new_dictionary = {"job_title" : job_title_value}

print("Print the 'new dictionary' : " +str(new_dictionary))





# Collections - Dictrionary practice (basic)

# Create a dictionary about Alex
alex = {"Age": 32 , "Married" : "Yes", "Kids": 3}
print("(1) - This is Alex's dictionary : " +str(alex))

print(alex['Age'])

# Extract values of the dictionary into variables
age = alex['Age']
marriage_status = alex['Married']
number_of_kids = alex['Kids']

print("(2) - Print of 'age' value : " +str(age))
print("(2) - Print of 'marriage_status' value : " +marriage_status)
print("(2) - Print of 'number_of_kids' value : " +str(number_of_kids))

# Change of 'Age' key cell value from 32 to 33
age_helper_dictionary = {'Age' : 33}
alex.update(age_helper_dictionary)
print("(4) - Alex's age update to '33' : " +str(alex))


kids_helper_dictionary = {'Kids' : 4}
alex.update(kids_helper_dictionary)

# Change of 'Kids' key cell value from 3 to 4
print("(5) - Alex's 'Kids' number update to '4' : " +str(alex))

# Print all keys out of 'alex' dictionary
print("(6) - 'keys' of the dictionary : " +str(alex.keys()))

# Print all 'values' out of 'alex' dictionary
print("(7) - 'values' of the dictionary : " +str(alex.values()))

joe = {'Age' : 35 , 'Kids' : {'David' : 'Boy' , 'Lisa' : 'Girl'}}
print(joe)




# Collections Dictionary Practice (Advanced)

# Create a dictionary of building attendants
build_attendants = {'floor_1' : {'first_apartment' : 'Rachel' , 'second_apartment' : 'Jeen'},
                    'floor_2' : {'third_apartment' : 'Jack'}}

print("(1) - Print of the dictionary : " +str(build_attendants))

# Extract the nested cell items
print("(2) - 1st floor items of the dictionary : " +str(build_attendants['floor_1']))

# Extract of who ever lives in the second apartment = 'Jeen'
print("(3) - Print of the attendant in the 2nd apartment : " +str(build_attendants['floor_1']['second_apartment']))

# Add a 4th apartment on floor 2
build_attendants['floor_2']['forth_apartment'] = "Carrol"
print("The dictionary after adding 'Carrol' : " +str(build_attendants))

# Remove the 1st apartment of the dictionary
build_attendants['floor_1'].pop("first_apartment")
print("Print of the dictionary after removing 1st apartment " +str(build_attendants))




