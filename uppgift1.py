"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding 
instructions clearly without using any shortcuts
"""
# Multiply 3 and any number
def mult(number):
    return number * 3

    
# adds two numbers together
def add(a, b):
    return a + b
    

"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
def sumOfList(someList):
    runningTotal = 0
    for number in someList:
        runningTotal = runningTotal + number
    return runningTotal

# Program checker (do not change the lines below)    
numbers = [1,2,3,6]
assert sumOfList(numbers) == 12
assert sumOfList([1,2,3,8,15]) == 29
assert mult(3) == 9
assert add(1,3) == 4
