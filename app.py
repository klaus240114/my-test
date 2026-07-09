import streamlit as st

st.set_page_config(page_title="90題深度性格特質測試", page_icon="🧬", layout="centered")

st.title("🧬 90題深度大五人格特質測試")
st.write("本測試基於心理學著名的大五人格理論（Big Five），從五個核心維度深度剖析你的性格。請根據你的真實感受填寫，預計耗時 8-10 分鐘。")
st.markdown("---")

# 90題資料庫 (維度: O=開放性, C=謹慎度, E=外向性, A=親和性, N=神經質)
# 符號 + 代表正向題，- 代表反向題
questions = [
    # --- 外向性 (E) ---
    {"text": "1. 我在聚會中總是能輕鬆主動與陌生人攀談。", "dim": "E", "sign": 1},
    {"text": "2. 我喜歡成為大家注目的焦點。", "dim": "E", "sign": 1},
    {"text": "3. 我通常充滿活力，說話速度較快。", "dim": "E", "sign": 1},
    {"text": "4. 我喜歡熱鬧、刺激的社交場合。", "dim": "E", "sign": 1},
    {"text": "5. 我擅長帶動團體氣氛。", "dim": "E", "sign": 1},
    {"text": "6. 我做決定非常果斷且迅速。", "dim": "E", "sign": 1},
    {"text": "7. 我容易向他人展現熱情。", "dim": "E", "sign": 1},
    {"text": "8. 我生活節奏很快，不喜歡慢吞吞。", "dim": "E", "sign": 1},
    {"text": "9. 我常主動發起團體活動。", "dim": "E", "sign": 1},
    {"text": "10. 我在人群中感到孤立時（反向），會覺得很不舒服。", "dim": "E", "sign": -1},
    {"text": "11. 我傾向於保持低調，不愛出風頭。", "dim": "E", "sign": -1},
    {"text": "12. 獨處能讓我更有效地恢復精力。", "dim": "E", "sign": -1},
    {"text": "13. 在團體討論中，我通常聽多過於說。", "dim": "E", "sign": -1},
    {"text": "14. 我不喜歡太嘈雜的娛樂場所。", "dim": "E", "sign": -1},
    {"text": "15. 我是一個比較內斂、不容易激動的人。", "dim": "E", "sign": -1},
    {"text": "16. 面對陌生環境，我通常採取觀望態度。", "dim": "E", "sign": -1},
    {"text": "17. 我不喜歡向外人透露太多個人生活細節。", "dim": "E", "sign": -1},
    {"text": "18. 我享受一個人安靜做事情的時間。", "dim": "E", "sign": -1},

    # --- 親和性 (A) ---
    {"text": "19. 我容易信任他人，並相信人性本善。", "dim": "A", "sign": 1},
    {"text": "20. 我樂於幫助他人，即使這需要犧牲我的時間。", "dim": "A", "sign": 1},
    {"text": "21. 我擅長設身處地為他人著想（同理心）。", "dim": "A", "sign": 1},
    {"text": "22. 我對身邊的人非常體貼與溫柔。", "dim": "A", "sign": 1},
    {"text": "23. 為了保持和諧，我願意與他人妥協。", "dim": "A", "sign": 1},
    {"text": "24. 我相信誠實是人際關係中最重要的事。", "dim": "A", "sign": 1},
    {"text": "25. 我對別人的不幸遭遇容易感到同情。", "dim": "A", "sign": 1},
    {"text": "26. 我不喜歡和人爭吵，盡量避免衝突。", "dim": "A", "sign": 1},
    {"text": "27. 我對他人抱持著寬容的態度。", "dim": "A", "sign": 1},
    {"text": "28. 為了個人利益，有時需要利用別人。", "dim": "A", "sign": -1},
    {"text": "29. 我覺得很多人都在背後算計別人。", "dim": "A", "sign": -1},
    {"text": "30. 我說話比較直接，不太在乎是否會傷到別人尊嚴。", "dim": "A", "sign": -1},
    {"text": "31. 我認為同情心有時候會誤事。", "dim": "A", "sign": -1},
    {"text": "32. 如果別人對我不客氣，我也會狠狠反擊。", "dim": "A", "sign": -1},
    {"text": "33. 我不輕易相信別人的口頭承諾。", "dim": "A", "sign": -1},
    {"text": "34. 我認為在競爭中手段強硬是必須的。", "dim": "A", "sign": -1},
    {"text": "35. 我很少對陌生人的困難產生真正的關心。", "dim": "A", "sign": -1},
    {"text": "36. 我覺得每個人都應該先顧好自己。", "dim": "A", "sign": -1},

    # --- 謹慎度 (C) ---
    {"text": "37. 我做事總是會提前做好詳細的規劃。", "dim": "C", "sign": 1},
    {"text": "38. 我對自己的工作或學業要求極高。", "dim": "C", "sign": 1},
    {"text": "39. 我隨時保持物品整齊與環境乾淨。", "dim": "C", "sign": 1},
    {"text": "40. 承諾過的事情，我一定會想辦法按時完成。", "dim": "C", "sign": 1},
    {"text": "41. 我非常注重細節，很少粗心大意。", "dim": "C", "sign": 1},
    {"text": "42. 面對困難，我有極強的毅力堅持到底。", "dim": "C", "sign": 1},
    {"text": "43. 我是一個生活作息非常有規律的人。", "dim": "C", "sign": 1},
    {"text": "44. 做決策前，我一定會反覆思考後果。", "dim": "C", "sign": 1},
    {"text": "45. 我總是嚴格遵守各種法規和社會規範。", "dim": "C", "sign": 1},
    {"text": "46. 我經常把事情拖延到最後一刻才做。", "dim": "C", "sign": -1},
    {"text": "47. 我的房間或辦公桌經常處於凌亂狀態。", "dim": "C", "sign": -1},
    {"text": "48. 我做決定時比較衝動，常憑感覺走。", "dim": "C", "sign": -1},
    {"text": "49. 我經常改變計畫，不喜歡死板的時程表。", "dim": "C", "sign": -1},
    {"text": "50. 遇到枯燥繁瑣的事情，我很容易分心。", "dim": "C", "sign": -1},
    {"text": "51. 我有時候答應別人的事會忘記做到。", "dim": "C", "sign": -1},
    {"text": "52. 我覺得過度追求完美是浪費時間。", "dim": "C", "sign": -1},
    {"text": "53. 我做事比較隨性，看心情決定進度。", "dim": "C", "sign": -1},
    {"text": "54. 我不喜歡被條條框框的規則束縛。", "dim": "C", "sign": -1},

    # --- 神經質 (N) ---
    {"text": "55. 我經常莫名感到焦慮或沒來由的擔心。", "dim": "N", "sign": 1},
    {"text": "56. 我的情緒起伏比較大，容易多愁善感。", "dim": "N", "sign": 1},
    {"text": "57. 面對壓力時，我很容易覺得承受不住。", "dim": "N", "sign": 1},
    {"text": "58. 只要別人眼神或口氣不對，我很容易覺得受挫。", "dim": "N", "sign": 1},
    {"text": "59. 我經常反思自己的缺點並感到自卑。", "dim": "N", "sign": 1},
    {"text": "60. 我很容易生氣或對周遭感到不耐煩。", "dim": "N", "sign": 1},
    {"text": "61. 當遇到突發事件，我容易感到驚慌失措。", "dim": "N", "sign": 1},
    {"text": "62. 悲傷或低落的情緒在我身上會持續很久。", "dim": "N", "sign": 1},
    {"text": "63. 我非常在乎別人對我的評價和看法。", "dim": "N", "sign": 1},
    {"text": "64. 我能快速地從挫折和打擊中恢復過來。", "dim": "N", "sign": -1},
    {"text": "65. 我大部分時間都覺得心情很平靜安穩。", "dim": "N", "sign": -1},
    {"text": "66. 面對緊急危機，我能保持冷靜清醒的頭腦。", "dim": "N", "sign": -1},
    {"text": "67. 我很少會因為小事而抓狂或生氣。", "dim": "N", "sign": -1},
    {"text": "68. 我對自己的未來和能力充滿自信。", "dim": "N", "sign": -1},
    {"text": "69. 我不易受外界環境的風吹草動影響情緒。", "dim": "N", "sign": -1},
    {"text": "70. 我是一個抗壓性很高的人。", "dim": "N", "sign": -1},
    {"text": "71. 我很少感到無助或絕望。", "dim": "N", "sign": -1},
    {"text": "72. 我不常有失眠或因為壓力導致的身體不適。", "dim": "N", "sign": -1},

    # --- 開放性 (O) ---
    {"text": "73. 我對各種抽象哲學和科學理論充滿好奇心。", "dim": "O", "sign": 1},
    {"text": "74. 我非常享受欣賞音樂、畫作或大自然美景。", "dim": "O", "sign": 1},
    {"text": "75. 我擁有豐富且天馬行空的想像力。", "dim": "O", "sign": 1},
    {"text": "76. 我喜歡嘗試沒吃過的食物或去沒去過的地方旅遊。", "dim": "O", "sign": 1},
    {"text": "77. 我樂於接觸和探討與我截然不同的思想與文化。", "dim": "O", "sign": 1},
    {"text": "78. 我常常有些與眾不同的新奇點子。", "dim": "O", "sign": 1},
    {"text": "79. 我容易沉浸在文藝作品或電影的情節中。", "dim": "O", "sign": 1},
    {"text": "80. 我喜歡尋找事物背後的深刻意涵，不滿足於表面。", "dim": "O", "sign": 1},
    {"text": "81. 相比於一成不變，我更熱愛多變的生活模式。", "dim": "O", "sign": 1},
    {"text": "82. 我覺得過度探討抽象的理論非常無聊實用性低。", "dim": "O", "sign": -1},
    {"text": "83. 我更喜歡遵循傳統和既有的習慣來做事。", "dim": "O", "sign": -1},
    {"text": "84. 我很少花時間去思考不切實際的幻想。", "dim": "O", "sign": -1},
    {"text": "85. 我對藝術品、當代展覽通常沒有太大興趣。", "dim": "O", "sign": -1},
    {"text": "86. 相比於創新，我更信任時間檢驗過的傳統智慧。", "dim": "O", "sign": -1},
    {"text": "87. 我不喜歡複雜燒腦的電影，更偏愛簡單娛樂的劇情。", "dim": "O", "sign": -1},
    {"text": "88. 我更關注現實生活中的柴米油鹽，而非精神理想。", "dim": "O", "sign": -1},
    {"text": "89. 學習未知的學科知識對我而言是件苦差事。", "dim": "O", "sign": -1},
    {"text": "90. 我不喜歡打破常規的變革，安穩現狀最好。", "dim": "O", "sign": -1}
]

