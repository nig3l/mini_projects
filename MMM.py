# calculating mean ,mode & median

# mean
# list = [1,2,3,4,5,6,11,12,23,45]
# mean = sum(list)/len(list)
# print(mean)

# median
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2

else:
    median = list1[len(list1)//2]

print(median)


