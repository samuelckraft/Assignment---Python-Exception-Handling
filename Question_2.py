#Task 1
try:
    original_servings = int(input("Please enter the number of servings the recipe originally makes: "))
    requested_servings = int(input("Please enter the number of servings you wish to make: "))

except (ValueError):
    print("Please enter a valid integer.")

#Task 2 & 3
try:
    adjusted_ratio = requested_servings/original_servings
    print(f"The adjusted recipe quantity is {adjusted_ratio}")

except (ValueError, ZeroDivisionError, NameError):
    print("Sorry, one or more of your inputs were invalid, please try again.")

finally:
    print("Enjoy your cooking!")