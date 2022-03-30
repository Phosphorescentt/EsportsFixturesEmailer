from flask import Flask

import PandaScore
import Processing

from config import SETTINGS, SECRETS

app = Flask(__name__)


@app.route("/")
def render():
    ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY, SETTINGS.PS_CONFIG)
    series = ps.get_running_series()

    html = Processing.generate_html_from_series(series)

    return html
