import pandas as pd

df = pd.read_csv("students.csv")
dup_data = df[df.duplicated()]

print(dup_data)
