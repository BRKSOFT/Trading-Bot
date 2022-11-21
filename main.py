from binance import Client
import pandas as pd
import scalping
import mlOne
import bollinger_bands
import rsi_sma


client = Client(api_key, secret_key)


def getminutedata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback))
    frame = frame.iloc[:, :6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame


df = getminutedata('ETHUSDT', '4h', '1 year ago')
scalping.scalping(df)
