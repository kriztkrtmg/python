
 '''Write a code to ask an input from the user which is a string.
 And display the string along with its length.
 Note: You cannot use len () function here.'''


my_input = input("Input a string :")
print("Your input string is :", my_input)


char_count = 0
##To count the number of characters in the string, we use for loop here.
for s in my_input:
    char_count += 1
print("Length of given string is :", char_count)


##Output
##Your input string is : Heaven is myth, Nepal is real
##Length of given string is : 29


    
