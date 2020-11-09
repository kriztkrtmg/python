'''2. Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

my_input = input("Enter a string to check palindrome : ")

string_to_list = list(my_input)

flip_list = string_to_list[::-1]

list_to_string = "".join(flip_list)

if list_to_string == my_input :
    print("{} is a palindrome".format(my_input))
else:
    print("{} is a not palindrome".format(my_input))


##Output
##Enter a string to check palindrome : banana
##banana is a not palindrome
