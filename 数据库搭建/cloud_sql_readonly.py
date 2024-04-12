from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from google.oauth2 import service_account
from sqlalchemy import text
import pandas as pd
import time
#pip install cloud-sql-python-connector

# 指定服务账户文件路径
SERVICE_ACCOUNT_FILE = 'C:\\Users\\User\\Desktop\\qf5214\\qf5214_wxc.json'
                                                            #各自修改成自己的密钥文件
# 创建服务账户凭据
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

connector = Connector(credentials=credentials)

def getconn() -> sqlalchemy.engine.base.Connection:
    instance_connection_string = "supple-folder-418707:us-central1:qf5214project-replica"
    db_user = "user_wxc"
    db_pass = "5214group4_cloud_wxc"
    db_name = "bitcoin_wxc"                                       # 替换为你的实际数据库名，不过没有好像也可以

    conn = connector.connect(
        instance_connection_string,
        "pymysql",  
        user=db_user,
        password=db_pass,
        db=db_name,
        ip_type=IPTypes.PUBLIC,  # 使用公共IP进行访问
    )
    return conn

# 创建SQLAlchemy engine
engine = sqlalchemy.create_engine(
    "mysql+pymysql://",  # 我们的数据库是MySQL8.0
    creator=getconn,
)

with engine.connect() as conn:
    # 执行查询以获取bitcoin数据库中的所有表格名称
    result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'bitcoin_wxc';"))
    # 打印出每个表格的名称
    for row in result:
        print(row[0])  # 使用索引0来访问table_name


# 导出数据库对应表格内容
start_time = time.time()

query = "SELECT * FROM news"
news_data = pd.read_sql(query, engine)
    
query = "SELECT * FROM market"
market_data = pd.read_sql(query, engine)

query = "SELECT * FROM talk_comments"
talk_comments = pd.read_sql(query, engine)

query = "SELECT * FROM talk_subjects"
talk_subjects = pd.read_sql(query, engine)

query = "SELECT * FROM talk_users"
talk_users = pd.read_sql(query, engine)

end_time = time.time()

print(end_time - start_time, "秒")












        