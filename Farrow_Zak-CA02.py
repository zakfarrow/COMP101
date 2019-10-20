#201417945
#October 2019
#A program which calculates the total distance, horizontal and vertical components of this distance, and details about battery usage of a robot rover

#input
import math
angleDeg = float(input("Enter direction from the vertical in degrees: "))
time = int(input("Enter time of travel in seconds: "))

#calculation
speed = 1.5
angleRad = angleDeg * (math.pi)/180
distanceTravelled = speed * time
horizontalDistance = distanceTravelled*(math.sin(angleRad))
verticalDistance = distanceTravelled*(math.cos(angleRad))
batteryUsage = 2.7 * time
remainingBattery = 100 - batteryUsage

#
print ("Total distance =",distanceTravelled)
print ("Horizontal = {:5.2f}".format(horizontalDistance))
print ("Vertical = {:5.2f}".format(verticalDistance))
print ("Battery usage =",batteryUsage,"%")

#message to user about battery
if batteryUsage > 100:
    print ("\nMessage to user: Not enough battery to reach final destination")
elif batteryUsage > 50 and batteryUsage <= 100:
    print ("\nMessage to user: Not enough battery to return to origin")
else:
    print ("\nMessage to user: Battery remaining fo return trip is",remainingBattery,"%")
