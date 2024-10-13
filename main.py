import streamlit as st
from python_helper_file import generate_restaurant_name_and_items
import os
from dotenv import load_dotenv
load_dotenv()

st.title("Restaurant name and item generator")

cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","French","Mexican","Italian","American","German","Chines","Korean","japanese","Thai","Greek","Brazilian","Spanish","Vietnamese","Caribbean",))

if cuisine:
    response=generate_restaurant_name_and_items(cuisine)
    st.header(response["Restaurant_name"])
    menu_items=response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)

os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_API_KEY']=os.getenv("langchain_api_key")
os.environ['GOOGLE_API_KEY']=os.getenv("API_KEY")
