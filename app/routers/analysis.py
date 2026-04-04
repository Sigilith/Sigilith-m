from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from app.analysis_wrapper import wrap_analysis
from app.storage import save_analysis, load_analysis
from app.templates import templates
from app.core import run_analysis

router = APIRouter()


@router.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, sequence: str = Form(...)):
    """
    Accepts a sequence, runs analysis, extracts metadata, stores result.
    """

    # Run the core analysis engine
    analysis_result = run_analysis(sequence)
    
    # Wrap with metadata extraction
    wrapped = wrap_analysis(sequence, analysis_result)

    # Store and get ID
    analysis_id = save_analysis(wrapped)

    # Return detail view
    return templates.TemplateResponse(
        "analysis_detail.html",
        {
            "request": request,
            "analysis": wrapped,
            "analysis_id": analysis_id
        },
    )


@router.get("/analysis/{analysis_id}", response_class=HTMLResponse)
async def analysis_detail(request: Request, analysis_id: str):
    """
    Fetch and display a specific analysis by ID.
    """
    analysis = load_analysis(analysis_id)
    
    if not analysis:
        return templates.TemplateResponse(
            "analysis_detail.html",
            {
                "request": request,
                "error": f"No analysis found with ID {analysis_id}",
                "analysis": None,
                "analysis_id": analysis_id
            },
        )
    
    return templates.TemplateResponse(
        "analysis_detail.html",
        {
            "request": request,
            "analysis": analysis,
            "analysis_id": analysis_id
        },
    )
