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
from dotenv import load_dotenv

load_dotenv()

def fetch_spl_list(base_uri: str, limit: int = 30) -> list[dict[str: Any]]:
    """ Fetch a list of Structured Product Label (SPL) entries. """

    spl_url = os.path.join(base_uri, "spls.json")
    response = requests.get(
        url = spl_url,
        params = {'pagesize': limit}
        )
    response.raise_for_status()
    data = response.json()
    return data.get("data", [])

def download_spl_xml(
        set_id, 
        base_uri: str, 
        output_dir: str
        ) -> Path:
    
    """Download SPL .xml file given a set_id."""

    download_url_json  = os.path.join(base_uri, f"spls/{set_id}.xml")
    response = requests.get(download_url_json)
    response.raise_for_status()

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{set_id}.xml")

    with open (file_path, "wb") as f: 
        f.write(response.content) 

    return file_path

def main(): 
    # flow_time = datetime.time(datetime.now())
    # output_dir_raw = f"./data/raw/{flow_time}/"
    # base_uri = os.getenv('BASE_URI')
    # print("BASE_URI: ", base_uri)

    # spls = fetch_spl_list(base_uri = base_uri, limit = 2)
    # return print(spls)

    # for spl in spls:
    #     set_id = spl["setid"]
    #     print(f"Downloading SPL for set_id {set_id} into {output_dir_raw}")


    pass

if __name__ == "__main__":
    main()