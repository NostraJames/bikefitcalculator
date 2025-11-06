import json
from RadCalcv5 import data_collection
from RadCalcv5 import data_calculation
from RadCalcv5 import report


def main():
    data_collection()
    data_calculation(bikedata)
    report(finalreport)



if __name__ == '__main__':
    main()