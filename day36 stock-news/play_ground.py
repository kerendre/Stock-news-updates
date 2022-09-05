import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
my_url = STOCK_ENDPOINT


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "204e30fe-b896-4c35-9245-537f38e6b0a5"
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()
print(stock_data)

# -------DATES------------------------------------ ------------------------------------ function returning the date
# yesterday and 2 days before :
# TODO if yesterday or day before there was trade trade use data day before try,except,else.finally
#   https://www.w3schools.com/python/python_try_except.asp

today = date.today()
yesterday = str(today - timedelta(days=1))
day_before_yesterday = str(today - timedelta(days=2))

stock_data_close_yesterday = float(data["Time Series (Daily)"][yesterday]["4. close"])
print(stock_data_close_yesterday)
#
stock_data_close_2days_ago = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])
print(stock_data_close_2days_ago)

# -----------------------------------------------------------
#TODO if the deffert between stock value today to tommorow bigger then 5 % do something
close_time_stock_delta = stock_data_close_yesterday - stock_data_close_2days_ago
print(close_time_stock_delta)

close_time_stock_percent = (close_time_stock_delta/stock_data_close_yesterday)*100
print((abs(close_time_stock_percent)))


if abs(close_time_stock_percent) >= 5:
    print("Get News")
    #oparetat_get_news

else:
    pass
#-----------------------------------------------_-------------------------------




## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


import requests

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = 'd799a79bcb9144fbaef9ecb8d101148b'  # '204e30fe-b896-4c35-9245-537f38e6b0a5'
# TODO change to global COMPANY_NAME
COMPANY_NAME = "Tesla Inc"
parameters = {
    "apiKey": api_key,
    "qInTitle": COMPANY_NAME,
    "language": "en",
}

response = requests.get(url=NEWS_ENDPOINT, params=parameters)
print(response)

# to get the data about connection mistakes to the API, always write this part
response.raise_for_status()
articles_data = (response.json())['articles']

