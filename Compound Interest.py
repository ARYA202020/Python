# Getting the Principal
principle = int(input("Enter the principle amount: "))

# Getting the Rate of Interest
rate = int(input("Enter the rate of interest: "))

# Getting the Time Period
time = int(input("Enter the time period: "))

# Entering the formula of CI
ci = principle * (pow((1 + rate / 100), time))

# Getting the output
print("Compound interest is", ci)