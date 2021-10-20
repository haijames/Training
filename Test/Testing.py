import pandas as pd


def check(data):
    d = tuple(data)
    print(len(d))
    # for index, row in d:
    #     print(index)



if __name__ == "__main__":
    data = pd.read_csv("input.csv")
    for index in range(1, len(data.columns)):
        check(data['No{}'.format(index)].items())
    # for index in range(1,len(data.columns)):
    #     check(data['No{}'.format(index)].items())
