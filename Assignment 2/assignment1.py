yearOfBirth = int(input("Enter your year of birth here: "))
currentYear = 2023 
ageInYears = currentYear - yearOfBirth
ageInMonths = ageInYears * 12
ageInDays = round(ageInMonths * 365.25,2)
print("Your age in years is " + str(ageInYears))
print("Your age in months is: " + str(ageInMonths))
print("Your age in days is: " + str(ageInDays))
