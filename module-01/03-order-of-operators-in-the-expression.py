# Create a Python program that calculates the total cost of electricity consumption, 
# taking into account different rates for daytime and nighttime.

# Tasks:

# Store the cost of one kilowatt-hour of electricity for the daytime rate in the variable rate. Set this variable to 1.68.
# Define the nighttime rate as half of the daytime rate.
# In the variable value_day, store the daytime meter reading, and in value_night, store the nighttime reading. 
# Set these to reasonable whole numbers.
# Calculate the total cost of electricity consumption using the daytime and nighttime readings and rates, 
# and save the result in the variable payment.

# Set the daytime rate per kilowatt-hour
daytime_rate = 1.68

# Define the nighttime rate as half of the daytime rate
nighttime_rate = daytime_rate / 2

# Store the daytime and nighttime meter readings
value_day = 300  # Daytime kilowatt-hours used, adjust as needed
value_night = 500  # Nighttime kilowatt-hours used, adjust as needed

# Calculate the total cost of electricity consumption
payment = (value_day * daytime_rate) + (value_night * nighttime_rate)

# Print the total cost of electricity consumption
print(f"The total cost of electricity consumption is: {payment:.2f} UAH")