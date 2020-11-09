'''3. Given a string, count all lower case, upper case, digits and special symbols.'''

my_input = input("Enter anything you like :")

string_to_list = list(my_input)

lowercase = 0
uppercase = 0
digits = 0
special_symbol = 0

for i in range(0, len(string_to_list)):
    if string_to_list[i].isdigit():
        digits += 1
    elif string_to_list[i].isalpha():
        if string_to_list[i].isupper():
            uppercase += 1
        else:
            lowercase += 1
    else:
        special_symbol += 1

print("Your input is : {}".format(my_input))
print("No of lowercase : ", lowercase)
print("No of uppercase : ", uppercase)
print("No of digits : ", digits)
print("No of special_symbol :", special_symbol)

        
