#List comprehension 
#syntax: [expression for item in iterable if condition]
myList = [ele for ele in range(5)]
print(myList)
# Output: [0, 1, 2, 3, 4]
squaredList = [ele*2 for ele in range(5)]
print(squaredList)
# Output: [0, 2, 4, 6, 8]
myList1 = [ele for ele in input().split()]
print(myList1)