'''Exercise 3. Write a program that takes seconds as time units and converts it to minutes and seconds.'''

input_second = input("Enter the time in seconds :")
second = int(input_second)
minute = int(second/60)
result_second = int(((second/60) - minute ) * 60)

print(input_second + " seconds results in " + str(minute) + " minutes and "+ str(result_second) + " seconds.")


##output
## Enter the time in seconds :100
## 100 seconds results in 1 minutes and 40 seconds.
