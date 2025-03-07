import pytse_client as tse

tse.download(symbols="فملی", write_to_csv=True)  # optional
data = tse.Ticker("فملی")
fplt.plot(data.history, type='candle')
# ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
# from matplotlib.finance import candlestick_ohlctickers = tse.download(symbols="all", write_to_csv=True)