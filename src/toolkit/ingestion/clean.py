import os
import json
from lxml import html 

def parse_drug_label(
          input_path: str, 
          output_path: str
          ):
    """
    Parse raw .html input and save to /data/processed directory as .json
    """
    with open(file = input_path, mode = 'rb') as file:
            file_content = file.read()
            
    tree = html.fromstring(html = file_content)
    result = {}

    sections = tree.xpath("//h2") 

    for heading in sections:
        title = heading.text_content().strip().upper()
        content = []

        next_node = heading.getnext()
        while next_node is not None and next_node.tag != "h2":
            content.append(next_node.text_content().strip())
            next_node = next_node.getnext() 

        if content:
            result[title] = "\n\n".join(content)

    if not os.path.exists(output_path): 
         os.mknod(output_path)
         
    with open(output_path, "w") as f:
         json.dump(result, f)

    return 


def process_all_tables():
    pass

