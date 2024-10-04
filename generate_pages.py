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
    "urban_air_quality_improvement": "城市空氣質量改善",
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
    <link rel="stylesheet" href="../style.css">
</head>
<body data-task="{task_key}">
    <h1>{task_title}</h1>
    <div id="start-container" class="question-box">
        <button id="start-button">開始</button>
    </div>
    <div id="question-container" class="question-box" style="display: none;">
        <p id="question">載入問題中...</p>
        <div class="timer">倒數時間: <span id="timer">20</span> 秒</div>
        <button id="reveal">顯示答案</button>
        <p id="feedback"></p>
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
index_content = """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>環境守護者遊戲規則</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <style>
    body {
      padding-top: 20px;
      text-align: center;
    }
    .container {
      max-width: 600px;
    }
    .list-group-item {
      font-size: 1.2em;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="mb-4">環境守護者遊戲規則</h1>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quaerat ut excepturi perferendis velit eligendi doloribus animi quia, voluptate quos quibusdam ipsum doloremque eius, veritatis enim dignissimos harum ad maiores rem aspernatur consectetur sed corporis libero consequatur. Totam, inventore! Dolorum, minima dignissimos, fugit consequatur recusandae unde ducimus harum sed error praesentium explicabo et dolore earum commodi consequuntur voluptas molestiae provident est repellat. Delectus, quos repellat. Dignissimos at eaque dolorem quam quos illo maxime dolores sunt distinctio tempora repudiandae laborum, quis iusto asperiores impedit quo? Dolorem incidunt porro non dolores, rem similique! Modi, dolorem tenetur provident vero aut fugit rerum accusamus. Doloremque vero illo optio odit eius inventore nesciunt quod aspernatur! In deleniti fugit, ducimus sed, reprehenderit sunt aliquam odio reiciendis nobis labore harum enim itaque a consequuntur corporis optio deserunt eaque ab similique! Totam sit perspiciatis voluptatum, cumque minus ipsam impedit laborum saepe necessitatibus reiciendis! Deleniti dolor repellat eligendi laudantium distinctio mollitia incidunt quaerat quis voluptatum magni sit facere magnam iure consectetur inventore ex cumque ducimus, expedita ut quidem possimus aut necessitatibus adipisci dicta! Reiciendis nihil eos repellendus quisquam totam? Placeat a possimus quisquam reiciendis odio ducimus animi velit natus aliquid repudiandae. Harum modi laborum commodi officia distinctio reprehenderit deserunt similique expedita quia nisi consequuntur dolorem, dignissimos doloribus velit corrupti perspiciatis. Dolor non voluptatibus, illo, delectus quo, eos a placeat optio atque expedita doloremque maxime. Odio saepe numquam eum error excepturi beatae earum nihil commodi facere similique, fuga velit sunt debitis totam fugit sequi ullam, suscipit impedit quasi in tempore? Adipisci sit dolorem veniam accusamus consequuntur pariatur harum blanditiis, magnam reprehenderit perferendis beatae optio illum. Laudantium molestiae tenetur aperiam libero, quos esse similique vel aut consectetur dolorem, tempora optio fugit numquam inventore, quam laboriosam autem. Error dolorum magnam architecto aspernatur voluptatum, natus nam, repellendus odio corporis perspiciatis neque explicabo excepturi ea.</p>
    <div class="list-group">
"""
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
