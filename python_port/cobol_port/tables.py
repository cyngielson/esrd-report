"""
Embedded data tables loader.
Loads tables.json (bit-perfect copy of COBOL VALUE literals) into Python
dicts/lists. Decimal values are preserved as strings to avoid float precision
bugs - convert to Decimal in caller if arithmetic is needed.
"""

import json
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict, List

_DATA_PATH = Path(__file__).with_name("tables.json")


def _load() -> Dict[str, Any]:
    raw = json.loads(_DATA_PATH.read_text(encoding="utf-8"))
    out: Dict[str, Any] = {}
    for t in raw:
        rows: List[Dict[str, Any]] = []
        for r in t["rows"]:
            rows.append(r["values"])
        out[t["name"]] = {
            "columns": t["columns"],
            "rows": rows,
            "declared_rows": t["declared_rows"],
            "row_width": t["row_width"],
            "source_file": t["source_file"],
        }
    return out


TABLES: Dict[str, Any] = _load()

# Helper: convert decimal-column string to Decimal (preserves precision).
def as_decimal(v: Any) -> Decimal:
    if isinstance(v, str):
        return Decimal(v)
    return Decimal(str(v))

# Helper: lookup row(s) by predicate over columns.
def lookup(table_name: str, **eq) -> List[Dict[str, Any]]:
    t = TABLES.get(table_name)
    if not t:
        return []
    out = []
    for r in t["rows"]:
        if all(str(r.get(k)) == str(v) for k, v in eq.items()):
            out.append(r)
    return out

# Per-table convenience accessors
