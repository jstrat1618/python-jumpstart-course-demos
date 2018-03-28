## *args and **kwargs   
*args are non-keyword arguments. It is very useful when you may supply an indefinite number of un-named arguments. The name "*args" is just a conventional name. When you use *args inside the function you do not use the "*" the function.  For example see play.add we add up all the arguments in *args except we don't call the variable *args, instead we call it *arg_vars.

**kwargs is short for "keyword" arguments. The name is merely "kwargs" is merely a convention. **kwargs allow you to pass multiple KEYWORD arguments. You can iterate through both the values and variable names of **kwargs by using the method kwargs.items() which produces a tuples with the variable names and values. See the method print_kwargs(). **kwargs is also useful when you want to supply an object with the appropriate names to a function with the corresponding names. For example, the named tuple. in movie_svc.find_movie we create a list of movies using the following line: movies = [MovieResult(**md) for md in movie_list].


## try/except
try/except blocks allow you to catch multiple exceptions. The syntax of try/catch is as follows:

try:    
    method1()    
    method2()
    
except ConnectionError as ce:    
    some commands     
except OtherException as other:    
    some commands
    
The order is very important. You should go from most specific to least specific errors.
