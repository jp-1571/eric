import pip
pip.main(['install','requests'])
import requests
import time
import random

sports_points = []
entertainment_points = []

url = "http://127.0.0.1:5002/putLocations"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def clearMap():
    global sports_points ; global entertainment_points
    sports_points = [] ; entertainment_points = [];
    data = {'sports': sports_points, 'entertainment': entertainment_points}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    
clearMap()
for i in range(1, 100):
    time.sleep(0.5)
    poslat = round(random.randint(0,10) / 10, 2)
    poslong = round(random.randint(0,10) / 10, 2)
    sports_points.append({"lat": 41.2 + poslat, "lng": -86.74 + poslong})

    #sports_points = [{"lat": 42.702496, "lng": -86.239694},                         
    #{"lat": 41.712496, "lng": -86.249694}]
    
    data = {'sports': sports_points, 'entertainment': entertainment_points}
    r = requests.put(url, data=json.dumps(data), headers=headers)
    

    
    
    
