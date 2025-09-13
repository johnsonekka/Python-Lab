def find_string_in_file(filename, search_str):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        found = False
        for line_no, line in enumerate(lines, start=1):
            if search_str in line:
                print(f"Found '{search_str}' in line {line_no}: {line.strip()}")
                found = True

        if not found:
            print(f"'{search_str}' not found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


# Take input from user
filename = input("Enter the filename: ")
search_str = input("Enter the string to search: ")

find_string_in_file(filename,search_str)

