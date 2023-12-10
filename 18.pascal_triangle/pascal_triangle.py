from math import factorial

def pascal_triangle(n):
    """
    Generate and print Pascal's Triangle up to n rows in a visually pleasing manner.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.

    The function prints each row of Pascal's Triangle, starting from the top.
    Each number in a row represents the number of combinations of elements at that position.
    """
    # Calculate the width of the largest number in the last row for formatting
    largest_num_width = len(str(factorial(n-1)))

    for i in range(n):
        # Print leading spaces for current row to center align
        print(' ' * (n - i - 1) * largest_num_width, end='')

        # Calculate and print each number in the row
        for j in range(i + 1):
            num = factorial(i) // (factorial(j) * factorial(i - j))
            # Print each number with spacing based on the largest number's width
            print(f'{num:{largest_num_width}d}', end=' ' * largest_num_width)

        # Move to the next line after each row
        print()

if __name__ == '__main__':
    try:
        # Get the number of rows from the user
        rows = int(input("Enter the number of rows for Pascal's Triangle: "))
        if rows < 0:
            print("Please enter a non-negative integer.")
        else:
            # Generate and print Pascal's Triangle for the specified number of rows
            pascal_triangle(rows)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
