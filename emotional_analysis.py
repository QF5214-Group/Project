# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:56:40 2024

@author: 666
"""
# %%
import csv
import pandas as pd
import re
import spacy
import textblob
from textblob import TextBlob
from operator import attrgetter
from spacy.tokens import Doc
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
pd.options.display.max_colwidth = 500

import time

start_time = time.time()


# %%
#csvName = '1WO_20190922-232209'   # Change this string value to the file
#csvName = '1AP_20190926-153722'
#csvName = 'BBOS_20190925-083726'
csvName = 'btccomment'
inputCsvName = 'C:/Users/666/Desktop/' + csvName + '.csv'  # Change the relative or absolute path here


# %%
Analyzer = SentimentIntensityAnalyzer()
# Custom Cryptocurrency word sentiment values
new_words = {
    'hold': 0.5,
    'lambo': 1.5,
    'moon': 1.5,
    'mooning': 1.6,
    'bull': 1,
    'bear': -0.5,
    'shill': -1,
    'shilling': -1.5,
    'pump': -0.75,
    'decentralized': 0.5,
    'noob': -0.5,
    'whale': 0.5,
    '51%': -1,
    'denial': -1.4,
    'fundamental': 0.1,
    'analysis': 0.3,
    'oracle': 0.25,
    'shitcoin': -3,
    'volatile': -0.75,
}
# Update the VADER lexicon with these additional sentiment values
Analyzer.lexicon.update(new_words)

# Rate the post content and categorize it based on compound score
def vader_polarity(text):
    """ Transform the output to a binary 0/1 result """
    score = Analyzer.polarity_scores(text)
    total_positive_score = score['pos']
    total_negative_score = score['neg']
    total_neutral_score = score['neu']
    
    if (total_neutral_score > 1 and total_positive_score > total_negative_score and total_positive_score >= total_neutral_score):
        sentiment = 'Positive'
    elif (total_neutral_score > 1 and total_negative_score > total_positive_score and total_negative_score >= total_neutral_score):
        sentiment = 'Negative'
    elif (total_neutral_score > 1 and total_neutral_score > total_positive_score and total_neutral_score > total_negative_score):
        sentiment = 'Neutral'
    elif (total_neutral_score > 1 and total_negative_score == total_positive_score and total_negative_score >= total_neutral_score):
        sentiment = 'Neutral'
    elif (total_neutral_score <= 1 and total_positive_score == total_negative_score and total_positive_score == total_neutral_score):
        sentiment = "Neutral"
    elif (total_neutral_score <= 1 and total_positive_score > total_negative_score):
        sentiment = "Positive"
    elif (total_neutral_score <= 1 and total_negative_score > total_positive_score):
        sentiment = "Negative"
    else:
        if score['compound'] >= 0.5:
            sentiment = 'Positive'
        elif score['compound'] > -0.5 and score['compound'] < 0.5:
            sentiment = 'Neutral'
        elif score['compound'] <= -0.5:
            sentiment = 'Negative'
    return sentiment

# A helper function that removes all the non ASCII characters
# from the given string. Retuns a string with only ASCII characters.
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

# %%
posts = []

# 提高CSV字段大小限制
maxInt = 1000000
csv.field_size_limit(maxInt)

row_count=0
with open(inputCsvName, 'r', encoding='utf-8', errors='ignore') as csvfile:
    reader = csv.reader((x.replace('\0', '') for x in csvfile), delimiter=',')
    for row in reader:
        # 仅处理前5行，这里是测试时取前100行
        if row_count < 100:
            post = dict()
            post['comment'] = row[4] 
            row_count += 1  # 更新行计数器

            post['clean'] = post['comment']

            # Remove all non-ascii characters
            post['clean'] = strip_non_ascii(post['clean'])

            # Normalize case
            post['clean'] = post['clean'].lower()

            # Remove URLS.
            post['clean'] = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', post['clean'])
            post['clean'] = re.sub(r'stratum[+]tcp?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', post['clean'])

            # Fix classic post lingo
            post['clean'] = re.sub(r'\bthats\b', 'that is', post['clean'])
            post['clean'] = re.sub(r'\bive\b', 'i have', post['clean'])
            post['clean'] = re.sub(r'\bim\b', 'i am', post['clean'])
            post['clean'] = re.sub(r'\bya\b', 'yeah', post['clean'])
            post['clean'] = re.sub(r'\bcant\b', 'can not', post['clean'])
            post['clean'] = re.sub(r'\bwont\b', 'will not', post['clean'])
            post['clean'] = re.sub(r'\bid\b', 'i would', post['clean'])
            post['clean'] = re.sub(r'wtf', 'what the fuck', post['clean'])
            post['clean'] = re.sub(r'\bwth\b', 'what the hell', post['clean'])
            post['clean'] = re.sub(r'\br\b', 'are', post['clean'])
            post['clean'] = re.sub(r'\bu\b', 'you', post['clean'])
            post['clean'] = re.sub(r'\bk\b', 'ok', post['clean'])
            post['clean'] = re.sub(r'\bsux\b', 'sucks', post['clean'])
            post['clean'] = re.sub(r'\bno+\b', 'no', post['clean'])
            post['clean'] = re.sub(r'\bcoo+\b', 'cool', post['clean'])
            
            # Fix Cryptocurrency lingo
            post['clean'] = re.sub(r'\bath\b', 'all time high', post['clean'])
            post['clean'] = re.sub(r'\batl\b', 'all time low', post['clean'])
            post['clean'] = re.sub(r'\bbtfd\b', 'buy the fucking dip', post['clean'])
            post['clean'] = re.sub(r'\bico\b', 'initial coin offering', post['clean'])
            post['clean'] = re.sub(r'\bfomo\b', 'fear of missing out', post['clean'])
            post['clean'] = re.sub(r'\bfud\b', 'fear uncertainty doubt', post['clean'])
            post['clean'] = re.sub(r'\bfucking\b', 'fuck', post['clean'])
            post['clean'] = re.sub(r'\bfudster\b', 'fear uncertainty doubt spreader', post['clean'])
            post['clean'] = re.sub(r'\broi\b', 'return on investment', post['clean'])
            post['clean'] = re.sub(r'\bmacd\b', 'moving average convergence divergence', post['clean'])
            post['clean'] = re.sub(r'\bpoa\b', 'proof of authority', post['clean'])
            post['clean'] = re.sub(r'\bpow\b', 'proof of work', post['clean'])
            post['clean'] = re.sub(r'\bpos\b', 'proof of stake', post['clean'])
            post['clean'] = re.sub(r'\bdapp\b', 'decentralized application', post['clean'])
            post['clean'] = re.sub(r'\bdao\b', 'decentralized autonomous organization', post['clean'])
            post['clean'] = re.sub(r'\bhodl\b', 'hold', post['clean'])
            post['clean'] = re.sub(r'\bddos\b', 'distributed denial of service', post['clean'])
            post['clean'] = re.sub(r'\bkyc\b', 'know your customer', post['clean'])
            post['clean'] = re.sub(r'\brekt\b', 'wrecked', post['clean'])
            post['clean'] = re.sub(r'\bbullish\b', 'bull', post['clean'])
            post['clean'] = re.sub(r'\bbearish\b', 'bear', post['clean'])
            post['clean'] = re.sub(r'\bpumping\b', 'pump', post['clean'])
            post['clean'] = re.sub(r'\basic\b', 'application specific integrated circuit', post['clean'])
            post['clean'] = re.sub(r'\bdyor\b', 'do your own research', post['clean'])
            post['clean'] = re.sub(r'\berc\b', 'ethereum request for comments', post['clean'])
            post['clean'] = re.sub(r'\bfa\b', 'fundamental analysis', post['clean'])
            post['clean'] = re.sub(r'\bjomo\b', 'joy of missing out', post['clean'])
            post['clean'] = re.sub(r'\bmcap\b', 'market capitalization', post['clean'])
            post['clean'] = re.sub(r'\bmsb\b', 'money services business', post['clean'])
            post['clean'] = re.sub(r'\boco\b', 'one cancels the other order', post['clean'])
            post['clean'] = re.sub(r'\bpnd\b', 'pump and dump', post['clean'])
            post['clean'] = re.sub(r'\brsi\b', 'relative strength index', post['clean'])
            post['clean'] = re.sub(r'\butxo\b', 'unspent transaction output', post['clean'])
            post['clean'] = re.sub(r'\bvolatility\b', 'volatile', post['clean'])
            post['clean'] = re.sub(r'\blamborghini\b', 'lambo', post['clean'])
            
            post['TextBlob'] = TextBlob(post['clean'])

            posts.append(post)
        else:
            break  # 如果已读取5行，则中断循环
            
# %%
#data = pd.read_csv(inputCsvName)
#data['date'] = pd.to_datetime(data.date)#读取日期并进行标准化处理
# %%
# DEVELOP MODELS
###!python -m spacy download en_core_web_sm

def polarity_scores(doc):
    return Analyzer.polarity_scores(doc.text)

Doc.set_extension('polarity_scores', getter=polarity_scores, force=True)
nlp = spacy.load('en_core_web_sm')

negResults = ''
posResults = ''
neuResults = ''
results = ''
for post in posts:
    doc = nlp(post['clean'])
    tokens = [token.text for token in doc if not token.is_stop]
    score = doc._.polarity_scores
    post['compound'] = score['compound']
    post['sentiment'] = vader_polarity(post['clean'])

posts_sorted = sorted(posts, key=lambda k: k['compound'])


negative_posts = [d for d in posts_sorted if d['sentiment'] == 'Negative']
for post in negative_posts:
    negResults += (post['clean'])

# Posts that have a compound Positive value
positive_posts = [d for d in posts_sorted if d['sentiment'] == 'Positive']
for post in positive_posts:
    posResults += (post['clean'])

# Posts that have a compound Neutral value.
neutral_posts = [d for d in posts_sorted if d['sentiment'] == 'Neutral']
for post in neutral_posts:
    neuResults += (post['clean'])

pos = len(positive_posts)
neu = len(neutral_posts)
neg = len(negative_posts)

ratio = (neg / (pos + neg + neu)) * 100

print('Negative Sentiment in content: ~', round(ratio,4), '%')

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码运行时间：{elapsed_time} 秒")