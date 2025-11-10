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
    st.markdown('**Thủ trong site** và **đừng peak**')
else:
    st.write('Đặt đi 😭')
z=st.multiselect(
    'Bạn gặp 3 quả bom, bạn sẽ nhặt quả nào?',
    ['Choáng', 'Khói', 'HE']
)
st.write('Bạn nhặt được  ',z)
st.header('Tình hướng xử lí')
a=st.selectbox(
    'Bạn đang ẩn nấp thì gặp 3 thg địch và bọn nó ko bt bạn ở đâu, bạn sẽ: ',
    ('Thg ở xa','Thg ở giữa', "Thg ở gần" )
)
if a == "Thg ở xa":
    st.write('Bạn bắn đc thg ở xa và 2 thg kia ko kịp phản ứng nên bạn làm "Ba"')
elif z == 'Thg ở giữa':
    st.write('Bạn bắn đc thg ở giữa và 2 thg kia nó kịp phản ứng nên bạn chết')
else:
    st.write('Quyết định tệ nhất bạn có thể làm 💀')