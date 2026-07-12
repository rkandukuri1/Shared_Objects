import pandas as pd

df_emp = pd.read_csv("emp.txt")

df_dept_sal = df_emp.groupby(["DNUM"]).agg(
   TOTAL_SAL = ("SALARY", "sum"),
   EMP_COUNT = ("ENUM", "count"),
   MIN_SAL = ("SALARY", "min"),
   MAX_SAL = ("SALARY", "max"),
   AVG_SAL = ("SALARY", "mean"),
)
print(df_dept_sal)

