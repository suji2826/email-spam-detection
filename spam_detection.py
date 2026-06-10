import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("spam.csv")
print("=== DATASET LOADED SUCCESSFULLY ===")
print(data)
print("\nTotal Emails:", len(data))
X = data["text"]
y = data["label"]
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\n=== MODEL PERFORMANCE ===")
print("Accuracy:", round(accuracy, 2))
all_predictions = model.predict(X_vectorized)
data["Predicted"] = all_predictions
print("\n=== ACTUAL VS PREDICTED ===")
print(data[["label", "Predicted"]])
print("\n=== EMAIL CLASSIFICATION RESULTS ===")
for i in range(len(data)):
    print(f"\nEmail {i+1}:")
    print("Text      :", data.loc[i, "text"])
    print("Actual    :", data.loc[i, "label"])
    print("Predicted :", data.loc[i, "Predicted"])
    print("-" * 50)