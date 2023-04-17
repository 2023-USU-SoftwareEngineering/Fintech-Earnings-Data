import datetime
import requests
import math
from datetime import date, timedelta, datetime
import pandas as pd
from IPython.display import display
from StockPricePull import StockData
import sql_functions


# CURRENT YEAR START SET TO 1970
# companies in list start the earliest as found up in 1968
# this file is to be ran once at the beginning, as it populates the ENTIRE DF but takes a long time to run


# this is the list of companies that will be populated in the dataframe
COMPANIES = [['AAPL', 'Apple'],
             ['GOOGL', 'Google'],
             ['MSFT', 'Microsoft'],
             ['INTC', 'Intel'],
             ['AMD', 'AMD']]


# this function calls the api to get the companies transcript
def getTransctipt(company, year, quarter):

    companyTranscript = []
    # COUNT is to get how many countRemarks are in the quarter transcript
    COUNT = {'key': 'C4E78FF3DEE74FADA9A117A256860987',
                  'company': company,
                  'year': year,
                  'quarter': quarter,
                  'countremarks': True,
             }

    countremarks = ((requests.get("https://api.aletheiaapi.com/EarningsCall", COUNT)).json())
    transcriptDate = countremarks['HeldAt']

    number_calls = math.ceil(countremarks['RemarksCount'] / 19)

    # loop gets all remarks from compay's call and puts them in a list
    for i in range(number_calls):
        PARAMETERS = {'key': 'C4E78FF3DEE74FADA9A117A256860987',
                      'company': company,
                      'year': year,
                      'quarter': quarter,
                      'begin': (i * 20),
                      'end': ((i+1) * 20) - 1,
                      }

        data = ((requests.get("https://api.aletheiaapi.com/EarningsCall", PARAMETERS)).json())['Remarks']

        for j in range(len(data)):
            remark = data[j]['Remark']
            companyTranscript.append(remark)

    return companyTranscript, transcriptDate


# this function populates a dataframe with companies transcripts starting at a specified year
# companies is a list of strings and year is an int
def populateDF(companies, year):

    todays_date = date.today()

    columns = ["transcript", "date", "SP Day Before", "SP Day After", "SP Avg 1 Month After", "SP Avg 3 Months After"]
    transcriptDF = pd.DataFrame(columns=columns)

    for comp in companies:
        # this company variable is for getting the stock price
        company = StockData(comp[0])
        startYear = year

        while startYear <= todays_date.year:
            #this loop is gets the 4 quarters in a year
            for i in range(1, 5):
                try:
                    transcript, theDate = getTransctipt(comp[0], startYear, 'q' + str(i))

                    #new date object
                    dateOfTranscript = datetime(int(theDate[:4]), int(theDate[5:7]), int(theDate[8:10]))

                    # this adds a row to the data frame
                    transcriptDF.loc[comp[1] + " " + theDate[:4] + " q" + str(i)] = [transcript, theDate[:10],
                        company.getStockPrice(str(dateOfTranscript + timedelta(days=-1))[:10]),
                        company.getStockPrice(str(dateOfTranscript + timedelta(days=+1))[:10]),
                        company.getAverageStockPrice(str(dateOfTranscript)[:10], 1),
                        company.getAverageStockPrice(str(dateOfTranscript)[:10], 3)]
                except:
                    continue
            startYear += 1

    return transcriptDF

# call the function to populate the dataframe with companies starting at year
fullDF = populateDF(COMPANIES, 1970)

#this displays the df
#display(fullDF)


# populate server
def popServer(dframe):

    for index, row in dframe.iterrows():
        try:
        # this says if the date is not in yyyy-mm-dd format then skip this row
            if len(row["date"]) < 9 or len(row["transcript"]) < 1:
                continue

            else:
                dtime = datetime(int(row["date"][:4]), int(row["date"][5:7]), int(row["date"][8:10]))
                # in case something missing in dataframe
                before = 0
                after = 0
                oneMonth = 0
                threeMonth = 0

                if row["SP Day Before"] is not None:
                    before = row["SP Day Before"]
                if row["SP Day After"] is not None:
                    after = row["SP Day After"]
                if row["SP Avg 1 Month After"] is not None:
                    oneMonth = row["SP Avg 1 Month After"]
                if row["SP Avg 3 Months After"] is not None:
                    threeMonth = row["SP Avg 3 Months After"]

                sql_functions.add_history(dtime, index[:-8], before, after, oneMonth, threeMonth, ''.join(str(x) for x in row["transcript"]))
        except:
            continue



popServer(fullDF)

