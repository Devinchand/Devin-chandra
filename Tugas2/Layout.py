import streamlit as st
import pandas as pd
import numpy as np
import time

st.write("Devin Chandra_32200042")
st.write("Show progress")

'Mohon Bersabar...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Progres {i+1}%')
  bar.progress(i + 1)
  time.sleep(0.1)

'...Terima Kasih telah Menunggu'