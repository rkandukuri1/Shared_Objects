import pandas as pd

df_students = pd.read_csv("students.csv")

df_students_2 = df_students.sort_values(
    by = "Marks",
    ascending = False
)
print(df_students_2)
