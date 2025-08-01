def gcd(a, b): 
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) //gcd(a, b)

# Take input from the keyboard
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("LCM of", a, "and", b, "is:", lcm(a, b))