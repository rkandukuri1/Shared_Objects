import pandas as pd

df_students = pd.read_csv("students.csv")   

print("Records having NULL in atleast one column")
df_students_2 = df_students[df_students.isnull().any(axis=1)] # Display records if any column has NULL
print(df_students_2)
print("==============\n")

print("Records having NO NULLs in any column")
df_students_3 = df_students.dropna() # Drop records if any column has NULL
print(df_students_3)
