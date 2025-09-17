def replace_word_in_file(filename, old_word, new_word):
    try:
        # Read file
        with open(filename, "r") as f:
            text = f.read()

        # Replace all instances
        updated_text = text.replace(old_word, new_word)

        # Write back to the same file
        with open(filename, "w") as f:
            f.write(updated_text)

        print(f"All instances of '{old_word}' replaced with '{new_word}' in '{filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


# --- Main program ---
filename = input("Enter filename: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

replace_word_in_file(filename, old_word, new_word)
