from lxml import html, etree
import json 
from typing import Dict 

def prettyprint_html(element, **kwargs):
    html_str = html.tostring(doc = element, pretty_print=True, **kwargs)
    print(html_str.decode(), end='')

def prettyprint_xml(element, **kwargs):
    xml = etree.tostring(element, pretty_print=True, **kwargs)
    print(xml.decode(), end='')

def load_json(input_file_path: str)-> Dict:
    with open(file = input_file_path, mode = 'rb') as f:
        json_file_contents = json.load(f)
        return json_file_contents
    
def dump_json(input_data, output_path, indent: int = 2):
    with open(output_path, "w") as f:
        json.dump(obj = input_data, fp = f, indent = indent)
