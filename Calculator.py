2
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

print("What do you want to do? (+, -, *, /)")
op = input("Enter operation: ")

if op == "+":
    ans = a + b
elif op == "-":
    ans = a - b
elif op == "*":
    ans = a * b
elif op == "/":
    if b != 0:
        ans = a / b
    else:
        ans = "Can't divide by zero!"
else:
    ans = "Wrong choice!"

print("Answer:", ans)
