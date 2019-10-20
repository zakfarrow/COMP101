#201417945 Farrow_Zak-CA01.py
#October 2019
#The program outputs the draft of a barge, given the dimensions of the barge, the interim calculations as well as the user's input

#user input
height = float(input("Enter height of barge(m): "))
length = float(input("Enter length of barge(m): "))
breadth = float(input("Enter breadth of barge(m): "))

#calculations
ironWeight = 1.06
surfaceArea = (2*breadth*height)+(2*length*height)+(length*breadth)
mass = ironWeight*surfaceArea
draft = mass/(length*breadth)
heightAboveWater = height-draft

#output
print ("\nUser input-"),
print ("Height(m):",str(height))
print ("Length(m):",str(length))
print ("Breadth(m):",str(breadth))
print ("\nCalculations-")
print ("Surface area(m) = {:5.3f}".format(surfaceArea))
print ("Mass(kg) = {:5.3f}".format(mass))
print ("Draft(m) = {:5.3f}".format(draft))
print ("Height of barge above water level(m) = {:5.3f}".format(heightAboveWater))
