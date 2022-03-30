import sendgrid

from sendgrid.helpers.mail import Email, To, HtmlContent, Mail

import render

from config import SETTINGS, SECRETS

sg = sendgrid.SendGridAPIClient(SECRETS.SG_API_KEY)

html = render.main()

from_email = Email(SETTINGS.FROM_EMAIL)
subject = SETTINGS.EMAIL_SUBJECT
content = HtmlContent(html)

for email in SETTINGS.TO_EMAILS:
    to_email = To(email)
    mail = Mail(from_email, to_email, subject, content)

    response = sg.send(message=mail)
    print(response.status_code)
    print(response.body)
    print(response.headers)

