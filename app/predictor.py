import pickle

# load model + vectorizer
with open("model/model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)


def predict_text(text):
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0].max()

    result = "Fake" if pred == 1 else "Real"
    return result, float(prob)


FAKE_KEYWORDS = ["sốc", "giật gân", "chưa kiểm chứng"]

def extract_keywords(text):
    text = text.lower()
    return [kw for kw in FAKE_KEYWORDS if kw in text]