from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='WYLFLXRTGTIV26S3',output_format='pandas')
import requests
import csv
#%%
data = ts.get_daily_adjusted('GOOGL')
