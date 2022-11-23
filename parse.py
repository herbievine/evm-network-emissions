# Parser to modify dates to make it easier to parse

import datetime
import pandas as pd

# Change path to where the file is located
txs = pd.read_csv(r'data/eth_txs.csv')

data = []
for index, row in txs.iterrows():
    date = datetime.datetime.fromtimestamp(row['UnixTimeStamp']).strftime('%Y-%m-%d')
    txs['Date(UTC)'][index] = date

txs.to_csv('data/eth_txs_parsed.csv', index=False)
