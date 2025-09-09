import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import random

st.set_page_config(
    page_title="EDAG AI Testing Dashboard",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 EDAG AI Data Testing Dashboard")
st.subheader("Autonomous Validation for Datalake → EDW → Datamart → QlikSense")

# Mock test results
layers = ["Datalake", "EDW", "Datamart", "Reporting"]
statuses = ["✅ PASS", "✅ PASS", "⚠️ WARN", "✅ PASS"]
tests = [12, 18, 8, 5]
durations = [15.2, 22.1, 8.7, 3.5]
last_runs = [
    datetime.now() - timedelta(minutes=2),
    datetime.now() - timedelta(minutes=5),
    datetime.now() - timedelta(minutes=1),
    datetime.now() - timedelta(seconds=30)
]

data = {
    "Layer": layers,
    "Status": statuses,
    "Tests Run": tests,
    "Duration (s)": durations,
    "Last Run": [lr.strftime("%H:%M:%S") for lr in last_runs]
}

df = pd.DataFrame(data)

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.dataframe(df, use_container_width=True, hide_index=True)

with col2:
    st.metric("Overall Status", "✅ PASS", "4/4 Layers")
    st.metric("Total Tests", sum(tests))
    st.metric("Avg Duration", f"{sum(durations)/len(durations):.1f}s")

with col3:
    pass_rate = sum(1 for s in statuses if "PASS" in s) / len(statuses) * 100
    st.metric("Pass Rate", f"{pass_rate:.0f}%")
    st.metric("Last Run", datetime.now().strftime("%Y-%m-%d"))
    st.metric("LLM Model", "Llama3")

# Chart
st.markdown("### 📈 Test Duration by Layer")
fig = px.bar(df, x="Layer", y="Duration (s)", color="Status", text="Duration (s)")
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# Recent Issues
st.markdown("### ⚠️ Recent Issues")
issues = [
    {"Layer": "Datamart", "Issue": "Sales metric variance 1.2% (threshold: 1.0%)", "Time": "2 min ago"},
    {"Layer": "Datalake", "Issue": "5.2% null emails (threshold: 5.0%)", "Time": "1 hour ago"}
]
issues_df = pd.DataFrame(issues)
st.dataframe(issues_df, use_container_width=True, hide_index=True)

# Manual Trigger
st.markdown("### ▶️ Manual Trigger")
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Run Full Validation", type="primary"):
        st.toast("▶️ Triggering AutoGen multi-agent validation...", icon="🚀")
        # Simulate run
        import time
        with st.spinner("Running validation..."):
            time.sleep(3)
        st.success("🎉 Validation completed! All layers PASSED.", icon="✅")

with col2:
    scope = st.selectbox("Scope", ["Full Pipeline", "Datalake Only", "EDW Only", "Datamart Only", "Reporting Only"])

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox("LLM Model", ["Llama3", "Mistral", "Phi-3"], index=0)
    tolerance = st.slider("Global Tolerance %", 0.1, 5.0, 1.0, 0.1)
    auto_run = st.checkbox("Auto-run on startup", value=False)
    
    st.markdown("---")
    st.write("📅 System Status")
    st.write(f"Last Sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.write(f"Agents: {len(layers)} active")