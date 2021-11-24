import requests
import os
import json
import pandas as pd
import csv
import datatime
import dateutil.parser
import unicodedata
import datatime


#Set a TOKEN variable
os.environ['TOKEN'] = '<ADD_BEARER_TOKEN'>


def auth():
	return os.getenv('TOKEN')

#take the bearer token, pass it for authorization and return headers
#taht are use to access the API
def create_headers (bearer_token):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	return headers


def create_url (keyword, start_date, end_datem max_results):

	#using full-archive search endpoint
	search_url = "https://api.twitter.com/2/tweets/search/all"

	query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': 100,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,geo,created_at',
                    'user.fields': 'id,name,username',
                    'place.fields': 'country,geo,name',
                    'next_token': {}}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#Inputs for the request
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "#pfizer"
start_time = "2021-03-01T00:00:00.000Z"
end_time = "2021-03-31T00:00:00.000Z"

url = create_url(keyword, start_time,end_time, max_results)

json_response = connect_to_endpoint(url[0], headers, url[1])

print(json.dumps(json_response, indent=4, sort_keys=True))