import math
import time
import sys


def main():
    print_header()
    introduction()
    data_collection()
    data_calculation(bikedata)
    result(moredata)
    report(finalreport)
    change()

def rerun():
    data_calculation(bikedata)
    result(moredata)
    newreport(finalreport)
    change()

def newbike():
    data_collection()
    data_calculation(bikedata)
    result(moredata)
    report(finalreport)
    change()

def print_header():
    print()
    print()
    print('-------------------------------------')
    print('  Welcome to the RAD Calculator')
    print('-------------------------------------')
    print()
    print()


def introduction():
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


def data_collection():
    datapoints = ['Reach', 'Stack', 'Spacers', 'Stem', 'Head Tube Angle', 'Handlebar Rise', 'Back Sweep', 'Up Sweep', 'Handlebar Length']
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
    htangle = float(bikedata.get('Head Tube Angle'))
    htrise = int(bikedata.get('Handlebar Rise'))
    backsweep = int(bikedata.get('Back Sweep'))
    upsweep = int(bikedata.get('Up Sweep'))
    handlebarlength = int(bikedata.get('Handlebar Length'))

    # Spacer Measurements
    spacerheight = abs(math.sin(math.radians(htangle))) * spacer
    spacerdepth = abs(math.cos(math.radians(htangle))) * spacer

    # Handle Bar Measurements
    hblength = ((handlebarlength/2) - 152)
    backdepth = hblength * math.tan(math.radians(backsweep))
    #upheight = hblength * math.tan(math.radians(upsweep))
    # IF YOU BRING BACK IN REMEMBER TO ADD TO NEW STACK

  
   # Stem of Kate
   # a = b * tan(90 - htangle)
   # new triangle hypot = stem - a
   # newstemlength = new hypot * sin(90 - htangle)
   # ASS = ASSUMPTION OF HALF OF STEM HEIGHT
    ass = 20
    a = ass * abs(math.tan(math.radians(90 - htangle)))
    newhyp = stem - a

    newstemlength = newhyp * abs(math.cos(math.radians(90 - htangle)))
    midstemsq = ((a ** 2) + (ass ** 2))
    midstem = round(math.sqrt(midstemsq), 2)
    #midstem = a / (abs(math.sin(math.radians(90 - htangle))))
    topstem = a * abs(math.tan(math.radians(90 - htangle)))

    # testing variables
    #print(upheight)

# Here is where we calculate the RAD
    newreach = (reach + newstemlength) - (spacerdepth + backdepth)
    newstack = stack + spacerheight + htrise + midstem + topstem
    newreach2 = int(newreach)
    newstack2 = int(newstack)
    radsqr = (newreach2 ** 2) + ( newstack2 ** 2)
    global rad
    rad = round(math.sqrt(radsqr), 2)
    radinch = round((rad * .0394), 2)
    negsin = newreach2 / rad
    global raad
    raad = round(90 - math.degrees((math.asin(negsin))), 2)
    global moredata
    moredata = [newreach2, newstack2, rad, radinch, raad]


def result(moredata):
    newreport = ['Effective Reach', 'Effective Stack', 'RAD', 'RAD in inches', 'RAAD']
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
        print("{:<30} {:>5}".format(label, Number))
    print()
    print()


def newreport(finalreport):
    print()
    print()
    print(' Enjoy your bike report!')
    print()
    print()
    time.sleep(1.5)
    print('====================================')
    print(' ', bikename, ' + ', changes, 'Change')
    print('====================================')
    for label, value in finalreport.items():
        Number = value
        print("{:<30} {:>5}".format(label, Number))
    print()
    print()
    print()



def change():
    print('Would you like to make a change? (yes / no)')
    print()
    response = input(' : ')
    print()
    if response == 'yes':
        print()
        print('What Would You Like To Change?')
        print()
        for label, value in bikedata.items():
            Number = value
            print("{:<30} {:>5}".format(label, Number))
        print()
        global changes
        changes = input(' : ')
        while True:
            if changes in bikedata.keys():
                print()
                print('What is the new measurement? : ')
                print()
                newvalue = input(' : ')
                bikedata[changes] = newvalue
                break
        
            print()
            print('Item Is Not On Report')
            change()
            break      
        rerun()
    else:
        print()
        print('Would You Like To Try A Different Bike? (yes / no)')
        print()
        newrun = input(' : ')
        print()
        print()
        if newrun == 'yes':
            newbike()
        else:
            print()
            print('Then Go Ride!')
            print()
            #Isys.exit('Ride Fast!')





if __name__ == '__main__':
    main()
    