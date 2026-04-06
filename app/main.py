"""
Main application entrypoint for Sigilith‑M.

This module handles:
- Routing (pure Starlette, no FastAPI)
- Dashboard rendering
- WebSocket telemetry streaming
- Static file serving
- No Pydantic dependencies
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route, WebSocketRoute, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocket
from collections import deque
import asyncio

templates = Jinja2Templates(directory="templates")
telemetry_buffer = deque(maxlen=200)

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
# App Definition
# ---------------------------------------------------------
app = Starlette(
    routes=[
        Route("/", dashboard),
        Route("/run-demo", run_demo, methods=["POST"]),
        WebSocketRoute("/ws/telemetry", telemetry_ws),
        Mount("/static", StaticFiles(directory="static"), name="static"),
    ]
)