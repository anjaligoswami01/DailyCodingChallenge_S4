# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# # Step 2: Create dataset (simple movie reviews)
# data = {
#     "review": [
#         "This movie was amazing",
#         "I loved the acting",
#         "Fantastic storyline and great visuals",
#         "Absolutely terrible movie",
#         "Worst film ever",
#         "I hated this movie",
#         "It was okay, not great",
#         "Pretty decent watch",
#         "Excellent direction and cast",
#         "Bad script and poor acting"
#     ],
#     "sentiment": [
#         "positive", "positive", "positive",
#         "negative", "negative", "negative",
#         "neutral", "neutral",
#         "positive", "negative"
#     ]
# }

# df = pd.DataFrame(data)

# # Step 3: Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     df["review"], df["sentiment"], test_size=0.2, random_state=42
# )

# # Step 4: Convert text to vectors
# vectorizer = CountVectorizer()
# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# # Step 5: Train model
# model = MultinomialNB()
# model.fit(X_train_vec, y_train)

# # Step 6: Evaluate model
# y_pred = model.predict(X_test_vec)

# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))

# # Step 7: Test on new inputs
# test_reviews = [
#     "I really loved this movie",
#     "This was the worst experience",
#     "It was just okay",
#     "Amazing visuals and story",
#     "Not good, very boring"
# ]

# test_vec = vectorizer.transform(test_reviews)
# predictions = model.predict(test_vec)

# print("\nManual Test Predictions:")
# for review, pred in zip(test_reviews, predictions):
#     print(f"{review} --> {pred}")