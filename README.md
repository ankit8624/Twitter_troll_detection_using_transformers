
# 🐦 Twitter Troll Detection using DeBERTa  
*A deep learning-based system to classify tweets as troll or not.*

## 🚀 Live Demo  
🔗 **Try the app here:** [Your Deployment Link](https://twitter-troll-detection.streamlit.app/)  

## 📌 Project Overview  
- This project uses **DeBERTa** (Deep Bidirectional Encoder Representations from Transformers) to classify tweets into three categories.  
- It includes a **Streamlit web app** for easy user interaction.  

## 🛠️ Features  
✅ Multi-class troll detection (3 categories)  
✅ Built using **Deep Learning** and **NLP**  
✅ Interactive **Streamlit web app**  
✅ Pre-trained **DeBERTa model**  


## 📦 Installation  
### 1️⃣ Clone the repository  
```bash
git clone https://github.com/ankit8624/Twitter_troll_detection_using_transformers.git
cd Twitter_troll_detection_using_transformers
```
### 2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
``` 
### 3️⃣ Run the Streamlit app  
```bash
streamlit run app.py
```

## 📊 Model Performance  
### 📜 Classification Report  
| Class | Precision | Recall | F1-Score | Support |
|-------|----------|--------|----------|---------|
| **0** | 0.95     | 0.88   | 0.91     | 3000    |
| **1** | 0.74     | 0.90   | 0.81     | 1000    |
| **2** | 0.79     | 0.80   | 0.79     | 1000    |
| **Accuracy** | **-** | **-** | **0.86** | **5000** |
| **Macro Avg** | 0.82 | 0.86 | 0.84 | 5000 |
| **Weighted Avg** | 0.87 | 0.86 | 0.87 | 5000 |

### 🔍 Confusion Matrix  
![Confusion Matrix](image.png)  

## 🗂 Dataset  
- **Source**: [Twitter and Reddit Sentimental Analysis Dataset](https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset)  
- **Description**: This dataset contains tweets and Reddit posts labeled for sentiment analysis.  
- **Usage**: Used for training and testing a troll detection model.  

## 🔄 Data Preprocessing  
- **Text Cleaning**: Removed special characters, links, hashtags, and mentions.  
- **Lowercasing**: Converted text to lowercase for uniformity.  
- **Stopword Removal**: Removed common words (e.g., "the", "is") using NLTK.  
- **Tokenization**: Split text into individual words using SpaCy.  
- **Lemmatization**: Converted words to their root form.  
- **Padding & Truncation**: Standardized tweet lengths for model input.  

## 🧠 Model Details  
- **Model**: DeBERTa (Deep Bidirectional Encoder Representations from Transformers)  
- **Training**: Fine-tuned on labeled dataset  
- **Performance**: **86% accuracy**  

## 🤝 Contribution  
Want to improve this project? Feel free to fork and submit a pull request!  

## 📬 Contact  
For any queries, reach out to me at:  
📧 **ankit.desale@example.com**  
📌 [GitHub Profile](https://github.com/your-username)  
