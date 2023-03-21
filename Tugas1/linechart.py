import streamlit as st
import pandas as pd
import numpy as np

st.write("Devin Chandra_32200042")
st.write("Line chart")
chart_data = pd.DataFrame(
     {
    'Tono': [10, 40, 20, 60],
    'Tini': [5, 10, 30, 75],
    'Tina': [90, 10, 65, 55]

    },
     columns=['Tono', 'Tini', 'Tina'])

st.line_chart(chart_data)