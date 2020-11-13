
''' Suppose you have a list [1, 5, 7, 12 ,15]
 Print each number using loop.
 Also, print the square of each number using loop'''

my_list = [1, 5, 7, 12, 15]

for element in range(0, len(my_list)):
    print("Given element :", my_list[element], end = " ")
    print("Square of given element :", my_list[element] ** 2)

##Output
##Given element : 1 Square of given element : 1
##Given element : 5 Square of given element : 25
##Given element : 7 Square of given element : 49
##Given element : 12 Square of given element : 144
##Given element : 15 Square of given element : 225
