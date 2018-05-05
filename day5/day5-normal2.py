import math

# hardcoded inputs
mean = 70
std = 10

# use built math.erf
def pdf(x, mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

def pdf_question(x):
    return pdf(x, mean, std)

# higher than 80
p_high = 1 - pdf_question(80)
print(round(p_high * 100, 2))

# passed the test, >= 60
p_passed = 1 - pdf_question(60)
print(round(p_passed * 100, 2))

# fail
p_fail = pdf_question(60)
print(round(p_fail * 100, 2))
