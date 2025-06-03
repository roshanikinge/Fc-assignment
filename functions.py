# # sum of two number by using functions :
# # def calc_sum(a,b):
# #     sum=a+b
# #     return sum
# # c= calc_sum(2,4)
# # print("sum is:",c)

# # more short program:
# # def sum(a,b):
# #     return a+b
# # c=sum(2,6)
# # print("sum is:",c)

# # #printhello
# # def print_hello():
# #     print("hello:")
# # print_hello()

# # #avg of 3 number:
# # def avg(a,b,c):
# #     sum=a+b+c
# #     avg=sum/3
# #     return avg
# # c=avg(1,2,3)
# # print("avg",c)

# #product of two number:
# # def product(a=4,b=9): here we can pass also argument insetead of paramater 
# #     print(a*b)
# #     return a*b
# # product() 

# #
# # def product(a,b=9): here we can take b=somthing but not a= ? means a,b=9 is correct and a=2,b not correct  
#                     # default value we take in last parameter and non default value we take in first value :
# #     print(a*b)
# #     return a*b
# # product(2)



# #print the length of list 
# # cities=["pune","delhi","mumbai"]
# # hearoes=["rk","pp","rkkk","nfhfvh"]
# # def length_list(list): #here we can also take any list name 
# #     print (len(list)) #and print the lenght of list 
# # length_list(cities) #we call the list like cities 
# # length_list(hearoes) # here we call the list like hearoes #to print the length of list 

# #print the element in a single line in a list :
# # cities=["pune","delhi","mumbai"]
# # hearoes=["thor","iornman","shaktiman","spiderman"]

# # print(hearoes[0] , end=" ") #end="\n" is used to print the element on next or new line  and if end=" " is keep empty then the elemnt will be display on same line 
# # print(hearoes[2] ,end=" ") #here we can directly print the element but single single element in the one one line :

# # #and print the element in a single line in a list : 
# # cities=["pune","delhi","mumbai"]
# # hearoes=["thor","iornman","shaktiman","spiderman"]

# # def print_element(list):
# #     for item in list:
# #      print(item,end="  ")
# #     # print(cities ,end="")

# # print_element(hearoes)
# # print_element(cities )


# #find the factorail where n is a parameter:
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# fact(3) 

#converte the usd into inr :
# def convert(USD):
#     inr_value=USD*83
#     print(USD,"USD =",inr_value,"INR")
# convert(4)

# #print  fact
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# fact(5)


#*************hw**************
# n=int(input("enter the number:"))
# def odd_even(n):
#     if (n%2==0):
#         print("even")
#     else:
#         print("odd")
# odd_even(n) 


#we can add function in function :

def add(a,b):
    print(a+b)
    return a+b
def avg(a,b):
    sum=a+b
    avg=sum/3
    print("avg is:",avg)
    return avg
avg(2,2)
add(2,3)










