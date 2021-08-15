# Commented out IPython magic to ensure Python compatibility.
from yahoo_fin import stock_info as si
from itertools import chain
from .constants import CHOICE, RECIEPIENT_EMAIL, PERCENT
from .save_file import save_prices_crypto_to_file, save_prices_snp500_to_file, save_prices_yahoo_to_file

OLD_TICKER_AND_PRICES = []


def option(opt):
    if (opt == 'crypto'):
        return 2
    elif (opt == 'yahoo_fin'):
        return 1
    else:
        return 3


def file_option(file):
    """
    """
    switcher = {
        'crypto': 'prices_crypto.txt',
        'sp500': 'prices_snp500.txt',
        'yahoo_fin': 'prices_yahoo.txt'
    }

    return switcher.get(file, "Invalid Selection")


def update_prices():
    # Display the message within the output widget.
    try:
        import json
        with open(file_option(CHOICE)) as f:
            json_data = json.load(f)

        # OLD_TICKER_AND_PRICES = json.loads("OLD_TICKER_AND_PRICES")
        OLD_TICKER_AND_PRICES = json_data
        #OLD_TICKER_AND_PRICES = [[i[0], float(i[1])] for i in OLD_TICKER_AND_PRICES.strip('][').split(', ')]
        print('Prices updated!')
    except Exception as e:
        print(file_option(CHOICE))
        print(f'Error encountered: {e}')


def value(ticker, Percentage):
    try:
        ticker_and_price = next(
            chain((c for c in OLD_TICKER_AND_PRICES if c[0] == ticker), []))
        if si.get_live_price(ticker) >= (1.0 + Percentage)*ticker_and_price[1] or \
                si.get_live_price(ticker) <= (1.0 - Percentage)*ticker_and_price[1]:
            return ticker_and_price[1]
        return False
    except:  # Exception as e:
        print('Error fetching ticker: ', ticker)


def get_and_save_prices(stocks, stock: str) -> None:
    TICKER_AND_PRICE = []
    for i in stocks:
        try:
            TICKER_AND_PRICE.append((i, si.get_live_price(i)))
        except:
            print('Could not locate stock for ticker: ', i)
    if stock == 'yahoo_fin':
        save_prices_yahoo_to_file()
    elif stock == 'crypto':
        save_prices_crypto_to_file()
    else:
        save_prices_snp500_to_file()
    return TICKER_AND_PRICE


def save_file(choice, TICKER_AND_PRICE):
    if choice == 1:
        TICKER_AND_PRICE = save_prices_yahoo_to_file(TICKER_AND_PRICE)
    elif choice == 2:
        TICKER_AND_PRICE = save_prices_crypto_to_file(TICKER_AND_PRICE)
    elif choice == 3:
        TICKER_AND_PRICE = save_prices_snp500_to_file(TICKER_AND_PRICE)


def percentage(perc):
    if not isinstance(perc, int):
        print("Please choose an integer value. Choose 0 to exit!")
        return None
    return perc
