from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    gold = {"rates": {"USD": 1950}}
    currency = {"rates": {"VND": 24500}}
    weather = {
        "name": "Hà Nội",
        "current_weather": {"temperature": 30},
        "weather": [{"description": "Trời nắng"}]
    }
    gold_history = {
        "years": ["2020", "2021", "2022", "2023", "2024"],
        "prices": [1500, 1600, 1700, 1800, 1950]
    }
    return render_template("giavang.html", gold=gold, currency=currency, weather=weather, gold_history=gold_history)

if __name__ == "__main__":
    app.run(debug=True)
