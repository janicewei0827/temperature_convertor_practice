#Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth','seventh']

#Get filename, can't be blank/ invalid
#assume valid data for now
filename = input("Entered a Filenmae (leave off the extension): ")

#add .txt suffix!
filename = filename

#create file to hold data
f = open(filename, "w+")

#add new line at end of each item
for item in data:
    f.write(item + "\n")

#close file
f.close()
