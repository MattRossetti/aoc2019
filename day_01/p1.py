import math


with open('../.input/in_01.txt') as file:
    mass_list = file.readlines()

fuel_needed = 0
for mass in mass_list:
    fuel_needed += (math.floor(float(mass) / 3) - 2)

print(fuel_needed)
