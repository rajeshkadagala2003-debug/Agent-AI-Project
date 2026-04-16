import streamlit as st
from main import run_agent, send_to_whatsapp
 
st.set_page_config(page_title="Agentic AI", page_icon="🤖")
 
st.title("🤖 Agentic AI Assistant")
 
if "messages" not in st.session_state:
    st.session_state.messages = []
 
for msg in st.session_state.messages:
 
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
 
query = st.chat_input("Ask anything...")
 
if query:
 
    st.session_state.messages.append({"role": "user", "content": query})
 
    with st.chat_message("user"):
        st.markdown(query)
 
    response = run_agent(query)
 
    with st.chat_message("assistant"):
 
        st.markdown(response)
 
        if st.button("Send to WhatsApp"):
            result = send_to_whatsapp(response)
            st.success(result)
 
    st.session_state.messages.append({"role": "assistant", "content": response})