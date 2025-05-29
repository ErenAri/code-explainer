from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()
API_URL = os.getenv("API_URL")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    explanation = ""
    user_code = ""
    if request.method == "POST":
        user_code = request.form["code"]
        try:
            response = requests.post(API_URL, json={"code": user_code})
            explanation = response.json().get("explanation", "No explanation found.")
        except Exception as e:
            explanation = f"API error: {e}"
    return render_template("index.html", explanation=explanation, user_code=user_code)

if __name__ == "__main__":
    app.run(debug=True)
