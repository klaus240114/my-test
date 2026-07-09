import streamlit as st

st.set_page_config(page_title="趣味心理測試", page_icon="🔮")
st.title("🔮 探索你的潛在性格")
st.write("這是一個簡單的趣味測試，幫助你快速了解自己的潛在性格傾向！")

with st.form("quiz_form"):
    q1 = st.radio("1. 當週末放假時，你通常更傾向於？", ["跟朋友出去聚會（E）", "待在家裡看劇（I）"])
    q2 = st.radio("2. 面對未來的規劃，你通常是？", ["走一步算一步（P）", "做詳細的計畫表（J）"])
    submit_button = st.form_submit_button("查看測試結果 🚀")

if submit_button:
    res = f"{'E' if 'E' in q1 else 'I'}{'J' if 'J' in q2 else 'P'}"
    st.info(f"你的性格核心密碼是：**{res}**")
    st.balloons()