# 選項與分數映射
options = ["1 - 非常不同意", "2 - 不同意", "3 - 沒意見", "4 - 同意", "5 - 非常同意"]
score_map = {"1 - 非常不同意": 1, "2 - 不同意": 2, "3 - 沒意見": 3, "4 - 同意": 4, "5 - 非常同意": 5}

# 使用 Streamlit 的 session_state 來記錄分頁狀態與使用者回答
if "page" not in st.session_state:
    st.session_state.page = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

# 計算分頁資訊 (共 90 題，一頁 18 題，共 5 頁)
ITEMS_PER_PAGE = 18
total_pages = 5
current_page = st.session_state.page
start_idx = current_page * ITEMS_PER_PAGE
end_idx = start_idx + ITEMS_PER_PAGE

st.subheader(f"📑 測試進行中：第 {current_page + 1} / {total_pages} 頁")
st.progress((current_page + 1) / total_pages)

# 顯示當前分頁的 18 個題目
for i in range(start_idx, end_idx):
    q = questions[i]
    q_key = f"q_{i}"
    # 讀取已保留的答案
    saved_ans = st.session_state.answers.get(q_key, None)
    default_idx = options.index(saved_ans) if saved_ans in options else None
    
    st.session_state.answers[q_key] = st.radio(
        q["text"], 
        options, 
        index=default_idx, 
        key=f"radio_{i}"
    )
    st.markdown("---")

