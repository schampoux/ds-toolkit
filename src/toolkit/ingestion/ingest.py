# Scrapes/downloads the messy data 
# base URL for the web application is: https://dailymed.nlm.nih.gov/
# base URL for the web service is: https://dailymed.nlm.nih.gov/dailymed/services/
    # The web service only supports the HTTP method GET, since the web service function is to retrieve data from DailyMed.
# sample URI: https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.xml

import requests 
import os 
from typing import Any
from pathlib import Path 
from datetime import datetime 

def fetch_spl_list(
        base_url: str, 
        limit: int = 30
        ) -> list[dict[str: Any]]:
    
    """ Fetch a list of Structured Product Label (SPL) entries. """
    response = requests.get(url = base_url,
                            params = {'pagesize': limit})
    response.raise_for_status()
    data = response.json()
    return data.get("data", [])

def download_spl_html(
        set_id, 
        download_url: str, 
        output_dir: str
        ) -> Path:
    
    """Download SPL SML file given a set_id."""
    download_url_json  = download_url + set_id + ".json"
    response = requests.get(download_url_json)
    response.raise_for_status()

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{set_id}.html")

    with open (file_path, "wb") as f: 
        f.write(response.content) 

    return file_path

if __name__ == "__main__":
    BASE_URL = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json"
    DOWNLOAD_URL = "https://dailymed.nlm.nih.gov/dailymed/downloadset/"

    flow_time = datetime.time(datetime.now())
    output_dir_raw = f"./data/raw/{flow_time}/"

    spls = fetch_spl_list(base_url = BASE_URL, limit = 30)
    for spl in spls:
        set_id = spl["setid"]
        print(f"Downloading SPL for set_id {set_id} into {output_dir_raw}")

        download_spl_html(
            set_id=set_id, 
            download_url=DOWNLOAD_URL, 
            output_dir=output_dir_raw
            )