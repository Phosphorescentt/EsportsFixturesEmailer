import PandaScore
import Processing

from settings import CONFIG, SECRETS
from data import DATA

# def main():
#     ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY, CONFIG.PS_CONFIG)
#     series = ps.get_running_series()
#
#     html = Processing.generate_html_from_series(series)
#
#     return html


def main():
    ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY, CONFIG.PS_CONFIG)

    leagues_by_videogame = {}

    for requested_game in CONFIG.GAMES_CONFIG:
        try:
            g = DATA.GAMES.find_id(requested_game)
        except ValueError as e:
            print(e)

        try:
            g = DATA.GAMES.find_name(requested_game)
        except ValueError as e:
            print(e)

        try:
            g = DATA.GAMES.find_slug(requested_game)
        except ValueError as e:
            print(e)
            
        if not g:
            raise ValueError(f"Could not find game {requested_game}")

        id = g["id"]
        leagues_by_videogame[id] = ps.get_leagues_by_game_id_slug(id)

    html = Processing.generate_html_from_leagues_by_vg(leagues_by_videogame)
    return html
