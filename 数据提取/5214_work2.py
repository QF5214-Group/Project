import requests
from datetime import datetime

api_key = 'f241bf8a6d6c42038e9a467f245dd3db'

base_url = 'https://newsapi.org/v2/everything'

keyword = 'bitcoin'


#今天有多少比特币新闻

keyword = 'bitcoin'

# 获取今天的日期
today = datetime.now().strftime('%Y-%m-%d')

# 构建 API 请求的参数
params = {
    'q': keyword,
    'apiKey': api_key,
    'from': "2024-03-24",
    'to': today,
    'sortBy': 'popularity',  # 按热度排序
}

# 发送 API 请求
response = requests.get(base_url, params=params)
data = response.json()

# 提取返回的新闻数据数量
if data['status'] == 'ok':
    total_results = data['totalResults']
    print(f"本月关于比特币的热门新闻数量为: {total_results} 条")
else:
    print("无法获取今天关于比特币的热门新闻数量")




'''
keyword = 'bitcoin'
today = datetime.now().strftime('%Y-%m-%d')

params = {
    'q': keyword,
    'apiKey': api_key,
    'from': today,
    'to': today,
    'sortBy': 'popularity',  # 按热度排序
    'pageSize': 10            # 只获取前10条新闻
}

response = requests.get(base_url, params=params)
data = response.json()


print(f"Today's Bitcoin news rankings:")
for i, article in enumerate(data['articles'], 1):
    print(f"{i}. {article['title']}")

'''

#test 验证API能否正常运行
'''
base_url = 'https://newsapi.org/v2/top-headlines'

# 构建 API 请求的参数
params = {
    'apiKey': api_key,
    'country': 'us',  # 限制搜索结果为美国的头条新闻
    'pageSize': 5     # 限制每次请求返回的文章数量为5
}

# 发送 API 请求
response = requests.get(base_url, params=params)
data = response.json()

# 输出返回的结果
print(data)
'''


#返回当天的一个bitcoin热搜
'''
keyword = 'bitcoin'

# 构建 API 请求的参数
params = {
    'q': keyword,
    'apiKey': api_key,
    'sortBy': 'popularity',  # 按热度排序
    'pageSize': 1            # 只获取一条新闻
}

# 发送 API 请求
response = requests.get(base_url, params=params)
data = response.json()

# 提取返回的新闻数据
if data['status'] == 'ok' and data['totalResults'] > 0:
    article = data['articles'][0]
    title = article['title']
    description = article['description']
    url = article['url']
    print(f"标题: {title}")
    print(f"描述: {description}")
    print(f"链接: {url}")
else:
    print("未找到关于比特币的热门新闻")
'''







