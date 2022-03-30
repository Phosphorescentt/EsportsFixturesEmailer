import requests

from data import DATA

class PandaScoreAPIClient:
    def __init__(self, API_KEY, CONFIG):
        self.API_KEY = API_KEY

        self.headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + self.API_KEY
        }

        self.config = CONFIG

    def _get_request(self, url: str):
        return requests.request("GET", url, headers=self.headers)
    
    def apply_config(self, url: str) -> str:
        url += "?"
        url += "&page=" + str(self.config["page"])
        url += "&per_page=" + str(self.config["items_per_page"])
        url += "&tier=" + self.config["tier"]

        return url

    def get_running_series(self) -> list:
        url = "https://api.pandascore.co/series"
        url = self.apply_config(url)
        
        return self._get_request(url).json()

    def get_running_tournament_by_id_slug(self, id_slug: str) -> dict:
        url = "https://api.pandascore.co/tournaments/"
        url += id_slug

        url = self.apply_config(url)

        return self._get_request(url).json()

    def get_leagues_by_game_id_slug(self, id_slug: str) -> list:
        try:
            id = DATA.GAMES.find_id(id_slug)["id"]
        except ValueError as e:
            print(e)

        try:
            id = DATA.GAMES.find_slug(id_slug)["id"]
        except ValueError as e:
            print(e)

        url = f"https://api.pandascore.co/videogames/{id}/leagues" 
        url = self.apply_config(url)

        return self._get_request(url).json()
