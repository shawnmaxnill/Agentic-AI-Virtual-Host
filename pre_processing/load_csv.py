# mini script to load in documents

import pandas as pd

def load_products(path: str):
    df = pd.read_excel(path)
    return df.to_dict(orient="records")
