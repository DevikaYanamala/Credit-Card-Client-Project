from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your dataset (adjust the path if needed)
df = pd.read_excel("C:/Users/devik/Downloads/default_of_credit_card_clients_0 (1).xlsx")

@app.route("/")
def home():
    return "<h1>Credit Card Clients Project</h1><p>Go to /summary to see dataset info.</p>"

@app.route("/summary")
def summary():
    # Get summary stats
    summary = df.describe().to_html()
    return f"<h2>Dataset Summary</h2>{summary}"

if __name__ == "__main__":
    app.run(debug=True)