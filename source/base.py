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
school_list = list(set(df['school'].tolist()))
school = st.selectbox("Pick a school to query data from", placeholder= "Both Schools", options=["Both Schools"] + school_list)
df2 = df
if school != "Both Schools":
    df2 = df2[df2['school'] == school]
category_list = df2.columns.tolist()
category_list.remove('school')
# print(category_list)
category = st.selectbox("Pick a category.", options=category_list)
all_options = list(set(df2[category].tolist()))
choice = st.selectbox("What parameter ", options= all_options)

st.dataframe(pd.DataFrame(df2[df2[category] == choice]),hide_index=True)