# Sigilith‑M

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-GitHub%20Codespaces-lightgrey)

Sigilith‑M is a symbolic sequence analysis engine designed to compute entropy, transition density, structural risk, and regime classification.

It provides a full end‑to‑end pipeline:

```
sequence → normalize → segment → transform → signature → score → vectorize → wrap → store → display
```

Built with FastAPI, Jinja2, and a modular analysis engine, Sigilith‑M is designed for research‑grade symbolic cognition experiments and structural risk modelling.

## Features

- **Full Analysis Pipeline**: Normalize → Segment → Transform → Signature → Score → Vectorize
- **Risk Classification**: HIGH, MEDIUM, LOW based on structural drift and stability
- **Regime Detection**: Stable, Transitional, Chaotic regimes based on entropy
- **Web Dashboard**: Real-time visualization of analyses
- **Persistent Storage**: File-based JSON storage with UUID indexing
- **FastAPI**: Modern async web framework with automatic API docs

## Installation

```bash
# Clone repository
git clone https://github.com/Sigilith/Sigilith-m.git
cd Sigilith-m

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Start Web Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Then visit:
- **Dashboard**: http://localhost:8000/
- **API Docs**: http://localhost:8000/docs

### Analyze a Sequence

Via web form on dashboard, or via API:

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "sequence=AABBBCCXYZ123"
```

### View Analysis Result

```
http://localhost:8000/analysis/{analysis_id}
```

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Dashboard with all analyses |
| `/analyze` | POST | Submit sequence for analysis |
| `/analysis/{id}` | GET | View single analysis detail |
| `/docs` | GET | Interactive API documentation |

## Architecture

### Pipeline Flow

```
sequence (string)
    ↓
[normalize] → strip whitespace, validate
    ↓
[segment] → split into character tokens
    ↓
[transform] → test structural stability & drift
    ↓
[signature] → compute length, stability, drift, regex_class
    ↓
[score] → compute risk score and classify HIGH/MEDIUM/LOW
    ↓
[vectorize] → convert signature to numerical vector
    ↓
[wrap] → add UUID, timestamp, config-based classifications
    ↓
[store] → persist to JSON file with index
    ↓
[retrieve] → load and display on dashboard
```

### Core Modules

- **`app/normalization.py`** — Input normalization
- **`app/segmentation.py`** — Sequence tokenization
- **`app/transforms.py`** — Stability & drift computation
- **`app/signature.py`** — Structural signature extraction
- **`app/scoring.py`** — Risk classification
- **`app/vectorize.py`** — Numerical vector conversion
- **`app/engine.py`** — Orchestrates full pipeline
- **`app/analysis_wrapper.py`** — Adds metadata (UUID, timestamp, config classifications)
- **`app/storage_backend.py`** — Persistent file-based storage
- **`app/config.py`** — Risk/regime classification thresholds

## Data Model

### Analysis Result

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2026-04-05T12:34:56.789012",
  "sequence": "AABBBCCXYZ123",
  "entropy": 0.42,
  "transition_density": 0.58,
  "risk_score": 0.59,
  "risk": "MEDIUM",
  "regime_class": "transitional",
  "vector": [0.13, 0.7, 0.3],
  "summary": "Moderate structural consistency; further analysis recommended."
}
```

## Storage

Analyses are stored in `data_storage/` directory:
- `data_storage/index.json` — Index of all analysis IDs
- `data_storage/{uuid}.json` — Individual analysis files

## Configuration

Edit `app/config.py` to adjust:
- `RISK_THRESHOLD` — Risk classification threshold for HIGH (default: 0.7)
- `RISK_MEDIUM_THRESHOLD` — Risk classification threshold for MEDIUM (default: 0.4)
- `REGIME_LEVELS` — Regime classification ranges

## Development

### Run Tests

```bash
pytest tests/
```

### Format Code

```bash
black app/
```

## License

MIT

## Author

Sigilith

## Support

For issues, visit: https://github.com/Sigilith/Sigilith-m/issues
