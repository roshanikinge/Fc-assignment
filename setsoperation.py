
#set ={} ne open and close hote

set=set()#here we print the empty sets
print(set)
set1={1,3,4,5,"hello","world",2,3,4}#here we print the sets we
# can print tuple boolean int float in set but list and dict can't pass into sets
print(set1)
print(len(set1)) #print the length of sets
print(type(set1))

#methods in set
set1.add("rk") #add element into sets
print(set1)

set1.remove(4) #remove specific element into sets
print(set1) #if non exist element try  to remove it gives error i.e keyerror
set1.pop()#remove random value into the sets
print(set1)
# set1.clear()#clear all set values
# print(set1)

set2={1,2,3,4,5}
print(set2)
print(set1.union(set2))#print all element into both sets
print(set1.intersection(set2))#print same element into both sets









