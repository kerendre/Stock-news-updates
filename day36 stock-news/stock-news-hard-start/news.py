import requests


class StockNews:
    def __init__(self, COMPANY_NAME, NEWS_ENDPOINT , NEWS_API_KEY ):

        parameters = {
            "apiKey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
            "language": "en",
            "excludeDomains":"breitbart.com,clickhole.com,Null,dailymail.co.uk,Daily Mail",
}

        self.response = requests.get(url=NEWS_ENDPOINT, params=parameters)
        print(self.response)

        # to get the data about connection mistakes to the API, always write this part
        self.response.raise_for_status()
        self.articles_data = (self.response.json())['articles']
        self.article_data_header3=(self.articles_data[:3])

