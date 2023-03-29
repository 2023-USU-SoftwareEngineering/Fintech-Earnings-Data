# APIkey for FMP 32c9aa6082d9a960d9d017b34df04bed
# !/usr/bin/env python

# APIkey for alphaAdvantage N2U1BIDGSQXM2SEY


from urllib.request import urlopen
import certifi
import json
from datetime import datetime, timedelta
from datetime import date as dateForm


class StockData:

    def __init__(self, companySymbol):  # Takes an input of a string of the stock symbol of the company like AAPL
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={companySymbol}&outputsize=full&apikey=N2U1BIDGSQXM2SEY"
        self.data = self.get_jsonparsed_data(url)["Time Series (Daily)"]


    def get_jsonparsed_data(self, url):
        #  uses the api and returns the json as a dictionary
        response = urlopen(url, cafile=certifi.where())
        data = response.read().decode("utf-8")
        return json.loads(data)

    def getStockPrice(self, date):
        """
        Takes a string that represents a date, and returns the stock price for that day
        """
        try:
            return float(self.data[date]["1. open"])

        except KeyError:  # This returns the next available stock price, happens if given date is a weekend or holiday

            nextDate = datetime.strptime(date, "%Y-%m-%d").date() + timedelta(days=1)
            today = dateForm.today()
            if today > nextDate:  # This makes sure that an infinite loop doesn't happen.
                dateStr = str(nextDate)
                return self.getStockPrice(dateStr)

    def getAverageStockPrice(self, startDate, numMonths=1):
        """
        Two inputs -> String (date), numMonths

        Company should be the stock symbol for the company wanted
        startDate first date of the average desired.
        numMonths number of months you would like to find the average stock price

        """

        totalDays = 30*numMonths  # Round down to 30 days in a month

        date = datetime.strptime(startDate, "%Y-%m-%d").date()  # + timedelta(days=1)

        if dateForm.today() + timedelta(totalDays) < date:
            return None

        total = 0  # sum of all the stock prices
        count = 0  # number of days that reported stock prices in the 31 day range
        for i in range(totalDays):
            if date.isoweekday() < 6:  # Stock Prices aren't reported on weekends
                total += self.getStockPrice(str(date))
                count += 1
            date = date + timedelta(days=1)
        return total / count


if __name__ == "__main__":
    # An example how to use this class

    apple = StockData("AAPL")
    print(apple.getStockPrice("2023-02-24"))
    print(apple.getAverageStockPrice("2023-02-10", 3))



