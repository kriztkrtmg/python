'''----------
6. Create a dictionary that has a key value pair of letters and the number of occurrences of
that letter in a string.
Given a string “pineapple”. The result should be as:
{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
Don’t worry about the order of occurrence of letters.
------------'''

my_input = input("Enter a string : ")   #pineapple

# conveting string to list
str_to_list = list(my_input)        # ['p','i','n','e','a','p','p','l','e']

#convering list to set to remove duplicates
list_to_set = set(str_to_list)      # {'l', 'p', 'e', 'i', 'a', 'n'}

#converting set to list for sorting
set_to_list = list(list_to_set)     # ['l', 'p', 'e', 'i', 'a', 'n']

#sorting list values in ascending order
set_to_list.sort()              # ['a', 'e', 'i', 'l', 'n', 'p']

#To get number of occurrences of letter in a string
my_value = list()
count = 0
for i in range(0, len(set_to_list)):
    for j in range(0, len(str_to_list)):
        if set_to_list[i] == str_to_list[j]:
            count += 1
    my_value.append(count)
    count = 0

#We got both keys and respective values, now we just have to put it in the empty dictionary

my_dictionary = dict()
for i in range(0, len(set_to_list)):
    my_dictionary[set_to_list[i]] = my_value[i]

print("Letter and it's number of occurrences in the string : \n ", my_dictionary)


##Output
##Enter a string : pineapple
##Letter and it's number of occurrences in the string :
##  {'a': 1, 'e': 2, 'i': 1, 'l': 1, 'n': 1, 'p': 3}













