import pytse_client as tse
tickers = tse.download(symbols="all", write_to_csv=True)
