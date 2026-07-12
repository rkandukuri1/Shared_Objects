import pandas as pd

df_students = pd.read_csv("students.csv")

class_specific_data = df_students[
    (df_students["Class"] == "Fourth")  & 
    (df_students["Marks"] > 70)
]

print(class_specific_data)
