def count_digits(n):
    n = abs(n) #remove minus sign if negative
    return len(str(n)) #convert to string and count characters

# Input from user
num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))
