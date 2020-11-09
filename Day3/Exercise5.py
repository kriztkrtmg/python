'''---------
5. Write a program to display the following pattern.
Check also with different number of rows.
     *
    **
   ***
  ****
 *****
 ----------------'''
my_input = int(input("Enter number of rows needed :"))

for i in range(1, my_input + 1):
    for j in range(0, my_input - i):
        print(" ", end = " ")
    for k in range(0, i):
        print("*", end = " ")
    print()

