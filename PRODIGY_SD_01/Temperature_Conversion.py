def convert_temperature():
    # Prompt the user for input
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

    # Conversion logic
    if unit == 'C':
        fahrenheit = (temperature * 9/5) + 32
        kelvin = temperature + 273.15
        print(f"{temperature}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
    elif unit == 'F':
        celsius = (temperature - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temperature}°F = {celsius:.2f}°C = {kelvin:.2f}K")
    elif unit == 'K':
        celsius = temperature - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temperature}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

# Call the function
convert_temperature()
