import hashlib
import os
import re
import pandas as pd 
from dotenv import load_dotenv
load_dotenv()

def normalize_phone(value):
    """
    Normalize phone numbers to a standard format.
    """
    if pd.isna(value): return None
    digits = re.sub(r"\D","",str(value))
    if len(digits) == 10 or (len(digits) == 11 and digits.startswith('1')):
        return digits[-10:]
    else: 
        return None

def make_id(value, salt = None):
    """
    Create a unique ID for a given value using SHA-256 hashing.
    """
    if value is None:
        return None
    salt = salt or os.environ["ANON_SALT"]
    return hashlib.sha256((salt + str(value)).encode()).hexdigest()[:10]

def anonymize(df, id_source = "phone", drop_cols = ("name", "phone", "email", "notes")):
    """
    Anonymize a DataFrame by creating unique IDs and dropping sensitive columns.
    """
    df = df.copy()
    df[id_source] = df[id_source].apply(normalize_phone)
    df["id"] = df[id_source].apply(make_id)
    return df.drop(columns=[c for c in drop_cols if c in df.columns])
