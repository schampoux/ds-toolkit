import unittest
import tempfile 
import os 
import json 
from toolkit.ingestion.clean import parse_drug_label
from pathlib import Path


class TestClean(unittest.TestCase):
    def test_parse_drug_label(self):
        cwd = Path(os.getcwd()) # /ingestion
        input_path = os.path.join(cwd, "tests/ingestion/sample_html.html") # /tests/ingestion/sample_html.html
        output_path = os.path.join(cwd, "tests/ingestion/sample_html.json") # /tests/ingestion/sample_html.json
    
        parse_drug_label(
            input_path = input_path, 
            output_path = output_path
            )
        
        expected_output =  {
            "DOSAGE": "Take one tablet daily.\n\nDo not exceed recommended dose.", 
            "WARNINGS": "Keep out of reach of children."
            }
        
        # load in the output 
        with open(output_path, "rb") as f:
            result = json.load(f)

        
        self.assertEqual(expected_output, result)

if __name__ =="__main__":
    unittest.main()
