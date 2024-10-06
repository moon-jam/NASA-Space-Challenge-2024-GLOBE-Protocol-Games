import json
import os

# Load the Q&A data from the JSON file
with open("QA.json", "r", encoding="utf-8") as file:
    qa_data = json.load(file)

# Create the 'qa' folder if it doesn't exist
os.makedirs("qa", exist_ok=True)

# Mapping of Chinese task names to English keys
task_names = {
    "river_water_quality_monitoring": "River Water Quality Monitoring",
    "soil_health_assessment": "Soil Health Assessment",
    "urban_air_quality_improvement": "Urban Air Quality Improvement",
    "community_waste_management": "Community Waste Management",
    "biodiversity_survey": "Biodiversity Survey",
    "energy_efficiency_improvement": "Energy Efficiency Improvement",
    "forest_restoration_project": "Forest Restoration Project",
    "environmental_regulations_awareness": "Environmental Regulations Awareness",
    "wetlands_protection": "Wetlands Protection",
    "agricultural_water_management": "Agricultural Water Management",
    "coastal_cleanup": "Coastal Cleanup",
    "soil_erosion_control": "Soil Erosion Control",
    "climate_change_education": "Climate Change Education",
    "renewable_energy_development": "Renewable Energy Development",
    "environmental_science_conference": "Environmental Science Conference",
    "urban_greening": "Urban Greening",
    "industrial_emissions_monitoring": "Industrial Emissions Monitoring",
    "environmental_volunteer_training": "Environmental Volunteer Training",
    "ecotourism_promotion": "Ecotourism Promotion",
    "environmental_regulation_enforcement": "Environmental Regulation Enforcement",
}

# HTML template for the Q&A page, including Chinese title and countdown timer
html_template = """
<!DOCTYPE html>
<html lang="en">
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
            <a href="/qa/{task_key}.html">繁體中文</a> | English
        </div>
        <div id="start-container" class="question-box text-center">
            <button id="start-button">Start</button>
        </div>
        <div id="question-container" class="question-box" style="display: none;">
            <p id="question">Loading question...</p>
            <div class="timer">Time remaining: <span id="timer">20</span> seconds</div>
            <button id="reveal">Reveal Answer</button>
            <p id="feedback"></p>
        </div>
    </div>
    <script src="../script.js"></script>
</body>
</html>
"""

# Generate HTML files for each task card
for task_key, task_title in task_names.items():
    with open(f"qa/{task_key}.html", "w", encoding="utf-8") as file:
        file.write(html_template.format(task_key=task_key, task_title=task_title))

# Generate the HTML content for the index page
index_content = ""

# Read the rule template file
with open("rule_template.html", "r", encoding="utf-8") as file:
    lines = file.readlines()
    index_content += "".join(lines[:-6])  # Exclude the last 6 lines

# Insert links to the task cards
for task_key, task_title in task_names.items():
    index_content += f' <a href="qa/{task_key}.html" class="list-group-item list-group-item-action">{task_title}</a>\n'

# Close HTML tags
index_content += """
</div>

</div>
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# Write the generated index page content to index.html
with open("index.html", "w", encoding="utf-8") as file:
    file.write(index_content)
