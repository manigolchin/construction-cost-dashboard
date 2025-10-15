from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Stelle sicher, dass Ordner existieren
os.makedirs('uploads', exist_ok=True)
os.makedirs('static', exist_ok=True)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and file.filename.endswith('.xlsx'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        df = pd.read_excel(filepath)

        # Erwartete Spalten: Datum, Soll-Kosten, Ist-Kosten, Beschreibung
        df['Abweichung'] = df['Ist-Kosten'] - df['Soll-Kosten']
        total_soll = df['Soll-Kosten'].sum()
        total_ist = df['Ist-Kosten'].sum()
        abweichung_prozent = ((total_ist - total_soll) / total_soll) * 100

        status = 'grün'
        if total_ist > total_soll * 1.1:
            status = 'rot'
        elif total_ist > total_soll:
            status = 'gelb'

        # Diagramm
        plt.figure(figsize=(8, 4))
        plt.bar(df['Beschreibung'], df['Soll-Kosten'], label='Soll-Kosten')
        plt.bar(df['Beschreibung'], df['Ist-Kosten'], label='Ist-Kosten', alpha=0.7)
        plt.xlabel('Beschreibung')
        plt.ylabel('Kosten (€)')
        plt.title('Soll- vs. Ist-Kosten pro Tätigkeit')
        plt.legend()
        chart_path = os.path.join('static', 'chart.png')
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

        return render_template('dashboard.html',
                               total_soll=round(total_soll, 2),
                               total_ist=round(total_ist, 2),
                               abweichung_prozent=round(abweichung_prozent, 2),
                               status=status,
                               chart_path=chart_path)

    return "Bitte eine gültige Excel-Datei hochladen (.xlsx)"

if __name__ == "__main__":
    app.run(debug=True)
