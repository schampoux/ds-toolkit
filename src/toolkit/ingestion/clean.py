from lxml import etree 
import json 
from typing import Optional, Dict
from pathlib import Path 
import os 

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


def parse_drug_label(input_path: str, output_path: str) -> Dict:

    with open(input_path, mode = 'rb') as xml_file: 
        tree = etree.parse(xml_file)

    root = tree.getroot() 

    if None in root.nsmap:
        namespace = root.nsmap.get(None) 
    else:
        namespace = 0
        print("No default namespace")
    
    output = {}
    for section in TARGET_SECTIONS_SET:
        output[section] = ''

    elements_found = find_elements_by_tag(element = root, tag = "section", namespace = namespace)

    for section in elements_found:
        # print("section: ", section.tag)

        title_element = section.find(f".//{{{namespace}}}title") if namespace else section.find("title")
        
        if title_element is not None:
            title = " ".join(title_element.itertext()).strip().upper()
            # print("\ntitle: ", title)

            if title in TARGET_SECTIONS_SET:
                text_elements = section.findall(f".//{{{namespace}}}text") if namespace else section.findall("text") # returns a list of matching Elements 

                if not text_elements:
                    print("findall returned and empty list")

                section_text = " ".join(
                    " ".join(t.itertext()).strip()
                    for t in text_elements if t is not None)
                
                # print("section text: ",section_text)
                output[title] = section_text
    
    # if the dir does not exist, create the dir 
    output_dir = Path(output_path).parent 
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # dump to the output_path 
    with open(output_path, "w") as f:
        json.dump(obj = output, fp = f, indent=2)

    return output


def find_elements_by_tag(element, tag, namespace: Optional[str]) -> list[etree.Element]:
    if namespace:
        return element.findall(f".//{{{namespace}}}{"section"}")
    else: 
        return element.findall(f".//{tag}")