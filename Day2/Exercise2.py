###---------------------------------------------###
## Write a program that returns a list which contains common elements from two lists.
## Avoid the duplicate elements from lists.
## For example
## a = [1, 1, 3, 5, 7, 9, 9]
## b = [2, 1, 6 ,9, 2, 1, 3, 5]
## The result should be [1, 3, 5, 9]
## Note: You cannot use if-else statement here.

a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6, 9, 2, 1, 3, 5]

set_a = set(a) ##We have to convert list into set to remove duplicate elements.
set_b = set(b) 

common_elements = set_a & set_b ##This is to get common elements between two sets.
##Since common_element is in the form of set, we need to convert back into list form.

result = list(common_elements) ##We need our result in list form according to question.

print("First list :", a)
print("Second list :", b)

print("The common elements between both list are :", result)

##Output
##First list : [1, 1, 3, 5, 7, 9, 9]
##Second list : [2, 1, 6, 9, 2, 1, 3, 5]
##The common elements between both list are : [1, 3, 5, 9]

