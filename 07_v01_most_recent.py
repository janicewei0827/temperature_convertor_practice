#input list
a = []

#ask for inputs
for i in range(5):
    item = input("Enter an item: ")
    a.append(item)
a.reverse()

#The FUll List
print("""
*** The Full List ***
""")
print(a)

#Most Recent 3
print("""
*** Most Recent 3 ***
""")
print(a[:3])
