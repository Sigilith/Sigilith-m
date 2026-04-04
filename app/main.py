from fastapi import FastAPI
from app.models import SequenceInput
from app.engine import analyze_sequence

app = FastAPI(title="Sigilith-M v0.1")

@app.post("/analyze")
def analyze(input_data: SequenceInput):
    result = analyze_sequence(input_data.sequence)
    return result