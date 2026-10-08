#set is collection of the unorder uique value
#it is mutable but its item should not be mutable eg [], and {}
set1 = {1,2,1,"nitan",2.9,(1,2)}
print(set1)

#it does not have index concept

#converting set to list 
print(list(set1))


#convertin  list to set 
print(set([1,2,3,4,5]))

#adding 
s1 = {1,2,3}
s1.add(4)
print(s1)

#removing  value 
s2 = {1,2,3}
s2.remove(2)
print(s2)#{1,3}

#remove random element
#remove random element  (unlink pop in list it remove random element and return poped elemnet )
s2 = {3,5,1,2,3}
s2.pop()
print(s2)

#removing duplicate value from the list
l1 = [1,2,3,1]
print(list(set(l1)))


