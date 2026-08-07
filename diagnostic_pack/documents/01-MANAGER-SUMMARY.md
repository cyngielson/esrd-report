# Manager Summary

## What We Found

This system should be treated as business logic infrastructure, not only source code.
This COBOL system is a payment decision engine:
- 232 execution units, 21 program(s)
- 699 return-code assignment sites
- 2224 hardcoded values in source
- 60 critical hotspots - too complex to auto-port
- 38 non-structured jumps (GO TO)

## Core Recommendation

**Do not start with automated rewrite.**
1. Evidence review
2. Golden-output tests
3. Config extraction
4. Hotspot review

---
*CobolIQ - Legacy COBOL Diagnostics*
