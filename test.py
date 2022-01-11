import pandas as pd
import numpy as np
import streamlit as st


df_five_step = pd.read_csv("C:\\Users\\bingtong.chua\\Desktop\\first_5_click.csv")
st.write(pd.unique(df_five_step['first_step'])
