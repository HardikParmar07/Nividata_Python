# #winner in election
# from collections import Counter
# votes = ["john", "johnny", "jackie", 
#         "johnny", "john", "jackie", 
#         "jamie", "jamie", "john","jackie",
#         "johnny", "jamie", "johnny", 
#         "john",]
# votes=Counter(votes)
# print(votes)
# dict={}
# for i in votes.values():
#     dict[i]=[]
# print(dict)
# for key,value in votes.items():
#     dict[value].append(key)
# print(dict)
# maxVotes=list(sorted(dict,reverse=True))[0]
# print(maxVotes)
# if len(dict[maxVotes])>=1:
#     print(sorted(dict[maxVotes])[0])
# else:
#     print(dict[maxVotes])


# # Python – Append Dictionary Keys and Values ( In order ) in dictionary
# # Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3} 
# # Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3] 
# # Explanation : All the keys before all the values in list.
# di1={'Gfg':1,'is':2,'Best':3}
# l1=[]
# l2=[]
# for key,value in di1.items():
#     l1.append(key)
#     l2.append(value)
# l1.extend(l2)
# print(l1)


# # Python | Sort Python Dictionaries by Key or Value
# # Input: {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# # Output:{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
# di1={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# # li=[]
# # for i in di1.items():
# #     li.append(i[0])
# li=list(di1.keys())
# li.sort()
# print(li)
# # di2={}
# # for i in range(len(li)):
# #     di2[li[i]]=di1[li[i]]
# di2={i:di1[i] for i in li}
# print(di2)


# #sorting on the basis of values.
# di3={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# di4={}
# for key,value in di3.items():
#     di4[value]=key
# print(di4)
# li=[]
# for i in di4.items():
#     li.append(i[0])
# li.sort()
# print(li)
# di5={}
# for i in range(len(li)):
#     di5[li[i]]=di4[li[i]]
# di6={}
# for key,value in di5.items():
#     di6[value]=key
# print(di6)

# di3={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# di4=sorted(di3,key=di3.values())
# print(di4)


# # Python – Sort Dictionary key and values List
# # Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]} 
# # Output : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]} 
# # Input : test_dict = {‘c’: [10, 34, 3]} Output : {‘c’: [3, 10, 34]}

# di1={'c':[3],'b':[12,10],'a':[19,4]}
# # {'c': [10, 34, 3]}
# li=dict(sorted(di1.items()))
# print(li)
# for i in li.values():
#     i.sort()
# print(li)

# # Handling missing keys in Python dictionaries
# #1
# di1 = {'India' : '0091',
#                 'Australia' : '0025',
#                 'Nepal' : '00977'}
# print(di1.get('India','Not found'))
# print(di1.get('Japan','Not Found'))
# #2
# di1.setdefault('Japan','Not in this')
# print(di1['Japan'])

# # Python dictionary with keys having multiple inputs
# di1={}
# n=int(input("How many k:v pair : "))
# for i in range(n):
#     x=int(input("Enter x : "))
#     y=int(input("Enter y : "))
#     z=int(input("Enter z : "))
#     di1[x,y,z]=x+y-z
# print(di1)

# # Print anagrams together in Python using List and Dictionary
# # Input: arr = ['cat', 'dog', 'tac', 'god', 'act']
# # Output: 'cat tac act dog god'
# input = ['cat', 'dog', 'tac', 'god', 'act']
# di={}
# for i in input:
#     key=''.join(sorted(i))
#     if key in di.keys():
#         di[key].append(i)
#     else:
#         di[key]=[]
#         di[key].append(i)
# print(di)
# s=''
# for i in di.values():
#     s=s+" ".join(i)+" "
# print(s)


