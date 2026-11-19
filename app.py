from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GCLA | BOD Standard MCost Simulator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SECRET_KEY = "gcla2026"


def get_query_key() -> str:
    """Safely read the optional ?key=... parameter across Streamlit versions."""
    try:
        if hasattr(st, "query_params"):
            raw_key = st.query_params.get("key", "")
            if isinstance(raw_key, list):
                return str(raw_key[0]).strip() if raw_key else ""
            return str(raw_key).strip()
        if hasattr(st, "experimental_get_query_params"):
            raw_key = st.experimental_get_query_params().get("key", [""])
            if isinstance(raw_key, list):
                return str(raw_key[0]).strip() if raw_key else ""
            return str(raw_key).strip()
    except Exception:
        return ""
    return ""


def load_html() -> str:
    """Load the standalone HTML simulator from disk."""
    base_dir = Path(__file__).parent
    for filename in ("GCLA_BOD_MCost_WhatIf_Simulator.html", "index.html"):
        candidate = base_dir / filename
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")
    return ""


if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if get_query_key().lower() == SECRET_KEY.lower():
    st.session_state.authenticated = True

if st.session_state.authenticated:
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
    html_content = load_html()
    if html_content:
        components.html(html_content, height=1350, scrolling=True)
    else:
        st.error("Simulator HTML file not found (expected GCLA_BOD_MCost_WhatIf_Simulator.html or index.html).")
else:
    st.markdown(
        """
        <style>
            #MainMenu {visibility: hidden;}
            header[data-testid="stHeader"] {height: 0; visibility: hidden;}
            footer {visibility: hidden;}
            .stApp {
                background: linear-gradient(135deg, #f0fdf4 0%, #f4f8f6 100%);
            }
            .lock-card {
                max-width: 540px;
                margin: 3.5rem auto 1.25rem auto;
                padding: 2.2rem 2.4rem;
                background: #ffffff;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(7, 94, 60, 0.08), 0 2px 6px rgba(0, 0, 0, 0.04);
                border-top: 5px solid #075e3c;
                text-align: center;
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            }
            .lock-icon {
                font-size: 2.8rem;
                margin-bottom: 0.6rem;
            }
            .lock-title {
                font-size: 1.35rem;
                font-weight: 800;
                color: #075e3c;
                margin-bottom: 0.4rem;
            }
            .lock-subtitle {
                font-size: 0.95rem;
                color: #4b5563;
                margin-bottom: 1.1rem;
                line-height: 1.5;
            }
            .lock-notice {
                font-size: 0.87rem;
                color: #536d62;
                background: #f4faf6;
                border: 1px dashed #bed8c9;
                border-radius: 8px;
                padding: 0.85rem 1rem;
                line-height: 1.45;
                text-align: left;
            }
        </style>
        <div class="lock-card">
            <div class="lock-icon">🔒</div>
            <div class="lock-title">Aboitiz Foods — GCLA Pilot</div>
            <div class="lock-subtitle">Standard MCost | Operational What-if Simulator<br><strong>Internal Board Decision Support</strong></div>
            <div class="lock-notice">
                ℹ️ <strong>Access Notice:</strong> Please enter the shared passcode below (or open via your direct VIP link) to view the simulator.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        with st.form("unlock_form", clear_on_submit=False):
            entered_key = st.text_input(
                "Passcode / Mật mã:",
                type="password",
                placeholder="Enter passcode and press Enter...",
            )
            submitted = st.form_submit_button(
                "🔓 Mở Dashboard / Unlock Dashboard",
                use_container_width=True,
                type="primary",
            )
        if submitted:
            if entered_key.strip().lower() == SECRET_KEY.lower():
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Mật mã không chính xác / Incorrect passcode.")
