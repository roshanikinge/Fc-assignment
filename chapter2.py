#concatination
str1="Roshhhani"
str2="kinge"
print(str1+str2)

#find the length of string
print(len(str1))
print(len(str2))

#indexing
print(str1[0])
print(str2[3])

#slicing
print(str1[4:6])
print(str1[:4])
print(str2[3:len(str2)])

#slicing for -ve string
print(str2[-3])

#string function
print(str1.endswith("ni"))
print(str2.capitalize())
print(str1.replace("a","k"))
print(str2.find("sh")) #it gives -1 bcz this sh not present in the string so it
                       #give - indexing otherwise it give proper indexing

print(str1.count("h")) #it give how many h is present in the string
