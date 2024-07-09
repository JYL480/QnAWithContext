import streamlit as st
from model import Predict

st.header("BERT Question Answering with Context Model:")

# Initialize session state variables
if 'question' not in st.session_state:
    st.session_state.question = ""
if 'context' not in st.session_state:
    st.session_state.context = ""
if 'answer' not in st.session_state:
    st.session_state.answer = ""
if 'time_taken' not in st.session_state:
    st.session_state.time_taken = 0.0

# Define a function to update the session state with example texts
def load_example():
    st.session_state.question = "Who is the father of Python?"
    st.session_state.context = "Python is a high-level programming language. It was created by Guido van Rossum and first released in 1991."

# Define a function to perform the prediction
def on_predict():
    if st.session_state.question and st.session_state.context:
        answer, time_taken = Predict(st.session_state.question, st.session_state.context)
        st.session_state.answer = answer
        st.session_state.time_taken = time_taken

# Inputs for question and context
st.text_input("Enter your question:", value=st.session_state.question, key="question")
st.text_area("Enter your context:", value=st.session_state.context, key="context")

# Button to load example texts
st.button("Load Example", on_click=load_example)

# Button to perform prediction
st.button("Predict", on_click=on_predict)

# Display the results if available
st.divider()
st.subheader("Predicted Answer:")
if st.session_state.answer:
    st.write(st.session_state.answer)
    st.write(f"Time taken: {st.session_state.time_taken} seconds")
