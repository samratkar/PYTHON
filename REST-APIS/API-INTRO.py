import numpy as np
import pandas as pdb
import requests, json
import pprint
api_key = 'AIzaSyBXrK8md7uaOcpRpaluEGZAtdXS4pcI5xo'
address = "Mana Pristine"
split_add = address.split(" ")
address = '+'.join(split_add)
print (address)
url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}".format(address,api_key)
response = requests.get(url)
print(type(response.text))
#print(response.text)
response_dict = json.loads(response.text)
print (response_dict)
pprint.pprint(response_dict)

##########################################################################3333
# Input to the fn: Address in standard human-readable form
# Output: Tuple (lat, lng)

api_key = "AIzaSyBXrK8md7uaOcpRpaluEGZAtdXS4pcI5xo"

def address_to_latlong(address):
    # convert address to the form x+y+z
    split_address = address.split(" ")
    address = "+".join(split_address)

    # pass the address to the URL
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}".format(address, api_key)

    # connect to the URL, get response and convert to dict
    r = requests.get(url)
    r_dict = json.loads(r.text)
    lat = r_dict['results'][0]['geometry']['location']['lat']
    lng = r_dict['results'][0]['geometry']['location']['lng']

    return (lat, lng)


# getting some coordinates
print(address_to_latlong("UpGrad, Nishuvi Building, Worli, Mumbai"))
print(address_to_latlong("IIIT Bangalore, Electronic City, Bangalore"))
