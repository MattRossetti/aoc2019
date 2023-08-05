import math


with open('../.input/in_01.txt') as file:
    mass_list = file.readlines()

fuel_needed = 0
for mass in mass_list:
    initial_fuel = (math.floor(float(mass) / 3) -2)
    while initial_fuel > 0:
        fuel_needed += initial_fuel
        initial_fuel = (math.floor(float(initial_fuel) / 3) - 2)

print(fuel_needed)
