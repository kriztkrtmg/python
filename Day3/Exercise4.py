'''4. Write a program to display the n terms of harmonic series and their sum.
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n '''

my_input = int(input("Input a number :"))

sum = 0
for i in range(1, (my_input + 1)):
    sum = sum + (1/i)

print("Sum of Harmonic series till {} is :".format(my_input), sum)

##Output
##Input a number : 5
##Sum of Harmonic series till 5 is : 2.283333333333333
