# Import the getpass module to handle password prompts securely
import getpass

# 1. Prompt for a password securely (without echoing the input)
def get_password():
    """Prompts the user for a password securely using getpass.getpass()"""
    try:
        password = getpass.getpass("Enter your password: ")
        return password
    except Exception as error:
        print(f"Error: {error}")

# 2. Get the username of the current user from the system
def get_username():
    """Returns the username of the current user using getpass.getuser()"""
    username = getpass.getuser()  # Fetches the username of the currently logged-in user
    return username

# Main function to demonstrate the use of getpass module methods
if __name__ == "__main__":
    # 1. Get the current user's username
    username = get_username()
    print(f"Current Username: {username}")

    # 2. Securely prompt the user for their password
    password = get_password()
    print(f"Password entered for {username}: {'*' * len(password)}")  # Masking the actual password for display
