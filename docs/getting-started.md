{% include sidebar.html %}
<div style="margin-left: 260px;">

<button onclick="toggleTheme()" style="position: fixed; right: 20px; top: 20px; z-index: 999;">
  Toggle Theme
</button>
<script src="assets/theme.js"></script>
<link rel="stylesheet" href="assets/theme.css">

# 🚀 Getting Started with Sigilith‑M

This guide walks you through installing, running, and using Sigilith‑M for the first time.

---

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Run the Starlette Server

```bash
uvicorn app.main:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

---

## 3. Analyze a Sequence

```bash
curl -X POST -F "sequence=AABBBCCXYZ123" http://127.0.0.1:8000/analyze
```

---

## 4. View the Dashboard

Open:

```
http://127.0.0.1:8000
```

---

## 5. Explore the Docs

- [Architecture](architecture.md)
- [Pipeline](pipeline.md)
- [Examples](examples.md)
- [API](api.md)

You're now ready to use Sigilith‑M.

{% include footer.html %}
</div>
