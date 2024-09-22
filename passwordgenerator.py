import random
import string

def generate_password(length):
    # Define character set (letters and digits)
    characters = string.ascii_letters + string.digits

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Simple Password Generator!")

    while True:
        length = input("Enter the desired length of the password (or '0' to quit): ")

        if length == '0':
            print("Exiting the Password Generator. Goodbye!")
            break

        try:
            length = int(length)
            if length < 1:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
