"""HTTP client for the public ClinicalTrials.gov registry."""

from urllib.parse import urlencode
from urllib.request import Request, urlopen

STUDIES_URL = "https://clinicaltrials.gov/api/v2/studies"


def fetch_studies():
    """Return the raw JSON bytes for the first page of study records."""
    query = urlencode({"format": "json", "pageSize": 10})
    request = Request(f"{STUDIES_URL}?{query}", headers={"Accept": "application/json"})
    with urlopen(request, timeout=15) as response:
        return response.read()