# # K'th Non-repeating Character in Python using List Comprehension and OrderedDict
# # Input : str = geeksforgeeks, k = 3
# # Output : r
# # First non-repeating character is f,
# # second is o and third is r.
# #1
# str = 'geeksforgeeks' 
# k = 3
# j=0
# for i in range(len(str)):
#     if str[i] not in str[0:i]+str[i+1:]:
#         j=j+1
#         if j==3:
#             print(str[i])
# #2
# str = 'geeksforgeeks' 
# k = 3
# di=dict.fromkeys(str,0)
# for i in str:
#     di[i]+=1
# nonRep=[key for key,value in di.items() if value==1]
# if len(nonRep)<k:
#     print("kth repeting not [present in this")
# else:
#     print(nonRep[k-1])  


# # Check if binary representations of two numbers are anagram
# # Input : a = 8, b = 4 
# # Output : Yes
# # Binary representations of both
# # numbers have same 0s and 1s.
# from collections import Counter
# a = 8
# b =4
# bi1=bin(a)[2:]
# bi2=bin(b)[2:]
# zeros=abs(len(bi1)-len(bi2))
# if len(bi1)<len(bi2):
#     bi1=zeros*'0'+bi1
# else:
#     bi2=zeros*'0'+bi2
# di1=Counter(bi1)
# print(di1)
# di2=Counter(bi2)
# print(di2)
# if di1==di2:
#     print("Yes, It is Anagram.")
# else:
#     print("No, It is not Anagram.")


# # Python Counter to find the size of largest subset of anagram words
# from collections import Counter
# input = 'ant magenta magnate tan gnamate'
# li=input.split()
# for i in range(len(li)):
#     li[i]="".join(sorted(li[i]))
# di=Counter(li)
# print(max(di.values()))


# # Python | Remove all duplicates words from a given sentence
# s1='My name is Hardik Parmar . Hardik Parmar is from LDCE and LDCE is Government College .'
# s=s1.split()
# string=''
# for i in range(len(s)):
#     if s[i] not in string:
#         string+=s[i]+" "
# print(string)
# print(" ".join(set(s1.split())))


# # Python Dictionary to find mirror characters in a string
# # Input : N = 3
# #         paradox
# # Output : paizwlc
# # We mirror characters from position 3 to end.

# orignal='abcdefghijklmnopqrstuvwxyz'
# reverse='zyxwvutsrqponmlkjihgfedcba'
# revDict=dict(zip(orignal,reverse))  
# ip='paradox'
# n=3
# output=ip[0:n-1]
# for i in range(n-1,len(ip)):
#     output+=revDict[ip[i]]
# print(output)


# # Counting the frequencies in a list using dictionary in Python
# from collections import Counter
# input = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# print(Counter(input))


# # Python | Convert a list of Tuples into Dictionary
# Input = [("akash", 10), ("gaurav", 12), ("anand", 14), 
#          ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# print(dict(Input))


# # Python counter and dictionary intersection example 
# # (Make a string using deletion and rearrangement)
# #1
# from collections import Counter
# s1 = 'ABHISHEKsinGH'
# s2 = 'gfhfBHkooIHnfndSHEKsiAnG'
# di1= Counter(sorted(s1))
# di2= Counter(sorted(s2))
# print(di1)
# print(di2)
# result =di2 & di1
# if result==di1:
#     print('Possible')
# else:
#     print('Not possible')
# #2
# from collections import Counter
# s1 = 'ABHISHEKsinGH'
# s2 = 'gfhfBHkooIHnfndSHEKsiAnG'
# di1= Counter(sorted(s1))
# di2= Counter(sorted(s2))
# print(di1)
# print(di2)
# print(set(di1.keys()).issubset(set(di2.keys())))
# print(set(s1).issubset(set(s2)))


#Python dictionary, set and counter to check if frequencies can become same
from collections import Counter
str = 'yyyyyzzz'

di1=Counter(str)
print(di1)

l1=list(set(di1.values()))
if len(l1)>2:
    print("No")
elif len(l1)==2 and l1[1]-l1[0]>1:
    print("No")
else:
    print("Yes")