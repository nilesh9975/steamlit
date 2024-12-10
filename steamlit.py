import streamlit as st
import pandas as pd
st.title ("StreamLit Text Input")

name=st.text_input ("Enter your name:")

age=st.slider("Select your age:",0,100,25)
st.write(f"your age is {age}")


options=["Python","Java","Devops","Javascript"]
choice=st.selectbox("choose your favorite language:",options)

if name:
    st.write(f"Hello, {name} these are options selected my you. Have a Nice day ")
    
    
uploaded_file=st.file_uploader("choose a CSV file",type="csv")    

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

