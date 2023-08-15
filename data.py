from datetime import datetime, timedelta
import requests 
import pandas as pd

url = "https://api.pro.coinbase.com"
symbol = "BTC-USD"
size = "3600"
time_end = datetime.now()
delta = timedelta(hours=1)
time_start = time_end - (300*delta)

time_end = time_end.isoformat()
time_start = time_start.isoformat()

param = {
    "start":time_start,
    "end":time_end,
    "granularity":size,
}
data = requests.get(f"{url}/products/{symbol}/candles", 
                    params = param, 
)

df = pd.DataFrame(data.json(), columns= ["Time", "Low", "High", "Open", "Close", "Volume"])

df["Date"] = pd.to_datetime(df["Time"], unit='s')

df = df[["Date", "Open", "Low", "High", "Close", "Volume"]]