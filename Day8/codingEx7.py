def life_in_weeks(age):
    """
    Calculates the number of weeks left until the age of 90, based on the current age.

    Parameters:
    age (int): The current age of the person.

    Returns:
    None
    
    Prints the number of weeks left until the age of 90.
    """
    total_weeks = 90 * 52  # Total weeks in 90 years
    current_weeks = age * 52  # Weeks lived so far based on current age
    weeks_left = total_weeks - current_weeks  # Remaining weeks until 90
    print(f"You have {weeks_left} weeks left.")

# Example usage
life_in_weeks(56)
