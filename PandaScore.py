import requests

class PandaScoreAPIClient:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.API_KEY
        }

    def get_running_series(self):
        url = "https://api.pandascore.co/series"
        url += "?&page=1&per_page=1&tier=s"
        
        response = requests.request("GET", url, headers=self.headers)
        return response.json()

    def get_running_tournament_by_id_slug(self, id_slug):
        url = "https://api.pandascore.co/tournaments/"
        url += id_slug

        response = requests.request("GET", url, headers=self.headers)
        return response.json()
