"""Browser entry point for Clinical Trial Finder."""
from flask import Flask, render_template, request

from registry import search_by_condition

app = Flask(__name__, template_folder=".")


@app.get("/")
def home():
    condition = request.args.get("condition", "").strip()
    trials = None
    error = None
    if condition:
        try:
            trials = search_by_condition(condition)
        except (OSError, ValueError, KeyError, TypeError):
            error = "ClinicalTrials.gov results are unavailable. Try again."
    return render_template("index.html", condition=condition, trials=trials, error=error)
