from fastapi import FastAPI # type: ignore
import pickle
import pandas as pd # type: ignore

app = FastAPI()

# charger modèle KNN (Surprise)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# charger dataset
df = pd.read_csv("df_final.csv")

def recommend_for_user(user_id, df, model, top_n=5):
    items = df['item_id'].unique()
    predictions = []

    for item in items:
        pred = model.predict(user_id, item)
        predictions.append((item, pred.est))

    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:top_n]

@app.get("/")
def home():
    return {"message": "API de recommandation étudiants"}

@app.get("/recommend")
def recommend(user_id: int):
    recs = recommend_for_user(user_id, df, model)
    return {
        "user_id": user_id,
        "recommendations": recs
    }