'''
# Feature of the list

-> List need to indicate by [] (I mean defined by [])
-> mutable data type (we can modified the data in List)
-> Store different type of elements
-> Allow the duplicates
-> Allow the indexing


methods
--------------
append
extend
remove
pop
count
index

'''


# v=[]
# print(type(v))

# v=[1,2,4,1,34,55,'gowtham']
# print(v[3])
# print(v[-1])
# print(v[0:4:2]) #  this is called as slice


# ----< append >------------------
# ----------------------------------------------------------
# we want to add one and two values means we can use append


# v=[1,2,4,1,34,55,'gowtham']
# v.append('hi')
# print(v)

# ----< extend >------------------
# ----------------------------------------------------------
# we want to add more and bulk numbers of values means we can use Extend


# v.extend([3,5,778,5555555555,])
# print(v)


#----< count  >------------------
# ----------------------------------------------------------
# we want to know the numbers how many times its repeating in List


# print(v.count(1))


#----< remove  >------------------
# ----------------------------------------------------------
# we want to Remove the number in the list means

# v=[1,2,4,1,34,55,'gowtham']
# v.remove(1)
# print(v)

#----< POP  >------------------
# ----------------------------------------------------------
# we want to Remove the number in the list means based on the index use POP

# v=[1,2,4,1,34,55,'gowtham']
# v.pop(1)
# print(v)



#----< index >------------------
# ----------------------------------------------------------
# based on the element we can display the number index 

# v=[1,2,4,1,34,55,'gowtham']

# print(v.index(4))


#----< insert >------------------
# ----------------------------------------------------------
# perticular location add any number means use insert command

v=[1,2,4,1,34,55,'gowtham']
v.insert(4,"xyz")
print(v)
