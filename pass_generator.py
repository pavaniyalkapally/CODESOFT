import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if length < 1:
        return "Password length must be greater than 0."

    # Randomly select characters to generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter desired password length: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"Generated Password: {password}")

        another = input("Generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    password_generator()
