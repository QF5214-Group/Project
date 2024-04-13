import pandas as pd
import numpy as np


file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_1_after_analysis.csv'
talk1 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})


'''
import chardet

# 检测文件编码
with open(file_path, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

print(result)

'''

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_2_after_analysis.csv'
talk2 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_3_after_analysis.csv'
talk3 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_4_after_analysis.csv'
talk4 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_5_after_analysis.csv'
talk5 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_6_after_analysis.csv'
talk6 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_7_after_analysis.csv'
talk7 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_8_after_analysis.csv'
talk8 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_9_after_analysis.csv'
talk9 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_10_after_analysis.csv'
talk10 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_11_after_analysis.csv'
talk11 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_12_after_analysis.csv'
talk12 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})

file_path = r'C:\Users\User\Desktop\out_and_in\bitcointalk_after_analysis\bitcointalk_after_analysis\split_13_after_analysis.csv'
talk13 = pd.read_csv(file_path, encoding='ISO-8859-1',dtype={0:'str',1:'str',2:'str',3:'str',4:'str',5:'str',6:'str',7:'str',8:'str',9:'str',10:'str',11:'str',12:'str'})


talks = [talk1, talk2, talk3, talk4, talk5, talk6, talk7, talk8, talk9, talk10, talk11, talk12, talk13]

big_talk = pd.concat(talks, ignore_index=True)

del [talk2, talk3, talk4, talk5, talk6, talk7, talk8, talk9, talk10, talk11, talk12, talk13]

big_talk['subject'].replace('.', np.nan, inplace=True)
big_talk.dropna(subset=['subject'], inplace=True)




big_talk['_c0'] = pd.to_numeric(big_talk['_c0'], errors='coerce')
big_talk.dropna(subset=['_c0'], inplace=True)
big_talk['replies'] = pd.to_numeric(big_talk['replies'], errors='coerce')
big_talk.dropna(subset=['replies'], inplace=True)
big_talk['views'] = pd.to_numeric(big_talk['views'], errors='coerce')
big_talk.dropna(subset=['views'], inplace=True)
big_talk['activity'] = pd.to_numeric(big_talk['activity'], errors='coerce')
big_talk.dropna(subset=['activity'], inplace=True)
big_talk['merit'] = pd.to_numeric(big_talk['merit'], errors='coerce')
big_talk.dropna(subset=['merit'], inplace=True)
big_talk['subject_sentiment'] = pd.to_numeric(big_talk['subject_sentiment'], errors='coerce')
big_talk.dropna(subset=['subject_sentiment'], inplace=True)
big_talk['subject_subjectivity'] = pd.to_numeric(big_talk['subject_subjectivity'], errors='coerce')
big_talk.dropna(subset=['subject_subjectivity'], inplace=True)
big_talk['comment_sentiment'] = pd.to_numeric(big_talk['comment_sentiment'], errors='coerce')
big_talk.dropna(subset=['comment_sentiment'], inplace=True)


big_talk['date'] = pd.to_datetime(big_talk['date'], format='%d-%b-%y', errors='coerce')
big_talk.dropna(subset=['date'], inplace=True)


big_talk = big_talk[[ '_c0' ,'date' ,'subject' ,'user' ,'clean_comment' ,'comment_sentiment']]
big_talk.rename(columns={'_c0': 'talk_comment_id', 'date': 'date'}, inplace=True)
big_talk.rename(columns={'subject': 'talk_subject', 'user': 'talk_user'}, inplace=True)
big_talk.rename(columns={'clean_comment': 'talk_comment', 'comment_sentiment': 'talk_comment_sentiment'}, inplace=True)


#big_talk_path = r'C:\Users\User\Desktop\out_and_in\big_talk_data.csv'
#big_talk.to_csv(big_talk_path, na_rep='NULL', index=False)
#big_talk.to_csv(big_talk_path, na_rep='NULL', index=False, header=True)




















