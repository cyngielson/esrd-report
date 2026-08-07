# Technical Review Guide

## Review Order

| # | File | Purpose |
|---|------|--------|
| 1 | `../02-code-mechanics-map.md` | Execution flow |
| 2 | `../03-modernization-readiness.md` | Modernization risk |
| 3 | `../evidence/full-report_01.md` | Project summary, graphs, issues |
| 3b | `../evidence/full-report_02..N.md` | Per-program detail (5 per file) |
| 4 | `../evidence/rules.ini` | Hardcoded values |
| 5 | `../evidence/states.md` | State machine flags |
| 6 | `../evidence/schemas.sql` | Data structures |
| 7 | `../starters/return-codes.py` | RC catalog |

## Key Points
- CRITICAL risk = manual review before porting
- Deep execution chains (>5 levels) = high migration risk
- PERFORM THRU edges may hide implicit control flow
- Every RC assignment site is a golden-output test candidate

---
*CobolIQ - Legacy COBOL Diagnostics*
