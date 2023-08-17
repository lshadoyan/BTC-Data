from datetime import datetime, timedelta
from tqdm import tqdm
import pandas as pd
import requests 


url = "https://api.pro.coinbase.com"
symbol = "BTC-USD"
size = "3600"
def candle_chunk(time_start, time_end):
    
    param = {
        "start":time_start,
        "end":time_end,
        "granularity":size,
    }
    data = requests.get(f"{url}/products/{symbol}/candles", 
                        params = param, 
    )
    df = pd.DataFrame(data.json(), columns= ["Time", "Low", "High", "Open", "Close", "Volume"])

    return df

def all_candles(start): 

    time_end = datetime.now()
    delta = timedelta(hours=1)
    df = pd.DataFrame()
    first_start = start
    candles = 300
    bar = tqdm(total=int((time_end - first_start).total_seconds() / 3600))
    while time_end > first_start:
        difference = time_end - first_start
        hour_difference = difference.total_seconds() / 3600
        if(hour_difference) <= 300:
            candles = hour_difference

        time_start = time_end - (candles*delta)

        end = time_end.isoformat()
        start = time_start.isoformat()
        df = pd.concat([df,candle_chunk(start, end)])
        time_end = time_end - candles*delta
        bar.update(int(candles))
    bar.close()
    to_csv(df)

def to_csv(df):
    df["Date"] = pd.to_datetime(df["Time"], unit='s')

    df = df[["Date", "Open", "Low", "High", "Close", "Volume"]]
    df.to_csv("Bitcoin_data.csv", index=False)

all_candles(datetime(2021, 1, 1))