# 控制按鈕區域
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if current_page > 0:
        if st.button("⬅️ 上一頁"):
            st.session_state.page -= 1
            st.rerun()

with col3:
    if current_page < total_pages - 1:
        if st.button("下一頁 ➡️"):
            # 檢查這一頁是不是都有填
            page_complete = True
            for i in range(start_idx, end_idx):
                if st.session_state.answers.get(f"q_{i}") is None:
                    page_complete = False
            
            if page_complete:
                st.session_state.page += 1
                st.rerun()
            else:
                st.error("🚨 本頁還有題目沒寫完喔！")
    else:
        # 最後一頁顯示送出按鈕
        if st.button("📊 送出並查看深度報告"):
            # 檢查最後一頁是否填寫完畢
            all_complete = True
            for i in range(90):
                if st.session_state.answers.get(f"q_{i}") is None:
                    all_complete = False
            
            if all_complete:
                st.session_state.page = 99  # 進入結果頁
                st.rerun()
            else:
                st.error("🚨 還有題目被漏掉了，請檢查前面各頁面！")

# 顯示結果頁
if st.session_state.page == 99:
    st.balloons()
    st.success("🎉 恭喜你完成了 90 題深度性格測驗！以下是你的性格剖析報告：")
    
    # 初始分數字典 (總分, 題數)
    scores = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}
    
    # 計算分數
    for i in range(90):
        q = questions[i]
        ans_text = st.session_state.answers.get(f"q_{i}")
        raw_score = score_map[ans_text]
        
        # 如果是反向題，分數要倒過來計算 (5分變1分，4分變2分...)
        if q["sign"] == -1:
            final_score = 6 - raw_score
        else:
            final_score = raw_score
            
        scores[q["dim"]] += final_score

    # 轉化為百分比（每維度 18 題，最高 90 分，最低 18 分）
    # 換算公式: (實際得分 - 18) / (90 - 18) * 100
    for dim in scores:
        scores[dim] = round((scores[dim] - 18) / 72 * 100)

    # 呈現結果
    st.markdown("### 📊 五大人格特質百分比")
    
    st.write(f"**🟢 外向性 (Extraversion)：{scores['E']}%**")
    st.progress(scores['E'] / 100)
    st.caption("代表你對外部世界的投入程度、社交意願與能量來源。得分高者熱情、善社交；低者內斂、享受獨處。")
    
    st.write(f"**🔵 親和性 (Agreeableness)：{scores['A']}%**")
    st.progress(scores['A'] / 100)
    st.caption("代表你對他人的信任、同理心與合作意願。得分高者體貼、樂於助人；低者具競爭心、現實直率。")

    st.write(f"**🟤 謹慎度 (Conscientiousness)：{scores['C']}%**")
    st.progress(scores['C'] / 100)
    st.caption("代表你的自律程度、組織能力與追求成就的毅力。得分高者有計畫、負責任；低者隨性、靈活。")

    st.write(f"**🔴 神經質 (Neuroticism)：{scores['N']}%**")
    st.progress(scores['N'] / 100)
    st.caption("代表你對壓力的敏感度與情緒穩定性。得分高者情感細膩、易焦慮；低者沉穩、抗壓性強。")

    st.write(f"**🟣 開放性 (Openness to Experience)：{scores['O']}%**")
    st.progress(scores['O'] / 100)
    st.caption("代表你對新事物、藝術與抽象思考的開放態度。得分高者具創造力、好奇心強；低者務實、尊重傳統。")

    st.markdown("---")
    if st.button("🔄 重新測試"):
        st.session_state.page = 0
        st.session_state.answers = {}
        st.rerun()
