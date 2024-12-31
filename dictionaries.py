# Dictionaries are like Object in JavaScript, 
# Dictionaries are collections of key-value pairs, and each key is connected to a value. You can use a key to access the value associated with that key. A key's value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.

# In Python, a dictionary is wrapped in braces, {}, with

# keys and values separated by a colon (:)
# key-value pairs separated by commas
# keys are unique
# keys are immutable
# values can be any type

# Here's a simple example of a dictionary that stores a person's name, age, location, and a list that includes the person's hobbies:

person = {
    'name': 'Jahir',
    'age': 32,
    'location': 'Dhaka',
    'hobbies': ['Reading', 'Coding', 'Traveling']
}

print(person['name'])
# It will print the value of the key name

print(person['age'])
# It will print the value of the key age

# person.pop('location')
# It will remove the key location from the dictionary

print(person)
# It will print the whole dictionary

# person.clear()
# It will clear the whole dictionary

person['location'] = 'Narayangonj'
# It will update the value of the key location

print(person)

person['hobbies'].append('Playing')
# It will add the value Playing to the list of hobbies

