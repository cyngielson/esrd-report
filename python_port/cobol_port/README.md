# `cobol_port` - Python port skeleton

Auto-generated from COBOL program `ESCAL056` (ESCAL056).

## Contents

| File | What |
|---|---|
| `enums.py` | 0 state-machine Enums (88-level) |
| `return_codes.py` | 9 RC assignment specs + constants |
| `tables.json` | 0 embedded data tables (bit-perfect) |
| `tables.py` | Lazy loader + lookup helpers |
| `io_contract.py` | LINKAGE SECTION dataclasses |
| `paragraphs.py` | 8 paragraph stubs (NotImplementedError bodies) |
| `pricer_engine.py` | Orchestrator entry point |
| `tests/test_smoke.py` | Import + table-load + RC-count tests |

## Data tables (bit-perfect from COBOL VALUE literals)

| Table | Rows | Row width | Columns |
|---|---|---|---|

## How to fill in paragraph bodies

1. Open the original COBOL source ({line range printed in each stub}).
2. Translate statements 1:1 using `tables`, `enums`, and `return_codes`.
3. Run `pytest tests/` to verify nothing imports broken.
4. Add scenario tests reproducing CMS test claims.

## What this port preserves vs. drops

**Preserved (high confidence):**
- Control flow structure (paragraph call graph)
- All return-code assignments with their IF conditions
- All 88-level state flags as type-safe Enums
- All embedded data tables, byte-perfect
- LINKAGE I/O contract

**NOT preserved (requires manual port):**
- Arithmetic expressions inside `COMPUTE` / `MOVE` statements
- `SEARCH ... AT END ... WHEN` branch bodies
- `EVALUATE ... WHEN` branch bodies
- File I/O (none expected for a pure pricer routine)
