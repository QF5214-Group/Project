import pandas as pd
import numpy as np


file_path = r'C:\Users\User\Desktop\out_and_in\news_after_analysis.csv'
news = pd.read_csv(file_path, encoding='gbk')



news['seendate'] = pd.to_datetime(news['seendate'], errors='coerce')

news = news.dropna(subset=['seendate'])
# news = news.set_index('seendate')
news = news[['seendate','title','url','domain','language','sourcecountry','polarity','subjectivity']]

news['news_important'] = 0

news.rename(columns={'seendate': 'date', 'title': 'news_title'}, inplace=True)
news.rename(columns={'url': 'news_url', 'domain': 'news_domain'}, inplace=True)
news.rename(columns={'language': 'news_language', 'sourcecountry': 'news_country'}, inplace=True)
news.rename(columns={'polarity': 'news_title_emotion', 'subjectivity': 'news_title_subjectivity'}, inplace=True)
news = news.reset_index(drop=True)

#news_path = r'C:\Users\User\Desktop\out_and_in\raw data\news_data.csv'
#news.to_csv(news_path, na_rep='NULL', header=True, index=True)





#news_path = r'C:\Users\User\Desktop\out_and_in\news_data.csv'
#news.to_csv(news_path, na_rep='NULL', header=False, index=True)
















