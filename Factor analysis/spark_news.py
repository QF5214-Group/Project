import pyspark
pyspark.SparkContext.setSystemProperty('spark.ui.showConsoleProgress', 'true')
pyspark.SparkContext.setSystemProperty('spark.sql.session.timeZone', 'UTC')
import time
#pip install pyspark textblob

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import FloatType
from textblob import TextBlob

start_time = time.time()

# 初始化SparkSession
spark = SparkSession.builder \
    .appName("TextBlob Sentiment Analysis") \
    .getOrCreate()

def sentiment_polarity(text):
    if text is None:
        return 0.0
    return TextBlob(text).sentiment.polarity

def sentiment_subjectivity(text):
    if text is None:
        return 0.5
    return TextBlob(text).sentiment.subjectivity

# 注册UDF
sentiment_polarity_udf = udf(sentiment_polarity, FloatType())
sentiment_subjectivity_udf = udf(sentiment_subjectivity, FloatType())

df = spark.read.csv('C:/Users/666/Desktop/news_rawdata.csv', header=True, inferSchema=True)

# 应用UDF进行情感分析
df = df.withColumn("polarity", sentiment_polarity_udf(col("title")))
df = df.withColumn("subjectivity", sentiment_subjectivity_udf(col("title")))

# 展示结果
df.show()
df.select('polarity','subjectivity').show()

# 使用 Pandas 的 to_csv 方法将数据保存到 CSV
pandas_df = df.toPandas()
pandas_df.to_csv('C:/Users/666/Desktop/news_after_analysis.csv', index=False)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码运行时间：{elapsed_time} 秒")
