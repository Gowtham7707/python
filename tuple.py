'''
# Feature of the Tuple

-> List need to indicate by () (I mean defined by ())
-> Store different type of elements
-> Allow the duplicates
-> Allow the indexing
-> immutable data type (we can't change the data in tuple)
-> No methods we can use builtin

Tuple operation
----------------------------------

-> concatenation
-> Iteration
-> membership operation
-> identity operation
-> repetation -> example: t2=(1,2) -> t2*5 -> (1,2,1,2,1,2,1,2)




'''

# v=()
# print(type(v))
# v=(1,2,4,1,34,55)
# print(v[3])
# print(v[-1])
# print(v[0:4:2]) #  this is called as slice


# print(max(v))
# print(min(v))
# print(sum(v))
# print(len(v))

# ----< concatenation >------------------
# ----------------------------------------------------------
# we want to add t1 and t2 values means we can use concatenation

# t1=(1,2,3)
# t2=(4,2,7)
# print(t1+t2)

# ----< repetation >------------------
# ----------------------------------------------------------
# we want to add t1*5 values means we can use repetation
# example:
# t2=(1,2) 
# t2*5 
# (1,2,1,2,1,2,1,2)

# t1=(1,2,3)
# print(t1*5)

# ----< Iteration >------------------
# ----------------------------------------------------------
# we want to use for loop  means we can use Iteration

# t1=(1,2,3)

# for i in t1:
#     print(i)


# ----< membership operation >------------------
# ----------------------------------------------------------
# we want to use "in or not in"  means we can use Iteration

# v=(1,2,4,1,34,55)

# print(2 in v)
# print(11 not in v)

# t1=(1,2,3)
# t2=(4,2,7)

# print(t1 is not t2)