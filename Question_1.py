#Task 1
try:
    f_temp = int(input("Enter the temperature in farenheit: "))

except ValueError:
    print("Please input a numerical value")

#Task 2/3
try:
    c_temp = (f_temp - 32) *(5/9)
except (ValueError, ZeroDivisionError, OverflowError):
    pass
else:
    print(f"It is {f_temp} degrees farenheit and {c_temp} degrees celsius")

finally:
    print("Thanks for using our weather forecaster")
