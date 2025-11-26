import pandas as pd
import re

def clean_merchant(name: str) -> str:
    if not isinstance(name, str):
        return "unknown"
    name = name.lower()
    name = re.sub(r"\d+", "", name)
    name = re.sub(r"[^a-z ]", "", name)
    name = re.sub(r"\s+", " ", name)
    return name.strip()

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.lower().strip() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    df["amount"] = df["amount"].astype(float).abs()
    df["merchant"] = df["description"].apply(clean_merchant)
    return df