def print_kwargs(**kwargs):
    print("Keyword arguments received:")
    for key, value in kwargs.items():
        print(f" {key}: {value}")
    print(f"Dictionary form: {kwargs}")

#Example 
print_kwargs(name="Bob", occupation="Developer",experience=5)