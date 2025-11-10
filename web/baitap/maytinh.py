import streamlit as st
st.set_page_config(page_title="Low quaity CASIO FX 580VNX", layout="centered")
st.title('Just a brick can calculate')
st.header('Nhập số mà bạn muốn:')
n1=st.number_input('Số đầu', value=0.0)
n2=st.number_input('Số thú hai', value=0.0)
st.header('Chọn phép toán')
op=st.selectbox(
    'Chọn phép toán'
    ('Cộng','Trừ','Nhân','Chia')
)
def x (op->str)->int:
    if op == "Cộng":
        