import yfinance as yf


class Stock:
    def __init__(self, name, code):
        """
        initalize
        :param code:
        """
        self.name = name
        self.code = code
        self.date = []
        self.price = []

    def find(self, start, end):
        """
        :param per: period
        :param start: date start
        :param end: date end
        :return:    Close price of the stock in from start to end in per
        """
        ticket = yf.Ticker(self.code)
        close = ticket.history(start=start, end=end)['Close']
        for ind in range(len(close)):
            self.date.append(close.index[ind].date())
            self.price.append(close[ind])
        return close
