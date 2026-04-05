{% include sidebar.html %}
<div style="margin-left: 260px;">

<button onclick="toggleTheme()" style="position: fixed; right: 20px; top: 20px; z-index: 999;">
  Toggle Theme
</button>
<script src="assets/theme.js"></script>
<link rel="stylesheet" href="assets/theme.css">

# 🔧 Analysis Pipeline

Sigilith‑M processes symbolic sequences through a deterministic, multi‑stage pipeline.
Each stage is isolated, auditable, and contributes to the final structural signature.

---

## 1. Normalize

Standardizes the raw sequence:
- uppercase conversion
- invalid character removal
- canonical symbol mapping

---

## 2. Segment

Splits the sequence into symbolic units for analysis.

---

## 3. Transform

Extracts structural features:
- frequency maps
- transition matrices
- local pattern windows

---

## 4. Signature Extraction

Generates a symbolic fingerprint representing the structure of the sequence.

---

## 5. Scoring

Computes:
- entropy
- transition density
- risk score

---

## 6. Vectorization

Converts symbolic features into numerical embeddings.

---

## 7. Wrapping

Adds metadata:
- UUID
- timestamp
- risk class
- regime class

---

## 8. Storage

Persists results in JSON format for dashboard retrieval.

---

## 9. Display

Dashboard renders results in real time.

{% include footer.html %}
</div>
