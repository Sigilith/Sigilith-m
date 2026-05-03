"""
Main application entrypoint for Sigilith‑M.

This module handles:
- Routing (pure Starlette, no FastAPI)
- Dashboard rendering
- WebSocket telemetry streaming
- Static file serving
- No Pydantic dependencies
- Snapshot persistence endpoints (GET /snapshot, POST /update)
"""

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, WebSocketRoute, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocket
from collections import deque
import asyncio
import json
import os
import tempfile

from app.routers.analysis import analyze, analysis_detail

templates = Jinja2Templates(directory="templates")
telemetry_buffer = deque(maxlen=200)

SNAPSHOT_PATH = "snapshot.json"
_DEFAULT_SNAPSHOT = {"site": {}, "version": 1}


def _deep_merge(base: dict, updates: dict) -> dict:
    """Recursively merge *updates* into *base*, returning the merged result."""
    result = dict(base)
    for key, value in updates.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def _load_snapshot() -> dict:
    """Load snapshot.json from disk, creating it with defaults if absent."""
    if not os.path.exists(SNAPSHOT_PATH):
        _save_snapshot(_DEFAULT_SNAPSHOT)
        return dict(_DEFAULT_SNAPSHOT)
    with open(SNAPSHOT_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_snapshot(data: dict) -> None:
    """Atomically persist snapshot data to disk."""
    dir_name = os.path.dirname(os.path.abspath(SNAPSHOT_PATH))
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=dir_name, delete=False, suffix=".tmp"
    ) as tmp:
        json.dump(data, tmp, indent=2)
        tmp_path = tmp.name
    os.replace(tmp_path, SNAPSHOT_PATH)

# ---------------------------------------------------------
# Dashboard Route
# ---------------------------------------------------------
async def dashboard(request):
    """Render the main dashboard."""
    return templates.TemplateResponse("dashboard.html", {"request": request})

# ---------------------------------------------------------
# WebSocket Telemetry Stream
# ---------------------------------------------------------
async def telemetry_ws(websocket):
    """Stream live telemetry data to connected WebSocket clients."""
    await websocket.accept()
    try:
        while True:
            if telemetry_buffer:
                await websocket.send_json(telemetry_buffer[-1])
            else:
                await websocket.send_json({"status": "waiting"})
            await asyncio.sleep(0.5)
    except Exception as e:
        print(f"WebSocket closed: {e}")

# ---------------------------------------------------------
# Demo Runner Endpoint
# ---------------------------------------------------------
async def run_demo(request):
    """Trigger the demo runner."""
    return JSONResponse({"status": "demo started"})

# ---------------------------------------------------------
# Snapshot Endpoints
# ---------------------------------------------------------
async def get_snapshot(request):
    """GET /snapshot — return the current snapshot.json contents."""
    return JSONResponse(_load_snapshot())


async def post_update(request):
    """POST /update — merge changes into snapshot.json when update=true."""
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"error": "Invalid JSON payload"}, status_code=400)

    if not body.get("update", False):
        return JSONResponse({"status": "no changes"})

    snapshot = _load_snapshot()
    changes = body.get("changes", {})
    updated = _deep_merge(snapshot, changes)
    _save_snapshot(updated)
    return JSONResponse({"status": "updated"})

# ---------------------------------------------------------
# App Definition
# ---------------------------------------------------------
app = Starlette(
    routes=[
        Route("/", dashboard),
        Route("/run-demo", run_demo, methods=["POST"]),
        Route("/analyze", analyze, methods=["POST"]),
        Route("/analysis/{analysis_id}", analysis_detail, methods=["GET"]),
        Route("/snapshot", get_snapshot, methods=["GET"]),
        Route("/update", post_update, methods=["POST"]),
        WebSocketRoute("/ws/telemetry", telemetry_ws),
        Mount("/static", StaticFiles(directory="static"), name="static"),
    ]
)