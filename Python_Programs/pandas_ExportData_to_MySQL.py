import pandas as pd
from sqlalchemy import create_engine

data = {
    'ID': [101, 102, 103],
    'Name': ['John', 'Steve', 'Mike'],
    'Marks': [85, 89, 75]
}
df = pd.DataFrame(data)

db_conn = create_engine("mysql+mysqlconnector://root:welcome@localhost/sales")
df.to_sql(name = "test_students", con = db_conn, if_exists = "replace", index = False)
db_conn.dispose()
