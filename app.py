import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

# Set Streamlit Page Configuration
st.set_page_config(page_title="Twitter Sentiment Analysis", layout="centered")

# Define label mappings
id2label = {0: "TROLL", 1: "NEUTRAL", 2: "POSITIVE"}
label2id = {"TROLL": 0, "NEUTRAL": 1, "POSITIVE": 2}

# Load the tokenizer and model
MODEL_PATH = "./model_save"  # Ensure this directory exists

with st.spinner("Loading model..."):
    try:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_PATH, num_labels=3, id2label=id2label, label2id=label2id
        )
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()



# Create a pipeline for easy text classification
pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer, device=-1 if device.type == "cpu" else 0)

# Streamlit UI
st.title("🐦 Twitter Sentiment Analysis with Transformers")
st.write("Enter a tweet below to analyze its sentiment.")

# User Input
tweet_text = st.text_area("Enter tweet:", "")

if st.button("Analyze Sentiment"):
    if tweet_text.strip():
        # Predict sentiment
        prediction = pipeline(tweet_text)[0]  # Get the first result
        sentiment_label = prediction['label']
        confidence = prediction['score']

        # Display results
        st.success(f"Predicted Sentiment: **{sentiment_label}** (Confidence: {confidence:.2f})")
    else:
        st.warning("⚠️ Please enter some text.")

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit and Transformers.")
