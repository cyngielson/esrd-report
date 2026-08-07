# CobolIQ Modernization Readiness Map

*Source-cited assessment: what to externalize, test, review - and what can be safely ported.*

---

## Modernization Posture

**Assessment:** Semi-automated with hotspot review

Portfolio baseline: 35 average risk across 21 program(s) - appears low at first glance. **However: 100/100 max risk**, with **60 critical hotspot(s)** concentrated in key paragraphs. 2224 hardcoded configuration candidates, 699 return-code assignments, 38 GO TO statements. 

Average risk is low because many paragraphs are small boilerplate or EXIT markers, but modernization risk is concentrated in critical calculation/validation hotspots that cannot be auto-ported blindly. **Review required before automated porting.**

### Key Metrics

| Metric | Value |
|--------|-------|
| Programs analyzed | 21 |
| Average risk | 35/100 |
| Max risk (hotspot) | 100/100 |
| Critical paragraphs | 60 |
| Configuration candidates | 2224 |
| Return-code assignments | 699 |
| GO TO statements | 38 |

## 1. Risk Heatmap

*Programs ranked by modernization risk. Higher max risk = more manual review needed.*

| # | Program | Avg | Max | Critical | Posture |
|---|---------|-----|-----|----------|--------|
| 1 | `ESCAL117` | 53 | 100 | 4 | [E] review required |
| 2 | `ESCAL122` | 48 | 100 | 4 | [E] review required |
| 3 | `ESCAL130` | 48 | 100 | 4 | [E] review required |
| 4 | `ESCAL140` | 48 | 100 | 4 | [E] review required |
| 5 | `ESCAL151` | 48 | 100 | 4 | [E] review required |
| 6 | `ESCAL160` | 46 | 100 | 4 | [E] review required |
| 7 | `ESCAL170` | 43 | 100 | 4 | [E] review required |
| 8 | `ESCAL171` | 43 | 100 | 4 | [E] review required |
| 9 | `ESCAL180` | 43 | 100 | 4 | [E] review required |
| 10 | `ESCAL191` | 43 | 100 | 4 | [E] review required |
| 11 | `ESCAL200` | 43 | 100 | 4 | [E] review required |
| 12 | `ESCAL202` | 43 | 100 | 4 | [E] review required |
| 13 | `ESCAL212` | 44 | 100 | 4 | [E] review required |
| 14 | `ESDRV212` | 26 | 100 | 1 | [E] review required |
| 15 | `ESCAL056` | 19 | 84 | 1 | [E] review required |
| 16 | `ESCAL062` | 18 | 84 | 1 | [E] review required |
| 17 | `ESCAL070` | 18 | 84 | 1 | [E] review required |
| 18 | `ESCAL071` | 18 | 84 | 1 | [E] review required |
| 19 | `ESCAL080` | 18 | 84 | 1 | [E] review required |
| 20 | `ESCAL091` | 18 | 84 | 1 | [E] review required |
| 21 | `ESCAL100` | 18 | 84 | 1 | [E] review required |

**Aggregate:** 21 programs, average 35/100, max 100/100, **60 critical hotspots**

## 2. Configuration Candidates

*Hardcoded values grouped by business category. Each was embedded directly in COBOL source - review and externalize before migration.*

### Return Codes - 705 candidates

| Value | Program | Paragraph | Line |
|-------|---------|-----------|------|
| **53** (?32) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 221 |
| **52** (?20) | `ESCAL056` | `0100-INITIAL-ROUTINE` | 188 |
| **54** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 227 |
| **55** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 233 |
| **56** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 239 |
| **57** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 245 |
| **58** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 254 |
| **71** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 260 |
| **72** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 266 |
| **02** (?13) | `ESCAL117` | `9000-SET-RETURN-CODE` | 1419 |
| ... | | 42 more unique values | |


### Payment Factors & Rates - 836 candidates

| Value | Program | Paragraph | Line |
|-------|---------|-----------|------|
| **1.000** (?238) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| **18** (?128) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 689 |
| **17** (?119) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 730 |
| **120** (?77) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 756 |
| **18.5** (?32) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 746 |
| **45** (?32) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 689 |
| **60** (?32) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 689 |
| **70** (?32) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 689 |
| **80** (?32) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 689 |
| **13** (?26) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 689 |
| ... | | 13 more unique values | |


