import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.header('10 API References')
st.write('Devin Chandra_32200042')
st.write(' ')


st.subheader('1. Write & Magic')
st.write('Write')
st.write(pd.DataFrame({
    'Nama': ['tono', 'tini', 'tina', 'toni'],
    'Nilai': [55, 90, 100, 75],
}))

('Magic')
('ini contoh magic')
st.write(' ')


st.subheader('2. Text Element')
st.markdown(':purple[ini contoh text elemen yang mengubah warna tulisan menjadi warna ungu]')
st.write(' ')


st.subheader('3. Data Display Element')
df = pd.DataFrame(
   np.random.randn(10, 3),
   columns=('nilai %d' % i for i in range(3)))

st.table(df)
st.write(' ')


st.subheader('4. Chart Element')
chart_data = pd.DataFrame(
    np.random.randn(10, 4),
    columns=['Data 1', 'Data 2', 'Data 3', 'Data 4'])

st.line_chart(chart_data)
st.write(' ')


st.subheader('5. Input Widget')
genre = st.radio(
    "Apa hewan Favorit anda?",
    ('Anjing', 'Kucing', 'Kelinci','Ikan'))

if genre == 'Anjing':
    st.write('Hewan Favorit anda adalah Anjing')
else:
    st.write("Hewan Favorit kamu bukan Anjing")
    st.write(' ')


st.subheader('6. Media Element')
image = Image.open("sunrise.jpg")

st.image(image, caption='Setiap matahari terbit membawa hari baru dengan harapan baru untuk awal yang baru.')
st.write(' ')

st.subheader('7. Layout & Container')
add_selectbox = st.sidebar.selectbox(
    "Apa yang lebih sering anda gunakan?",
    ("Smart Phone", "Computer", "Home Phone")
)
st.write('Output dapat di lihat di sidebar sebelah kiri')
st.write(' ')

st.subheader('8. Status Element')
st.balloons()
st.write('Dapat dilihat dari efek Balon di atas')
st.write(' ')

st.subheader('9. Control Flow')
form = st.form("my_form")
form.slider("Inside the form")
st.slider("Outside the form")
form.form_submit_button("Submit")
st.write(' ')

st.subheader('10. Utilities')
def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')

st.write(' ')