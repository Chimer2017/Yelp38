from yelpapi import YelpAPI
from pprint import pprint
import os
import json



yelp_api = YelpAPI(os.environ.get('YELP_API'))
search_results = []

nameRes = ""
addressRes = ""
stateRes = 'CO'
cityRes = 'Denver'


with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data:
        nameRes = p['name']
        addressRes = p['address']
        response = yelp_api.business_match_query(name=nameRes,
                                         address1=addressRes,
                                         city=cityRes,
                                         state=stateRes,
                                         country='US')
        p['rating'] = response.rating
        p['review_count'] = response.review_count
    