### Thresholds & Limits - 138 candidates

| Value | Program | Paragraph | Line |
|-------|---------|-----------|------|
| **17** (?21) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| **300.00** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 260 |
| **500.00** (?20) | `ESCAL056` | `1000-EDIT-THE-BILL-INFO` | 266 |
| **18** (?13) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| **18.5** (?7) | `ESCAL056` | `2000-ASSEMBLE-PPS-VARIABLES` | 337 |
| **44** (?7) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| **45** (?7) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| **59** (?7) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| **60** (?7) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| **69** (?7) | `ESCAL056` | `1200-CALC-AGE` | 292 |
| ... | | 4 more unique values | |


### Defaults & Fallbacks - 51 candidates

| Value | Program | Paragraph | Line |
|-------|---------|-----------|------|
| **1.000** (?31) | `ESCAL117` | `2100-CALC-COMORBID-ADJUST` | 912 |
| **0.980** (?5) | `ESCAL122` | `1200-INITIALIZATION` | 629 |
| **0.985** (?5) | `ESCAL122` | `1200-INITIALIZATION` | 629 |
| **0.990** (?5) | `ESCAL122` | `1200-INITIALIZATION` | 629 |
| **0.995** (?5) | `ESCAL122` | `1200-INITIALIZATION` | 629 |

### Other Constants - 494 candidates

| Value | Program | Paragraph | Line |
|-------|---------|-----------|------|
| **17** (?75) | `ESCAL117` | `2500-CALC-OUTLIER-FACTORS` | 1123 |
| **18** (?75) | `ESCAL117` | `2500-CALC-OUTLIER-FACTORS` | 1123 |
| **2011** (?70) | `ESCAL122` | `9100-MOVE-RESULTS` | 1830 |
| **.007184** (?39) | `ESCAL056` | `2000-ASSEMBLE-PPS-VARIABLES` | 324 |
| **.1** (?39) | `ESCAL056` | `2000-ASSEMBLE-PPS-VARIABLES` | 330 |
| **.425** (?39) | `ESCAL056` | `2000-ASSEMBLE-PPS-VARIABLES` | 324 |
| **.725** (?39) | `ESCAL056` | `2000-ASSEMBLE-PPS-VARIABLES` | 324 |
| **10000** (?39) | `ESCAL056` | `2000-ASSEMBLE-PPS-VARIABLES` | 324 |
| **74** (?23) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 889 |
| **1.87** (?15) | `ESCAL117` | `2000-CALCULATE-BUNDLED-FACTORS` | 730 |
| ... | | 10 more unique values | |


**Total: 2224 configuration candidates** across 5 categories.

*These values are not external configuration - they are embedded in COBOL paragraph logic. Review each group to determine what should become external config vs. documented business constants.*

## 3. Schema Candidates

*COBOL data structures that can be converted to DTOs / database schemas.*

*No OCCURS-based tables found in WORKING-STORAGE.*

## 4. Test Harness TODO

*Golden-output test requirements for migration validation.*

### `ESCAL056`

**Return-code test cases:** 9 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '41' | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' ' | TODO |
| **54** | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) | TODO |
| **55** | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) | TODO |
| **56** | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00 | TODO |

**Complex decision points requiring coverage:** 4

- `1000-EDIT-THE-BILL-INFO` - 17 branches -> need 34 test scenarios
- `1200-CALC-AGE` - 7 branches -> need 14 test scenarios
- `3000-CALC-PAYMENT` - 3 branches -> need 6 test scenarios
- `9000-MOVE-RESULTS` - 4 branches -> need 8 test scenarios

### `ESCAL062`

**Return-code test cases:** 9 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '41' | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' ' | TODO |
| **54** | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) | TODO |
| **55** | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) | TODO |
| **56** | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00 | TODO |

**Complex decision points requiring coverage:** 4

- `1000-EDIT-THE-BILL-INFO` - 17 branches -> need 34 test scenarios
- `1200-CALC-AGE` - 7 branches -> need 14 test scenarios
- `3000-CALC-PAYMENT` - 3 branches -> need 6 test scenarios
- `9000-MOVE-RESULTS` - 3 branches -> need 6 test scenarios

### `ESCAL070`

