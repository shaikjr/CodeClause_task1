import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

messages = [
    ("Congratulations, you've won a free iPhone!", "spam"),
    ("Hi, how are you? Let's meet tomorrow.", "ham"),
    ("URGENT: Your account needs verification.", "spam"),
    ("Can you please send me the report?", "ham"),
    ("hello, heres your pincode fo shopping offer","spam")
]

X = [message[0] for message in messages]
y = [message[1] for message in messages]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

classifier = MultinomialNB()
classifier.fit(X_train_tfidf, y_train)

y_pred = classifier.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_rep)
