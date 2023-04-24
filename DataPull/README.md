**FintechPredictionModels.ipynb**

This file is a .ipynb file, that which creates the prediction models for the website. These
files use python, but will need to be run using jupyter notebook, or through google colab. There is
advantage to using this type of file while doing machine learning it lets you easily run specific chunks
of code and not others. Often when doing machine learning functions and tests, can run for hours, so
being able to run specific things without running others becomes invaluable. 


Basic prediction models have been made, and those predictions have been pushed to the database.

To update the predictions in the database, you can run all the cells of this file. 

**StockPricePull.py**

This file contains a class that will find a stock price for any given day, or the average stock price over a number of
months. To create an instance of this class, you need one parameter. It needs the stock symbol of the company you would
like to find the stock price for. There are two methods that are useful from this class getStockPrice(),
and getAverageStockPrice(). getStockPrice requires one parameter, which is just the string representation of the date, 
you are looking for the stock price for. getAverageStockPrice() has two required parameters, startDate, and numMonths. 
startDate is just the first date of the range you are looking for an average of, and numMonths is the number of months
you need the average to run. 