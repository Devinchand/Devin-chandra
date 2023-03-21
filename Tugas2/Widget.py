import streamlit as st
import pandas as pd
import numpy as np

st.write("Devin Chandra_32200042")

st.write("Selectbox")
df = pd.DataFrame({
    'Angka': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    })

option = st.selectbox(
    'Pilih angka Favorit anda?',
     df['Angka'])

'Angka Favorit Anda adalah: ', option
