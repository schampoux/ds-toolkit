import json
import spacy 
from pathlib import Path 
from typing import Dict 


nlp = spacy.load("en_core_web_sm")

def extract_entities_from_section(text: str) -> Dict[str, list[dict]]:
    # Language object 
    nlp = spacy.load("en_core_web_sm")

    # Calling the nlp object on a string of text will return a processed Doc object 
    doc = nlp(text)
    entities = list(
        {"text": ent.text, "label": ent.label_} for ent in doc.ents
        )
    return {'entities': entities}