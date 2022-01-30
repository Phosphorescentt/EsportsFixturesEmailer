import requests

class PandaScoreAPIClient:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.API_KEY
        }

    def get_running_tournaments(self):
        url = "https://api.pandascore.co/tournaments/running?"
        url += "&page=1&per_page=50&tier=s"
        response = requests.request("GET", url, headers=self.headers)

        return response.json()
