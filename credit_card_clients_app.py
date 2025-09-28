from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your dataset (adjust the path if needed)
df = pd.read_excel("default_of_credit_card_clients_0 (1).xlsx")

@app.route("/")
def home():
    return "<h1>Credit Card Clients Project</h1><p>Go to /summary to see dataset info.</p>"

@app.route("/summary")
def summary():
    # Get summary stats
    summary = df.describe().to_html()
    return f"<h2>Dataset Summary</h2>{summary}"

import matplotlib.pyplot as plt
import io
from flask import send_file

@app.route("/plot")
def plot():
    # Example: Age distribution
    fig, ax = plt.subplots(figsize=(6,4))
    df["AGE"].hist(bins=20, ax=ax, color="skyblue", edgecolor="black")
    ax.set_title("Age Distribution of Clients")
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")

    # Save to memory instead of a file
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()
    return send_file(img, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)


