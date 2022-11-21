from binance import Client
import pandas as pd
import scalping
import mlOne
import bollinger_bands
import rsi_sma


api_key = 'kgcF15uxEQiQ6axBDxzUO2XZzUebzvAaDmzVI0JLoMNExwPmOralZ7iON7WZ56gR'
secret_key = 'fHkz7A3ESW7ynD74OPnYDUvRxS70nTJZVzF9et5gIidoO5EpcrZNY0LNMFfxUJM4'
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
