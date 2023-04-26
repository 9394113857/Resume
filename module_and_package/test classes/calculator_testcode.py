from module_and_package.calculator.basic_operations import add, subtract, multiply, divide
from module_and_package.calculator.advanced_operations import square_root, power, sine, cosine, tangent

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("======================================")
print("1).Sum:", add(a, b))
print("2).Difference:", subtract(a, b))
print("3).Product:", multiply(a, b))
print("4).Quotient:", divide(a, b))
print("=======================================")
print("5).Square root of", a, ":", square_root(a))
print("6).", a, "to the power of", b, ":", power(a, b))
print("7).Sine of", a, ":", sine(a))
print("8).Cosine of", a, ":", cosine(a))
print("9).Tangent of", a, ":", tangent(a))
