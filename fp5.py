# Function to format text in red color
def redText(text):
    return f"\033[91m{text}\033[0m"  # ANSI escape code for red text

# Function to format text in blue color
def blueText(text):
    return f"\033[94m{text}\033[0m"  # ANSI escape code for blue text

# Function to format text in green color
def greenText(text):
    return f"\033[92m{text}\033[0m"  # ANSI escape code for green text

# Function to format text in yellow color
def yellowText(text):
    return f"\033[93m{text}\033[0m"  # ANSI escape code for yellow text

# Function to format text in brown color
def brownText(text):
    return f"\033[38;5;94m{text}\033[0m"  # ANSI escape code for brown text

# Main program logic
def main():
    # Display options to the user
    print("Choose a color to display your text:")
    print("1. Red")
    print("2. Blue")
    print("3. Green")
    print("4. Yellow")
    print("5. Brown")

    # Get user input for color choice
    choice = input("Enter the number of your choice (1-5): ")
    user_text = input("Enter the text you want to display: ")

    # Call the appropriate function based on user choice and print the result
    if choice == '1':
        print(redText(user_text))
    elif choice == '2':
        print(blueText(user_text))
    elif choice == '3':
        print(greenText(user_text))
    elif choice == '4':
        print(yellowText(user_text))
    elif choice == '5':
        print(brownText(user_text))
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

# Calling the main function to run the program
main()
