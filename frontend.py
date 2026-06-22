from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="AI Chatbot Agents", layout="wide")

# --- Session state init ---
if "history" not in st.session_state:
    st.session_state.history = []
if "selected_index" not in st.session_state:
    st.session_state.selected_index = None
if "current_response" not in st.session_state:
    st.session_state.current_response = None

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("## 🕘 History")

    if not st.session_state.history:
        st.caption("No queries yet. Ask something!")
    else:
        if st.button("🗑 Clear all", use_container_width=True):
            st.session_state.history = []
            st.session_state.selected_index = None
            st.session_state.current_response = None
            st.rerun()

        st.divider()

        for i, item in enumerate(reversed(st.session_state.history)):
            real_idx = len(st.session_state.history) - 1 - i
            icon = "🌐" if item["allow_search"] else "💬"
            short = item["query"][:40] + ("..." if len(item["query"]) > 40 else "")
            is_active = st.session_state.selected_index == real_idx

            label = f"{icon} {short}"
            if st.button(label, key=f"hist_{real_idx}", use_container_width=True,
                         type="primary" if is_active else "secondary"):
                st.session_state.selected_index = real_idx
                st.session_state.current_response = None
                st.rerun()

            st.caption(f"  {item['model']} · {item['time']}")

# ===== MAIN PANEL =====
st.title("🤖 AI Chatbot Agents")
st.caption("Configure your agent and ask anything")

# Show selected history item
if st.session_state.selected_index is not None:
    item = st.session_state.history[st.session_state.selected_index]

    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button("✕ Close"):
            st.session_state.selected_index = None
            st.rerun()

    with st.container(border=True):
        st.markdown(f"**Query:** {item['query']}")
        st.caption(f"{item['model']} · {item['provider']} · {'🌐 Web search' if item['allow_search'] else '💬 No search'} · {item['time']}")

    with st.container(border=True):
        st.markdown("#### 🤖 Agent Response")
        st.markdown(item["response"])

    st.divider()

# Always show the input form below
with st.container(border=True):
    system_prompt = st.text_area("🧠 Agent personality", height=60,
        placeholder="e.g. Act as a smart and friendly AI assistant...",
        key="system_prompt_input")

with st.container(border=True):
    provider = st.radio("Provider", ("Groq", "OpenAI"), horizontal=True)
    if provider == "Groq":
        selected_model = st.selectbox("Model", ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"])
    else:
        selected_model = st.selectbox("Model", ["gpt-4o-mini"])
    allow_web_search = st.toggle("🌐 Allow web search")

with st.container(border=True):
    user_query = st.text_area("💬 Your query", height=100,
        placeholder="Ask anything...",
        key="user_query_input")

if st.button("Ask Agent ✦", use_container_width=True, type="primary"):
    if not user_query.strip():
        st.warning("Please enter a query first.")
    else:
        with st.spinner("Agent is thinking..."):
            try:
                payload = {
                    "model_name": selected_model,
                    "model_provider": provider,
                    "system_prompt": system_prompt or "Act as a smart and friendly AI assistant",
                    "messages": [user_query],
                    "allow_search": allow_web_search
                }
                res = requests.post("http://127.0.0.1:9999/chat", json=payload)

                if res.status_code == 200:
                    data = res.json()
                    if "error" in data:
                        st.error(data["error"])
                    else:
                        # Save to history
                        st.session_state.history.append({
                            "query": user_query,
                            "response": data["response"],
                            "model": selected_model,
                            "provider": provider,
                            "allow_search": allow_web_search,
                            "time": datetime.now().strftime("%I:%M %p")
                        })
                        st.session_state.selected_index = None
                        st.session_state.current_response = data["response"]
                        st.rerun()
                else:
                    st.error(f"Server error: {res.status_code}")
            except Exception:
                st.error("Could not connect to backend. Make sure the server is running on port 9999.")

# Show latest response
if st.session_state.current_response:
    st.success("Response received!")
    with st.container(border=True):
        st.markdown("#### 🤖 Agent Response")
        st.markdown(st.session_state.current_response)