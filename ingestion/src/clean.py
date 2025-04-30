import os 
from lxml import etree 
import json 

<<<<<<< Updated upstream
def parse_drug_label(path: str):
    with open(path) as p:
        p

    parser = etree.XMLParser(recover=True) # recover = True to ignore errors from parsing invalid characters 
    root = etree.parse(data = p, parser = parser)

    # tree = et.parse(source = path, parser = parser)
    # root.tag
    # et.ElementTree(file=path)
    return print(root.tag)
=======
def parse_drug_label():
    try:
        from lxml import etree 
        print("running with lxml.etree")
    except:
        import xml.etree.ElementTree as etree 
        print("running with Python's xml.etree.ElementTree")        
>>>>>>> Stashed changes

def get_section_text():
    pass

def process_all_tables():
    pass 
