import streamlit as st

st.set_page_config(page_title="90題深度性格特質測試", page_icon="🧬", layout="centered")

# 90題資料庫 (維度: O=開放性, C=謹慎度, E=外向性, A=親和性, N=神經質)
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

options = ["1 - 非常不同意", "2 - 不同意", "3 - 沒意見", "4 - 同意", "5 - 非常同意"]
score_map = {"1 - 非常不同意": 1, "2 - 不同意": 2, "3 - 沒意見": 3, "4 - 同意": 4, "5 - 非常同意": 5}

if "page" not in st.session_state:
    st.session_state.page = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

current_page = st.session_state.page
ITEMS_PER_PAGE = 18
total_pages = 5

# 【修正核心】如果頁面是 99，代表要顯示結果，不顯示題目和進度條
# 【請替換 app.py 的後半段結果頁邏輯，從 if st.session_state.page == 99: 開始】

if st.session_state.page == 99:
    st.balloons()
    st.success("🎉 90題深度性格測驗完成！以下為您的專屬深度性格剖析報告：")
    
    scores = {"O": 0, "C": 0, "E": 0, "A": 0, "N": 0}
    
    for i in range(90):
        q = questions[i]
        ans_text = st.session_state.answers.get(f"q_{i}")
        raw_score = score_map[ans_text]
        final_score = (6 - raw_score) if q["sign"] == -1 else raw_score
        scores[q["dim"]] += final_score

    # 換算百分比
    for dim in scores:
        scores[dim] = round((scores[dim] - 18) / 72 * 100)

    # --- 綜合性格評判邏輯 ---
    high_o = scores["O"] >= 50
    high_c = scores["C"] >= 50
    high_e = scores["E"] >= 50
    high_a = scores["A"] >= 50
    high_n = scores["N"] >= 50

    # 初始化報告文本
    personality_title = ""
    description = ""
    strengths = []
    weaknesses = []

    # 根據高低分數組合判定 8 種主要人格原型
    if high_e and high_c and high_o:
        personality_title = "👑 開創型領袖 (The Visionary Leader)"
        description = "你充滿活力與遠見，既有天馬行空的創新想法，又能腳踏實地地將計畫執行到位。你在團隊中通常扮演引領方向的角色，擅長激勵他人並帶領團隊開疆闢土。"
        strengths = ["具備強大的目標導向與超強執行力", "樂於接受挑戰，創新思維活躍", "社交能力極佳，能輕鬆發揮影響力", "善於統籌大局與分配資源"]
        weaknesses = ["有時對下屬或旁人要求過高，顯得有些強勢", "當進度不如預期時，容易產生焦慮與不耐煩", "可能因過於追求完美而給自己帶來極大壓力", "容易同時開太多戰線，導致體力透支"]
        
    elif high_e and high_a and not high_c:
        personality_title = "🌟 陽光社交家 (The Enthusiastic Connector)"
        description = "你是人群中的開心果與黏著劑！你極具親和力，熱愛與人互動，天生自帶吸引大眾的魅力。你更看重人與人之間的和諧情感，而非冰冷的死板規矩。"
        strengths = ["同理心極強，擅長療癒與安慰他人", "溝通能力絕佳，能快速融入新環境並建立人脈", "樂觀開朗，能為團隊帶來積極正向的氛圍", "處事靈活彈性，適應能力強"]
        weaknesses = ["做事較缺乏條理與規劃，容易丟三落四或拖延", "常常因為不好意思拒絕他人而承擔過多不屬於自己的責任", "容易受到他人情緒或負面評價的影響", "在處理繁瑣的數據與行政細節時容易分心"]

    elif not high_e and high_c and not high_o:
        personality_title = "🛡️ 沉穩守護者 (The Reliable Anchor)"
        description = "你是一個極其踏實、低調且無比靠譜的人。你不喜歡流於表面或花哨的事物，更傾向於在幕後默默耕耘。社會與團隊因為有你的自律和嚴謹，才能穩定運作。"
        strengths = ["做事極其細心、負責任，承諾的事一定做到", "生活與工作井然有序，抗干擾能力強", "尊重傳統與既定規範，處事沉穩讓人安心", "擅長處理繁瑣、需要耐心的長線任務"]
        weaknesses = ["思維相對保守，面對突如其來的重大變革容易感到抗拒", "不擅長表達內心真實情感，容易把壓力藏心底", "過度聚焦於細節，有時會陷入「見樹不見林」的盲點", "在社交場合顯得較為被動或嚴肅"]

    elif not high_e and high_o and high_a:
        personality_title = "🔮 靈魂思想家 (The Idealistic Thinker)"
        description = "你擁有深邃的內心世界與豐富的想像力。比起喧囂的社交場合，你更喜歡安靜地探索藝術、哲學或內心精神世界。你對人性的敏銳洞察讓你往往充滿智慧。"
        strengths = ["具有深度思考能力與獨特的審美與創造力", "高度精神自省，不容易盲從社會主流價值觀", "對朋友極其忠誠，心思細膩體貼", "擅長文字創作、策略規劃或深度諮詢"]
        weaknesses = ["容易陷入想得多、做得少的「思想巨人，行動矮子」困境", "過度敏感，容易被周遭的負面能量或衝突所灼傷", "有時顯得過於孤僻或不食人間煙火", "面對嚴酷、現實的激烈競爭時容易退縮"]
        
    elif high_n and not high_e:
        personality_title = "🔍 敏銳觀察家 (The Sensitive Analyst)"
        description = "你是一個情感極其細膩、警覺性很高的觀察者。你對環境的微小變化和潛在風險有著天生的雷達，這讓你能夠在危機發生前就做好最壞的打算與防範。"
        strengths = ["危機意識極高，能提早發現計畫中的漏洞", "情感細膩，對文藝、心理學有極高的天賦", "做事謹慎，很少因為衝動而犯下大錯", "注重細節，交出來的成果通常非常嚴謹"]
        weaknesses = ["容易過度焦慮、內耗，常為還沒發生的事情失眠", "自信心較不足，遇到挫折容易陷入自我懷疑", "在壓力環境下決策容易變得猶豫不決", "需要較長的獨處時間來修復受傷的情緒"]
        
    else:
        personality_title = "⚖️ 務實平衡者 (The Pragmatic Realist)"
        description = "你是一個非常均衡、務實的人。你不會極端地偏向某個特質，而是能根據當下的現實情況靈活調整自己。你既能參與社交，也能享受獨處；既仰望星空，也腳踏實地。"
        strengths = ["情緒狀態相對穩定，處事客觀冷靜", "沒有明顯的性格短板，能夠勝任多種角色", "既講求效率，也能兼顧人際關係的平衡", "務實理性，不輕易被天馬行空的幻想誤導"]
        weaknesses = ["有時在團隊中顯得特色不夠鮮明", "在需要極致創新或極端激進的環境中可能顯得保守", "傾向於打安全牌，可能會因此錯失一些高風險高回報的機會", "容易流於安穩的舒適圈而不願輕易打破現狀"]

    # --- 精美排版輸出結果 ---
    st.markdown(f"## 🏆 您的綜合性格原型：{personality_title}")
    st.markdown("---")
    
    st.markdown("### 📝 性格特寫描述")
    st.info(description)
    
    # 左右分欄顯示優劣勢
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("### 💪 核心核心優勢")
        for s in strengths:
            st.write(f"✅ {s}")
            
    with col_right:
        st.markdown("### ⚠️ 潛在盲點與劣勢")
        for w in weaknesses:
            st.write(f"❌ {w}")

    st.markdown("---")
    if st.button("🔄 重新測試"):
        st.session_state.page = 0
        st.session_state.answers = {}
        st.rerun()

