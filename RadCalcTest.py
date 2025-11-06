import math
import time


def main():
    print_header()
    data_collection()
    data_calculation(bikedata)
    result(moredata)
    report(finalreport)

def print_header():
    print()
    print()
    print('-------------------------------------')
    print('  Welcome to the RAD Calculator')
    print('-------------------------------------')
    print()
    print()


def data_collection():
    time.sleep(2.5)
    print('We will collect data about your bike.')
    time.sleep(2.5)
    print('With this data we can calculate the RAD of your bike')
    time.sleep(2.5)
    print('Please provide requested criteria in mm. Head Tube Angle, Back Sweep, Up Sweep will be in degrees.')
    time.sleep(3.5)
    print()
    print('Let us begin')
    print()
    print()
    time.sleep(2.5)


    datapoints = ['Reach', 'Stack', 'Spacers', 'Stem', 'HT Angle', 'HB Rise', 'Back Sweep', 'Up Sweep', 'HB Length']
    global bikedata
    dataentry = []
    bikedata = {}
    for i in datapoints:
        print(i)
        data = input('  :  ')
        dataentry.append(data)
        print()
    bikedata = dict(zip(datapoints, dataentry))
    global bikename
    bikename = input(' What bike is this? : ')
    print()
    print()
    print()


def data_calculation(bikedata):
    # Convert Dictionary to objects

    reach = int(bikedata.get('Reach'))
    stack = int(bikedata.get('Stack'))
    spacer = int(bikedata.get('Spacers'))
    stem = int(bikedata.get('Stem'))
    htangle = float(bikedata.get('HT Angle'))
    htrise = int(bikedata.get('HB Rise'))
    backsweep = int(bikedata.get('Back Sweep'))
    upsweep = int(bikedata.get('Up Sweep'))
    handlebarlength = int(bikedata.get('HB Length'))

    # Spacer Measurements
    spacerheight = abs(math.sin(math.radians(htangle))) * spacer
    spacerdepth = abs(math.cos(math.radians(htangle))) * spacer

    # Handle Bar Measurements
    hblength = handlebarlength/2
    backdepth = hblength * math.tan(math.radians(backsweep))
    upheight = hblength * math.tan(math.radians(upsweep))

  
   # Stem of Kate
   # a = b * tan(90 - htangle)
   # new triangle hypot = stem - a
   # newstemlength = new hypot * sin(90 - htangle)
   # ASS = ASSUMPTION OF HALF OF STEM HEIGHT
    ass = 20
    a = ass * abs(math.tan(math.radians(90 - htangle)))
    newhyp = stem - a
    newstemlength = newhyp * abs(math.cos(math.radians(90 - htangle)))


    newreach = reach + newstemlength - (spacerdepth + backdepth)
    newstack = stack + spacerheight + htrise + upheight
    radsqr = (newreach ** 2) + ( newstack ** 2)
    newreach2 = int(newreach)
    newstack2 = int(newstack)
    global rad
    rad = round(math.sqrt(radsqr), 2)
    radinch = round((rad * .0394), 2)
    global moredata
    moredata = [newreach2, newstack2, rad, radinch]


def result(moredata):
 
    newreport = ['New Reach', 'New Stack', 'RAD', 'RAD in inches']
    appenddata = dict(zip(newreport, moredata))
    global finalreport
    finalreport = dict(bikedata)
    finalreport.update(appenddata)
  

def report(finalreport):
    print(' Enjoy your bike report!')
    print()
    print()
    time.sleep(1.5)
    print('====================================')
    print('        ', bikename)
    print('====================================')

    for label, value in finalreport.items():
        Number = value
        print("{:<30} {:>30}".format(label, Number))

    print()
    print()
    print()


if __name__ == '__main__':
    main()
    