**Return-code test cases:** 9 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '41' | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' ' | TODO |
| **54** | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) | TODO |
| **55** | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) | TODO |
| **56** | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00 | TODO |

**Complex decision points requiring coverage:** 4

- `1000-EDIT-THE-BILL-INFO` - 17 branches -> need 34 test scenarios
- `1200-CALC-AGE` - 7 branches -> need 14 test scenarios
- `3000-CALC-PAYMENT` - 3 branches -> need 6 test scenarios
- `9000-MOVE-RESULTS` - 3 branches -> need 6 test scenarios

### `ESCAL071`

**Return-code test cases:** 9 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '41' | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' ' | TODO |
| **54** | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) | TODO |
| **55** | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) | TODO |
| **56** | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00 | TODO |

**Complex decision points requiring coverage:** 4

- `1000-EDIT-THE-BILL-INFO` - 17 branches -> need 34 test scenarios
- `1200-CALC-AGE` - 7 branches -> need 14 test scenarios
- `3000-CALC-PAYMENT` - 3 branches -> need 6 test scenarios
- `9000-MOVE-RESULTS` - 3 branches -> need 6 test scenarios

### `ESCAL080`

**Return-code test cases:** 9 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '41'  THEN | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |

**Complex decision points requiring coverage:** 4

- `1000-EDIT-THE-BILL-INFO` - 17 branches -> need 34 test scenarios
- `1200-CALC-AGE` - 7 branches -> need 14 test scenarios
- `3000-CALC-PAYMENT` - 3 branches -> need 6 test scenarios
- `9000-MOVE-RESULTS` - 3 branches -> need 6 test scenarios

### `ESCAL091`

**Return-code test cases:** 9 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '41'  THEN | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |

**Complex decision points requiring coverage:** 4

- `1000-EDIT-THE-BILL-INFO` - 17 branches -> need 34 test scenarios
- `1200-CALC-AGE` - 7 branches -> need 14 test scenarios
- `3000-CALC-PAYMENT` - 3 branches -> need 6 test scenarios
- `9000-MOVE-RESULTS` - 3 branches -> need 6 test scenarios

### `ESCAL100`

**Return-code test cases:** 9 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '41'  THEN | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |

**Complex decision points requiring coverage:** 4

- `1000-EDIT-THE-BILL-INFO` - 17 branches -> need 34 test scenarios
- `1200-CALC-AGE` - 7 branches -> need 14 test scenarios
- `3000-CALC-PAYMENT` - 3 branches -> need 6 test scenarios
- `9000-MOVE-RESULTS` - 3 branches -> need 6 test scenarios

### `ESCAL117`

**Return-code test cases:** 47 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMOR | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 5 branches -> need 10 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 27 branches -> need 54 test scenarios
- `1200-INITIALIZATION` - 7 branches -> need 14 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 26 branches -> need 52 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 11 branches -> need 22 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 11 branches -> need 22 test scenarios
- `5000-CALC-COMP-RATE-FACTORS` - 11 branches -> need 22 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 5 branches -> need 10 test scenarios

### `ESCAL122`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMOR | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 12

- `0000-START-TO-FINISH` - 5 branches -> need 10 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 29 branches -> need 58 test scenarios
- `1200-INITIALIZATION` - 11 branches -> need 22 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 28 branches -> need 56 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 11 branches -> need 22 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 11 branches -> need 22 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `5000-CALC-COMP-RATE-FACTORS` - 11 branches -> need 22 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 6 branches -> need 12 test scenarios

### `ESCAL130`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMOR | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 12

- `0000-START-TO-FINISH` - 5 branches -> need 10 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 29 branches -> need 58 test scenarios
- `1200-INITIALIZATION` - 11 branches -> need 22 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 28 branches -> need 56 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 11 branches -> need 22 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 11 branches -> need 22 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `5000-CALC-COMP-RATE-FACTORS` - 11 branches -> need 22 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 6 branches -> need 12 test scenarios

### `ESCAL140`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMOR | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 12

- `0000-START-TO-FINISH` - 5 branches -> need 10 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 29 branches -> need 58 test scenarios
- `1200-INITIALIZATION` - 11 branches -> need 22 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 28 branches -> need 56 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 11 branches -> need 22 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 11 branches -> need 22 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `5000-CALC-COMP-RATE-FACTORS` - 11 branches -> need 22 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 6 branches -> need 12 test scenarios

