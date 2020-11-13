'''
Implement question number 1, 2 and 4 from Session 2 Exercise
as different functions in a single (.py) file.
i.e
  - Choose a list with numbers and find sum of all elements
    Note : You cannot use inbuilt sum() function
    
  - Write a program that returns a list which contains common elements
    from two lists.
    Avoid the duplicate elements from lists.
     For example
      a = [1, 1, 3, 5, 7, 9, 9]
      b = [2, 1, 6 ,9, 2, 1, 3, 5]
      The result should be [1, 3, 5, 9]
      Note: You cannot use if-else statement here.
      
  - Write a code to ask an input from the user which is a string
    and display the string along with its length.
    Note: You cannot use len () function here.
'''

#Globals
list1 = [1, 1, 3, 5, 7, 9, 9]
list2 = [2, 1, 6 ,9, 2, 1, 3, 5]

#Function to get sum of all elements of the list.
def my_sum(my_list):
  add_sum = 0
  for i in range(0, len(my_list)):
    add_sum += my_list[i]
  return add_sum

#Function to get common elements between two lists (No duplicates)
def common_elements(first_list, second_list):
  set_1 = set(first_list)
  set_2 = set(second_list)
  get_common = set_1 & set_2
  return list(get_common)

#Function to get a length of the string
def get_length(_string):
  char_count = 0
  for s in _string:
    char_count += 1
  return char_count


def main():
  #To get the sum of all the elements of the list
  print("Given list is : ", list1 )
  print("Sum of all elements of this list :", my_sum(list1))
  print("\n Given list is : ", list2 )
  print("Sum of all elements of this list : ", my_sum(list2))

  #To get common elements between two list (Avoiding the duplicates)
  print("\n Given lists : \n List1 : {} \n List2 : {}".format(list1, list2))
  print("Common elements between these list :", common_elements(list1, list2))

  #Length of string
  my_input = input("Input a string : ")
  print("Length of string :", get_length(my_input))

  print("\n Program Finished...")

if __name__ == "__main__":
  main()
