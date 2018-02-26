# File Searcher App

## Core Concept: Recursion
A recursive function is a function that is defined iteratively referencing itself until you arrive at a pre-specified stopping point. The factorial function is a recursive function because the the factorial of an integer n, is n times the factorial of n-1. The function repeats until n = 1 (or 0 if you want). See the script play.py. You can also define the fibonacci sequence recursively.  Recursion may actually slow down your application, but it is sometimes simpler to use or necessary. See th book Grocking Algorithms.


### Coroutines
Generator methods are useful when you have lots of data because they allow you to pull one item into memory at a time. They allow you to pull one item at a time into memory. Generator methods use the yield keyword to return values. When the python interpreter encounters the yield keyword, it understands it to create a sequence that we can input to one item at a time.
When the output of a function may be a long list itself you can use the from keyword to return one item at a time.