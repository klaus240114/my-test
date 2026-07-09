
import streamlit as st

st.set_page_config(page_title="專業趣味心理測試", page_icon="🔮")
st.title("🔮 探索你的潛在性格")
st.write("這是一個簡單的趣味測試，幫助你快速了解自己的潛在性格傾向！")

with st.form("quiz_form"):
    st.subheader("請回答以下問題：")
    
    q1 = st.radio("1. 當週末放假時，你通常更傾向於？", ["跟朋友出去聚會唱歌（E）", "待在家裡看劇休息（I）"])
    q2 = st.radio("2. 面對未來的規劃，你通常是？", ["隨遇而安，走一步算一步（P）", "做詳細的計畫表按部就班（J）"])
    q3 = st.radio("3. 當朋友跟你訴苦時，你的第一反應通常是？", ["幫他分析原因並給出建議（T）", "先安慰他的情緒表示理解（F）"])
    q4 = st.radio("4. 在觀察周遭事物時，你更在意的是？", ["眼前的現實與具體細節（S）", "未來的可能性與直覺靈感（N）"])
    
    submit_button = st.form_submit_button("查看測試結果 🚀")

if submit_button:
    st.markdown("---")
    # 計算性格密碼
    score_e = "E" if "E" in q1 else "I"
    score_j = "J" if "J" in q2 else "P"
    score_t = "T" if "T" in q3 else "F"
    score_s = "S" if "S" in q4 else "N"
    res = f"{score_e}{score_s}{score_t}{score_j}"
    
    st.info(f"你的性格核心密碼是：**{res}**")
    
    # 根據不同傾向給出評語
    if "E" in score_e:
        st.success("🌟 **陽光社交達人**：你充滿能量，喜歡與人互動！")
    else:
        st.success("🐱 **靈魂自由行者**：你享受獨處，在安靜的環境最自在。")
        
    st.balloons() # 噴出慶祝氣球
