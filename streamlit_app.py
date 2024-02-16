import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with API key
client = OpenAI(api_key="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")

# Function to generate response
def generate_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional skilled in explaining complex concepts in simple way"},
            {"role": "user", "content": prompt}
        ]
    )
    generated_content = completion.choices[0].message.content
    return generated_content

# Streamlit UI
def main():
    st.set_page_config(page_title="Dattu's GPT", page_icon="🧠")
    st.title("Dattu's AI-3.5 Turbo Response Generator")

    # # Add background image
    # st.markdown(
    #     """
    #     <style>
    #         body {
    #             background-image: url('c:\Users\DATTAT~1\AppData\Local\Temp\cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA2L3JtMzc4LTA4LXguanBn.webp');
    #             background-size: cover;
    #         }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    
    # Add instructions to the sidebar with different style and font
    st.sidebar.title("Instructions:")
    # st.markdown("---")
    st.sidebar.markdown(
        """
        This is a GPT-3.5 Turbo response generator by Dattu.
        
        1. Enter your prompt in the text area on the right.
        2. Click the 'Generate Response' button to generate a response.
        3. The generated response will appear below the text area.
        4. You can exit the application by typing 'exit' in the prompt.
        """
    )

    prompt = st.text_input("Enter the prompt ('exit' to quit):")
    
    if prompt.lower() == 'exit':
        st.write("Exiting...")
    elif st.button("Generate Response"):
        with st.spinner("Generating..."):
            response = generate_response(prompt)
        st.write("Generated Content:", response)
    
     # Add icons to the footer
    # st.markdown("---")
    # st.markdown(
    #     """
    #     <p style='text-align:center'>
    #         Powered by <a href="https://openai.com">OpenAI</a> &#x2022; Icons by <a href="https://fontawesome.com">Font Awesome</a>
    #     </p>
    #     """,
    #     unsafe_allow_html=True
    # )
        
    # Add footer
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: grey;
                padding: 8px 0;
                text-align: center;
                text-size:30px;
            }
        </style>
        <div class="footer">
            <p  style="color:white";>Powered by OpenAI • Icons by Font Awesome</p>
        </div>
        """,
        unsafe_allow_html=True
    )
if __name__ == "__main__":
    main()
