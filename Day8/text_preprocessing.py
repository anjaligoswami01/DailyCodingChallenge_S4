# text_preprocessing.py

import pandas as pd
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample dataset
data = {
    "Text": [
        "AI is transforming the world!",
        "Natural Language Processing helps machines understand text.",
        "Machine Learning models require clean data.",
        "Text preprocessing improves NLP performance."
    ]
}

df = pd.DataFrame(data)

# Initialize NLP tools
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Text preprocessing function
def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    stemmed = [stemmer.stem(word) for word in tokens]

    # Lemmatization
    lemmatized = [lemmatizer.lemmatize(word) for word in stemmed]

    return " ".join(lemmatized)

# Apply preprocessing
df["Processed_Text"] = df["Text"].apply(preprocess_text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Processed_Text"])

# Display results
print("Original Text:\n")
print(df["Text"])

print("\nProcessed Text:\n")
print(df["Processed_Text"])

print("\nTF-IDF Feature Names:\n")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:\n")
print(tfidf_matrix.toarray())