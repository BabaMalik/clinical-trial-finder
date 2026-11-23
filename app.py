"""Browser entry point for Clinical Trial Finder."""
from flask import Flask, render_template

app = Flask(__name__, template_folder=".")


@app.get("/")
def home():
    return render_template("index.html")
