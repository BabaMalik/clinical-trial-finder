# Clinical Trial Finder

A Python web app for searching public study records from [ClinicalTrials.gov](https://clinicaltrials.gov/data-api/api).

The app will let users search by condition, intervention, study location, and overall recruiting status. Users will be able to read explanations of each filter and save named searches for later.

## Run locally

Install dependencies with Python 3.10 or newer, then start Flask.

    python -m pip install -r requirements.txt
    python -m flask --app app run

Open [the local app](http://127.0.0.1:5000/) in your browser.

## Development status

Increment 02 adds the Flask entry point and verifies that the browser can load the app. Search and saved searches are planned for later increments.
