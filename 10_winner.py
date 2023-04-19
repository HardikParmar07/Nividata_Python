# Dictionary and counter in Python to find winner of election
#1
votes = ["john", "johnny", "jackie", 
        "johnny", "john", "jackie", 
        "jamie", "jamie", "john","jackie",
        "johnny", "jamie", "johnny", 
        "john",]
di={}
for i in range(len(votes)):
    if votes[i] not in di.keys():
        di[votes[i]]=1
    else:
        di[votes[i]]+=1
# print(di)
x=sorted(di.items(),reverse=True)
# print(x)
y=''
for i in range(len(x)-1):
    if x[i][1]>=x[0][1] and  x[i][1]==x[i+1][1]:
        y=min(x[i][0],x[i+1][0])
print(y)
#2
from collections import Counter
input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']
votes=Counter(input)
dict={}
for value in votes.values():
    dict[value]=[]
for key,value in votes.items():
    dict[value].append(key)
maxVotes=list(sorted(dict,reverse=True))[0]
if len(dict[maxVotes])>1:
    print(sorted(dict[maxVotes])[0])
else:
    print(dict[maxVotes])


