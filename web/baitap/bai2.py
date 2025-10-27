import streamlit as st
st.header('Bạn đang chơi rank tại map Mirage')
st.header('Đi site nào??')
Site=st.radio(
    "Đi:",
    ('A','Mid','B')
)
st.header('Đây là cái nút')
if st.button('Plant Bomb'):
    st.write("Bomb has been planted")
else:
    st.write('Press 4 to plant')
y=st.checkbox('Đặt Bomb A chưa')
if y:
    st.markdowm('**Thủ trong site** và **đừng peak**')
else:
    st.write('Đặt đi 😭')
st.header('Tình hướng xử lí')
