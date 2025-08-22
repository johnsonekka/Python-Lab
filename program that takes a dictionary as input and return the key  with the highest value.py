def key_with_max_value(dictionary):
    if not dictionary:
        return None
    
    max_key = None
    max_value = float('-inf')

    for key, value in dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    
    return max_key

my_dict = {'a': 10, 'b': 23, 'c': 37, 'e':50}
result = key_with_max_value(my_dict)
print(f"key with maximum value: {result}")