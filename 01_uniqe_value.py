# Python – Extract Unique values dictionary values

dict1 = {'gfg': [5, 6, 7, 8],
         'is': [10, 11, 7, 5],
         'best': [6, 12, 10, 8],
         'for': [1, 2, 5]}
#1
li1=[]
for i in dict1.values():
    li1.extend(i)
print(list(set(li1)))
#2
li2=list(sorted({x for i in dict1.values() for x in i}))
print(li2)


