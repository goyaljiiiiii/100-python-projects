# This is file number 2- simple calculator

num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
operator=input("Enter the operator : ")

if operator=="+":
    print("The sum is: ",int(num1)+int(num2))
elif operator=="-":
    print("The difference is: ",int(num1)-int(num2))
elif operator=="*":
 print("The product is: ",int(num1)*int(num2))
elif operator=="/":
    if num2!=0:
      print("The quotient is: ",int(num1)/int(num2))
    else:
       print("Error! Division by zero is not allowed")
else:
   print("Invalid operator") 


   