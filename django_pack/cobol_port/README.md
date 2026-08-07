# `cobol_port` — Django Migration Pack

**CobolIQ v0.8.2** — auto-generated from COBOL portfolio.

- **21 programs**, 232 total paragraphs
- **736 models** from 01-level data items, **0 helper structures**
- **699 return-code sites**, **13 state machines**
- **7 resolved copybooks**

## Generated Files

| File | Purpose |
|------|--------|
| `models_candidates.py` | Django models from LINKAGE/WS/copybooks |
| `admin_candidates.py` | Django Admin registration |
| `urls_candidates.py` | URL routing from CICS TRANSID / entry points |
| `views_candidates.py` | REST API stubs |
| `services_candidates.py` | Paragraph logic stubs (portable) |
| `settings_candidates.py` | Extracted WORKING-STORAGE constants |
| `tables.json` | Embedded copybook data tables |

## Next Steps

1. Review `models_candidates.py` — verify model mapping
2. Fill in `services_candidates.py` — port COBOL paragraphs
3. Run `python manage.py makemigrations`
4. Build tests from return-code catalog

---
*CobolIQ — AI-ready intelligence for your COBOL portfolio.*
