#import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cereal.csv")
st.set_page_config(page_title="Cereals!", page_icon=":bowl_with_spoon:", layout='wide')



with st.container():
   st.title("A Streamlit analysis demonstration using the Cereals Dataset!")
   st.subheader("Below is the full dataset we will be using for our demonstration.")
   st.write(df)
st.write("------------------------------------------------------------------------------")

with st.container():
    st.subheader("Below is a Demonstration of a Suggestive Seach bar and a drop down menu for selecting elements from the dataset")
    st.title("Search Bar")
    search_term = st.text_input("Search for a cereal:", "")
    filtered_df = df[df["name"].str.contains(search_term, case=False)]
    st.write(filtered_df)
