FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = int(input("Enter the temperature to convert:"))
if type(temp) != int or type(temp) != float:
    print("Invalid temperature. Please enter a numeric value")

opt = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if opt.lower() == 'c':
    print(convert_to_fahrenheit(temp))
elif opt.lower() == 'f':
    print(convert_to_celsius(temp))
else:
    print("Invalid option entered")
