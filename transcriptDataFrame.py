import requests
import math
import pandas as pd
imort IPython.display import display


#Jan, April, July, Oct are usually when the quarters happen

companyTranscript = []

def getTransctipt(company, year, quarter):

    # COUNT is to get how many countRemarks are in the quarter transcript
    COUNT = {'key': 'C4E78FF3DEE74FADA9A117A256860987',
                  'company': company,
                  'year': year,
                  'quarter': quarter,
                  'countremarks': 'True',
             }

    countremarks = ((requests.get("https://api.aletheiaapi.com/EarningsCall", COUNT)).json())['RemarksCount']
    #print(countremarks)

    number_calls = math.ceil(countremarks / 19)

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

    print(companyTranscript)


getTransctipt('DLTR', '2019', 'q1')


# up to this point puts the asked for info in a list

# after this point is testing code so far
# todo: I need to make a lot of calls and put them all in a data frame to be accessed
# todo: The trascript will be the list in as a df entry, each company will be a row, columns will contain the transcript from each quarter 
# of each year available



# transcriptDF = pd.DataFrame(companyTranscript, columns=['Transcript'])
# display(transcriptDF)

