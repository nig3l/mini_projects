def find_missing_number(n):
    number = set(n)
    #length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in number:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(find_missing_number(listOfNumbers))

# n = (1,1,1.3,3,6,7,8,9,10)
# sort = set(n)
# print(sort)
#set function creates a set by removing all duplicatable elements from the iterable
