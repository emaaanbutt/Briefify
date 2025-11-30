import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# CSS
st.markdown("""
    <style>
    body {
        background-color: #ffe6f2;
    }
    .stTextArea>div>div>textarea {
        background-color: #fff0f5;
        color: #330033;
    }
    .stButton>button {
        background-color: #ff66b3;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff3399;
        color: white;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #990066;
    }
    </style>
    """, unsafe_allow_html=True)

model_path = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)

st.title("Briefify")

text = st.text_area("Enter text to summarize")

if st.button("Summarize"):
    if text.strip() != "":
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt")
        summary_ids = model.generate(
            inputs,
            max_length=100,
            min_length=20,
            num_beams=4,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        st.subheader("Summary:")
        st.write(summary)
    else:
         st.warning("Please enter some text to summarize!")

