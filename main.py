import sendgrid
import os

from sendgrid.helpers.mail import *

import PandaScore

import CONFIG
import SECRETS

sg = sendgrid.SendGridAPIClient(SECRETS.SG_API_KEY)
ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY)

tournaments = ps.get_running_tournaments()

tournament_slugs = [t["slug"] for t in tournaments]

data_content = "<br>".join(tournament_slugs)

from_email = Email(CONFIG.FROM_EMAIL)
to_email = To(CONFIG.TO_EMAIL)
subject = CONFIG.EMAIL_SUBJECT
content = HtmlContent(data_content)
mail = Mail(from_email, to_email, subject, content)

response = sg.send(message=mail)
print(response.status_code)
print(response.body)
print(response.headers)
