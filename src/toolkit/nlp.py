import json
import spacy 
from pathlib import Path 
from typing import Dict 


nlp = spacy.load("en_core_web_sm")

def extract_entities_from_dict(input_dict: Dict) -> Dict[str, list[Dict[str, str]]]:
    # Language object 
    nlp = spacy.load("en_core_web_sm")

    # create dict { section : doc object}
    sections_doc = {}
    for section, text in input_dict.items():
        if text:
            sections_doc[section] = nlp(' '.join(text.split()))
        else: 
            sections_doc[section] = ''

    # create output   
    entities = {}
    if sections_doc:
        for section, doc in sections_doc.items():
            if type(sections_doc[section]) == spacy.tokens.doc.Doc:
                entities[section] = [{'text': ents.text, 'label': ents.label_} for ents in doc.ents]

            else: 
                continue 
    

    return entities