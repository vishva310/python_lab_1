def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
   
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum_result = addition(num1, num2)
diff_result = subtraction(num1, num2)
prod_result = multiplication(num1, num2)
div_result = division(num1, num2)


print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {diff_result}")
print(f"Multiplication: {num1} * {num2} = {prod_result}")
print(f"Division: {num1} / {num2} = {div_result}")