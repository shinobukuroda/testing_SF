import streamlit as st

conn = st.connection("snowflake")
df = conn.query("SELECT * FROM FRUIT_OPTIONS;", ttl="10m")

for row in df.itertuples():
    st.write(f"{row.FRUIT_ID} has a :{row.FRUIT_NAME}:")
