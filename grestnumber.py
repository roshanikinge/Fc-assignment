num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

# if num3<=num1>=num2:
#     print("The greatest number is :",num1)
# elif num3<=num2>=num1:
#     print("The greatest number is :",num2)
# else :
#     print("The greatest number is :",num3)


if num1>=num2 and num1>=num3:
    print("the first number is greatest:",num1)
elif num2>=num3:
    print("the second number is greatest :",num2)
else :
   print ("the third number is greatest:",num3)
