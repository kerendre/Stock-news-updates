from datetime import date, timedelta


class DatesFinder:
    def __init__(self, stock_data):
        today = date.today()
        self.days_list = [str(today - timedelta(days=1)),
                          str(today - timedelta(days=2)),
                          str(today - timedelta(days=3)),
                          str(today - timedelta(days=4)),
                          str(today - timedelta(days=5))
                          ]

        self.stock_data_close_yesterday = ""
        self.stock_data_close_2days_ago = ""

        for day in self.days_list:
            if (self.stock_data_close_yesterday or self.stock_data_close_2days_ago) == "":
                try:
                    self.stock_data_close_yesterday = float(stock_data["Time Series (Daily)"][day]["4. close"])

                except KeyError:
                    self.last_trading_day = day
                    print(f"yesterday:no stock trade on {day} moving to the previous day ")

                else:
                    for day_before in self.days_list[(self.days_list.index(day) + 1):]:
                        if self.stock_data_close_2days_ago == "":
                            try:
                                self.stock_data_close_2days_ago = float(
                                    stock_data["Time Series (Daily)"][(day_before)]["4. close"])

                            except KeyError:
                                print(f"no stock trade on {day_before} moving to the previous day ")

                            else:
                                print(
                                    f"stock_data_at closing time stock data at {day} the last trading day "
                                    f"is {self.stock_data_close_yesterday} \n "
                                    f"stock_data_at closing time  at {day_before} the one before last trading day"
                                    f"is {self.stock_data_close_2days_ago}")
