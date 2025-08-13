# def reverse_string(s):
#     if len(s) <= 1:
#         return s
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("he"))



# def reverse_string(s):
#     stack = list(s)
#     reversed_str = []
#     while stack:
#         reversed_str.append(stack.pop())
#     return ''.join(reversed_str)

# print(reverse_string("he"))


def reverse_string(s):
    #convert the string to a list for a in place modification
    chars = list(s)
    left , right = 0, len(chars) - 1

    while left < right:
        #seap characters
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    #convert the list back to a string
    return ''.join(chars)

#user input and output 
user_str = input("Enter a string: ")
print(f"Reversed string: {reverse_string(user_str)}")