from yahoo_fin import stock_info as si
import json

def save_prices_snp500_to_file(TICKER_AND_PRICE):
    TICKER_AND_PRICE = []
    with open('prices_snp500.txt', 'w') as f:
        stocks = si.tickers_sp500()
        for stock in stocks:
            TICKER_AND_PRICE.append((stock, si.get_live_price(stock)))
        f.write(json.dumps(TICKER_AND_PRICE))
    return TICKER_AND_PRICE


def save_prices_crypto_to_file(TICKER_AND_PRICE):
    TICKER_AND_PRICE = []
    with open('prices_crypto.txt', 'w') as f:
        stocks = si.get_top_crypto()
        stocks = stocks['Symbol']
        for stock in stocks:
            TICKER_AND_PRICE.append((stock, si.get_live_price(stock)))
        f.write(json.dumps(TICKER_AND_PRICE))
    return TICKER_AND_PRICE


def save_prices_yahoo_to_file(TICKER_AND_PRICE):
    TICKER_AND_PRICE = []
    with open('prices_yahoo.txt', 'w') as f:
        stocks = si.get_day_most_active()
        stocks = stocks['Symbol']
        for stock in stocks:
            TICKER_AND_PRICE.append((stock, si.get_live_price(stock)))
        f.write(json.dumps(TICKER_AND_PRICE))
    return TICKER_AND_PRICE