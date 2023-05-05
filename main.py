#******************************************************************************
# Author:           Patrick Adigweme and Julia Empleo
# Lab:              Discussion 2 - Driving Costs
# Date:             April 12, 2023
# Description:      This program prompts the user for a number of miles and
#                   the price per gallon of gas, returning the cost to drive
#                   the inputted number of miles.
# Input:            float - number of miles, float - price per gallon
# Output:           Cost to drive the inputted number of miles - float
# Sources:          Discussion 2 instructions
# Sample Run:       Users should see the cost, in USD, to drive the number
#                   of inputted miles: "It would cost $xx.xx to drive y miles"
# Contributions:    Patrick created the Replit and drafted the initial
#                   code. Julia debugged the code and corrected the output
#                   to match the assignment's instructions (cost per miles)
# Struggles:        Patrick encountered some struggles with reading
#                   comprehension late at night after PCC's server outages  
#                   were resolved, which caused incorrect code to be written 
#                   that did not align with the instructions. Additionally,
#                   we struggled a bit with formatting floats within a string.
#******************************************************************************
# Welcome message 
print('Welcome to the Driving Cost Calculator.') 
# user input mpg 
mpg = float(input('Please enter the miles per gallon of your vehicle.\n'))
# user input price per gallon
price = float(input('Please enter the price per gallon of gas.\n$'))  

# calculations 
cost_per_20_miles = round((20 / mpg) * price, 2) 
cost_per_75_miles = round((75 / mpg) *  price, 2)
cost_per_500_miles = round((500 / mpg) * price, 2)


print('\nBased on your vehicle\'s miles per gallon:') 
# user output with 20 miles
print(f'It would cost ${cost_per_20_miles:.2f} to drive 20 miles.')
# user output with 75 miles 
print(f'It would cost ${cost_per_75_miles:.2f} to drive 75 miles.')
# user output with 500 miles 
print(f'It would cost ${cost_per_500_miles:.2f} to drive 500 miles.') 