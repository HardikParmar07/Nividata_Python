# Ways to sort list of dictionaries by values in Python – Using lambda function
di1=[{"name": "Nandini", "age": 20},
     {"name": "Manjeet", "age": 20},
     {"name": "Nikhil", "age": 19}]
li1 = list(sorted(di1, key=lambda x:x['age']))
print(li1)
li2=list(sorted(di1,key=lambda x:(x['name'],x['age'])))
print(li2)