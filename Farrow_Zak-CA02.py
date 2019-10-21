#201417945
#October 2019
#A program which, given the direction and time of travel, calculates the total distance a robot rover has travelled, the
#horizontal and vertical components of this distance, and details about the robot's battery usage.

import math

#input
angleDeg = float(input("Enter direction from the vertical in degrees: "))
time = float(input("Enter time of travel in seconds: "))

#calculation
speed = 1.5
angleRad = angleDeg*(math.pi)/180
distanceTravelled = speed*time
horizontalDistance = distanceTravelled*(math.sin(angleRad))
verticalDistance = distanceTravelled*(math.cos(angleRad))
rateOfBatteryLoss = 2.7
batteryUsage = rateOfBatteryLoss*time
remainingBattery = 100-batteryUsage

#output
print ("\nTotal distance travelled in metres = {:5.2f}".format(distanceTravelled))
print ("Horizontal distance in metres = {:5.2f}".format(horizontalDistance))
print ("Vertical distance in metres = {:5.2f}".format(verticalDistance))
print ("Battery usage = {:5.2f}".format(batteryUsage),"%")

#message to user about battery
if batteryUsage > 100:
    print ("\nMessage to user: Not enough battery to reach intended destination")
elif batteryUsage > 50 and batteryUsage <= 100:
    print ("\nMessage to user: Not enough battery to return to origin")
else:
    print ("\nMessage to user: Battery remaining for return trip is {:5.2f}".format(remainingBattery),"%")
