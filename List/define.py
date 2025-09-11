# Define a list
myList = [10 , 20, 30, 40, 50]
# Print the list
print(myList)
# Print the type of the list
print(type(myList))
# Print the length of the list
print(len(myList))  
# Printing the zeroth index
print(myList[0])
# Printing the last index
print(myList[-1])
print(myList[len(myList)-1])  # Last index using length function
# Printing the second last index
print(myList[-2])
print(myList[len(myList)-2])  # Second last index using length function
# Define a list with different data types
myList2 = [10, "Hello", 20.5, True]
print(myList2)
print(type(myList2))
print(len(myList2))
# Define a nested list
nestedList = [10, 20, [30, 40], 50]
print(nestedList)
print(type(nestedList))
print(len(nestedList))

myList3 = [1, 2, 3, 4, 5]
myList3.append(6)  # Adding an element to the end of the list
print(myList3) 
myList3.insert(1, 49)  # Inserting an element at the beginning of the list
print(myList3)
myList3.remove(3)  # Removing an element from the list
print(myList3)
myList3.pop()  # Removing the last element from the list
print(myList3)