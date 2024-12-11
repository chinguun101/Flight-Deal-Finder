import os
from twilio.rest import Client
import smtplib

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:
    """
    A class to manage sending notifications via different channels, such as SMS, WhatsApp, and email.
    """

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])


    def send_emails(self, mail_list, message_body):
        """
        Sends email notifications to a list of recipients with the specified message body.

        Parameters:
            mail_list (list): A list of email addresses to send the notification to.
            message_body (str): The content of the email message.
        """
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(os.environ['EMAIL'],os.environ['PASSWORD'])
            for mail in mail_list:
                connection.sendmail(
                    from_addr=os.environ['EMAIL'],
                    to_addrs=mail,
                    msg= message_body
                )

    def send_sms(self, message_body):
        """
        Sends an SMS notification with the specified message body.

        Parameters:
            message_body (str): The content of the SMS message.
        """
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        """
        Sends a WhatsApp notification with the specified message body.

        Parameters:
            message_body (str): The content of the WhatsApp message.
        """
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)
