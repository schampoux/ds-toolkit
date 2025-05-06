import os
import json
from lxml import etree 
from typing import Optional 

TARGET_SECTIONS_SET = {
    'INDICATIONS & USAGE',
    'WARNINGS',
    'ADVERSE REACTIONS',
    'CONTRAINDICATIONS',
    'ACTIVE INGREDIENTS',
    'PURPOSE',
    'USES',
    'PRODUCT LABEL',
    'OTHER INFORMATION',
    'DIRECTIONS',
    'INACTIVE INGREDIENTS',
    
}

def get_namespace(tree: etree.ElementTree):
    root = tree.getroot()
    if None in root.nsmap:
        namespace = root.nsmap.get(None) 
    else:
        namespace = 0
        print("No default namespace")
    return namespace 

def create_etree(input_path: str) -> etree.ElementTree:
    """Create etree from xml file"""
    with open(input_path, mode = 'rb') as xml_file: 
        tree = etree.parse(xml_file)
    return tree

def gather_titles(tree: etree.ElementTree, target_sections: set = TARGET_SECTIONS_SET) -> Dict:
    root = tree.getroot()
    namespace = get_namespace(tree=tree)
    
    dynamic_titles = set()

    elements_found = find_elements_by_tag(element = root, tag = "section", namespace = namespace)

    for section in elements_found:
        title_element = section.find(f".//{{{namespace}}}title") if namespace else section.find("title")
        
        if title_element is not None and title_element.text:
            title = " ".join(title_element.itertext()).strip().upper()
            print("\ntitle: ", title)

            if title in TARGET_SECTIONS_SET:
                text_elements = section.findall(f".//{{{namespace}}}text") if namespace else section.findall("text") # returns a list of matching Elements 

                if not text_elements:
                    print("findall returned and empty list")

                section_text = " ".join(
                    " ".join(t.itertext()).strip()
                    for t in text_elements if t is not None)
                
                print("section text: ",section_text)
                output[title] = section_text

    return output


def find_elements_by_tag(element, tag, namespace: Optional[str]) -> list[etree.Element]:
    if namespace:
        return element.findall(f".//{{{namespace}}}{"section"}")
    else: 
        return element.findall(f".//{tag}")
