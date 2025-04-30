import os 
from lxml import etree 
import json 

def parse_drug_label(path: str):
    with open(path) as p:
        p

    parser = etree.XMLParser(recover=True) # recover = True to ignore errors from parsing invalid characters 
    root = etree.parse(data = p, parser = parser)

    # tree = et.parse(source = path, parser = parser)
    # root.tag
    # et.ElementTree(file=path)
    return print(root.tag)

def get_section_text():
    pass

def process_all_tables():
    pass 
