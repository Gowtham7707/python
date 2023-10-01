'''
# Feature of the Set

-> List need to indicate by {} (I mean defined by {})
-> do not allow duplicate
-> No Index
-> un ordered
-> Do not allow the mutable types as set elements




Set methods
----------------------------------
add()
update()
pop()
remove()


Set Operations
-----------------------------------
Union()
Intersection()
different()
issubset()
issuperset()


'''


# s={1,234,13}
# print(type(s))

# ----------------< Unorder >-------------------------------
# s={2,3,5,6,88,4,22,999}
# print(s)



# ----------------< add >-------------------------------
# s={2,3,5,6,88,4,22,999}
# s.add(123)
# print(s)



# ----------------< update >-------------------------------
# bulk data we can data based on the update

# s={2,3,5,6,88,4,22,999}
# s.update({123,67,5555,73})
# print(s)

# ----------------< POP >-------------------------------
# s={2,3,5,6,88,4,22,999}
# s.pop()
# print(s)



# ----------------< POP >-------------------------------
# s={2,3,5,6,88,4,22,999}
# s.remove(2)
# print(s)


# ----------------< UNION >-------------------------------
#  all numbers are come if common number are comes one time(I means without duplicate)
# s1={2,3,5,6}
# s2={2,10,15,16}

# print(s1.union(s2))


# ----------------< INtersection >-------------------------------
# what are the common number in both sets it will be display
# s1={2,3,5,6}
# s2={2,10,15,16}

# print(s1.intersection(s2))


# ----------------< Difference >-------------------------------
# Only set1 will be display
# s1={2,3,5,6}
# s2={2,10,15,16}

# print(s1.difference(s2))

# ----------------< issuperset >-------------------------------
# the s1 data completly have s2 means then only its True otherwise false
# s1={2,3,5,6}
# s2={2,10,15,16}

# print(s1.issuperset(s2))

# ----------------< issubset >-------------------------------

# the s2 data completly have s1 means then only its True otherwise false

# s1={2,3,5,6}
# s2={2,10,15,16}

# print(s2.issubset(s1))


# for i in {2,4,5,7,8}:
#     print(i)