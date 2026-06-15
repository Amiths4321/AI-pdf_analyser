import os
import streamlit as st

# Railway port binding — must be set before anything else
os.environ["STREAMLIT_SERVER_PORT"]    = os.environ.get("PORT", "8501")
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

