## Exercise 5. Create a list of any arbitrary elements. ##
## Your code should show the list methods as pop, insert and remove. ##

numbers = [15,25,84,114,56,73,224,35,312,444,90,87]
print("Initial number list :", numbers)

##List methods...

##pop
numbers.pop()
print("Number list after first pop :", numbers)

##insert
print("Insert at 7 :", numbers.insert(7,4567))
print("Number list after insert :", numbers)

##remove

print("Remove number 224 :", numbers.remove(224))
print("Number list after removing number 224 :", numbers)

##Output

## Initial number list : [15, 25, 84, 114, 56, 73, 224, 35, 312, 444, 90, 87]
## Number list after first pop : [15, 25, 84, 114, 56, 73, 224, 35, 312, 444, 90]
## Insert at 7 : None
## Number list after insert : [15, 25, 84, 114, 56, 73, 224, 4567, 35, 312, 444, 90]
## Remove number 224 : None
## Number list after removing number 224 : [15, 25, 84, 114, 56, 73, 4567, 35, 312, 444, 90]
