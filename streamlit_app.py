import streamlit as st

st.title('🎈 App Name')

st.write('Oi Cate')

x = st.slidebar("Rate Cate", 1, 10)

if x == 10:
    st.write("Yes, cate is a 10")
else:
    st.write("Nope, you're mistaken.")
