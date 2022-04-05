# Python code to demonstrate deque
from collections import deque

#create an empty deque
a_deque = deque()

#ask for inputs
for i in range(5):
    item = input("Enter an item: ")
    a_deque.appendleft(item)

#The FUll List
print("""
*** The Full List ***
""")
print(a_deque)

#Most Recent 3
print("""
*** Most Recent 3 ***""")
print(a_deque[0])
print(a_deque[1])
print(a_deque[2])




