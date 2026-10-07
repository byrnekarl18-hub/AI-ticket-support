import joblib

cat_model = joblib.load("cat_model.pkl")
cat_vector = joblib.load("cat_vectorizer.pkl")

def predict_category(query):
    category_prediction = cat_vector.transform([query])
    return cat_model.predict(category_prediction)[0]

query = "every time i log into the website it crashes"

print(predict_category(query))