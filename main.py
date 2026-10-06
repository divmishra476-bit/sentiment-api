from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from database import SessionLocal, Prediction, Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
classifier = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Hello bhai!"}

@app.post("/predict")
def predict(data: TextInput):
    result = classifier(data.text)[0]

    db = SessionLocal()
    row = Prediction(
        text=data.text,
        label=result["label"],
        confidence=result["score"],
    )
    db.add(row)
    db.commit()
    db.close()

    return {
        "you_sent": data.text,
        "sentiment": result["label"],
        "confidence": result["score"],
    }

@app.get("/history")
def history():
    db = SessionLocal()
    rows = db.query(Prediction).all()
    db.close()
    return [
        {"id": r.id, "text": r.text, "label": r.label, "confidence": r.confidence}
        for r in rows
    ]