# Function to validate the password
def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check if password length is at least 8 characters
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    # Loop through each character in the password
    for char in password:
        if char.isupper():  # Check for uppercase letter
            has_upper = True
        elif char.islower():  # Check for lowercase letter
            has_lower = True
        elif char.isdigit():  # Check for digits
            has_digit = True
        elif char in "!@#$%^&*()-_+=<>?/":  # Check for special characters
            has_special = True

    # Check if all criteria are met
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one digit.")
    if not has_special:
        print("Password must contain at least one special character.")

    # Return True if all conditions are met
    return has_upper and has_lower and has_digit and has_special

# Main program to ask user for a password
while True:
    user_password = input("Enter your password: ")

    # Validate the password
    if validate_password(user_password):
        print("Password is valid!")
        break  # Exit the loop if password is valid
    else:
        print("Please try again with a stronger password.\n")
