import streamlit as st
import pandas as pd
from duckdb_connection import DuckDBConnection


conn = st.experimental_connection("duckdb", type=DuckDBConnection, database=':memory:')


st.write("A DEMO APP USING ""st.experimental_connection!")


c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS Students(Name VARCHAR, Age INTEGER, Marks INTEGER)")


c.execute("DELETE FROM Students")


c.execute("INSERT INTO Students VALUES ('Daniel', 20, 85), ('Luis', 22, 45),('Jessy', 22, 56),('Marry', 21, 81)")

c.execute("INSERT INTO Students VALUES (?, ?, ?)", ['Danny', 22, 69])

c.commit()
df = conn.query("SELECT * FROM Students")


st.dataframe(df)
