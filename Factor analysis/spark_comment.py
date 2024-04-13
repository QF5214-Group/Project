from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, lower, regexp_replace
from pyspark.sql.types import StringType
import re

import time

start_time = time.time()

spark = SparkSession.builder.appName("Data Cleaning and Sentiment Analysis").getOrCreate()

#替换缩写
def replace_lingo(text):
    replacements = {
        # Fix classic post lingo
        r'\bthats\b': 'that is',
        r'\bive\b': 'i have',
        r'\bim\b': 'i am',
        r'\bya\b': 'yeah',
        r'\bcant\b': 'can not',
        r'\bwont\b': 'will not',
        r'\bid\b': 'i would',
        r'wtf': 'what the fuck',
        r'\bwth\b': 'what the hell',
        r'\br\b': 'are',
        r'\bu\b': 'you',
        r'\bk\b': 'ok',
        r'\bsux\b': 'sucks',
        r'\bno+\b': 'no',
        r'\bcoo+\b': 'cool',
        
        # Cryptocurrency lingo
        r'\bath\b': 'all time high',
        r'\batl\b': 'all time low',
        r'\bbtfd\b': 'buy the fucking dip',
        r'\bico\b': 'initial coin offering',
        r'\bfomo\b': 'fear of missing out',
        r'\bfud\b': 'fear uncertainty doubt',
        r'\bfucking\b': 'fuck',
        r'\bfudster\b': 'fear uncertainty doubt spreader',
        r'\broi\b': 'return on investment',
        r'\bmacd\b': 'moving average convergence divergence',
        r'\bpoa\b': 'proof of authority',
        r'\bpow\b': 'proof of work'
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    return text

# 去除URLs
def remove_urls(text):
    return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|stratum[+]tcp?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)

# 去除非ASCII字符
def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

# 注册为UDF
replace_lingo_udf = udf(replace_lingo, StringType())
remove_urls_udf = udf(remove_urls, StringType())
strip_non_ascii_udf = udf(strip_non_ascii, StringType())

# 读取CSV文件到DataFrame
df = spark.read.csv("C:/Users/666/Desktop/btccomment.csv", header=True, inferSchema=True)

# 应用数据清洗UDF
df_clean = df.withColumn("clean_comment", lower(col("comment"))) \
             .withColumn("clean_comment", remove_urls_udf(col("clean_comment"))) \
             .withColumn("clean_comment", replace_lingo_udf(col("clean_comment")))\
             .withColumn("clean_comment", strip_non_ascii_udf(col("clean_comment")))

from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# 定义情感分析的UDF
def sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(text)
    return result['compound']

sentiment_analysis_udf = udf(sentiment_analysis, StringType())

# 应用情感分析UDF
df_sentiment = df_clean.withColumn("sentiment", sentiment_analysis_udf(col("clean_comment")))

# 展示结果
df_sentiment.select("comment", "clean_comment", "sentiment").show()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码运行时间：{elapsed_time} 秒")