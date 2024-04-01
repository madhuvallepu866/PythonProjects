import os
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

operations_dict={
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division
}
def calculator():
    number1=float(input("Enter first Number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an Operator:")
        number2=float(input("Enter Next Number: "))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        should_continue=input(f"Enter 'y' to continue calculation with {output} OR 'n' to start a new calculation OR 'x' to exit: ").lower()
        if should_continue == 'y':
            number1=output
        elif should_continue == 'n':
            continue_flag=False
            os.system('cls')
            calculator()
        elif should_continue == 'x':
            continue_flag=False
            print("Bye !!!")

calculator()
