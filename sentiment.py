import author
import requests, json
from datetime import datetime, timedelta
from time import localtime, time

import pandas as pd


class Sentiment(author.GetAcess):
    '''Sub Class'''

    def __init__(self):
        super().__init__()
        self._hostURL = "https://api2.sprinklr.com/api/v1/reports/query"
        self._header = {
            'Authorization': 'Bearer '+ self._token,
            'Content-Type' : 'application/json',
            'cache-control': 'no-cache',
            'key': self._api_key
        }
        

    ''' 
        REST: POST
        Response Data: Json
            [Create Time, IM_Sentiment Total, IM_Positive Mention, IM_Negative Mention]
        Return Date: DataFrame
    '''
    def sentiment_topic(self, s_time, e_time, topic_id, **kwargs):
        
        # REST API, request data
        with open('sentiment.json', encoding='UTF-8') as f:
            json_data = json.load(f)

        with open('filters.json', encoding='UTF-8') as f:
            filter_data = json.load(f)

        
        ### Set Start and End Date ###
        json_data['startTime'] = s_time
        json_data['endTime'] = e_time
        json_data['filters'][0]['values'].append(topic_id)  # Topic ID

        # Keyword Query - GOS & Theme - South Korea Regions
        for key,val in kwargs.items():
            filter_data[key]['values'].append(val)
            json_data['filters'].append(filter_data[key])

        # POST Method
        res = requests.post(self._hostURL,headers=self._header,data=json.dumps(json_data))
        

        res_dict = {
            'date':[], 
            'IM_Sentiment Total':[], 
            'IM_Positive Mention':[],
            'IM_Negative Mention':[]
        }

        for row in res.json()['rows']:
            res_dict['date'].append(datetime.fromtimestamp(int(row[0])/1e3))
            res_dict['IM_Sentiment Total'].append(int(row[1]))
            res_dict['IM_Positive Mention'].append(int(row[2]))
            res_dict['IM_Negative Mention'].append(int(row[3]))


        # DataFrame
        sentiment_data = pd.DataFrame(res_dict)
        
        return sentiment_data

