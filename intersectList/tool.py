import argparse
import pandas as pd
import settings.config as cf
from src.mod_1 import Module1
from src.mod_2 import Module2


if __name__ == '__main__':
    # CIL-command line interface
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", '--file_name', type=str, default=cf.Ipath, help=cf.Fihelp)
    opt = parser.parse_args()

    # read data from csv file
    data = pd.read_csv(opt.file_name)

    # create output data columns
    to_append = []

    for index, row in data.iterrows():
        module1 = Module1(row['min_arr'], row['max_arr'])
        # finding list of odd number and number divisible by 3
        list_odd, list_db3 = module1.check()
        module2 = Module2()
        # finding intersection list from 2 list above
        inter_list = module2.intersect_number(list_odd, list_db3)
        # add result to output data columns
        to_append.append(inter_list)

    # write output data to file
    data['Intersect'] = to_append
    data.to_csv(cf.Opath, index=False)
