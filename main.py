from flask import Flask, render_template, request
from ai_module import generate_budget_recommendation
import plotly.express as px
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    budget_recommendation = None
    graph = None

    if request.method == "POST":
        account_balance = float(request.form["account_balance"])
        spending_timeframe = int(request.form["spending_timeframe"])
        budget_recommendation, recommended_allocation = generate_budget_recommendation(
            account_balance, spending_timeframe)
        categories = ["Food", "Housing", "Entertainment", "Savings"]

        graph_data = {
            "data": [
                {"x": categories, "y": recommended_allocation,
                 "type": "bar", "name": "Budget Allocation"}
            ],
            "layout": {"title": "Recommended Budget Allocation"}
        }

        graph = json.dumps(graph_data)

    return render_template("index.html", budget_recommendation=budget_recommendation, graph=graph)

if __name__ == "__main__":
    app.run(debug=True)
