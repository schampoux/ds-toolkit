from prefect import flow, task
from toolkit.ingestion.ingest import fetch_spl_list, download_spl_html
from toolkit.ingestion.clean import parse_drug_label
from pathlib import Path 
from dotenv import load_dotenv
import os 
from typing import Any 
from datetime import datetime 


load_dotenv()

# fetches drug label metadata from DailyMed
# downloads raw html
# parses + structures the HTML 
# saves clean JSON 

@task 
def fetch_metadata(base_url: str, limit: int) -> list[dict[str: Any]]:

    metadata = fetch_spl_list(
        base_url = base_url, 
        limit = limit
        )
    return metadata

@task 
def download_html(set_id, download_url, output_dir) -> Path:
    
    file_path = download_spl_html(
        set_id = set_id, 
        download_url=download_url, 
        output_dir=output_dir
        )
    
    return file_path

@task
def parse_and_clean(input_path, output_path):
    parse_drug_label(input_path=input_path,
                     output_path=output_path 
                     )
    return

@flow
def drug_label_pipeline(limit: int):
    processed_data_dir = "./data/processed"
    flow_time = datetime.time(datetime.now())
    output_dir_raw = f"./data/raw/{flow_time}/"

    metadata_list = fetch_metadata(
        base_url = os.getenv('BASE_URL'), 
        limit = limit
        )

    for spl in metadata_list:
        set_id = spl["setid"]

        download_html(
            set_id = set_id, 
            download_url = os.getenv('DOWNLOAD_URL'), 
            output_dir = output_dir_raw
            )
        
    for file in os.listdir(output_dir_raw):
        input_path_raw = os.path.join(output_dir_raw, file)
        file_name = file + '.json'
        output_path_processed = os.path.join(processed_data_dir, str(flow_time), file_name)
        parse_drug_label(input_path = input_path_raw, output_path = output_path_processed)

if __name__ == "__main__":
    drug_label_pipeline(limit=2)