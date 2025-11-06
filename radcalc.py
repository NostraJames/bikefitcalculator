import math
reach = int(input("What is the Reach numbers (in mm)? : "))
stack = int(input("What is the Stack numbers (in mm)? : "))
spacer = int(input("How many mm of spacers before the stem? : "))
stem = int(input("What is the stem length (in mm)? : "))
htangle = input("What is the head tube angle? : ")
htrise = int(input("What is the handle bar Rise (in mm)? : "))

spacerangle = 90 - float(htangle)

spacerheight = abs(math.sin(float(htangle))) * spacer
spacerdepth = abs(math.cos(float(htangle))) * spacer

newreach = reach + stem - spacerdepth
newstack = stack + spacerheight + htrise


radsqr = (newreach ** 2) + ( newstack ** 2)
rad = round(math.sqrt(radsqr), 2)

print('The RAD for this bike is : ', rad, ' mm')

inchreq = input(' Do you want that in inches? : ')

if inchreq == 'yes' :
    radinch = round((rad * .0394), 2)
    print ('fine... ', radinch, ' inches')

