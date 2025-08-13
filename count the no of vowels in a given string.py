def count_vowels(s):
    vowels = { 'a', 'e', 'i' , 'o', 'u'}
    count = 0
    for char in s.lower(): # convert to lowercase for case-insensitive check
      if char in vowels:
        count += 1
    return count

# user input and output
user_str = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(user_str)}")