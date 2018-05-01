# Input is hard-coded
p_defect = 1 / 3
turn_defect = 5
p_good = 1 - p_defect

probability = (p_good ** (turn_defect - 1)) * p_defect
print(round(probability, 3))
