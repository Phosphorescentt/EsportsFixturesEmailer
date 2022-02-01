import sendgrid
import os

from sendgrid.helpers.mail import *

import PandaScore

import CONFIG
import SECRETS

sg = sendgrid.SendGridAPIClient(SECRETS.SG_API_KEY)
ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY)

tournaments = ps.get_running_tournaments()

# Next actions for me 
# 1) Get rid of all the garbage tournaments that I don't care about
# ==> Filtering by game
# ==> Filtering by region
# 2) Show results for finished matches
# 3) Improve formatting (include images, actually use formatting stuff)

html_content = ""
for tournament in tournaments:
    output_string = ""

    league = tournament["league"]
    serie = tournament["serie"]
    tournament = tournament
    matches = tournament["matches"]

    output_string += "<h1>" + league["name"] + "</h1><br>"

    try:
        output_string += "<h2>" + serie["name"] + "</h2><br>"
    except:
        pass

    output_string += "<h3>" + tournament["name"] + "</h3><br>"

    for match in matches:
        output_string += match["name"] + "<br>"

    html_content += output_string + "<hr>"

from_email = Email(CONFIG.FROM_EMAIL)
to_email = To(CONFIG.TO_EMAIL)
subject = CONFIG.EMAIL_SUBJECT
content = HtmlContent(html_content)
mail = Mail(from_email, to_email, subject, content)

response = sg.send(message=mail)
print(response.status_code)
print(response.body)
print(response.headers)
