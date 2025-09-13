def find_string_index(filename, search_str):
    try:
        # open the file and read entire text
        with open(filename, "r") as f:
            text = f.read()

        # find() returns the index of the first occurrence
        index = text.find(search_str)

        if index != -1:
            print(f"'{search_str}' found at index {index}")
        else:
            print(f"'{search_str}' not found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


# ---- Main Program ----
filename = input("Enter filename: ")
search_str = input("Enter string to search: ")

find_string_index(filename, search_str)
