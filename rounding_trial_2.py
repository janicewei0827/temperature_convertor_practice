#Display output using int/float


to_round= [1, 0.5, 0.333333]
print("****Numbers to Round****")
print(to_round)

print()
print("****Rounded Numbers****")

for item in to_round:
    if item%1 == 0:
        print("{:.0f}".format(item))
    else:
        print("{:.1f}".format(item))

