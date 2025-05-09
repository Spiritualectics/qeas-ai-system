"""
QEAS Core Module
Author: Badru Michael Oluwarotimi
Model: Quantifiable Energy-Aura Scale (QEAS)
Version: 1.0
"""
from typing import Dict

PARAMETERS = {
    "emotional_state": 1.0,
    "lifestyle_risk": 1.2,
    "social_alignment": 0.8,
    "spiritual_frequency": 1.5,
    "health_behavior": 1.3,
    "dominant_archetype": 1.0,
}

def calculate_qeas_score(input_scores: Dict[str, float]) -> float:
    total_score = 0
    total_weight = 0
    for param, value in input_scores.items():
        if param in PARAMETERS:
            weight = PARAMETERS[param]
            total_score += value * weight
            total_weight += weight
    return round(total_score / total_weight, 2) if total_weight != 0 else 0.0