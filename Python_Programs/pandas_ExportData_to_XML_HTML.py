import pandas as pd

data = {
    'ID': [101, 102, 103],
    'Name': ['John', 'Steve', 'Mike'],
    'Marks': [85, 89, 75]
}
df = pd.DataFrame(data)

df.to_xml("test_students.xml", index=False)   # xml file
df.to_html("test_students.html", index=False)   # html file
