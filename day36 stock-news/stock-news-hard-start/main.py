import requests
import os
from news import StockNews
from dates_generator import DatesFinder
from sending_sms import SendingSms

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL  = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "204e30fe-b896-4c35-9245-537f38e6b0a5"
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()

# -------DATES------------------------------------ ------------------------------------ function returning the date

# if yesterday or day before there was no stock trade use stock data for the previous trade day
stock_dates = DatesFinder(stock_data)

# -----------------------------------------------------------
#  if the deffer between stock value yesterday to the day before bigger than -5 % or +2 %
#  find 3 top headlines obout the company from the last month
close_time_stock_delta = float(stock_dates.stock_data_close_yesterday) - float(stock_dates.stock_data_close_2days_ago)
close_time_stock_percent = (close_time_stock_delta/stock_dates.stock_data_close_yesterday)*100
print(close_time_stock_percent)

if 2 <= close_time_stock_percent <= -5:
    news = StockNews(COMPANY_NAME,(self,COMPANY_NAME,NEWS_ENDPOINT,NEWS_API_KEY))
    #send_sms=SendingSms(news.article_data_header3, close_time_stock_percent, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


