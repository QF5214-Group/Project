from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from google.oauth2 import service_account
from sqlalchemy import text
import pandas as pd
import time
#pip install cloud-sql-python-connector   # Firstly, installing this package to connect cloud sql!!!

# Specify the service account file path
SERVICE_ACCOUNT_FILE = r'C:\Users\User\Desktop\read_me\qf5214_professor.json'
                                                          
# Create service account credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

connector = Connector(credentials=credentials)

def getconn() -> sqlalchemy.engine.base.Connection:
    instance_connection_string = "supple-folder-418707:us-central1:qf5214project-replica"
    #instance_connection_string = "supple-folder-418707:us-central1:qf5214project"
    db_user = "user_professor"
    db_pass = "qf5214_group4"
    db_name = "Bitcoin_data"                                       # Replace with your actual database name, but none seems to work

    conn = connector.connect(
        instance_connection_string,
        "pymysql",  
        user=db_user,
        password=db_pass,
        db=db_name,
        ip_type=IPTypes.PUBLIC,  # Use public IP for access
    )
    return conn

# Create the SQLAlchemy engine
engine = sqlalchemy.create_engine(
    "mysql+pymysql://",  # Our database is MySQL8.0
    creator=getconn,
)

with engine.connect() as conn:
    # Perform a query to get all table names in the bitcoin database
    result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'Bitcoin_data';"))
    # Print out the name of each form
    for row in result:
        print(row[0])  


# Export the table contents of the database
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

print("Time cost: ", end_time - start_time, "seconds")

del  end_time,  start_time, query, row, SERVICE_ACCOUNT_FILE










        