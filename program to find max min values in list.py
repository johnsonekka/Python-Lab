import json
def find_max_min(lst):
    if not lst:
        return None, None
    
    #Initialize with first elements
    max_value = lst[0]
    min_value = lst[0]

    #Iterate through the list 
    for num in lst[0:]:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return max_value, min_value

#Get input from user 
user_input = input("Enter a JSON list: ")
numbers = json.loads(user_input)

max_value, min_value = find_max_min(numbers)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
