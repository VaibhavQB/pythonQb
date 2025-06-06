# Function to perform basic arithmetic operations 
def calculate(a, b, operation):
    match operation:
         case '+':
             return a + b
         case '-':
             return a - b
         case '*':
             return a * b
         case '/':
             if b == 0:
                 return None
             return a / b
         case '%':
             if b == 0:
                 return None
             return a % b
         
    return None


# Input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
o = input("Enter operation (+, -, *, /, %): ")

# Call the calculate function and print the result         
result = calculate(a, b, o)
if result == None:
    print("Invalid operation or division by zero.")
else:
    print(f"The result of \n {a} {o} {b} is: {result}")    