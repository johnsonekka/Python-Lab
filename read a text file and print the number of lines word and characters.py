



def file_statistics(filename):
    with open(filename, "r") as f:
        text = f.read()

    # Count lines
    with open(filename, "r") as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_words = len(text.split())
    num_chars = len(text)

    print("Lines:", num_lines)
    print("Words:", num_words)
    print("Characters:", num_chars)


# Example usage
filename = input("Enter the filename: ")  # replace with your file name
file_statistics(filename)
