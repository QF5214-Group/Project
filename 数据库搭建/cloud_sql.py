from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from google.oauth2 import service_account
from sqlalchemy import text
import pandas as pd
#pip install cloud-sql-python-connector

# 指定服务账户文件路径
SERVICE_ACCOUNT_FILE = 'C:\\Users\\User\\Desktop\\qf5214\\qf5214_wxc.json'
                                                            #各自修改成自己的密钥文件
# 创建服务账户凭据
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

# 初始化Connector对象
connector = Connector(credentials=credentials)

def getconn() -> sqlalchemy.engine.base.Connection:
    # 连接信息
    instance_connection_string = "supple-folder-418707:us-central1:qf5214project"
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
    # 执行查询以获取所有数据库的列表（MySQL版本）
    result = conn.execute(text("SHOW DATABASES;"))
    # 遍历结果并打印每个数据库名称
    for row in result:
        print(row[0])



with engine.connect() as conn:
    result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'bitcoin_wxc';"))
    # 打印出每个表格的名称
    for row in result:
        print(row[0])  # 使用索引0来访问table_name

'''
with engine.connect() as conn:
    # 使用conn执行删除表的SQL语句
    conn.execute(text("DROP TABLE IF EXISTS news;"))
    print("Table 'news' has been deleted successfully.")

'''

query = "SELECT * FROM news_2024"

# 使用pandas读取数据
df = pd.read_sql(query, engine)

    


with engine.connect() as conn:

    result = conn.execute(text("""
    CREATE TABLE IF NOT EXISTS news (
        url VARCHAR(2048),
        url_mobile VARCHAR(2048),
        title VARCHAR(512),
        senddate VARCHAR(512),
        socialimg VARCHAR(2048),
        domain VARCHAR(255),
        language VARCHAR(50),
        sourcecountry VARCHAR(255)
    );
    """))

        
        






        
        