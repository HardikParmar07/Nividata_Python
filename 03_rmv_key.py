# Python | Ways to remove a key from dictionary
di1={'Stark':100,'Captain':95,'Loky':75,'Peter':90,'Thor':100}
#1
del di1['Loky']
print(di1)
#2
x=di1.pop('Loky','Key not found')
print(x)
print(di1)


