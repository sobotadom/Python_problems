__author__ = 'Dom'
#creating a new list from input

list = [1,1,2,3,5,8,13,21,34,55,89]
list2 = []

a = int(input('give a number\n'))

for i in range(0, len(list)):
    if(list[i] >= a):
        list2.append(list[i])

print(list2)