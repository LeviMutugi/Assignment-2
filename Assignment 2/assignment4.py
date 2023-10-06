year = int(input("Enter the year you want to check: "))

if (year % 100 == 0) and (year % 400==0):
    print("The year is a leap year")
elif(year % 100 !=0) and (year %4==0):
    print("The year is a leap year")
else:
    print("The year is not leap")
    