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

**transcriptDataFrame.py**

This file contains the code to initially populate the Database.  It is currently configured to add entries to the data base from Apple, Google, AMD, Intel
and Microsoft from the years 2017 to current.  The Aletheia API currently does not have data before 2017 so the file can be modified to use the FMD API.  
This API costs $20 a month however, data is available up to 20 years in the past.  This could be purchased for the one month to fully populate the data 
base with older entries.  More companies can also be added in the COMPANYS list at the top of the file.  


**updateTranscript.py**

This file contains the code to update the database with new transcripts that are realeased and the stock prices we have associated with that transcript.  
This is a seprate file to cut down computation power as transcriptDataFrame always looks for data from the last 50 years while updateTranscipt just looks 
for transcripts and prices from the last two years.  It has been set for the last two years incase there is a mistake in the API that gets updated.  This 
way our database can update those transcripts and prices as well instead of having the incorrect data. UpdateTranscipt.py is the file that the crontab runs every Monday after noon to look for updates.  
