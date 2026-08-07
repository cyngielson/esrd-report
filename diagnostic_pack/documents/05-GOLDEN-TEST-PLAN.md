# Golden Output Test Plan

## Why Golden Tests Matter

699 return-code assignment sites - each a business decision.
Without golden tests, a ported system may silently produce different results.

## Priority Groups

**Group 1 - Return-Code Coverage (Highest)**
699 test scenario candidates. Trigger each RC, capture full output as golden fixture.

**Group 2 - Critical Hotspot Coverage**
60 critical paragraphs. At least 2 test scenarios each.

**Group 3 - Configuration Boundary Tests**
Thresholds: test at boundary, +/-1, extreme values.

**Group 4 - Year/Version Branch Coverage**
If the system routes by calendar year, test each branch.

## Validation During Modernization

1. Run golden tests against original COBOL
2. Run same tests against modernized component
3. Compare outputs field-by-field
4. Difference = bug (fix) or intentional change (document)

---
*CobolIQ - Legacy COBOL Diagnostics*
