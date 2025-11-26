import pandas as pd

def detect_recurring(df: pd.DataFrame) -> pd.DataFrame:
    results = []
    for merchant, group in df.groupby("merchant"):
        if len(group) < 2:
            continue
        group = group.sort_values("date")
        date_diffs = group["date"].diff().dt.days.dropna()
        if len(date_diffs) == 0:
            continue
        avg_gap = date_diffs.mean()
        is_monthly = 28 <= avg_gap <= 32
        if not is_monthly:
            continue
        avg_amount = group["amount"].mean()
        annual_cost = avg_amount * 12
        results.append({
            "merchant": merchant,
            "avg_amount": round(avg_amount, 2),
            "annual_cost": round(annual_cost, 2),
            "transactions": len(group), })
    return pd.DataFrame(results)