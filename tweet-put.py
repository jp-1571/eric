import pip
pip.main(['install','tweepy'])
pip.main(['install','requests'])
import tweepy
import requests
from tweepy import *

CONSUMER_KEY = 'j8WuV98aFQgnwr6zfrVfTxTJy'
CONSUMER_SECRET = 'eAApX62NWp0I0ppC3uAzsaGFFfqOTDZifKvlx0HMtPzzLcwV4i'
ACCESS_KEY = '956010179769839621-TcLGJVwi8d1J6p0IUdW4bGruse9re9w'
ACCESS_SECRET = 'xQvXqMPyXEq85tNIIa8ijv7EVwAQ7BEfskYMBU5jyeHGZ'
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
url = "http://127.0.0.1:5002/putLocations"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

sports_points = [] ; entertainment_points = []

def clearMap():
    global sports_points ; global entertainment_points
    sports_points = [] ; entertainment_points = [];
    data = {'sports': sports_points, 'entertainment': entertainment_points}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    
def gatherPoints(status):
    lng = status.coordinates.get('coordinates')[0]
    lat = status.coordinates.get('coordinates')[1]
    sports_points.append({"lat": lat, "lng": lng})
    data = {'sports': sports_points, 'entertainment': entertainment_points}
    return data

class MyStreamListener(StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
    
    def on_status(self, status):
        if (status.coordinates is not None):
            self.num_tweets += 1
            #print("found tweet")
            data = gatherPoints(status)
            r = requests.put(url, data=json.dumps(data), headers=headers)
        if self.num_tweets > 100:
            return False
        return True

clearMap()
myGeoStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
myGeoStream.filter(follow=None, locations=[-125,26,-69,47])

    
