import requests
from datetime import datetime

def get_sofr_data(date='', api_key='051f69ecb49f2cecf43a9ad162820cd1'):
    # 检查日期输入，如果为空则使用当前日期
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    # 构建请求URL
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": "SOFR",  # 使用SOFR作为序列ID
        "api_key": api_key,
        "file_type": "json",
        "observation_start": date,
        "observation_end": date,
    }

    # 发送GET请求
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_data = response.json()
        # 确保观测数据存在且不为空
        if 'observations' in json_data and json_data['observations']:
            # 提取并返回利率值
            value = json_data['observations'][0]['value']
            return value
        else:
            return None
    else:
        print("")
        return None
    
#example
get_sofr_data()
get_sofr_data("2023-08-17")
