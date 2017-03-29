import random
__author__ = 'Dom'
"""
write a program that returns a list that contains only the elements that are common between the lists

"""


#Two random lists generated with random lengths
len1 = random.sample(range(1, 12), 1)
len2 = random.sample(range(1, 12), 1)

a = random.sample(range(1, 25), len1[0])
b = random.sample(range(1, 25), len2[0])


def com(list1, list2):
    common = []
    for i in range(0,len(a)):
        for j in range(0, len(b)):
            if list1[i] == list2[j]:
                common.append(list1[i])
    return common;
print(a)
print(b)
print(com(a,b))