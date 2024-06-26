import requests
from datetime import datetime, timedelta

def fetch_bitcoin_volume(date=None):
    if date is None:
        date = datetime.utcnow().strftime('%Y-%m-%d')  # 使用UTC时间

    # 设定当天的开始和结束时间戳
    start_of_day = datetime.strptime(date, "%Y-%m-%d")
    end_of_day = start_of_day + timedelta(days=1) - timedelta(seconds=1)  # 当天的23:59:59

    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range'
    params = {
        'vs_currency': 'usd',
        'from': int(start_of_day.timestamp()),
        'to': int(end_of_day.timestamp())
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # 检查交易量数据并返回当天最后一条记录的交易量
    if 'total_volumes' in data and data['total_volumes']:
        return data['total_volumes'][-1][1]  # 返回最后一条交易量数据
    else:
        return None

# 使用示例
#fetch_bitcoin_volume('2024-04-07')
#fetch_bitcoin_volume()

