import streamlit as st
from sqlalchemy import create_engine, text

with st.form("employee_form"):

    name = st.text_input("Name")
    age = st.number_input("Age")
    department = st.selectbox("Department", ["IT", "HR", "Finance"])
    submit = st.form_submit_button("Submit")

    if submit:
       engine = create_engine("mysql+pymysql://root:welcome@localhost:3306/sales")
       query = text("INSERT INTO emp2 (name, age, department) VALUES (:name, :age, :department)")
       with engine.connect() as conn:
            conn.execute(
                query,
                {
                    "name": name,
                    "age": age,
                    "department": department
                }
            )
            conn.commit()
       st.success(f"Employee {name} Registered")
