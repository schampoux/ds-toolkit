from fastapi import FastAPI
from pydantic import BaseModel
from spacy_utils import extract_entities

app = FastAPI()

class LabelRequest(BaseModel):
    text: str 

@app.post("/entities")
def get_entities(request: LabelRequest):
    return extract_entities(request.txt)