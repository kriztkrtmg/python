'''
1. Write a program to display all prime numbers from 1 to 100.
'''

my_list = list()
for i in range(2, 101):
    count = 0
    for j in range(2, i):
        if(i % j == 0):
            count += 1
            break
    if count == 0 :
        my_list.append(i)

print("Prime numbers from 1 to 100 : \n ", my_list)
        
 
         
##Output
##Prime numbers from 1 to 100 : 
##  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
