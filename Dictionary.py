'''
# Feature of the Dictionary

-> List need to indicate by {} (I mean defined by {})
-> key , value data (k:v)
-> key should be immutable
-> value is mutable
-> key will ask as Index
-> No slicing
-> keys are unique



method
------------------------------------------------
-> get()
-> update()
-> values()
-> keys()
-> Items()


'''


# v={}
# print(type(v))

# d={1:"abc","gowtham":2}
# print(d[1])
# print(d.get(1))
# print(d.keys())
# print(d.values())
# print(d.items())
# d.update({111:222})
# print(d)


# for i in {1:"abc","gowtham":2}.keys():
#    print(i)
   
   
# for i in {1:"abc","gowtham":2}.values():
#    print(i)
   
for i,j in {1:"abc","gowtham":2}.items():
   print(i,j)   