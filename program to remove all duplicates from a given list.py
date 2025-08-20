#get input from user 
user_input = input("Enter elements separated by spaces: ")

#Convert input string to list 
original_list = user_input.split()

#Remove duplicate using set 
unique_list = list(set(original_list))


print("Original list:", original_list)
print("List without duplicates:", unique_list)