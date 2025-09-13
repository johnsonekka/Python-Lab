# import json
# def find_max_min(lst):
#     if not lst:
#         return None, None
    
#     #Initialize with first elements
#     max_value = lst[0]
#     min_value = lst[0]

#     #Iterate through the list 
#     for num in lst[0:]:
#         if num > max_value:
#             max_value = num
#         if num < min_value:
#             min_value = num
    
#     return max_value, min_value

# #Get input from user 
# user_input = input("Enter a JSON list: ")
# numbers = json.loads(user_input)

# max_value, min_value = find_max_min(numbers)
# print(f"Maximum value: {max_value}")
# print(f"Minimum value: {min_value}")



def find_max_min(lst):
    if not lst:
        return None, None
    
    # Initialize with first element
    max_value = lst[0]
    min_value = lst[0]

    # Iterate through the list
    for num in lst:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return max_value, min_value

# Get input from user and convert to list of integers
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Find max and min
max_value, min_value = find_max_min(numbers)

# Display results
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")


# def find_max_min(lst):
#     if not list : 
#         return None
#     return max(lst), min(lst)

# number = [98,63,45,66,97]
# print(find_max_min(number))