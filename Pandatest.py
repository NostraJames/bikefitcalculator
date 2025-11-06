import pandas as pd
import RadCalcv5 as rc5


def main():
    rc5.main()
    datatable()

def datatable():
    print()
    print()
    df = pd.DataFrame(list(rc5.finalreport.items()), columns = ['Element','Measurement'])
    print(df)



if __name__ == '__main__':
    main()


