list1=[1,2,3,3,2,1,4,5]

copy_list=list1.copy()
print (copy_list)
copy_list.reverse()
print(copy_list)

if list1==copy_list:
    print("palindrome:")
else :
    print("not palindrome:")



#count grade a in tuple
# grade=("c","d","a","a","b","b","a") here we take grade as a tuple name
# print(grade.count("a")) and print the tuple