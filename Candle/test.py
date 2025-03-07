import pytse_client as tse
tickers = tse.download(symbols="all", write_to_csv=True)
for stock in tickers:
    open = tickers[stock].open.tail(3).to_numpy()
    high = tickers[stock].high.tail(3).to_numpy()
    low = tickers[stock].low.tail(3).to_numpy()
    close = tickers[stock].adjClose.tail(3).to_numpy()

