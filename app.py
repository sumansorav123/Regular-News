from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__)

api_key = "0c5e762e2e2f4c38bc4e6e177b33c46a"

def fetch_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url, timeout=5)
        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            return []

        return random.sample(articles, min(6, len(articles)))

    except Exception as e:
        print("Error:", e)
        return []
    
@app.route('/')
def home():
    articles = fetch_news()   
    return render_template("index.html", news=articles)

# 🔹 API for auto reload
@app.route('/news')
def news():
    articles = fetch_news()   
    return jsonify({"articles": articles})

if __name__ == '__main__':
    app.run(debug=True)