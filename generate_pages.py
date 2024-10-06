import json
import os

# 加載問答集 JSON 檔案
with open("QA.json", "r", encoding="utf-8") as file:
    qa_data = json.load(file)

# 創建 'qa' 資料夾
os.makedirs("qa", exist_ok=True)

# 任務卡的中文名稱映射表
task_names = {
    "river_water_quality_monitoring": "河川水質監測",
    "soil_health_assessment": "土壤健康評估",
    "urban_air_quality_improvement": "城市空品質改善",
    "community_waste_management": "社區廢棄物管理",
    "biodiversity_survey": "生物多樣性調查",
    "energy_efficiency_improvement": "能源效率提升",
    "forest_restoration_project": "森林復育計畫",
    "environmental_regulations_awareness": "環境法規宣導",
    "wetlands_protection": "濕地保護",
    "agricultural_water_management": "農業用水管理",
    "coastal_cleanup": "海岸線清理",
    "soil_erosion_control": "土壤侵蝕防治",
    "climate_change_education": "氣候變遷教育",
    "renewable_energy_development": "可再生能源開發",
    "environmental_science_conference": "環境科學研討會",
    "urban_greening": "城市綠化",
    "industrial_emissions_monitoring": "廢氣排放監測",
    "environmental_volunteer_training": "環境保護志工培訓",
    "ecotourism_promotion": "生態旅遊推廣",
    "environmental_regulation_enforcement": "環境法規執行"
}

# 問答頁面模板，包含中文標題和倒數計時功能
html_template = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{task_title}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="../style.css">
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #f8f9fa;
            padding: 20px;
        }}
        h1 {{
            color: #343a40;
            margin-bottom: 20px;
        }}
        .language-switch {{
            margin-bottom: 20px;
            font-size: 1.1em;
        }}
        .language-switch a {{
            color: #007bff;
            text-decoration: none;
        }}
        .language-switch a:hover {{
            text-decoration: underline;
        }}
        .question-box {{
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}
        #start-button, #reveal {{
            background-color: #007bff;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }}
        #start-button:hover, #reveal:hover {{
            background-color: #0056b3;
        }}
        .timer {{
            font-size: 1.2em;
            margin-top: 10px;
        }}
        #feedback {{
            margin-top: 20px;
            font-size: 1.1em;
        }}
    </style>
</head>
<body data-task="{task_key}">
    <div class="container">
        <h1>{task_title}</h1>
        <div class="language-switch">
            繁體中文 | <a href="/en/qa/{task_key}.html">English</a>
        </div>
        <div id="start-container" class="question-box text-center">
            <button id="start-button">開始</button>
        </div>
        <div id="question-container" class="question-box" style="display: none;">
            <p id="question">載入問題中...</p>
            <div class="timer">倒數時間: <span id="timer">20</span> 秒</div>
            <button id="reveal">顯示答案</button>
            <p id="feedback"></p>
        </div>
    </div>
    <script src="../script.js"></script>
</body>
</html>
"""

# 生成每個任務卡的 HTML 文件
for task_key, task_title in task_names.items():
    with open(f"qa/{task_key}.html", "w", encoding="utf-8") as file:
        file.write(html_template.format(task_key=task_key, task_title=task_title))

# 生成首頁的 HTML 內容
index_content = ""

with open("rule_template.html", "r", encoding="utf-8") as file:
    lines = file.readlines()
    index_content += ''.join(lines[:-6])

# 插入任務卡的鏈接
for task_key, task_title in task_names.items():
    index_content += f'      <a href="qa/{task_key}.html" class="list-group-item list-group-item-action">{task_title}</a>\n'

# 關閉 HTML 標籤
index_content += """
    </div>
  </div>
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# 將生成的首頁內容寫入 index.html
with open("index.html", "w", encoding="utf-8") as file:
    file.write(index_content)
