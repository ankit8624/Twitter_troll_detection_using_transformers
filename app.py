import os
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
from safetensors.torch import load_file  # Import safetensors

# Fix for torch.classes.__path__ issue
torch.classes.__path__ = []  

# Set Streamlit page configuration
st.set_page_config(page_title="Twitter Sentiment Analysis", layout="centered")

# Define label mappings
id2label = {0: "TROLL", 1: "NEUTRAL", 2: "POSITIVE"}
label2id = {"TROLL": 0, "NEUTRAL": 1, "POSITIVE": 2}

# Model path
MODEL_DIR = "./model_save"
MODEL_WEIGHTS_PATH = f"{MODEL_DIR}/model.safetensors"

st.write("Loading model...")

try:
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)

    # Load model architecture only (without weights)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR, num_labels=3, id2label=id2label, label2id=label2id)

    # Load model weights manually
    state_dict = load_file(MODEL_WEIGHTS_PATH)
    model.load_state_dict(state_dict)

    # Move model to CPU (avoid CUDA for cloud deployment)
    model.to("cpu")
    model.eval()

    # Create a text classification pipeline
    pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer, device=-1)

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
            st.success(f"Predicted Sentiment: **{sentiment_label}** ({confidence:.2f} confidence)")
        else:
            st.warning("⚠️ Please enter some text.")

except Exception as e:
    st.error(f"❌ Error loading the model: {str(e)}")

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit and Transformers.")
