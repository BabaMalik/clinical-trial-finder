"""HTTP client for the public ClinicalTrials.gov registry."""

import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

STUDIES_URL = "https://clinicaltrials.gov/api/v2/studies"


def fetch_studies():
    """Return the raw JSON bytes for the first page of study records."""
    query = urlencode({"format": "json", "pageSize": 10})
    request = Request(f"{STUDIES_URL}?{query}", headers={"Accept": "application/json"})
    with urlopen(request, timeout=15) as response:
        return response.read()


def fetch_study_page():
    """Return the decoded first page, including any pagination token."""
    page = json.loads(fetch_studies())
    if not isinstance(page, dict) or not isinstance(page.get("studies"), list):
        raise ValueError("Expected a ClinicalTrials.gov response with a studies list.")
    return page
