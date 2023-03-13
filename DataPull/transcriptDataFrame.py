import requests
import math
from datetime import date
import pandas as pd
from IPython.display import display

#Jan, April, July, Oct are usually when the quarters happen


#todo: update database in django with the transcripts



# this is the list of companies that will be populated in the dataframe
COMPANYS = ['AAPL']#, 'GOOGL'] #, 'MSFT', 'INTC', 'AMD']


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
    # print(transcriptDate)
    # print(countremarks)

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

    # print(companyTranscript)
    return companyTranscript, transcriptDate


# this function populates a dataframe with companies transcripts starting at a specified year
# companys is a list of strings and year is an int
def populateDF(companys, year):

    todays_date = date.today()

    columns = ["transcript", "date"]
    transcriptDF = pd.DataFrame(columns=columns)

    for comp in companys:
        startYear = year
        allCompanyTranscripts = []
        while startYear <= todays_date.year:
            #this loop is gets the 4 quarters in a year
            for i in range(1, 5):
                try:
                    transcript, theDate = getTransctipt(comp, startYear, 'q' + str(i))
                    transcriptDF.loc[comp + " " + theDate[:10] + " q" + str(i)] = [transcript, theDate]
                except:
                    transcriptDF.loc[comp + " " + theDate[:4] + " q" + str(i)] = ([None, theDate[:4] + " q" + str(i)])

                #transcriptDF.loc[comp + " " + theDate] = allCompanyTranscripts

            startYear += 1



    #display(transcriptDF)
    #print(transcriptDF)


# call the function to populate the dataframe with companies starting at year
populateDF(COMPANYS, 2023)






#Jan, April, July, Oct are usually when the quarters happen
