import numpy as np
import pandas as pd

# add ichimoku cloud data
def ichimoku(df):
    nine_period_high = df['high'].rolling(window= 9).max()
    nine_period_low = df['low'].rolling(window= 9).min()
    df['tenkan_sen'] = (nine_period_high + nine_period_low) /2

    period26_high = df['high'].rolling(window=26).max()
    period26_low = df['low'].rolling(window=26).min()
    df['kijun_sen'] = (period26_high + period26_low) / 2

    df['senkou_span_a'] = ((df['tenkan_sen'] + df['kijun_sen']) / 2).shift(26)

    period52_high = df['high'].rolling(window=52).max()
    period52_low = df['low'].rolling(window=52).min()
    df['senkou_span_b'] = ((period52_high + period52_low) / 2).shift(26)

    df['chikou_span'] = df['close'].shift(-26)

    return df

# moving average indicator #
def moving_average(df):
    df['ma5'] = df['close'].rolling(window=5).mean()
    df['ma10'] = df['close'].rolling(window=10).mean()
    df['ma20'] = df['close'].rolling(window=20).mean()
    df['ma60'] = df['close'].rolling(window=60).mean()
    df['ma120'] = df['close'].rolling(window=120).mean()
    df['ma240'] = df['close'].rolling(window=240).mean()
    return df


# add RSI data #
def RSI(df):
    U = np.where(df['close'].diff(1) > 0, df['close'].diff(1), 0)
    D = np.where(df['close'].diff(1) < 0, df['close'].diff(1)*(-1), 0)
    AU = pd.DataFrame(U).rolling(window=14, min_periods=14).mean()
    AD = pd.DataFrame(D).rolling(window=14, min_periods=14).mean()
    RSI = AU.div(AD+AU)*100
    df['RSI'] = RSI.values
    return df

