# Real Estate App

##Core Concept: Dictionaries
Dictionaries store data through values called keys. There are several ways to define a dictionary. For example we can define a dictionary with keys "age" and "loc" with values "42" and "Italy" respectively as follows.

lookup = {"age":42, "loc":"Italy"}   
lookup = dict(age=42, loc="Italy")

The values do not have to be the same data type at all, they can be lists, tuples, or even other dictionaries.

As opposed to lists, you can lookup the value of a certain object using the keys rather than numbers. For example, we can find the location by running
print(lookup['loc'])

You can add values later after a dictionary simply as follows 

lookup['cat']='Fun Code Demo' 

You can check if a value is in a dictioray as follows:    
if 'cat' in lookup:    
        print(lookup['cat'])
        
When you define a class as we did for the Wizard class two apps ago, python actually interprets the attributes of that class through dictionaries.  IN FACT ALL OBJECTS ARE BUILT ON THE CONCEPT OF DICTIONARIES. In fact you can even inspect the dictionary representation of an object using \_\_dict__. See the example in play_dictionaries.py.

You can also use dictionaries to lookup objects by certain properties. For example, in play_dictionaries we have a list of named tuples. We then create a dictionary and input data into that dictionary with the user id being the dictionary then lookup the user with a particular ID. However, the key must be unique. If you input one user with id 2, then input another user with id 2, python will interpret this to mean you are updating user 2. 


## Core Concept: lambdas
Lambdas are small methods that you often only want to use once for  very specific purpose.
For example lambda x: x % 2 == 1 returns True or False if x % 2 ==1 holds True (If x is odd). 


## Core Concept: Python 2 and 3
You can use try/except to import modules that may not be available on earlier versions of python. Notice the keyword as helps import the module with a different name so you can keep the same name as the module of the module.

## Concept: List Comprehensions
A list comprehension allows you to write in a single list based on a loop of iterable object. Here are some examples:

data = [1,2,3,4,5,6]

x1 = [x for x in data] #will set x1 = data

x2 = [x+1 for x in data] # will set x2 = data +1

z = [x for x in data if x % 2 == 0] # list the even numbers in data


# Generator Expressions
Generator expressions are like list comprehensions, but for coroutines instead of lists. They allow you application to only process one item at a time in memory.
() indicate a generator expression. E.g    
paying_usernames = (
u.name 
for u in get_active_users():   
if u.last_purchase == today
)

## Concept: Data Pipelines with Generators
Applying multiple generators can help establish efficient data pipelines. For example, you may have one generator that loops through a bunch of data and pulls out a particular subset. You may then have another generator that loops through that subset and returns a smaller subset or splits that subset into other subsets, and so forth.