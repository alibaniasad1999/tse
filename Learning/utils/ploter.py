import pandas as pd
import matplotlib.pyplot as plt

def plot_stock(df):
    df = df.reset_index()
    df.index = pd.to_datetime(df.index)
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111)
    ax.set_title('Stock Closing Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.plot(df['close'], label='Close Price')
    ax.plot(df['ma5'], label='MA5')
    ax.plot(df['ma10'], label='MA10')
    ax.plot(df['ma20'], label='MA20')
    ax.plot(df['ma60'], label='MA60')
    ax.plot(df['ma120'], label='MA120')
    ax.plot(df['ma240'], label='MA240')
    ax.legend()
    plt.show()


# plot ichimoku cloud #
def plot_ichimoku(df):
    df = df.reset_index()
    df.index = pd.to_datetime(df.index)
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111)
    ax.set_title('Stock Closing Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.plot(df['close'], label='Close Price')
    ax.plot(df['tenkan_sen'], label='Tenkan-sen')
    ax.plot(df['kijun_sen'], label='Kijun-sen')
    ax.plot(df['senkou_span_a'], label='Senkou Span A')
    ax.plot(df['senkou_span_b'], label='Senkou Span B')
    # ax.plot(df['chikou_span'], label='Chikou Span')
    ax.legend()
    plt.show()



# plot RSI #
def plot_RSI(df):
    df = df.reset_index()
    df.index = pd.to_datetime(df.index)
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(111)
    ax.set_title('Stock Closing Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.plot(df['RSI'], label='RSI')
    ax.legend()
    plt.show()

