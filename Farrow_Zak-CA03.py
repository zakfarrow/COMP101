#201417945 Farrow_Zak-CA03.py
#10/2019
#Program which outputs the human equivalent of a cat's age (input) and the cat's life stage
option = " "
while option not in "X":    #loop to return user to main menu

    print("Main Menu-") #main menu
    print("Option A: Your cat is 1 to 24 months old")
    print("Option B: Your cat is 3 to 18 years old")
    print("Option X: Exit menu")
    print()
    option = (input("Select menu option (Enter A, B or X): "))  #user input
    option = option.upper()

    if option == "A":
        catAge = int(input("Enter cat age in months: "))
        if catAge < 4:  #function for cat age to human age in condition where cat is 1 to 3 months
            humanAge = catAge
            print("\nYour cat is in the kitten life stage")
            print("\nHuman age in years:",humanAge)
            print()
        elif catAge > 3 and catAge < 8: #function for cat age to human age in condition where cat is 4 to 7 months
            humanAge = catAge + 4
            print("\nYour cat is in the kitten life stage")
            print("\nHuman age in years:",humanAge)
            print()
        elif catAge > 7 and catAge < 25:    #function for cat age to human age in condition where cat is 8 to 24 months
            humanAge = catAge + 3
            print("\nYour cat is in the junior life stage")
            print("\nHuman age in years:",humanAge)
            print()

    elif option == "B":
        catAge = int(input("Enter cat age in years: "))
        humanAge = (catAge - 3) * 4 + 28    #function for cat age to human age for option B
        if catAge > 2 and catAge < 7:
            print("\nYour cat is in the prime life stage")
            print("\nHuman age in years:",humanAge)
            print()
        elif catAge > 6 and catAge < 11:
            print("\nYour cat is in the mature life stage")
            print("\nHuman age in years:",humanAge)
            print("")
        elif catAge > 10 and catAge < 15:
            print("\nYour cat is in the senior life stage")
            print("\nHuman age in years:",humanAge)
            print("")
        elif catAge > 14 and catAge < 19:
            print("\nYour cat is in the geriatric life stage")
            print("\nHuman age in years:",humanAge)
            print("")






