# Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
print(od)
od.pop('c')
od.update({'c':0})
od.move_to_end('c',last=False)
print(od)

# from collections import OrderedDict
# od=OrderedDict([('a',1),('b',2),('c',3)])
# print(od)
# x=[('d',4),('e',5)]
# od.update(x)
# print(od)
# od.move_to_end('d',last=False)
# for key,values in od.items():
#     print(key,values)
