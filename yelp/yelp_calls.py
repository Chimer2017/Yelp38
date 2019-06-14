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

output_json = []




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
        biz_info = response['businesses']
        idRes=""
        if len(biz_info) > 0:
            idRes = biz_info[0]['id']
            response = yelp_api.business_query(id=idRes)
            output_json.append({
                'name': nameRes,
                'address': addressRes,
                'website': p['website'],
                'rating': response['rating'],
                'review_count': response['review_count'],
            })

with open('final.json','w') as outfile:
    json.dump(output_json,outfile)







    
