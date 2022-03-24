import sendgrid

from sendgrid.helpers.mail import Email, To, HtmlContent, Mail

import PandaScore
import Processing

import CONFIG
import SECRETS


ps = PandaScore.PandaScoreAPIClient(SECRETS.PS_API_KEY)
sg = sendgrid.SendGridAPIClient(SECRETS.SG_API_KEY)

series = ps.get_running_series()

html = Processing.generate_html(series)

from_email = Email(CONFIG.FROM_EMAIL)
subject = CONFIG.EMAIL_SUBJECT
content = HtmlContent(html)

for email in CONFIG.TO_EMAILS:
    to_email = To(email)
    mail = Mail(from_email, to_email, subject, content)

    response = sg.send(message=mail)
    print(response.status_code)
    print(response.body)
    print(response.headers)
