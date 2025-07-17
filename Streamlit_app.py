import streamlit as st
import openai

st.set_page_config(page_title="JamesChatGPT", page_icon="🤖")
st.title("🧠 Welcome to JamesChatGPT")
st.write("Ask anything — I’m ready to help!")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are JamesChatGPT, a helpful assistant built by James Vasanth."}]

user_input = st.text_input("Your Question:", placeholder="Type your question here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            reply = f"Error: {e}"
            st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages[1:]:
    role = "You" if msg["role"] == "user" else "JamesChatGPT"
    st.markdown(f"**{role}:** {msg['content']}")
