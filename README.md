# 🏗️ Construction Cost Dashboard
A simple Flask web application for visualizing and analyzing planned vs. actual construction costs. Upload an Excel file, and the app will automatically calculate deviations and generate a cost comparison chart.

## 🚀 Features
- Upload an `.xlsx` Excel file with construction tasks
- Calculates total planned and actual costs
- Shows percentage deviation and budget status
- Displays a bar chart comparing planned vs. actual costs
- Status indicator:
  - 🟢 Within budget  
  - 🟡 Slightly over budget  
  - 🔴 Over budget  

## 🧩 Example Excel Format
| Beschreibung         | Soll-Kosten | Ist-Kosten |
|----------------------|-------------|-------------|
| Aushub               | 1000        | 2200        |
| Pflasterarbeiten     | 800         | 850         |
| Betonieren           | 1200        | 1300        |
Save this as `demo_baustelle.xlsx` and upload it through the web interface.

## 🛠️ Installation
```bash
# 1. Clone the repository
git clone https://github.com/manigolchin/construction-cost-dashboard.git
cd construction-cost-dashboard

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install flask pandas matplotlib openpyxl

# 4. Run the application
python app.py

