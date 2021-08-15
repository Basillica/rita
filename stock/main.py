# Commented out IPython magic to ensure Python compatibility.
from yahoo_fin import stock_info as si
from .constants import CHOICE, RECIEPIENT_EMAIL, PERCENT
from .utils import get_and_save_prices, value, percentage, update_prices, save_file, option
from .mail import send_mail

PERCENT = 5
RECIEPIENT_EMAIL = "eienneceasar@gmail.com"


# Initialize arrays
TICKERS = []
message = []
TICKER_AND_PRICE = []


def driver(stock: str, Percentage, TICKER_AND_PRICE) -> None:
    if stock == 'yahoo_fin':
        stocks = si.get_day_most_active()
        stocks = stocks['Symbol']
    elif stock == 'crypto':
        stocks = si.get_top_crypto()
        stocks = stocks['Symbol']
    else:
        stocks = si.tickers_sp500()
    print(f'Chosen portfolio: {stock}')
    TICKER_AND_PRICE = get_and_save_prices(stocks, stock)

    for i in stocks:
        evaluator = value(i, Percentage)
        if evaluator:
            message.append((i, si.get_live_price(i), evaluator))
    return TICKER_AND_PRICE


def main(TICKER_AND_PRICE):
    _percentage = percentage(PERCENT)
    update_prices()
    save_file(option(CHOICE), TICKER_AND_PRICE)
    print('Done fetching current prices. File is ready to be downloaded.')

    print(f'Chosen percentage: {_percentage}')
    _percentage = _percentage/100.0
    TICKER_AND_PRICE = driver(CHOICE, _percentage)

    try:
        send_mail(RECIEPIENT_EMAIL)
    except:
        print('Email could not be sent!')
