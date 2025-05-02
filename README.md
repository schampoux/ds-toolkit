# FDA Drug Label Ingestion & Parsing

## Project Summary
This project ingests unstructured drug labeling data from the [DailyMed](https://dailymed.nlm.nih.gov/) public API, extracts meaningful sections, and structures it into clean JSON for downstream NLP/ML use. 

## Tech Stack 
- Python 
- `requests`, `lxml`, `json`
- Basic CLI orchestration

## Workflow
1. `ingest.py`: Downloads HTML files using the DailyMed SPL web service. 
2. `clean.py`: Parses HTML sections using LXML and extracts clinical sections like "INDICATIONS", "WARNINGS", etc. 
3. Outputs are saved as structured JSON to `data/processed`.

## Example Output 

```json
{
  "INDICATIONS AND USAGE": "This medication is used for...",
  "WARNINGS": "Do not use if you are allergic to...",
  ...
}
