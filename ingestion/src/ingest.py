# Scrapes/downloads the messy data 
# base URL for the web application is: https://dailymed.nlm.nih.gov/
# base URL for the web service is: https://dailymed.nlm.nih.gov/dailymed/services/
    # The web service only supports the HTTP method GET, since the web service function is to retrieve data from DailyMed.
# sample URI: https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.xml

import requests 
import os 

BASE_URL = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json"

def fetch_spl_list(limit: int = 30) -> list:
    """ Fetch a list of Structured Product Label (SPL) entries. """
    response = requests.get(url = BASE_URL,
                            params = {'pagesize': limit})
    response.raise_for_status()
    data = response.json()
    return data.get("data", [])

def download_spl_xml(set_id, output_dir="data/raw"):
    """Download SPL SML file given a set_id."""
    xml_url = f"https://dailymed.nlm.nih.gov/dailymed/downloadset/{set_id}.json"
    response = requests.get(xml_url)
    response.raise_for_status()

    os.makedirs(output_dir, exist_ok=True)
    with open (os.path.join(output_dir, f"{set_id}.xml"), "wb") as f: 
        f.write(response.content) 

if __name__ == "__main__":
    spls = fetch_spl_list(limit = 30)
    for spl in spls:
        set_id = spl["setid"]
        print(f"Downloading SPL for set_id {set_id}")
        download_spl_xml(set_id)