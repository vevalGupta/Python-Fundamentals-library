import os; os.system('cls')
# SETs(non duplication)
#    /    \
# Empty   filled
# Empty set 
empset = set()
# filled Set
s={34,56,67}
print(type(s))
# method
empset.add(56)# used to add element in set
print(empset)
# empset.discard(1)# no action taken if element no found
print(empset)
# UNION
print(s.union(empset))
# INTERSECTION
print(s.intersection(empset))
# difference
print(s.difference(empset)) # s-empty
print(empset.difference(s)) # empty - s
print(s.symmetric_difference(empset))