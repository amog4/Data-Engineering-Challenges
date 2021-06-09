import requests
import pandas as pd


class APIError(Exception):

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "API ERROR Status {}".format(self.status)


response = requests.get('http://127.0.0.1:5000/')

if response.status_code == 200:
    print('proceed')
    response_json = response.json()
else:
    raise APIError(status = str(response.status_code))

# process the data 

list_columns = ['field','id','options','timestamp','user_id']

dataset = {n: [] for n in list_columns}


# loop through response 

for ind,resp in enumerate(response_json):
    dataset['field'].append(resp['field'])
    dataset['id'].append(resp['id'])
    dataset['options'].append(resp['options'])
    dataset['timestamp'].append(resp['timestamp'])
    dataset['user_id'].append(resp['user_id'])


# create dataframe from dictionary
data = pd.DataFrame(data=dataset)
