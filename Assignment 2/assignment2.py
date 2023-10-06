#SCT211-0067/2022
#LEVI MUTUGI MUTHARIMI

totalBillAmount= int(input("Enter the total bill : "))
print("The following are the avalable tip options: \n 1. 10% \n 2. 12% \n 3. 15%\n")
option = int(input("Please enter your prefered option: "))
noOfPeople=int(input("Enter the number of people splitting the bill: "))



match option:
    case 1:
        tip = round(0.1*totalBillAmount/noOfPeople,2)
        print("The tip is: ", tip, "for each person")
    case 2:
        tip = round(0.1*totalBillAmount/noOfPeople,2)
        print("The tip is: " ,tip ,"for each person")
    case 3:
        tip = round(0.1*totalBillAmount/noOfPeople,2)
        print("The tip is: ",tip, " for each person")
    case _:
        print("Invalid option")        
           
        



