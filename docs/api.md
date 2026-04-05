{% include sidebar.html %}
<div style="margin-left: 260px;">

<button onclick="toggleTheme()" style="position: fixed; right: 20px; top: 20px; z-index: 999;">
  Toggle Theme
</button>
<script src="assets/theme.js"></script>
<link rel="stylesheet" href="assets/theme.css">

# 🧩 API Documentation

Sigilith‑M exposes a simple FastAPI interface for sequence analysis.

---

## POST /analyze

Submit a sequence for analysis.

### Request

Form field:
- `sequence`: string

### Response

```json
{
  "id": "uuid",
  "timestamp": "2026-04-05T20:14:00Z",
  "entropy": 0.42,
  "transition_density": 0.58,
  "risk_score": 0.51,
  "risk": "medium",
  "regime_class": "mid-stability",
  "vector": [...]
}
```

---

## GET /

Dashboard view.

---

## GET /analysis/{id}

Returns detailed analysis for a specific sequence.

{% include footer.html %}
</div>
