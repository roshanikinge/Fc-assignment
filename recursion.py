#recursion Means === make short and simple code same IT is loop 

# def show(n): #here we are take a simple function 
#     print (n)
# show(5)

#but if print 5,4,3,2,1 then 

# def show(n):
#     if (n==-1): #it is the stoping condition or we can say it is a base conditions 
#                         #it is also decide recusrions is stop or not 

#         return #here we are used directly retrun means it is a controls return means it is not return the value 
#     print(n)
#     show(n-1) #here we can not used show funcion directly means infinitly so we need the stoping conditions 
# show (5)

# it is also knows as rescursive function
#and recursive function means in this function used recursion 

# def show (n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show (3)



#fact of n number

# def fact(n): 
#     if n==1 or n==0:# it is stoping condition 
#          return 1 
#     return fact(n-1)*(n)
# print(fact(5))

#wite a recursive function to calculate the first n natural number 
def c_sum(n):
    if (n==0):
        return 0
    return c_sum(n-1)+n
sum = c_sum(9)
print(sum)





