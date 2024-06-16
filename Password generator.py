import random
import string

def generate_password(length):
    # Define the character sets to be used for generating the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine the character sets
    characters = lowercase + uppercase + digits + special_chars

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate and display the password
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
