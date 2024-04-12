#pip install gdeltdoc

from gdeltdoc import GdeltDoc, Filters, repeat
import pandas as pd
from datetime import datetime, timedelta


result_df = pd.DataFrame()


start_date = datetime.today().date() - timedelta(days=1)
end_date = datetime.today().date() - timedelta(days=1)
error = list()

current_date = start_date
while current_date <= end_date:

    next_date = current_date + timedelta(days=1)
    
    current_date_str = current_date.strftime('%Y-%m-%d')
    next_date_str = next_date.strftime('%Y-%m-%d')
    
    f = Filters(
        keyword = "bitcoin",
        start_date = current_date_str,
        end_date =  next_date_str,
        num_records = 250,
        
        
        #domain = ["bbc.co.uk", "nytimes.com", "yahoo.com", "newsbtc.com", "coindesk.com",
        #          "twitter.com", "medium.com", "bitcoinmagazine.com", "reddit.com"],
        
        
        country = ["US", "UK", "CN", "JA", "GM"],
        repeat = repeat(5, "bitcoin")
    )

    gd = GdeltDoc()
    try:
        articles = gd.article_search(f)
    except Exception as e:
        print('导出异常，跳过！！')
        error.append(current_date)
        current_date = next_date
        continue
    #timeline = gd.timeline_search("timelinevol", f)
    
    result_df = pd.concat([result_df, articles], ignore_index=True)
    
    print(current_date_str,"新闻条数：",articles.shape[0])

    # 将日期向前推进一天
    current_date = next_date
    
result_df = result_df.drop_duplicates()
#bitcoin_20170101_20170630_big = r'C:\Users\User\Desktop\2024_2.xlsx'
#result_df.to_excel(bitcoin_20170101_20170630_big, sheet_name="Sheet1", index=False)





