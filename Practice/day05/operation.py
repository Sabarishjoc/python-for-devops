import sys
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def sub(a, b):
    return a - b

# Function to multiply two numbers
def mul(a, b):
    return a * b

# Function to divide two numbers
def div(a, b):
    return a / b

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

if operation == "add":
    output = add(a, b)
    print(output)

elif operation == "sub":
    output = sub(a ,b)
    print("sub of two number:", output)
elif operation == "mul":
    output = mul(a, b)
    print("mul of two numbers:", output )
elif operation == "div":
    output = div(a, b)
    print("div of two numbers:", output)
else : 
    output = "unsuporrted operation"
    print (output)

    