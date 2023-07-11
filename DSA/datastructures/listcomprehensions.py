# note to self : every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.




#  want to separate the letters of the word human and add the letters as items of a list. 
# in a for loop this is how it would look

'''h_letter = []

for letter in 'human':
    h_letter.append(letter)

print(h_letter)

'''
# now to use LIST 'COMPREHENSIONS'

h_letter = [letter for letter in 'human']
print(h_letter)

# conditionals within this elegant syntax

number_list = [x for x in range(20) if x % 2 == 0 ]
print(number_list)

# nested IF with list comprehension
# if y satisfies both conditions its appended to the list

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0] 
print(num_list)

# if...else With List Comprehension

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(20)]
print(obj)
