import datetime
import pandas as pd

network = 'eth'

emissions_df = pd.read_csv(f'data/{network}_emissions.csv')
txs_df = pd.read_csv(f'data/{network}_txs.csv')

data = []
for index, row in emissions_df.iterrows():
    txs_count = txs_df.loc[txs_df['Date(UTC)'] == row['Date']]['Value'].values[0]
    timestamp = int(datetime.datetime.strptime(row['Date'], '%Y-%m-%d').timestamp())
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    data.append({
        "timestamp": timestamp,
        "date": date,
        "total_txs": txs_count,
        "emissions_per_day": round(row['best'] * 1_000_000),
        "emissions_per_tx": txs_count > 0 and (row['best'] * 1_000_000) / txs_count or 0
    })

with open(f'out/{network}_data.json', 'w') as outfile:
	outfile.write(str(data))
