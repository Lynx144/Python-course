import streamlit as st
st.header("Ví dụ về Radio Button")
muc_do = st.radio(
    "Bạn thích Streamlit ở mức độ nào?",
    ("Rất thích", "Bình thường", "Chưa rõ")
)
st.write(f"Bạn đã chọn: {muc_do}")