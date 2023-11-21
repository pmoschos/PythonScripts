from datetime import date

def calculate_age(birth_date):
    """
    Calculate the exact age in years, months, and days from the given birth date.
    
    :param birth_date: The date of birth as a datetime.date object.
    """
    today = date.today()
    year_diff = today.year - birth_date.year
    month_diff = today.month - birth_date.month
    day_diff = today.day - birth_date.day

    if month_diff < 0 or (month_diff == 0 and day_diff < 0):
        year_diff -= 1
        month_diff += 12

    if day_diff < 0:
        month_diff -= 1
        day_diff += 30

    print(f"Age: {year_diff} Years, {month_diff} Months and {day_diff} Days")

def get_valid_input(prompt, min_value, max_value):
    """
    Prompt the user for input and validate it against the specified range.

    :param prompt: The prompt message for input.
    :param min_value: Minimum acceptable value.
    :param max_value: Maximum acceptable value.
    :return: Validated integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    print("Simple Age Calculator")
    birth_year = get_valid_input("Enter the birth year (1900 or later): ", 1900, date.today().year)
    birth_month = get_valid_input("Enter the birth month (1-12): ", 1, 12)
    birth_day = get_valid_input("Enter the birth day (1-31): ", 1, 31)

    birth_date = date(birth_year, birth_month, birth_day)
    calculate_age(birth_date)
