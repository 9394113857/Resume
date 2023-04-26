from module_and_package.calculator.basic_operations import add, subtract, multiply, divide

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("===============")
print("1).Sum:", add(a, b))
print("2).Difference:", subtract(a, b))
print("3).Product:", multiply(a, b))
print("4).Quotient:", divide(a, b))
