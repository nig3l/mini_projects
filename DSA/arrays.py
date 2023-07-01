from array import *

# array1 = array('i', [10,20,30,40,50])   #'i'specifies that its an integer

'''
for x in array1:
    print (x)
'''


# accessing array elements

'''
print(array1[0])
print(array1[4])

'''

# Insertion
'''
array1.insert(1,90)

for x in array1:
    print(x)

'''

# search operation
''' 
print (array1.index(50))

'''


# 2D ARRAYS
# is an array within an array

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
'''
print(T[3])

print(T[1][2])

'''
# to print the entire two dimensional array,wihtout the brackets like the second method
'''
for r in T:
   for c in r:
      print(c,end = " ")
   print()

'''

# still works

# for x in T:
#     print(x,end = " ")


# inserting values

T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
      print(c,end = " ")
   print()



# updating values

T[2] = [11,9]
T[0][3] = 7
for r in T:
   for c in r:
      print(c,end = " ")
   print()

# Deleting values

del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()