### `ESCAL151`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMOR | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 12

- `0000-START-TO-FINISH` - 5 branches -> need 10 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 29 branches -> need 58 test scenarios
- `1200-INITIALIZATION` - 11 branches -> need 22 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 28 branches -> need 56 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 11 branches -> need 22 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 11 branches -> need 22 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `5000-CALC-COMP-RATE-FACTORS` - 11 branches -> need 22 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 6 branches -> need 12 test scenarios

### `ESCAL160`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '  ' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 12

- `0000-START-TO-FINISH` - 5 branches -> need 10 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 29 branches -> need 58 test scenarios
- `1200-INITIALIZATION` - 10 branches -> need 20 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 28 branches -> need 56 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `5000-CALC-COMP-RATE-FACTORS` - 11 branches -> need 22 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 6 branches -> need 12 test scenarios

### `ESCAL170`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '  ' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 3 branches -> need 6 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 34 branches -> need 68 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches -> need 80 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 7 branches -> need 14 test scenarios

### `ESCAL171`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87'  | TODO |
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 3 branches -> need 6 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches -> need 70 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches -> need 80 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 7 branches -> need 14 test scenarios

### `ESCAL180`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87'  | TODO |
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 3 branches -> need 6 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches -> need 70 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches -> need 80 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 7 branches -> need 14 test scenarios

### `ESCAL191`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87'  | TODO |
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 3 branches -> need 6 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches -> need 70 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches -> need 80 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 7 branches -> need 14 test scenarios

### `ESCAL200`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87'  | TODO |
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 3 branches -> need 6 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches -> need 70 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches -> need 80 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 7 branches -> need 14 test scenarios

### `ESCAL202`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87'  | TODO |
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 3 branches -> need 6 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches -> need 70 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 41 branches -> need 82 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 8 branches -> need 16 test scenarios

### `ESCAL212`

**Return-code test cases:** 48 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87'  | TODO |
| **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SE | TODO |
| **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN | TODO |
| **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  | TODO |
| **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERI | TODO |
| **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERI | TODO |
| **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' | TODO |
| **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4'  | TODO |
| **71** | B-PATIENT-HGT > 300.00 | TODO |
| **72** | B-PATIENT-WGT > 500.00  THEN | TODO |
| **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM | TODO |
| **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM- | TODO |
| **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN | TODO |
| **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN | TODO |
| **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20"  | TODO |
| **17** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **16** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **15** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **14** | TRAINING-TRACK                  = "Y"  THEN | TODO |
| **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **30** | ONSET-TRACK         = "Y"  THEN | TODO |
| **28** | ONSET-TRACK         = "Y"  THEN | TODO |
| **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **09** | ONSET-TRACK         = "Y"  THEN | TODO |
| **03** | ONSET-TRACK         = "Y"  THEN | TODO |
| **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **32** | ONSET-TRACK         = "Y"  THEN | TODO |
| **10** | ONSET-TRACK         = "Y"  THEN | TODO |
| **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN | TODO |
| **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **08** | ONSET-TRACK               = "Y"  THEN | TODO |
| **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN | TODO |
| **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN | TODO |
| **31** | LOW-BMI-TRACK = "Y"  THEN | TODO |
| **02** | LOW-BMI-TRACK = "Y"  THEN | TODO |

**Complex decision points requiring coverage:** 10

- `0000-START-TO-FINISH` - 3 branches -> need 6 test scenarios
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches -> need 70 test scenarios
- `2000-CALCULATE-BUNDLED-FACTORS` - 43 branches -> need 86 test scenarios
- `2100-CALC-COMORBID-ADJUST` - 7 branches -> need 14 test scenarios
- `2500-CALC-OUTLIER-FACTORS` - 28 branches -> need 56 test scenarios
- `2600-CALC-COMORBID-OUT-ADJUST` - 7 branches -> need 14 test scenarios
- `3000-LOW-VOL-FULL-PPS-PAYMENT` - 4 branches -> need 8 test scenarios
- `3100-LOW-VOL-OUT-PPS-PAYMENT` - 5 branches -> need 10 test scenarios
- `9000-SET-RETURN-CODE` - 32 branches -> need 64 test scenarios
- `9100-MOVE-RESULTS` - 9 branches -> need 18 test scenarios

