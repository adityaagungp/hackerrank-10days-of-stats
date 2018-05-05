import math

# hardcoded inputs
mean = 20
std = 2

# use built math.erf
def pdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

def pdf_question(x):
    return pdf(x, mean, std)

# less than 19.5
print(round(pdf_question(19.5), 3))
# between 20 and 22
print(round(pdf_question(22) - pdf_question(20), 3))
