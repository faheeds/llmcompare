import streamlit as st
import openai
# Import other necessary libraries for Anthropic Claude and Falcon

# Retrieve API Keys from secrets.toml
OPENAI_API_KEY = st.secrets["openai_key"]
# ANTHROPIC_CLAUDE_API_KEY = st.secrets["claude_key"]
# FALCON_API_KEY = st.secrets["falcon_key"]

openai.api_key = OPENAI_API_KEY

def query_openai(question):
    response = openai.Completion.create(
      engine="davinci",
      prompt=question,
      max_tokens=150
    )
    return response.choices[0].text.strip()

def query_anthropic_claude(question):
    # Implement the actual API call for Anthropic Claude using ANTHROPIC_CLAUDE_API_KEY
    # For now, returning a placeholder
    return "Claude's response to: " + question

def query_falcon(question):
    # Implement the actual API call for Falcon using FALCON_API_KEY
    # For now, returning a placeholder
    return "Falcon's response to: " + question

def main():
    st.title("Question Answering using Multiple APIs")
    question = st.text_input("Enter your question:")

    if st.button("Query APIs"):
        with st.spinner("Fetching responses..."):
            openai_response = query_openai(question)
            claude_response = query_anthropic_claude(question)
            falcon_response = query_falcon(question)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**OpenAI's Response**")
            st.write(openai_response)

        with col2:
            st.markdown("**Anthropic Claude's Response**")
            st.write(claude_response)

        with col3:
            st.markdown("**Falcon's Response**")
            st.write(falcon_response)

if __name__ == "__main__":
    main()
