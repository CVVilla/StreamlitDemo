#import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cereal.csv")
st.set_page_config(page_title="Cereals!", page_icon=":bowl_with_spoon:", layout='wide')




st.title("A Streamlit analysis demonstration using the Cereals Dataset!")
