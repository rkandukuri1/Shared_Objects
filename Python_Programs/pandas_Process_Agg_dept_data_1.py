import pandas as pd

df_emp = pd.read_csv("emp.txt")

df_dept_sal = df_emp.groupby(["DNUM"]).agg(
   TOTAL_SAL = ("SALARY", "sum")
)
print(df_dept_sal)
