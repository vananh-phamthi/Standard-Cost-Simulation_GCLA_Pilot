# GCLA | BOD Standard MCost Operational What-If Simulator

Interactive Operational What-If Simulator for **GCLA Pilot (PEMDO)** standard manufacturing cost (`USD / MT`), built as a standalone HTML dashboard and wrapped for deployment on **Streamlit Community Cloud**.

## Files
- `app.py` — Streamlit wrapper that renders `GCLA_BOD_MCost_WhatIf_Simulator.html` (with fallback to `index.html`).
- `GCLA_BOD_MCost_WhatIf_Simulator.html` — Standalone interactive BOD simulator.
- `index.html` — Copy of the standalone simulator for GitHub Pages / fallback rendering.
- `requirements.txt` — Python dependencies (`streamlit>=1.36`).
- `v1.0_Asia_Standard_Cost_Model_GCLA_Pilot (1).xlsx` — Source cost model workbook.

## Deploy on Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **New app** and choose repository `vananh-phamthi/Standard-Cost-Simulation_GCLA_Pilot`, branch `main`.
3. Set **Main file path** to `app.py` and click **Deploy**.
