import argparse
import setting.config as cf
import pandas as pd
import src.Func as Fu
from matplotlib import pyplot as plt


if __name__ == "__main__":
    #   CIL - Command line interface
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--file_path", type=str, default=cf.Ipath, help=cf.Fihelp)
    opt = parser.parse_args()
    data = pd.read_csv(opt.file_path)
    # input timestamp
    print("nhap khoang thoi gian theo format YYYY-MM-DD")
    date_start = (input("thoi gian bat dau: ") or "2021-9-1")
    date_end = (input("thoi gian ket thuc: ") or "2021-10-1")

    stocks = Fu.loadData(data, date_start, date_end)

    # draw chart
    plt.figure(figsize=(9, 6)) # Make bigger picture

    for index in range(len(stocks)):
        plt.plot(stocks[index].date, stocks[index].price, label=stocks[index].name)

    #plt.xticks(rotation=25)
    plt.gcf().autofmt_xdate()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock market value')
    plt.legend() # Place a note on plt
    plt.savefig('output/plot.png')
    plt.show()
