import requests
import json
import urllib

class Clash_Studio():
    def __init__(self, API_TOKEN):
        self.headers = {"content-type":"application/json", "Authorization":f"Bearer {API_TOKEN}"}
    
    def get_player_data(self, player_tag):
        safe_tag = urllib.parse.quote_plus(player_tag)

        r = requests.get(f"https://api.clashofclans.com/v1/players/{safe_tag}", headers = self.headers)
        resp = json.loads(r.text)

        return resp

    