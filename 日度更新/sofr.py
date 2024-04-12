import requests
from datetime import datetime
import pandas as pd

def get_fedfunds_data(date, api_key='051f69ecb49f2cecf43a9ad162820cd1'):
    # 构建请求URL
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": "FEDFUNDS",
        "api_key": api_key,
        "file_type": "json",
        "observation_start": date,
        "observation_end": date,
    }

    # 发送GET请求
    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_data = response.json()
        if 'observations' in json_data:
            # 获取数据
            value = json_data['observations'][0]['value']
            return value
        else:
            return None
    else:
        print(f"Failed to retrieve interest rate data for {date}, status code: {response.status_code}")
        return None

# 读取输入日期
input_date = input("请输入日期（YYYY-MM-DD）: ")

# 获取对应日期的FEDFUNDS数据
interest_rate = get_fedfunds_data(input_date)

if interest_rate is not None:
    print(f"On {input_date}, FEDFUNDS interest rate is: {interest_rate}")
else:
    print("No data found for the specified date.")
