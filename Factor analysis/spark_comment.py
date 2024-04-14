from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, lower, regexp_replace
from pyspark.sql.types import StringType, FloatType
from textblob import TextBlob
from pyspark.sql.functions import to_timestamp
import time
import re


start_time = time.time()

spark = SparkSession.builder.appName("Data Cleaning and Sentiment Analysis").getOrCreate()

csvName = 'split_13'
inputCsvName = 'C:/Users/666/Desktop/' + csvName + '.csv'


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
    if text is None:
        return ""
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
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

schema = StructType([
    StructField("_c0", StringType(), True),  
    StructField("subject", StringType(), True),
    StructField("replies", IntegerType(), True),
    StructField("views", IntegerType(), True),
    StructField("comment", StringType(), True),
    StructField("date", StringType(), True), 
    StructField("user", StringType(), True),
    StructField("activity", StringType(), True),
    StructField("merit", IntegerType(), True)
])


df = spark.read.csv(inputCsvName, header=True, schema=schema)

# 应用数据清洗UDF
df_clean = df.withColumn("clean_comment", lower(col("comment"))) \
             .withColumn("clean_comment", remove_urls_udf(col("clean_comment"))) \
             .withColumn("clean_comment", replace_lingo_udf(col("clean_comment")))\
             .withColumn("clean_comment", strip_non_ascii_udf(col("clean_comment")))

from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# 定义评论情感分析的UDF
def sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(text)
    return result['compound']

#定义主题情感分析的UDF
def sentiment_polarity(text):
    if text is None:
        return 0.0
    return TextBlob(text).sentiment.polarity

#定义主题主观性分析的UDF
def sentiment_subjectivity(text):
    if text is None:
        return 0.5
    return TextBlob(text).sentiment.subjectivity

sentiment_analysis_udf = udf(sentiment_analysis, FloatType())
sentiment_polarity_udf = udf(sentiment_polarity, FloatType())
sentiment_subjectivity_udf = udf(sentiment_subjectivity, FloatType())

# 应用情感分析UDF
df = df_clean.withColumn("subject_sentiment", sentiment_polarity_udf(col("subject"))) \
             .withColumn("subject_subjectivity", sentiment_subjectivity_udf(col("subject"))) \
             .withColumn("comment_sentiment", sentiment_analysis_udf(col("clean_comment")))

# 展示和保存结果
df.show(5)



pandas_df = df.toPandas()
pandas_df.to_csv('C:/Users/666/Desktop/bitcointalk_after_analysis/' + csvName + '.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码运行时间：{elapsed_time} 秒")