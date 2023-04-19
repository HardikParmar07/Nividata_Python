# Python – Convert key-values list to flat dictionary
di1 = {'month' : [1, 2, 3],
       'name' : ['Jan', 'Feb', 'March']}
#1
x=di1.get('month')
y=0
z=di1.get('name')
n_di=dict.fromkeys(x,y)
i=0
for x in n_di:
    n_di[x]=z[i]
    i+=1
print(n_di)
#2
di2 = {'month' : [1, 2, 3],
       'name' : ['Jan', 'Feb', 'March']}
print(dict(zip(di2.get('month'),di2.get('name'))))
#3
di3 = {'month' : [1, 2, 3],
       'name' : ['Jan', 'Feb', 'March']}
a=di3['month']
b=di3['name']
new_dict={}
for i in range(len(a)):
    new_dict[a[i]]=b[i]
print(new_dict)
