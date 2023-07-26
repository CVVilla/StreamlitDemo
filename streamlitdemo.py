#IMPORT Streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



#import our csv file
df = pd.read_csv("cereal.csv")

#Create a page title for the page
#Emojis can be used as icons from https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Cereals!", page_icon=":bowl_with_spoon:", layout='wide')

with st.container():
    st.title("A Streamlit analysis demonstration using the Cereals Dataset!")
    st.subheader("Below is the full dataset we will be using for our demonstration.")
    st.write(df)



#A selection option for choosing desired cereal brand
#after selecting a cereal brand, information regarding brand is displayed onto the user
with st.container():
    st.subheader("Select a cereal brand below from the dataset")
    cereals_name = st.selectbox("Choose a Cereal Brand", df['name'].unique())
    cereal_info = df[df['name'] == cereals_name]
    st.header(f"Selected: {cereals_name}")
    st.write(cereal_info)
    
fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df["name"], df["calories"])
    ax.set_xlabel("Cereal")
    ax.set_ylabel("Calories")
    ax.set_title("Calories Comparison of Cereals")
    plt.xticks(rotation=90)
    st.pyplot(fig)


