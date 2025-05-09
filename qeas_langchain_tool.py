"""
QEAS LangChain Tool
Author: Badru Michael Oluwarotimi
"""
from langchain.tools import tool
from typing import Dict
from qeas_core import calculate_qeas_score

@tool
def qeas_tool(input_scores: Dict[str, float]) -> str:
    score = calculate_qeas_score(input_scores)
    if score >= 2.5:
        interpretation = "High Vibrational Alignment"
    elif 1.5 <= score < 2.5:
        interpretation = "Moderate Alignment – At risk of vibrational dissonance"
    else:
        interpretation = "Low Alignment – Possible terminal energy pattern"
    return f"QEAS Score: {score} – {interpretation}"