import pandas as pd
import numpy as np


file_path = r'C:\Users\User\Desktop\out_and_in\nonfarm_population_ratio_2008_to_present.csv'
market_index = pd.read_csv(file_path)
market_index['date'] = pd.to_datetime(market_index['date'])
market_index = market_index.set_index('date')
market_index = market_index[[ 'cpi', 'nonfarm_employment', 'total_population', 'nonfarm_population_ratio']]

file_path = r'C:\Users\User\Desktop\out_and_in\bitcoin_data.csv'
bitcoin_trade = pd.read_csv(file_path)
bitcoin_trade['date'] = pd.to_datetime(bitcoin_trade['date'])
bitcoin_trade = bitcoin_trade.set_index('date')
bitcoin_trade = bitcoin_trade[[ 'close', 'volume']]
bitcoin_trade.rename(columns={'close': 'bitcoin_close', 'volume': 'bitcoin_volume'}, inplace=True)

file_path = r'C:\Users\User\Desktop\out_and_in\ethereum_2015-08-21_2024-03-25.csv'
ethereum = pd.read_csv(file_path)
ethereum['End'] = pd.to_datetime(ethereum['End'])
ethereum = ethereum.set_index('End')
ethereum = ethereum[[ 'Close', 'Volume']]
ethereum.rename(columns={'Close': 'ethereum_close', 'Volume': 'ethereum_volume'}, inplace=True)

with open(r'C:\Users\User\Desktop\out_and_in\FEDFUNDS_2008-01-01_2024-03-27.txt', 'r') as file:
    lines = file.readlines()
data = [line.strip().split('|')[1:3] for line in lines[3:-1]]
fed_rate = pd.DataFrame(data, columns=['Date', 'Interest Rate'])
fed_rate['Date'] = pd.to_datetime(fed_rate['Date'].str.strip())
fed_rate['Interest Rate'] = fed_rate['Interest Rate'].astype(float)
fed_rate = fed_rate.set_index('Date')
fed_rate.rename(columns={'Interest Rate': 'fed_rate'}, inplace=True)

with open(r'C:\Users\User\Desktop\out_and_in\SOFR_2008-01-01_2024-03-27.txt', 'r') as file:
    lines = file.readlines()
data = [line.strip().split('|')[1:3] for line in lines[3:-1]]
sofr = pd.DataFrame(data, columns=['Date', 'Interest Rate'])
sofr['Date'] = pd.to_datetime(sofr['Date'].str.strip())
sofr['Interest Rate'] = pd.to_numeric(sofr['Interest Rate'].str.strip(), errors='coerce')
for index, row in sofr[sofr['Interest Rate'].isnull()].iterrows():
    if index > 0 and index < len(sofr) - 1:
        prev_val = sofr.loc[index - 1, 'Interest Rate']
        next_val = sofr.loc[index + 1, 'Interest Rate']
        if not np.isnan(prev_val) and not np.isnan(next_val):
            sofr.at[index, 'Interest Rate'] = (prev_val + next_val) / 2
sofr = sofr.set_index('Date')
sofr.rename(columns={'Interest Rate': 'sofr_rate'}, inplace=True)

#合并数据
market = pd.concat([bitcoin_trade, ethereum, market_index, fed_rate, sofr], axis=1)

#补全数据
market['fed_rate'] = market['fed_rate'].ffill()
market['nonfarm_employment'] = market['nonfarm_employment'].ffill()
market['sofr_rate'] = market['sofr_rate'].ffill()
market['total_population'] = market['total_population'].ffill()
market['nonfarm_population_ratio'] = market['nonfarm_population_ratio'].ffill()
market['cpi'] = market['cpi'].ffill()


#del data, lines, file_path, file, prev_val, row, next_val, index


#统一列名
market.rename(columns={'bitcoin_close': 'btc_price', 'bitcoin_volume': 'btc_volume'}, inplace=True)
market.rename(columns={'ethereum_close': 'eth_price', 'ethereum_volume': 'eth_volume'}, inplace=True)
market.rename(columns={'fed_rate': 'fed_rate', 'sofr': 'sofr'}, inplace=True)
market.rename(columns={'nonfarm_employment': 'nofarm', 'CPI': 'CPI'}, inplace=True)
market.rename(columns={'nonfarm_population_ratio': 'nofarm_ratio', 'total_population': 'population'}, inplace=True)


# K M B 
market['btc_price'] = market['btc_price'].astype(str).str.replace(',', '').astype(float)


market['btc_volume'] = market['btc_volume'].apply(
    lambda x: float(x.upper().replace('K', 'e3').replace('M', 'e6').replace('B', 'e9')) if isinstance(x, str) else x
)

#market_path = r'C:\Users\User\Desktop\out_and_in\raw data\market_data.csv'
#market.to_csv(market_path, na_rep='NULL', index=True, header=True)
















