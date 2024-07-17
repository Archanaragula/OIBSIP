import random
import string

# Function to generate a random password based on given criteria
def generate_password(length, letters, numbers, symbols):
    # Initialize an empty character pool
    char_pool = ''
    # Include letters in the character pool if selected
    if letters:
        char_pool += string.ascii_letters
    # Include numbers in the character pool if selected
    if numbers:
        char_pool += string.digits
    # Include symbols in the character pool if selected
    if symbols:
        char_pool += string.punctuation
    
    # Raise an error if no character types are selected
    if not char_pool:
        raise ValueError("At least one character type must be selected")

    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Main function to interact with the user and generate the password
def main():
    print("Random Password Generator")
    # Get the desired password length from the user
    length = int(input("Enter the desired password length: "))
    # Ask the user if they want to include letters in the password
    letters = input("Include letters? (yes/no): ").lower() == 'yes'
    # Ask the user if they want to include numbers in the password
    numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    # Ask the user if they want to include symbols in the password
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    try:
        # Generate the password based on the user's inputs
        password = generate_password(length, letters, numbers, symbols)
        # Print the generated password
        print(f"Generated Password: {password}")
    except ValueError as e:
        # Print the error message if no character types were selected
        print(e)

# Check if this script is being run directly
if __name__ == "__main__":
    main()
