"""
QEAS API Server with CORS
Author: Badru Michael Oluwarotimi
"""
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from qeas_core import calculate_qeas_score

app = FastAPI(title="QEAS API", description="Quantifiable Energy-Aura Scale API with CORS and Key Protection")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for now; can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VALID_API_KEY = "spiritualectics2025"

class QEASInput(BaseModel):
    emotional_state: float
    lifestyle_risk: float
    social_alignment: float
    spiritual_frequency: float
    health_behavior: float
    dominant_archetype: float

@app.post("/qeas/score")
def compute_qeas_score(data: QEASInput, x_api_key: Optional[str] = Header(None)):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    input_dict = data.dict()
    score = calculate_qeas_score(input_dict)
    return {
        "author": "Badru Michael Oluwarotimi",
        "qeas_score": score,
        "input": input_dict,
        "signature": "QEAS Original Model | © 2025 Badru Michael Oluwarotimi"
    }