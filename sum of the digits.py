num = int(input("Enter a 3-digit number: ")) #Step 1: Take input
a = num % 10  #last digit
num = num // 10 
b = num % 10  #middle digit
num = num // 10 
c = num    #First digit
total = a + b + c
print("Sum of digits:", total)