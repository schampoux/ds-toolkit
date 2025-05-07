from prefect import flow, task
from toolkit.ingestion.ingest import fetch_spl_list, download_spl_xml
from toolkit.ingestion.clean import parse_drug_label
from pathlib import Path 
from dotenv import load_dotenv
import os 
from typing import Any 
from datetime import datetime 

load_dotenv()

@task 
def fetch_metadata(base_uri: str, limit: int) -> list[dict[str: Any]]:

    metadata = fetch_spl_list(
        base_uri = base_uri, 
        limit = limit
        )
    return metadata

@task 
def download_xml(set_id, base_uri, output_dir) -> Path:
    if not os.path.exists("./data/raw"):
        os.mkdir("./data/raw")

    file_path = download_spl_xml(
        set_id = set_id, 
        base_uri=base_uri, 
        output_dir=output_dir
        )
    
    return file_path

@task
def parse_and_clean(input_path, output_path):
    if not os.path.exists('./data/processed'):
        os.mkdir('./data/processed')
        
    parse_drug_label(input_path=input_path,
                     output_path=output_path 
                     )
    return

@task
def extract_concepts():
    pass

@flow
def drug_label_pipeline(limit: int):
    processed_data_dir = "./data/processed"
    flow_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    output_dir_raw = f"./data/raw/{flow_time}/"

    metadata_list_future = fetch_metadata.submit(
        base_uri = os.getenv('BASE_URI'), 
        limit = limit
        )
    metadata_list = metadata_list_future.result()

    for spl in metadata_list:
        set_id = spl["setid"]

        raw_path_future = download_xml.submit(
            set_id = set_id, 
            base_uri = os.getenv('BASE_URI'), 
            output_dir = output_dir_raw
            )
        
        raw_path = raw_path_future.result() 

        processed_path = os.path.join(processed_data_dir, flow_time, f"{set_id}.json")
 
        parse_and_clean_future = parse_and_clean.submit(input_path = raw_path, output_path = processed_path)
        parse_and_clean_future.result()


if __name__ == "__main__":
    drug_label_pipeline(limit=2)