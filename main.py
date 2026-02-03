# TASK: Write a program that converts a temperature from Celsius to Fahrenheit.

# Prompt the user to enter a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert the Celsius temperature to Fahrenheit using the formula
fahrenheit = (celsius * 9/5) + 32

# Display the converted temperature
print(f"{celsius}°C is equal to {fahrenheit}°F")