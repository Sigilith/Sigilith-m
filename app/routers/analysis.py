from starlette.responses import HTMLResponse
from app.analysis_wrapper import wrap_analysis
from app.storage import save_analysis, load_analysis
from app.templates import templates
from app.core import run_analysis


async def analyze(request):
    """
    Accepts a sequence, runs analysis, extracts metadata, stores result.
    """
    form = await request.form()
    sequence = form.get("sequence")
    if not sequence:
        return HTMLResponse("Missing required field: sequence", status_code=400)

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
            "analysis_id": analysis_id,
        },
    )


async def analysis_detail(request):
    """
    Fetch and display a specific analysis by ID.
    """
    analysis_id = request.path_params["analysis_id"]
    analysis = load_analysis(analysis_id)

    if not analysis:
        return templates.TemplateResponse(
            "analysis_detail.html",
            {
                "request": request,
                "error": f"No analysis found with ID {analysis_id}",
                "analysis": None,
                "analysis_id": analysis_id,
            },
            status_code=404,
        )

    return templates.TemplateResponse(
        "analysis_detail.html",
        {
            "request": request,
            "analysis": analysis,
            "analysis_id": analysis_id,
        },
    )
