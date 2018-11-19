import requests, bs4
from bs4 import BeautifulSoup

req = requests.get("https://www.honeywell.com/")
#req = requests.get("https://play.google.com/store/apps/details?id=com.facebook.orca&hl=en")
soup = bs4.BeautifulSoup(req.text,"html5lib")
