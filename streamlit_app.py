
import streamlit as st
from backtester import run_backtest
from strength_engine import get_strength_data
from executor_model import suggest_trades
from gpt_reasoner import reason_trade
from auto_coder import apply_code_upgrade
from gui_auto_updater import refresh_layout

st.set_page_config(page_title="DaRealPips-AI", layout="wide")

st.title("📊 DaRealPips-AI Control Panel")
st.caption("Self-evolving AI trading bot for NAS100")

# Tabs for different functions
tab1, tab2, tab3, tab4 = st.tabs(["📈 Strategy Backtest", "⚡ Strength Analyzer", "🤖 AI Trade Assist", "🧠 Self-Coding Engine"])

with tab1:
    st.header("Run Backtest")
    if st.button("▶️ Start Backtest"):
        result = run_backtest("nas100_m1.csv", "sample_strategy.json")
        st.success("Backtest completed")
        st.json(result)

with tab2:
    st.header("Currency Strength Analysis")
    if st.button("📊 Analyze Strength"):
        strength = get_strength_data("nas100_m1.csv")
        st.dataframe(strength)

with tab3:
    st.header("AI Trade Suggestion")
    if st.button("💡 Suggest Trade"):
        suggestion = suggest_trades("nas100_m1.csv")
        st.write("📍 Suggested Trade:")
        st.json(suggestion)

    st.divider()
    st.header("GPT Reasoning")
    user_input = st.text_input("Enter a trade or scenario")
    if st.button("🧠 Get Reasoning"):
        response = reason_trade(user_input)
        st.write(response)

with tab4:
    st.header("Self-Updating Code Engine")
    if st.button("🧪 Run Code Upgrade"):
        result = apply_code_upgrade()
        st.write(result)

    if st.button("🔄 Refresh GUI"):
        refresh_layout()
        st.success("GUI layout updated!")

st.sidebar.markdown("✅ Built by DaRealPips")
