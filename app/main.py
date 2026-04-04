from fastapi import FastAPI
from app.models import SequenceInput
from app.engine import analyze_sequence
from app.clustering import cluster_vectors
from app.vectorize import signature_to_vector
from app.drift import compute_drift_trajectory

app = FastAPI(title="Sigilith-M v0.3")

@app.post("/analyze")
def analyze(input_data: SequenceInput):
    result = analyze_sequence(input_data.sequence)
    return result

@app.post("/cluster")
def cluster(signatures: list[dict]):
    vectors = [signature_to_vector(sig) for sig in signatures]
    result = cluster_vectors(vectors)
    return result

@app.post("/drift")
def drift(analyses: list[dict]):
    """
    Compute temporal drift trajectory across a list of analysis results.
    
    Input: list of analysis dicts (from /analyze endpoint)
    Output: drift trajectory with regime changes and trend analysis
    """
    result = compute_drift_trajectory(analyses)
    return result