from lxml import etree
from utilities.misc import prettyprint_html
from ingestion.src.clean import parse_drug_label
import os 



def process_data(raw_data_dir, processed_data_dir):
    raw_files = os.listdir(raw_data_dir)
    for file in raw_files: 
        input_loc = os.path.join(raw_data_dir, file)
        # save output as json 
        output_loc = os.path.join(processed_data_dir, file).replace('.html', '.json')
        parse_drug_label(input_path = input_loc, output_path = output_loc)

def main():
    print("Running entry point for ds toolkit")

    base_dir = os.getcwd()
    processed_data_dir = os.path.join(base_dir, "data/processed/")
    raw_data_dir = os.path.join(base_dir, "data/raw/")
    

    # process raw files and save into jsons in /data/processed 
    process_data(
        raw_data_dir=raw_data_dir,
        processed_data_dir=processed_data_dir
    )




if __name__ == "__main__":
    main()
