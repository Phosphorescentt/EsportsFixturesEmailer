import PandaScore

from settings import CONFIG, SECRETS

def generate_html_from_series(data):
    """
    1. iterate over data
    2. get tournaments for each serie
    3. get matches for each tournament
    4. get match info
    5. collect into html
    6. return data
    """

    ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY, CONFIG.PS_CONFIG)

    out = ""
    for serie in data:
        out += "<hr>"
        league = serie["league"]
        out += "<h1>" + league["name"] + "</h1><br>"

        s_name = serie["name"]
        if s_name is not None:
            out += "<h2>" + s_name + "</h2><br>"

        tournaments = serie["tournaments"]
        if tournaments is not None:
            for tournament in tournaments:
                out += "<h3>" + tournament["name"] + "</h3><br>"
                slug = tournament["slug"]
                tournament_info = ps.get_running_tournament_by_id_slug(slug)

                matches = tournament_info["matches"]
                if matches is not None:
                    for match in matches:
                        out += match["name"] + "<br>"

    return out


def generate_html_from_leagues_by_vg(leagues_by_vg):
    ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY, CONFIG.PS_CONFIG)

    return leagues_by_vg
