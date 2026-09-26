from __future__ import annotations
import re
from .catalog import CATALOG

def normalize_code(code:str)->str:
    m=re.search(r"(?:ORA[- ]?)?(\d{1,5})",code,re.I)
    if not m: raise ValueError(f"Not an ORA error code: {code}")
    return f"ORA-{int(m.group(1)):05d}"

def lookup(code:str):
    return CATALOG.get(normalize_code(code))

def search(text:str):
    q=text.lower()
    out=[]
    for code,item in CATALOG.items():
        hay=" ".join([code,item["title"],item["meaning"],*item["causes"],*item["checks"]]).lower()
        if q in hay: out.append((code,item))
    return out
