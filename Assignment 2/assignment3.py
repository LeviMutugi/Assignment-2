#SCT211-0067/2022
#LEVI MUTUGI MUTHARIMI

weight= round(float(input("Enter your weight in kg: ")),2)
height= round(float(input("Enter your height in meters: ")),2)
bmiHeight= height * height
BMI=weight/bmiHeight

if BMI<18.5:
    print("You are underweight")
elif (BMI> 18.5) and (BMI<=25) :
    print("You have a normal BMI")   
else:
    print("You are overweight")    
