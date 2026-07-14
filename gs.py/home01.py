print("Please select operation -")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

select_op = int(input("Select operation from 1,2,3,4 : "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select_op == 1:
    result = num1 + num2
    print(num1 ,"+" ,num2 ,"=" ,result)
elif select_op == 2:
    result = num1 - num2
    print(num1 ,"-" ,num2 ,"=" ,result)
elif select_op == 3:
    result = num1 * num2
    print(num1 ,"*" ,num2 ,"=" ,result)
elif select_op == 4:
    result = num1 / num2
    print(num1 ,"/" ,num2 ,"=" ,result)
else:
    print("Invalid input")