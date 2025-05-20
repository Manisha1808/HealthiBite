# train_model.py
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample prompts for each category
data = {
    "fatigue": [
        "I feel very tired", "I'm always exhausted", "low energy lately", "feeling drained"
    ],
    "digestion": [
        "I have stomach pain", "bloating and gas", "digestion problem", "acid reflux"
    ],
    "headache": [
        "constant headache", "pain in my head", "feeling pressure in head", "migraine"
    ],
    "insomnia": [
        "I can't sleep", "trouble sleeping", "restless nights", "not able to fall asleep"
    ],
    "weight_loss": [
        "I want to lose weight", "belly fat", "overweight", "reduce my weight"
    ],
    "stress": [
        "I'm feeling very stressed", "I have anxiety", "feeling overwhelmed", "too much on my plate"
    ],
    "diet_issues": [
        "I eat too much sugar", "too salty food", "my diet isn't healthy", "I need to eat better"
    ],
    "hydration": [
        "I'm not drinking enough water", "feeling dehydrated", "too little water intake", "I need more water"
    ]
}

# Prepare training data
X, y = [], []
for intent, examples in data.items():
    X.extend(examples)
    y.extend([intent] * len(examples))

# Convert text to vectors
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train classifier
clf = LogisticRegression()
clf.fit(X_vec, y)

# Save model and vectorizer
with open('model/intent_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ NLP model trained and saved.")
