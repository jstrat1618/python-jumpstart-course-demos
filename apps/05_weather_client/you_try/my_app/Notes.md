# Weather Client
This app will allow the user to enter a zip code an get the forecast in that area. We will get the weather info from https://www.wunderground.com/.


## Core Concept: PyPI (Python Package Index)
PyPI (Pronounced like "Pie P.I.")houses thousands packages for all sorts of tasks. Sometimes people refer to PyPI as "PyPy" but this can create confusion because there is an implementation of Python called PyPy. Sometimes people refer to it as the "Cheese Shop" referencing  Monty Python.
PyPI can be found at https://pypi.python.org/pypi. 

## Core Concept: pip
pip allows you to get packages from pypi and their dependencies. 
To install a package with pip you just call "pip install (package)." On windows, depening on how python is installed you may have to use "sudo pip install" if python is installed under your user profile and not the root.
You can see what packages you have installed using "pip list".

## Core Concept: Slicing
You can slice through lists in python easily. Remember python is a 0th iterable language so the first item is indexed by 0. 
A colon is used to denote a range of indices, e.g. x\[0:1\] prints the first two elements of x. A colon with an unspecified index at the beginning or end assumes the first or last element respectively.
You can also use negative indices in python, e.g x\[-1\] denotes the last element of x.

### Examples
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]  

first_prime = nums[0] #2    
last_prime = nums[-1] #23    
lowest4 = nums[0:4] #[2, 3, 5, 7]    
lowest4 = nums[:4] #[2, 3, 5, 7]    

middle = nums[3:6] #[7, 11, 13, 17]    

last4 = nums[5:9] #[13, 17, 19, 23]    
last4 = nums[5:] #[13, 17, 19, 23]    
last4 = nums[-4:] #[13, 17, 19, 23]   

## Core Concept: tuples
Tuples are similar to lists but more rigid in that you cannot change any of the elements, take away elements or append elements. 

Commas define tuples. e.g. x = 1,2 defines the tuple (1,2). Sometimes parentheses are shown for good measure x=(1,2) to show more clearly that it is a tuple.

Tuples can be unpacked easily by assigning the appropriate number of variables to a tuple. E.g a,b = x assigns the first element of x to a and the second element of x to b. This won't work if the x is not a 2-dimensional tuple.


x = 1,2,3         
x[0] #1    
x[1:3]#(2,3)    
a,b,c =x # assigns a to 1, b to 2, and c to 3    
x[0]=1 #causes an error


#### Named Tuples
 You can use named tuples from the collections module to help assure you use the correct elements of the tuple. All the indexing and methods of tuples still apply, but you can refer to the elements of a tuple by named attributes.
 
import collections   

WeatherReport = collections.namedtuple("WeatherReport", "condition, temp, scale, location")

report = WeatherReport(temp=72, condition="Cloudy", scale="F", location="El Paso")    
report.loc #returns "El Paso"




