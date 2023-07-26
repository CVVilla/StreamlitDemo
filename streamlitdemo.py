# -*- coding: utf-8 -*-
"""StreamlitDemo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tuHQUtc01mVuxnRNLhgdfJfw9ec0M3C1
"""

#download streamlit dependencies
#pip install streamlit
#IMPORT Streamlit
import streamlit as st
import pandas as pd


#import our csv file
cereals = pd.read_csv("cereal.csv")

#Create a page title for the page
#Emojis can be used as icons from https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Cereals!", page_icon=":bowl_with_spoon:", layout='wide')
st.subheader("This is a Streamlit demonstration!")
st.title("A Streamlit analysis demonstration using the Cereals Dataset!")

#A selection option for choosing desired cereal brand
cereals_name = st.selectbox("Choose a Cereal Brand", cereals['name'].unique())
name = cereals[cereals['name'] == cereals_name]

st.header("Selected: {name}")
st.write(name)

