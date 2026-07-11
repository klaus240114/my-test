<!DOCTYPE html>
<html lang="zh-CH">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2026隱藏天賦潛能測試</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f9; color: #333; padding: 20px; text-align: center; }
        .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); max-width: 500px; margin: 40px auto; }
        button { background: #6c5ce7; color: white; border: none; padding: 12px 25px; border-radius: 8px; cursor: pointer; font-size: 16px; margin: 10px; width: 80%; }
        button:hover { background: #5b4cc4; }
        .hidden { display: none; }
        #result { font-weight: bold; font-size: 18px; line-height: 1.6; color: #2d3436; }
    </style>
</head>
<body>

<div class="card">
    <!-- 歡迎界面 -->
    <div id="start-page">
        <h2>🔮 隱藏天賦潛能測試</h2>
        <p>你這輩子，其實帶了個隱藏天賦出生。憑直覺回答3道題，解鎖你潛意識裡的終極潛能。</p>
        <button onclick="startTest()">開始測試</button>
    </div>

    <!-- 題目界面 -->
    <div id="question-page" class="hidden">
        <h3 id="question-text">題目加載中...</h3>
        <div id="options-container"></div>
    </div>

    <!-- 結果界面 -->
    <div id="result-page" class="hidden">
        <h2>✨ 測試結果</h2>
        <div id="result"></div>
        <p style="margin-top:30px; color:#666; font-size:14px;">想要獲取精準的【個人搞錢方向深度報告】？<br><b>請返回小紅書私信我「領取報告」！</b></p>
    </div>
</div>

<script>
    const questions = [
        { q: "1. 走在森林裡，迷路時你直覺會選擇哪條路？", o: [{t:"長滿鮮花的小徑",v:"A"}, {t:"青磚鋪成的古道",v:"B"}, {t:"陽光斑駁的林蔭道",v:"C"}, {t:"怪石嶙峋的近路",v:"D"}] },
        { q: "2. 如果獲得一筆意外之財，你第一反應會用來做什麼？", o: [{t:"買直覺想買很久的文創/禮物",v:"A"}, {t:"規劃投資或存起來",v:"B"}, {t:"請朋友大吃一頓分享快樂",v:"C"}, {t:"解決眼前的某個棘手難題",v:"D"}] },
        { q: "3. 看到朋友情緒低落，你平時的本能反應是？", o: [{t:"安靜陪伴，默默感知對方的痛苦",v:"A"}, {t:"幫他理智分析原因並找解決辦法",v:"B"}, {t:"講笑話或帶他出去玩轉移注意力",v:"C"}, {t:"告訴他別慌，天塌下來有辦法解決",v:"D"}] }
    ];

    let currentQ = 0;
    let scores = {A:0, B:0, C:0, D:0};

    function startTest() {
        document.getElementById('start-page').classList.add('hidden');
        document.getElementById('question-page').classList.remove('hidden');
        showQuestion();
    }

    function showQuestion() {
        let q = questions[currentQ];
        document.getElementById('question-text').innerText = q.q;
        let container = document.getElementById('options-container');
        container.innerHTML = '';
        q.o.forEach(opt => {
            let btn = document.createElement('button');
            btn.innerText = opt.t;
            btn.onclick = () => nextQuestion(opt.v);
            container.appendChild(btn);
        });
    }

    function nextQuestion(val) {
        scores[val]++;
        currentQ++;
        if(currentQ < questions.length) {
            showQuestion();
        } else {
            showResult();
        }
    }

    function showResult() {
        document.getElementById('question-page').classList.add('hidden');
        document.getElementById('result-page').classList.remove('hidden');
        
        let maxKey = Object.keys(scores).reduce((a, b) => scores[a] > scores[b] ? a : b);
        let resultText = "";
        
        if(maxKey === 'A') resultText = "【高階 直覺感知者】<br>你擁有極強的同理心和洞察力，別人的微表情你一眼就能看穿。適合心理、諮詢、文創、創意策劃領域！";
        if(maxKey === 'B') resultText = "【隱藏的 系統架構師】<br>你看似不愛管事，但擅長在混亂中理出邏輯。你的執行力極強，適合獨立項目主理人、創業或管理！";
        if(maxKey === 'C') resultText = "【天然的 能量擴音器】<br>你有一種天然的感染力和說服力。你天生適合做自媒體、買手帶貨、演講，靠分享和說話發財！";
        if(maxKey === 'D') resultText = "【高智商 危機解碼器】<br>遇到突發狀況越緊急你大腦越冷靜，逆境破局力一流。適合談判、操盤手或高難度自由職業！";
        
        document.getElementById('result').innerHTML = resultText;
    }
</script>
</body>
</html>
