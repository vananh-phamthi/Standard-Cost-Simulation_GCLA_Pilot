from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GCLA | BOD Standard MCost Simulator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header[data-testid="stHeader"] {height: 0; visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {padding: 0.25rem 0.5rem 0 0.5rem; max-width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_html() -> str:
    """Load the standalone HTML simulator from disk."""
    base_dir = Path(__file__).parent
    for filename in ("GCLA_BOD_MCost_WhatIf_Simulator.html", "index.html"):
        candidate = base_dir / filename
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")
    return ""


html_content = load_html()
if html_content:
    components.html(html_content, height=1350, scrolling=True)
else:
    st.error("Simulator HTML file not found (expected GCLA_BOD_MCost_WhatIf_Simulator.html or index.html).")
