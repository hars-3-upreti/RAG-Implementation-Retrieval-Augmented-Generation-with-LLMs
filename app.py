import streamlit as st
import requests

st.title("Document Query with Ollama")
st.write("Ask a question to query the document.")

# Input field for question
question = st.text_input("Question")

# Button to process input
if st.button('Ask Question'):
    # Call your API endpoint here
    api_endpoint = "https://9f03-34-16-178-63.ngrok-free.app/split/?str="
      # Adjust payload as per your API requirements
    api_endpoint_final = api_endpoint+question
    response = requests.get(api_endpoint_final)

    if response.status_code == 200:
        answer = response.json()
        st.text_area("Answer", value=answer['string'], height=300, disabled=True)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
