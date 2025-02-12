import streamlit as st
import torch
import pickle
from transformers import AutoModelForSequenceClassification, TextClassificationPipeline

# Set Streamlit page configuration
st.set_page_config(page_title="Twitter Sentiment Analysis", layout="centered")

# Define label mappings
id2label = {0: "TROLL", 1: "NEUTRAL", 2: "POSITIVE"}
label2id = {"TROLL": 0, "NEUTRAL": 1, "POSITIVE": 2}

# Load tokenizer from tokenizer.pkl
st.write("Loading tokenizer...")
with open("tokenizer.pkl", "rb") as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# Load model from model.pkl
st.write("Loading model...")
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Ensure model is in evaluation mode
model.eval()

# Create a text classification pipeline
pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer, device=-1)  # No GPU

# Streamlit UI
st.title("🐦 Twitter Sentiment Analysis with Transformers")
st.write("Enter a tweet below to analyze its sentiment.")

# User Input
tweet_text = st.text_area("Enter tweet:", "")

if st.button("Analyze Sentiment"):
    if tweet_text.strip():
        # Predict sentiment
        prediction = pipeline(tweet_text)[0]  # Get the first result
        label_index = int(prediction['label'].split("_")[-1])  # Extract numeric part
        sentiment_label = id2label[label_index]  # Convert to human-readable label
        confidence = prediction['score']

        # Display results
        st.success(f"Predicted Sentiment: **{sentiment_label}** (Confidence: {confidence:.2f})")
    else:
        st.warning("⚠️ Please enter some text.")


# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit and Transformers.")
