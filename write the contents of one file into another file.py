def copy_file(src, dest):
    try:
        #Open source file in read mode
        with open(src, "r") as fsrc:
            data = fsrc.read()

        #Open destination file in write mode 
        with open(dest, "w") as fdest:
            fdest.write(data)

        print(f"Contents of '{src}' copied to '{dest}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{src}' does not exist.")

#Take input from user
src_file = input("Enter the source filename: ")
dest_file = input("Enter the destination filename: ")

copy_file(src_file, dest_file)