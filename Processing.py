import PandaScore

import SECRETS


def generate_html(data):
    """
    1. iterate over data
    2. get tournaments for each serie
    3. get matches for each tournament
    4. get match info
    5. collect into html
    6. return data
    """

    ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY)    

    out = "<hr>"
    # out = []
    for serie in data:
        tournaments = serie["tournaments"]
        out += "<h1>" + serie["name"] + "</h1><br>"
        for tournament in tournaments:
            out += "<h3>" + tournament["name"] + "</h3><br>"
            slug = tournament["slug"]
            tournament_info = ps.get_running_tournament_by_id_slug(slug)

            for match in tournament_info["matches"]:
                # out += match
                out += match["name"] + "<br>"
                # out.append(match)

    return out
