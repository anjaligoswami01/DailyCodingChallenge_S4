import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("news.csv")

# Features and labels
X = df["headline"]
y = df["category"]

# Convert text into numbers
vectorizer = CountVectorizer()
X_vectors = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_vectors,
    y,
    test_size=0.25,
    random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Test custom headline
sample = ["New cricket tournament announced"]

sample_vector = vectorizer.transform(sample)

prediction = model.predict(sample_vector)

print("Predicted Category:", prediction[0])