### `ESDRV212`

**Return-code test cases:** 13 scenarios

| RC Value | Trigger Condition | Test Input Needed |
|----------|-------------------|-------------------|
| **00** | always | TODO |
| **98** | (B-THRU-DATE < 20050401) OR (B-THRU-DATE NOT NUMER | TODO |
| **50** | P-ESRD-RATE NOT NUMERIC | TODO |
| **01** | (B-THRU-DATE < 20110101)  AND  (P-ESRD-RATE > ZERO | TODO |
| **01** | (B-THRU-DATE > 20101231)        AND (B-THRU-DATE < | TODO |
| **98** | (B-THRU-DATE > 20050331 AND B-THRU-DATE < 20060101 | TODO |
| **60** | always | TODO |
| **60** | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN | TODO |
| **61** | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN | TODO |
| **60** | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN | TODO |
| **61** | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN | TODO |
| **60** | H-ESRD-SUPP-WI-RATIO < -0.05 | TODO |
| **60** | W-SUB3 > BUN-PTR (BUN-INDX - 1) THEN | TODO |

**Complex decision points requiring coverage:** 3

- `0100-ENTER-DRIVER` - 30 branches -> need 60 test scenarios
- `0700-FIND-COMPOSITE-CBSA-WI` - 3 branches -> need 6 test scenarios
- `0800-FIND-BUNDLED-CBSA-WI` - 9 branches -> need 18 test scenarios

### Test Strategy

1. **Golden-output tests:** Run COBOL with known inputs, capture outputs. Compare with migrated version.
2. **Return-code coverage:** Ensure every RC value in the catalog is triggerable in tests.
3. **Boundary tests:** Test each threshold/default value ? 1 (from Section 2).
4. **Copybook validation:** Test with extreme values in COPYBOOK fields (max/min/numeric overflow).
5. **Regression suite:** Store all test inputs/outputs for automated re-validation.

## 5. Expert Review Notes

*Items flagged for manual COBOL expert review before automated migration.*

- `ESCAL056`: COPYBOOK deps [BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL062`: COPYBOOK deps [BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL070`: COPYBOOK deps [BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL071`: COPYBOOK deps [BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL080`: COPYBOOK deps [BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL091`: COPYBOOK deps [BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL100`: COPYBOOK deps [BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL117`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL122`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL130`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL140`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL151`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL160`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL170`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL171`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL180`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL191`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL200`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL202`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESCAL212`: COPYBOOK deps [RTCCPY, BILLCPY, WAGECPY] - verify copybook versions and contents
- `ESDRV212`: 38 GO TO statements - verify restructuring strategy
- `ESDRV212`: 10 REDEFINES - need union/polymorphic mapping
- `ESDRV212`: COPYBOOK deps [DSCNTRL, ESWRT151, ESCOM151, ESBUN210, ESCHI151, WAGECPY, RTCCPY, BILLCPY] - verify copybook versions and contents

### Review Checklist

? All GO TO statements understood and migration strategy defined
? REDEFINES structures mapped to target language equivalents
? COPYBOOK contents verified (external copybooks may contain critical constants)
? Business logic in high-risk paragraphs documented and validated
? PERFORM THRU ranges confirmed - these may hide implicit control flow
? COMP-3 / packed decimal fields identified and conversion strategy defined
? Any JCL/DB2/VSAM/CICS dependencies documented

## 6. Recommended Next Actions

1. **Externalize configuration** - 2224 hardcoded values identified. Extract to config files (INI->YAML/TOML) before migration.
2. **Build golden-output test harness** - 699 return-code scenarios documented. Capture COBOL outputs as test fixtures first.
3. **Expert review of 60 critical hotspots** - paragraphs scoring ?76/100. Cannot be auto-ported.
4. **GO TO restructuring** - 38 non-structured jumps. Design target-language equivalents.
5. **Generate full Diagnostic Pack** - `coboliq <path> --diagnostic-pack` for complete dossier with starter artifacts.
---

*Generated by CobolIQ v0.8.2 - Modernization Readiness Map*
*Analysis timestamp: 2026-08-06 18:43:15*
