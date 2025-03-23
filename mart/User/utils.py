from django.core.mail import EmailMessage as Em
import os

class Utils:
    @staticmethod
    def send_email(data):
        email = Em(
            subject = data['subject'],
            body = data['body'],
            from_email = os.environ.get('EMAIL_FROM'),
            to= [data['to_email']]
        )
        email.send()
        

