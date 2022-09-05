from twilio.rest import Client


class SendingSms:

    def __init__(self, headlines, percent, account_sid, auth_token):
        client = Client(account_sid, auth_token)
        self.sms_stock_news = client.messages \
            .create(

            body=f"TSLA: {percent} ,Headline: {headlines}",
            from_='+19733812827',
            to='+972548367811',
        )
