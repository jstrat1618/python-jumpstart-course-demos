# Birthday App
This is an app that will let the user enter user's birthday, then will compute how many days until the user's birthday?

## Function definitions
We first sketched out the app with the function definitions and supplying only the pass to the function body. The pass keyword stops python from executing the code in that function, and lets us know that we have yet to supply the body.
All functions in python are defined with the keyword def.

Some programming languages require you to create a method called main. Python does not, but people often do sometimes only for the sake of convention.


## Dates
To create this app we'll use the datetime module. We'll call import datetime at the top.
The datetime module has a class date that is great for working with dates when you only have the month, year, and day. 
Use a different module if you only have something like just the time.

The date class has a today method that returns the today's date.


## PyCharm Debugger
In Pycharm if you click inside the "gutter" (the space between the numbers on the left and the text inside the editor), you will set a stopping point. You can click it again to remove the stopping point. When a stopping point is placed you can click the bug in the top right corner. It will run the code but pause where the stopping points were placed. You can then step through, step over, step into and step out of functions and see what variables are being created.
