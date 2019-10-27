#main menu
    


print("Main Menu-")
print("Option A: 1 to 24 months")
print("Option B: 3 to 18 years")
print("Option X: exit menu")

option = (input("Select menu option (Enter A, B or X): "))
option = option.upper()

while option not in "X":
    if option == "A":
        catAge = int(input("Enter cat age in months: "))
        if catAge < 4:
            humanAge = catAge
            print ("Human age in years:",humanAge)
        elif catAge > 3 and catAge < 8:
            humanAge = catAge + 4
            print("Human age in years:",humanAge)
        elif catAge > 7 and catAge < 25:
            humanAge = catAge + 3
            print("Human age in years:",humanAge)

    elif option == "B":
        catAge = int(input("Enter cat age in years: "))
        catThree = 3
        humanAge = (catAge - catThree) * 4 + 28
        print ("Human age in years:",humanAge)
        







