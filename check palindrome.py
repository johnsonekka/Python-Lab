def is_palindrome(s):
    s = str(s) #Convert numbers to string
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# User input and output 
user_input = input ("Enter a string or number: ")
print(f"is '{user_input}' a palindrome? {is_palindrome(user_input)}")