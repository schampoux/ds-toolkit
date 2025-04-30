import os
import json

try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    import xml.etree.ElementTree as etree
    print("running with Python's xml.etree.ElementTree")


def parse_drug_label(path: str):
    parser = etree.XMLParser(recover=True) if 'lxml' in str(etree) else None

    with open(path, 'r') as file:
        if 'lxml' in str(etree):
            root = etree.parse(file, parser=parser).getroot()
        else:
            root = etree.parse(file).getroot()

    print(root.tag)
    return root


def get_section_text():
    pass

def process_all_tables():
    pass

