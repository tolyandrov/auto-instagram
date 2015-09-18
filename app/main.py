from instagram.client import InstagramAPI
import time, random
import urllib,json,urllib2, requests, re


user_agent = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7'
headers = { 'User-Agent' : user_agent,
            "Content-type": "application/x-www-form-urlencoded"
            }
likedDict = {}


# Auth for Scraping method
# TODO: Scraping method :D
# def reqAuth(user, pas):
#     r = requests.get('https://websta.me/login/', auth=(user, pas))
#     print(r.status_code)


client_id = raw_input("Client ID: ").strip()
client_secret = raw_input("Client Secret: ").strip()
redirect_uri = raw_input("Redirect URI: ").strip()
raw_scope = ("").strip()
scope = raw_scope.split(' ')
if not scope or scope == [""]:
    scope = ["basic"]
api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

redirect_uri = api.get_authorize_login_url(scope = scope)
print ("Visit this page and authorize access in your browser: "+ redirect_uri)
code = (str(raw_input("Paste in code in query string after redirect: ").strip()))
access_token, userdata = api.exchange_code_for_access_token(code)
print ("access token: " )
print (access_token)



def get_relationship(userId):
    unfollowed=0

    followUrl = "https://api.instagram.com/v1/users/%s/relationship?access_token=%s&client_id=%s" \
                % (userId, access_token, client_id)

    values = {'access_token' : access_token,
              'client_id' : client_id}
    try:
        data = urllib.urlencode(values)
        req = urllib2.Request(followUrl,None,headers)
        response = urllib2.urlopen(req)
        result = response.read()
        dataObj = json.loads(result)
        status = dataObj["data"]
        incoming = status["incoming_status"]
        print '%s - %s ' % (userId, incoming)
        if incoming != "followed_by":
            return DOES_NOT_FOLLOW
        else:
            return FOLLOWS
    except Exception, e:
        print e
    return unfollowed
