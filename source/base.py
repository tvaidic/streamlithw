import requests
import pandas as pd
import pymongo
import streamlit as st
def pipeline(file):
    df = pd.read_csv(file, sep=';',quotechar='"')
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    client = pymongo.MongoClient('mongodb+srv://tvaidic:mahadev13@cluster0.53ntqbw.mongodb.net/?retryWrites=true&w=majority')
    db = client.schools
    collections = db.class1
    records = df.to_dict(orient='records')
    collections.insert_many(records)
    return df

df = pipeline(r'C:\Users\User\Documents\Bonfire\Homework\mogohw\student\student-por.csv')
df
s_list = list(set(df['school'].tolist()))
grades = list((df["g1"] + df["g2"]+ df["g3"]))
x = st.selectbox(label =" schools",options=s_list)
y = st.selectbox(label = "grades", options=grades)
st.bar_chart