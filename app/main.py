"""
Main application entrypoint for Sigilith‑M.

This module handles:
- Routing
- Dashboard rendering
- Analysis submission
- Summary statistics
- Integration with the storage backend
- Unified classification via app.config
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import config
from app.storage_backend import StorageBackend
from app.analysis_wrapper import wrap_analysis

import json

app = FastAPI()
storage = StorageBackend()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ---------------------------------------------------------
# Utility: Compute Dashboard Statistics
# ---------------------------------------------------------

def compute_statistics(analyses):
    """
    Compute summary statistics for the dashboard.
    Returns:
        - total analyses
        - average risk score
        - average entropy
        - risk counts
        - regime counts
    """

    if not analyses:
        return {
            "total": 0,
            "avg_risk": 0,
            "avg_entropy": 0,
            "risk_counts": {"HIGH": 0, "MEDIUM": 0, "LOW": 0},
            "regime_counts": {"stable": 0, "transitional": 0, "chaotic": 0},
        }

    total = len(analyses)

    avg_risk = sum(a.get("risk_score", 0) for a in analyses) / total
    avg_entropy = sum(a.get("entropy", 0) for a in analyses) / total

    risk_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    regime_counts = {"stable": 0, "transitional": 0, "chaotic": 0}

    for a in analyses:
        risk = a.get("risk", "LOW")
        regime = a.get("regime_class", "stable")

        if risk in risk_counts:
            risk_counts[risk] += 1

        if regime in regime_counts:
            regime_counts[regime] += 1

    return {
        "total": total,
        "avg_risk": avg_risk,
        "avg_entropy": avg_entropy,
        "risk_counts": risk_counts,
        "regime_counts": regime_counts,
    }


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    analyses = storage.load_all_analyses()

    stats = compute_statistics(analyses)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "analyses": analyses,
            "total_analyses": stats["total"],
            "avg_risk_score": stats["avg_risk"],
            "avg_entropy": stats["avg_entropy"],
            "risk_counts": stats["risk_counts"],
            "regime_counts": stats["regime_counts"],
        },
    )


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, sequence: str = Form(...)):
    """
    Accepts a sequence, runs the analysis engine (mocked for now),
    wraps the result, stores it, and returns the updated dashboard.
    """

    # Placeholder engine output — replace with real engine later
    raw_output = {
        "entropy": 0.42,
        "transition_density": 0.58,
        "risk_score": 0.51,
        "risk": None,
        "regime_class": None,
    }

    wrapped = wrap_analysis(raw_output)
    storage.save_analysis(wrapped)

    analyses = storage.load_all_analyses()
    stats = compute_statistics(analyses)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "analyses": analyses,
            "total_analyses": stats["total"],
            "avg_risk_score": stats["avg_risk"],
            "avg_entropy": stats["avg_entropy"],
            "risk_counts": stats["risk_counts"],
            "regime_counts": stats["regime_counts"],
        },
    )


# ---------------------------------------------------------
# NEW: Analysis Detail Route
# ---------------------------------------------------------

@app.get("/analysis/{analysis_id}", response_class=HTMLResponse)
async def view_analysis(request: Request, analysis_id: str):
    """
    Display a detailed view of a single analysis.
    """

    analysis = storage.load_analysis(analysis_id)

    if not analysis:
        return templates.TemplateResponse(
            "analysis_detail.html",
            {
                "request": request,
                "error": f"No analysis found with ID {analysis_id}",
                "analysis": None,
            },
        )

    return templates.TemplateResponse(
        "analysis_detail.html",
        {
            "request": request,
            "analysis": analysis,
        },
    )