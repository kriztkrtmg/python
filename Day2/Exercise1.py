###-------------------------###
## Exercise 1 : Choose a list of your choice and find the sum of all elements of that list.
## For example, the sum of [6,9,7,5,4] is 31.
## Note: You cannot use sum () function here

my_list = [6,9,7,5,4]
my_sum = 0
for i in range(0, len(my_list)):
    my_sum += my_list[i]
print("The list given is :", my_list)
print("The sum of all elements of the given list is :", my_sum)

##Output
##The list given is : [6, 9, 7, 5, 4]
##The sum of all elements of the given list is : 31
