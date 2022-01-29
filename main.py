import sendgrid
import os

from sendgrid.helpers.mail import *

import CONFIG
import SECRETS

sg = sendgrid.SendGridAPIClient(api_key=SECRETS.SG_API_KEY)
from_email = Email(CONFIG.FROM_EMAIL)
to_email = To(CONFIG.TO_EMAIL)
subject = CONFIG.EMAIL_SUBJECT
content = Content("text/plain", "TESTING")
mail = Mail(from_email, to_email, subject, content)

response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
