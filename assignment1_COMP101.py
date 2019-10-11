#user input
height_ = float(input("Enter height of barge(m): "))
length_ = float(input("Enter length of barge(m): "))
breadth_ = float(input("Enter breadth of barge(m): "))

#process
sa_ = (height_)*(breadth_)*(length_)
mass_ = 1.06*(sa_)
draft_ = (mass_)/((length_)*(breadth_))
height_AW = (height_)-(draft_)
#output
print ("\nSurface area(m) =",sa_)
print ("Mass(kg) =",mass_)
print ("Draft(m) =",draft_)
print ("Height of barge above water level(m) =",height_AW)
