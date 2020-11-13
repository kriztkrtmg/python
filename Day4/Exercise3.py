'''Implement question number 1, 2 and 6 from Session 3 Exercise
as different functions in a single(.py) file.
i.e
  - Write a program to display all prime numbers from 1 to 100.
      Lets ask user to enter the number.
      And print all prime numbers from 1 to that number.
  
  - Ask the user for a string and print out
      whether this string is a palindrome or not.
      
  - Create a dictionary that has a key value pair of letters
    and the number of occurrences of that letter in a string.
    
    Given a string “pineapple”. The result should be as:
    {“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
'''

#Function for prime number

def _prime(num):
  list1 = list()
  for i in range(2, num):
    count = 0
    for j in range(2, i):
      if(i % j == 0):
        count += 1
        break
    if count == 0:
      list1.append(i)
  return list1

'''--------------------------------------'''

#Function to check palindrome

def check_palindrome(get_input_string):
  string_to_list = list(get_input_string)
  flip_list = string_to_list[::-1]
  list_to_string = "".join(flip_list)
  if list_to_string == get_input_string:
    print("{} is a palindrome".format(get_input_string))
  else:
    print("{} is a not palindrome".format(get_input_string))

'''-------------------------------------------------------------'''

#Function to create dictionary from a string in which key = letter, value = no. of occurrences of that letter

def my_dictionary(lets_get_input_string):
  create_dictionary = dict()
  create_list = list()
  count = 0
  my_unique_list = list(set(lets_get_input_string))
  my_unique_list.sort()
  for i in range(0, len(my_unique_list)):
    for j in range(0, len(lets_get_input_string)):
      if my_unique_list[i] == lets_get_input_string[j]:
        count += 1
    create_list.append(count)
    count = 0
    
  for i in range(0, len(my_unique_list)):
    create_dictionary[my_unique_list[i]] = create_list[i]
  return create_dictionary


'''----------------------------------------------------------'''

def main():
  #Prime numbers
  number = int(input("Enter a number. I will display all the prime numbers from 1 to this number :"))
  print("Prime numbers from 1 to " + str(number) + " are : \n", _prime(number))

  #Palindrome section
  _input = input("\n Enter a string to check palindrome : ")
  check_palindrome(_input)
  
  #Create dictionary from a string, that has key = letter , value = no. of occurrences of letter
  my_input = input("\n Enter a string : ")
  print("Letter and it's number of occurrences in the string :\n", my_dictionary(my_input))

if __name__ == "__main__":
  main()
