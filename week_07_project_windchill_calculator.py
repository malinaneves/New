
# Function to calculate and return wind chill based on given temp and wind speed
def calculate_wind_chill(windchill, temperature):
    windchill = 35.74 + (0.6215 * temperature) - (35.75 * (speed**0.16)) + (0.4275 * temperature * (speed**0.16))
    return windchill

# Function to convert Celsius to Fahrenheit
def convert_to_f(temperature):
    temperature = (temperature * (9/5)) + 32
    return temperature
    
# Establish variables
windchill = 0
speed = 5

# Ask user for input
temperature = int(input("What is the temperature? "))
label = input("Fahrenheit or Celsius (F/C)? ")

# If user gives temp in Celsius, convert it to Fahrenheit
if label.lower() == "c":
    temperature = convert_to_f(temperature)

# Loop through wind speeds 5 to 60
for i in range(12):
    windchill = calculate_wind_chill(windchill, temperature)
    print(f"At temperature {temperature:.1f}F, and wind speed {speed} mph, the windchill is: {windchill:.2f}F")
    speed += 5