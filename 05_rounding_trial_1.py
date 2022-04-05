#rounding non-integer numbers to one dp
#try and except

def rounding_1(from_list):
    try:
        new_number =int(from_list)
        rounded_number = round(new_number,0)
        rounded_numbers.append(rounded_number)

    except ValueError:
        new_number=float(from_list)
        rounded_number = round(new_number,1)
        rounded_numbers.append(rounded_number)


#main routine
numbers=[1,0.5,0.333333333]
rounded_numbers=[]

for item in numbers:
    number= rounding_1(item)

print("****Numbers to Round****")
print(numbers)
print("****Rounded Numbers****")
print(rounded_numbers)
