# This code defines a list and prints it along with its type.
myList = [10, 20, 30, 40, 50]
print("Original List:", myList , type(myList)) # Output: Original List: [10, 20, 30, 40, 50] <class 'list'>
print(myList[0]) # Output: 10
print(myList[1]) # Output: 20
print(myList[2]) # Output: 30
print(myList[3]) # Output: 40
print(myList[4]) # Output: 50
#print(myList[5]) # This will raise an IndexError since there is no index 5 in the list output: IndexError: list index out of range
print(len(myList)) # Output: 5
print(myList[len(myList)-1]) # Output: 50
print(myList[-1]) # Output: 50
print(myList[-2]) # Output: 40
print(myList[-3]) # Output: 30
print(myList[-4]) # Output: 20
print(myList[-5]) # Output: 10
#print(myList[-6]) # This will raise an IndexError since there is no index -
#in python in a list we can use the data of different types in a single list
myList1 = ["Apple", 10, 20.5, True, [1, 2, 3],1+2j]
print("Original List1:", myList1 , type(myList1)) # Output: Original List1: ['Apple', 10, 20.5, True,