from fastapi import FastAPI
from pydantic import BaseModel

from app.feature_engineering import hashed_feature


app = FastAPI()


class PredictRequest(BaseModel):
    user_id: str
    num_buckets: int = 1000


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(req: PredictRequest):
    bucket = hashed_feature(req.user_id, req.num_buckets)
    return {"bucket": bucket}
