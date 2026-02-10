# Indexes document

from langchain_core.documents import Document
import pandas as pd

METADATA_KEYS = {"product_id", "category", "warranty"}

def row_to_document(row: dict) -> Document:
    lines = []
    metadata = {}

    for col, value in row.items():
        if pd.isna(value):
            continue

        value_str = str(value).strip()
        if value_str == "":
            continue

        label = col.replace("_", " ").title()

        if col in METADATA_KEYS:
            metadata[col] = value_str
            continue

        if "  " in value_str or ";" in value_str:
            parts = [p.strip() for p in value_str.replace(";", " ").split() if p.strip()]
            value_str = ", ".join(parts)

        lines.append(f"{label}: {value_str}")

    return Document(
        page_content="\n".join(lines),
        metadata=metadata
    )
