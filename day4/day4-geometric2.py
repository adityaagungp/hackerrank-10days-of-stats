# Input is hard-coded
p_defect = 1 / 3
turn_defect = 5
p_good = 1 - p_defect

# The probability is calculated as 1 minus the probability that the first 5 inspections yield good machine
probability = 1 - (p_good ** turn_defect)
print(round(probability, 3))
