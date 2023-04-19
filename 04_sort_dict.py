# Ways to sort list of dictionaries by values in Python – Using itemgetter
di1=[{"name": "Nandini", "age": 20},
     {"name": "Manjeet", "age": 20},
     {"name": "Nikhil", "age": 19}]
from operator import itemgetter
print(sorted(di1,key=itemgetter('age')))
print(sorted(di1,key=itemgetter('name','age')))
print(sorted(di1,key=itemgetter("age"),reverse=True))
