import pandas as pd

df_emp = pd.read_csv("emp.txt", delimiter = "|")
df_dept = pd.read_csv("dept.txt")

df_joined = pd.merge(df_emp, df_dept, on="DNUM", how="inner")
print(df_joined)
