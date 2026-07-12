import pandas as pd

df_students = pd.read_csv("students.csv")   
total_rec_count = len(df_students)

df_students_temp = df_students
null_rec_count = len(df_students) - len(df_students_temp.dropna())

print(f"\nTotal Records: {total_rec_count}, NULL data records: {null_rec_count}")

NULL_rec_Percenge = int((null_rec_count / total_rec_count) * 100)
print(f"\n\t Null Record Percentage: {NULL_rec_Percenge}%\n")
