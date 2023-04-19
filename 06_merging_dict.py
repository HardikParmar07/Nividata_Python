# Python | Merging two Dictionaries
di1={'Stark':100,'Captain':95,'Loky':75,'Peter':90,'Thor':100}
di2={'Mike':200,'Rohit':300,'Virat':420,'Pant':350}
# #1
# di1.update(di2)
# print(di1)
#2
for i in di2:
    di1[i]=di2.get(i)
print(di1)

