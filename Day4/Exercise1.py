'''
  Implement question number 2, 3, 4 and 5 from Session 1 Exercise
  as different functions in a single file.
  i.e.
    - Convert fahrenheit to celsius
    - Input seconds as time unit and converts it into minutes and seconds
    - Take list and print it's length with its first and fourth element.
    - Take list and show list methods - pop, insert and remove.
'''

#Fahrenheit to celsius Function
def celsius_value(temperature):
  return ((temperature - 32) * 5)/9

#Time conversion Function
def time_conversion(seconds):
  minute = int(seconds/60)
  result_second = int(((seconds/60) - minute ) * 60)
  print(str(seconds) + " seconds results in " + str(minute) + " minutes and "+ str(result_second) + " seconds.")

#List related Functions
def list_length(my_list):
  return len(my_list)

def show_element(my_list, input_num):
  return my_list[input_num - 1]
  
def insert_number(my_list, pos, num):
  return my_list.insert(pos, num)

#Main Function
def main():
  
  '''Convert degree Fahrenheit into degree celsius'''
  fahrenheit = float(input("Enter the temperature in degree Fahrenheit :"))
  print("It's celsius degree value is :", celsius_value(fahrenheit))

  '''Input seconds as time unit and converts it into minutes and seconds'''
  input_second = int(input("\n Enter the time in seconds :"))
  time_conversion(input_second)


  '''Take list and print it's length with its first and fourth element.
    Take list and show list methods - pop, insert and remove.'''
  
  number = ['17','7','49','78','2','456','198','32','11','45','98','34','56']
  print("\n Given List :\n", number)
  print("Length of list :", list_length(number))

 
  my_position = int(input("Enter position, I will show you the element of that position:"))
  show_element(number, my_position)
  print(str(my_position) + " position of list has number : " + str(show_element(number, my_position)))

  
  check_me = input("Do you want to take out last element? (yes/no) :").lower()
  if check_me == "yes":
    number.pop()
    print("List after removing last element : ", number)
  elif check_me == "no":
    print("No any changes in the list.")
  else:
    print("You entered neither yes nor no. So No changes in the list")


  print("\n Let's insert a number :")
  input_position = int(input("On which position, do you want to put the new number? :"))
  input_number = int(input("Enter number to insert in the list : "))
  insert_number(number, input_position, input_number)
  print("Updated list : \n", number)
  

  print("\n Program finished...")


#Calling main Function
if __name__ == "__main__":
  main()
