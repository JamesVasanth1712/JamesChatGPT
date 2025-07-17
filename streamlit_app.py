import streamlit as st
import openai

st.set_page_config(page_title="JamesChatGPT")

st.title(" Welcome to JamesChatGPT")
st.write("Ask anything — I’m here to help you!")

# Input your OpenAI API key below
openai.api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are JamesGPT, a helpful assistant built by James Vasanth."}
    ]

# User prompt
prompt = st.text_input("You:", placeholder="Type your question here and hit Enter")

# When user enters input
if prompt and openai.api_key:
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.success("JamesGPT: " + reply)

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Display chat history
st.subheader("Chat History")
for msg in st.session_state.messages[1:]:  # Skip system message
    role = "You" if msg["role"] == "user" else "JamesGPT"
    st.markdown(f"**{role}:** {msg['content']}")
