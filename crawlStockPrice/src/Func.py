import sqlite3
from crawlStockPrice.src.Stocks import Stock


def loadData(data, date_start, date_end):
    """
    :param data:
    :param date_start:
    :param date_end:
    :return: a list of stock
    """
    conn = sqlite3.connect('stockdata.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Stock')
    cur.execute('CREATE TABLE IF NOT EXISTS Stock (name TEXT, code TEXT, date DATE, price FLOAT)')

    stocks = []
    for index, row in data.iterrows():
        stock = Stock(row['name'], row['code'])
        stock.find(date_start, date_end)
        for ind in range(len(stock.date)):
            cur.execute('''INSERT INTO Stock(name,code,date,price)
                VALUES (?, ?, ?, ?) ''', (stock.name, stock.code, stock.date[ind], stock.price[ind]))
        stocks.append(stock)
    conn.commit()
    return stocks
