import math

def main():
    print_header()
    measurements = data_gather()
  # report(measurements)
    #result(rad)


def print_header():
    print('                                                                                       ')
    print('                                                                                       ')
    print('                                                                                       ')
    print('                                                                                       ')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++               ')
    print('                                                                                       ')
    print('                                                                                       ')
    print('     |-----------|            /--------\            |---------\                        ')
    print('     |           |           /          \           |          \                       ')
    print('     |           |          /            \          |           \                      ')
    print('     |-----------|         /              \         |           |                      ')
    print('     |        \           / -------------- \        |           |                      ')
    print('     |         \         /                  \       |           /                      ')
    print('     |          \       /                    \      |          /                       ')
    print('     |           \     /                      \     |---------/                        ')
    print('                                                                                       ')
    print('                                                                                       ')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++               ')
    print('                                                                                       ')
    print('                                                                                       ')
    print('                                                                                       ')
    print('                                                                                       ')




def data_gather():
    print()
    reach = int(input("What is the Reach numbers (in mm)? : "))
    print()
    stack = int(input("What is the Stack numbers (in mm)? : "))
    print()
    spacer = int(input("How many mm of spacers before the stem? : "))
    print()
    stem = int(input("What is the stem length (in mm)? : "))
    print()
    htangle = input("What is the head tube angle? : ")
    print()
    htrise = int(input("What is the handle bar Rise (in mm)? : "))
    print()
    backsweep = int(input("What is the Back Sweep of the handle bars? : "))
    print()
    upsweep = int(input("What is the Up Sweep of the handle bars? : "))
    print()
    handlebarlength = int(input("What is the length of the handle bars? : "))
    print(handlebarlength)
    print()
    print()

    measurements = (reach, stack, spacer, stem, htangle, htrise, backsweep, upsweep, handlebarlength)
    data_calc(reach, stack, spacer, stem, htangle, htrise, backsweep, upsweep, handlebarlength)
    return measurements

def data_calc(reach, stack, spacer, stem, htangle, htrise, handlebarlength, backsweep, upsweep):
    # ORIGINAL spacerangle = 90 - float(htangle)
    # RADIANS TEST
    spacerangle = float(htangle)
    spacerheight = abs(math.sin(math.radians(float(htangle)))) * spacer
    spacerdepth = abs(math.cos(math.radians(float(htangle)))) * spacer

    # this is relatively complicated trig to get the small side of the triangle measurement.
    hblength = handlebarlength/2
    #backc = (hblength/math.cos(backsweep))
    #backdepth = math.sqrt((backc ** 2 - hblength ** 2))
    backdepth = hblength * math.tan(math.radians(backsweep))
    
   # print('-------------')
    #print(backdepth)
    #print('-------------')

    #upc = hblength/math.cos(upsweep)
    #upheight = math.sqrt((upc ** 2 - hblength ** 2))
    upheight = hblength * math.tan(math.radians(upsweep))
    
   # print('-------------')
    #print(upheight)
    #print('-------------')

    # Stem of Kate
    # a = b * tan(90 - htangle)
    # new triangle hypot = stem - a
    #newstemlength = new hypot * sin(90 - htangle)

    # ASS = ASSUMPTION OF HALF OF STEM HEIGHT
    ass = 20
    a = ass * abs(math.tan(math.radians(90 - float(htangle))))
    
    newhyp = stem - a

    newstemlength = newhyp * abs(math.cos(math.radians(90 - float(htangle))))

    newreach = reach + newstemlength - (spacerdepth + backdepth)
    newstack = stack + spacerheight + htrise + upheight
    radsqr = (newreach ** 2) + ( newstack ** 2)
    rad = round(math.sqrt(radsqr), 2)
    #result(rad)

    print(spacerdepth)
    print(spacerheight)
    print(handlebarlength)
    print(hblength)
    print()
    print(newstemlength)
    print(backdepth)
    print(upheight)
    


# def result(rad):
#     print()
#     print()
#     print(" BIKE RAD IS : ")
#     print()
#     print('===========')
#     print(rad, ' mm')
#     print('===========')
#     print()

#     inchreq = input(' Do you want that in inches? : ')

#     if inchreq == 'yes' :
#         radinch = round((rad * .0394), 2)
#         print()
#         print ('fine... ')
#         print()
#         print('=============')
#         print(radinch, ' inches')
#         print('=============')

# def report(measurements):
#    # print(measurements)
#     print()
 



if __name__ == '__main__' :
    main()


