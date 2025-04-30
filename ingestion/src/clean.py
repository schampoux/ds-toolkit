import os
import json
from lxml import html 

def parse_drug_label(path: str):
    with open(file = path, mode = 'rb') as file:
            file_content = file.read()
    tree = html.fromstring(html = file_content)
    result = {}

    sections = tree.xpath("//h2") # .xpath() performs a global XPath query against the document 

    for heading in sections:
        title = heading.text_content().strip().upper()
        content = []

        # gather sibling elements up until the next <h2> or end of section
        next_node = heading.getnext()
        while next_node is not None and next_node.tag != "h2":
            # append the next node to our content list 
            content.append(next_node.text_content().strip())
            next_node = next_node.getnext() # move to the node after 

        if content:
            # if our content list is not empty, add title: content 
            # for handling content paragraphs, two newlines are inserted in between each. 
            result[title] = "\n\n".join(content)
    return result 


def get_section_text():
    pass

def process_all_tables():
    pass

