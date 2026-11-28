"""HTTP client for the public ClinicalTrials.gov registry."""

import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

STUDIES_URL = "https://clinicaltrials.gov/api/v2/studies"


def fetch_studies(condition=None):
    """Return the raw JSON bytes for the first page of study records."""
    params = {"format": "json", "pageSize": 10}
    if condition:
        params["query.cond"] = condition
    query = urlencode(params)
    request = Request(f"{STUDIES_URL}?{query}", headers={"Accept": "application/json"})
    with urlopen(request, timeout=15) as response:
        return response.read()


def fetch_study_page(condition=None):
    """Return the decoded first page, including any pagination token."""
    page = json.loads(fetch_studies(condition))
    if not isinstance(page, dict) or not isinstance(page.get("studies"), list):
        raise ValueError("Expected a ClinicalTrials.gov response with a studies list.")
    return page


def search_by_condition(condition):
    """Return display fields for the first page of matching studies."""
    trials = []
    for study in fetch_study_page(condition)["studies"]:
        protocol = study["protocolSection"]
        identity = protocol["identificationModule"]
        nct_id = identity["nctId"]
        trials.append({
            "id": nct_id,
            "title": identity["briefTitle"],
            "status": protocol["statusModule"]["overallStatus"],
            "url": f"https://clinicaltrials.gov/study/{nct_id}",
        })
    return trials
