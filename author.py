import requests
import traceback
import json



from spr_api.listening.Query import Query
from spr_api.spr_app import SprApp



### OAuth 2.0 : Authorization Code Grand | 권한 부여 승인 코드 방식

# 1. Key(client_id/{{apikey}}): 6xnzg5u87cw6zpr2aexbfbrb
# 2. Secret: jgDaM3U9FQrDrKnJkztkujqpFjtNMvDRNS6XXSuPUymRvArU9jfG9VxMPgbfDt8Z
# 3. __SPR_ENV__.env : 'prod' 
#    -> Not required {{env}}
#    -> app.sprinklr.com: https://api2.sprinklr.com/api/v1/{{endpoint}}
# https://api2.sprinklr.com/oauth/authorize?client_id=6xnzg5u87cw6zpr2aexbfbrb&response_type=code&redirect_uri=https://www.sprinklr.com/
# code=625eba6c17603d5a7803536b
# https://api2.sprinklr.com/oauth/token?client_id=6xnzg5u87cw6zpr2aexbfbrb&client_secret=jgDaM3U9FQrDrKnJkztkujqpFjtNMvDRNS6XXSuPUymRvArU9jfG9VxMPgbfDt8Z&redirect_uri=https://www.sprinklr.com/&grant_type=authorization_code&code=6256c38817603d5a780f7d39
# "access_token":"W+Itb9X7vYr3qPAIiEvFvDOkF4Wvj9wjDYNaB6u8zHJjMjhlNmNlMDk5MzYwNTBiMjVhYjgyZWJhYzU5OWViMw=="
# "refresh_token":"NmFG7vUhBWtbVx1WNiBmhHfL/14V1763CRlR2zmb/6I1ZjcxYzIyZjUxZmJlZDJkM2E4YjUxYjQ5YTkxY2ViMw=="
# "token_type":"Bearer"
# "expires_in":315569519


class GetAcess:
    """Super Class"""

    def __init__(self):
        self._callback_url = "https://www.sprinklr.com/"
        self._api_key = "6xnzg5u87cw6zpr2aexbfbrb"
        self._secret = "jgDaM3U9FQrDrKnJkztkujqpFjtNMvDRNS6XXSuPUymRvArU9jfG9VxMPgbfDt8Z"
        self._user = "Jaeyeon.Yu@kr.ey.com"
        self._pw = "Ey_2022!"
        self._code = None
        self._token = "W+Itb9X7vYr3qPAIiEvFvDOkF4Wvj9wjDYNaB6u8zHJjMjhlNmNlMDk5MzYwNTBiMjVhYjgyZWJhYzU5OWViMw=="


    '''
        REST: GET
        Response Data: Json
        Return Data: Topic ID
    '''
    def listening_topics(self, *topic_Name):
        
        url = "https://api2.sprinklr.com/api/v1/listening/topics"
        header = {
            'Authorization': 'Bearer '+ self._token,
            'cache-control': 'no-cache',
            'key': self._api_key
        }


        res = requests.get(url, headers=header)

        self._topicGroups = res.json()['response']['topicGroups'] # list

        # Data Format: [ { 'id':'', 'name':'', 'topicGroup':'', 'tags':[],... }, {...}, ... ]
        topics = res.json()['response']['topics'] # list

        for topic in topics:
            if topic['name'] in topic_Name:
                topicID = topic['id']
                # topicGroups = topic['topicGroup']
                # topicTags = topic['tags'] # return type: list
                break

        return topicID



    '''
        REST: GET
        Response Data: Json
        Return Data: Topic ID
    '''
    def listening_themes(self, *theme_Name):
        pass






"""
    # Using Sprinklr API
    def __get_SPR_auth(self):
        app = SprApp(env='prod', key=self._api_key, secret=self._secret, redirect_uri=self._callback_url,
         username=self._user, password=self._pw, auth_code=self._code)
        
        return app

    def func_name(self):
        print(traceback.extract_stack(None, 2)[0][2])


    def test_hello(self):
        self.func_name()
        app = self.__get_SPR_auth()
        res = app.request("GET", "me")
        print(json.dumps(res))

    
    # Using REST API
    def apiTest(self):
        headers = {
            'Authorization': 'Bearer '+ self._token,
            'cache-control': 'no-cache',
            'key': self._api_key
        }
        params = {'types':'CLIENTS'}
        res = requests.get(self._host+"bootstrap/resources", headers=headers, params=params)
        return res.json()



    # Using REST API
    def get_auth(self):
        host_1 = "https://api2.sprinklr.com/oauth/authorize"
        params = {
            'client_id': self._api_key,
            'response_type': 'code',
            'redirect_uri': self._callback_url
        }
        res_1 = requests.get(url=host_1, params=params)
        return res_1

"""