else:
    # 正常顯示題目分頁（這段保持跟之前一樣即可，此處為結構完整性保留）
    st.title("🧬 90題深度大五人格特質測試")
    st.write("本測試基於心理學著名的大五人格理論（Big Five）。請根據真實感受填寫。")
    st.markdown("---")
    st.subheader(f"📑 測試進行中：第 {current_page + 1} / {total_pages} 頁")
    st.progress((current_page + 1) / total_pages)

    start_idx = current_page * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE

    for i in range(start_idx, end_idx):
        q = questions[i]
        q_key = f"q_{i}"
        saved_ans = st.session_state.answers.get(q_key, None)
        default_idx = options.index(saved_ans) if saved_ans in options else None
        
        st.session_state.answers[q_key] = st.radio(q["text"], options, index=default_idx, key=f"radio_{i}")
        st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if current_page > 0:
            if st.button("⬅️ 上一頁"):
                st.session_state.page -= 1
                st.rerun()
    with col3:
        if current_page < total_pages - 1:
            if st.button("下一頁 ➡️"):
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
            if st.button("📊 送出並查看深度報告"):
                all_complete = True
                for i in range(90):
                    if st.session_state.answers.get(f"q_{i}") is None:
                        all_complete = False
                if all_complete:
                    st.session_state.page = 99
                    st.rerun()
                else:
                    st.error("🚨 還有題目被漏掉了，請檢查前面各頁面！")
