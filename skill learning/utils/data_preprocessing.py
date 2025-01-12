# skill_learning/utils/data_preprocessing.py

import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Download stopwords if not already done
nltk.download('stopwords')

def clean_text(text):
    """
    Cleans input text by removing special characters, stopwords, and converting to lowercase.
    
    Args:
        text (str): The input text to be cleaned.
        
    Returns:
        str: The cleaned text.
    """
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text

def tokenize_and_vectorize(texts):
    """
    Tokenizes and vectorizes input texts using TF-IDF.
    
    Args:
        texts (list): A list of cleaned texts.
        
    Returns:
        sparse matrix: TF-IDF vectorized representation of input texts.
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    return vectors, vectorizer
