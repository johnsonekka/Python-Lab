def check_numeric(value):
    if not isinstance(value, (int, float)):
        raise ValueError(f"Invalid input: {value} is not a numeric value.")
    return value

# --- Main Program ---
try:
    user_input = input("Enter a number: ")

    # convert input to float or int
    if '.' in user_input:
        user_input = float(user_input)
    else:
        user_input = int(user_input)

    result = check_numeric(user_input)
    print("You entered:", result)

except ValueError as e:
    print("Error:", e)
