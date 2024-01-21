def is_perfect(number):
    """
    Check if a given number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper divisors.

    Args:
    number (int): The number to check.

    Returns:
    bool: True if the number is perfect, False otherwise.
    """
    # Find all divisors of the number, excluding the number itself
    divisors = [i for i in range(1, number) if number % i == 0]
    
    # Return True if the sum of the divisors equals the number
    return sum(divisors) == number

def get_positive_integer():
    """
    Prompt the user for a positive integer and validate the input.

    Continuously prompts the user until a valid positive integer is entered.

    Returns:
    int: The positive integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number > 0:
                return number
            else:
                print("Please enter a positive integer.")
        except ValueError:
            # Handle the case where the input is not an integer
            print("Invalid input. Please enter an integer.")

def main():
    """
    Main function to execute the program.

    Prompts the user to enter a number and checks if it is a perfect number.
    """
    # Get user input for the number
    number = get_positive_integer()

    # Check if the number is a perfect number and print the result
    if is_perfect(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

if __name__ == "__main__":
    main()
