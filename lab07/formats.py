import json

def csv_to_record(text: str) -> list[dict]:
    if not text or not text.strip():
        return []
    
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    if len(lines) < 2:
        return []
    
    head = [h.strip() for h in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        val = [v.strip() for v in line.split(",")]
        rec = {head[i]: val[i] for i in range(min(len(head), len(val)))}
        records.append(rec)

    return records
