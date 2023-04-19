# Python | Check order of character in string using OrderedDict( )
from collections import OrderedDict
def od(input,pattern):
    od=OrderedDict.fromkeys(input)
    ptrln=0
    for key,value in od.items():
        if key==pattern[ptrln]:
            ptrln+=1
        if ptrln==len(pattern):
            return 'True'
    return 'False'
print(od("engineers rock","er"))