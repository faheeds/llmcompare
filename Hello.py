import streamlit as st
import openai

# Initialize the OpenAI API key
# Replace 'YOUR_OPENAI_API_KEY' with your actual API key.
openai.api_key = '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'

def generate_response(prompt, model="gpt-3.5-turbo"):
    """Generate a response from OpenAI based on the given prompt and model."""
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150  # Limit to 150 tokens for this example
    )
    return response.choices[0].text.strip()

def main():
    st.title("LLM Response Comparison")

    # Add prompt
    prompt = st.text_input("Enter your prompt:")

    # Choose models for comparison
    models = st.multiselect("Select models for comparison", ["gpt-3.0-turbo", "gpt-3.5-turbo", "gpt-4.0-turbo", "anthropic", "falcon", "stability"])

    # Generate and display results
    if st.button("Generate"):
        for model in models:
            if model in ["gpt-3.0-turbo", "gpt-3.5-turbo", "gpt-4.0-turbo"]:
                # This assumes the OpenAI API can handle these model names (this is just for illustration)
                response = generate_response(prompt, model)
                st.write(f"{model} Response:")
                st.write(response)
            # Add conditions for other LLMs (like Anthropic, Falcon, etc.) here
            # For example:
            # elif model == "anthropic":
            #     response = generate_response_from_anthropic(prompt)
            #     st.write(f"{model} Response:")
            #     st.write(response)
            else:
                st.write(f"API for {model} not integrated yet.")

if __name__ == "__main__":
    main()
