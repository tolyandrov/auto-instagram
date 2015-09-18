from instagram.client import InstagramAPI
import time, random
import urllib,json,urllib2, requests, re


user_agent = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7'
headers = { 'User-Agent' : user_agent,
            "Content-type": "application/x-www-form-urlencoded"
            }
likedDict = {}


#Auth for Scraping method
#TODO: Scraping method :D
def reqAuth(user, pas):
    r = requests.get('https://websta.me/login/', auth=(user, pas))
    print(r.status_code)

