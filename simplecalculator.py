#Rondeezee simple calculator
print("welcome to the simple calculator") 

#Get user input for 2 numbers
num1=float(input("enter your first number:"))
num2=float(input("enter your second number:"))

#Display Operation Choices
print("\n choose an operation:")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")

#Get user input for operation
operation=input("\n enter the number corresponding to the operation you want:")
#Perform the entered operations and display the results.

if operation=="1":
    result=num1 + num2
    print(f"\n result : {num1} + {num2} = {result}")
elif operation=="2":
        result=num1-num2
        print(f"\n result: {num1} - {num2} ={result}")
elif operation=="3":
            result=num1*num2
            print(f"\n result:{num1} * {num2} ={result} ")
elif operation == "4":
                if num2 !=0:
                    result=num1/num2
                    print(f"\n result:{num1} / {num2} ={result} ") 
                else:
                    print("zero division not allowed")
else:
  print("/n Error: invalid operation enter a number between 1 and 4 only")





