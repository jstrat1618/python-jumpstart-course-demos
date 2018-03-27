## **kwargs
**kwargs is short for "keyword" arguments. The name is merely "kwargs" is merely a convention. **kwargs allow you to pass multiple KEYWORD arguments.

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
