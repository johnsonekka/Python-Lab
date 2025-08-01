num = int(input("Enter a number: ")) #Step 1: Get user input 
div_by_2 = num % 2 == 0
div_by_3 = num % 3 == 0
div_by_4 = num % 4 == 0
div_by_5 = num % 5 == 0
div_by_6 = num % 6 == 0
is_small_prime = num > 1 and not(div_by_2 or div_by_3 or div_by_4 or div_by_5 or div_by_6)
if is_small_prime or num in (2, 3, 5):
    print(num, "is a prime number")
else:
    print(num, "is Not a prime number")