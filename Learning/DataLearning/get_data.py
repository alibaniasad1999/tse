import pytse_client as tse

def get_data(symbols=None, write_to_csv=False, adjust=False):
    if symbols is None:
        symbols = "all"
    tickers = tse.download(symbols=symbols, write_to_csv=write_to_csv, adjust=adjust)  # Download the data
    return tickers  # Return the tickers
