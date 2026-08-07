# Global Business Rules - Cross-Program View

**Root:** `d:\cobol\ESRDCY212MainframePricerReleaseFiles`

**158 unique rules** | **2224 total occurrences** across portfolio

> **ATTENTION:** 4 field(s) have inconsistent values across programs - potential regulatory bug. See Divergences section.

## Shared Rules (appear in multiple programs)

| Field | Kind | Value | Category | Programs | Count |
|---|---|---|---|---|---|
| `H-PATIENT-AGE` | threshold | `18` | AGE_FACTORS | ESCAL056, ESCAL062, ESCAL070, 17 more | **141** |
| `H-PATIENT-AGE` | threshold | `17` | AGE_FACTORS | ESCAL056, ESCAL062, ESCAL070, 17 more | **140** |
| `H-OUT-COMORBID-MULTIPLIER` | default | `1.000` | OTHER | ESCAL117, ESCAL122, ESCAL130, 10 more | **52** |
| `H-BUN-ONSET-FACTOR` | threshold | `120` | RATE_FACTORS | ESCAL117, ESCAL122, ESCAL130, 10 more | **51** |
| `H-BUN-COMORBID-MULTIPLIER` | default | `1.000` | OTHER | ESCAL117, ESCAL122, ESCAL130, 10 more | **39** |
| `H-PATIENT-AGE` | threshold | `60` | AGE_FACTORS | ESCAL056, ESCAL062, ESCAL070, 17 more | **39** |
| `H-PATIENT-AGE` | threshold | `70` | AGE_FACTORS | ESCAL056, ESCAL062, ESCAL070, 17 more | **39** |
| `H-PATIENT-AGE` | threshold | `45` | AGE_FACTORS | ESCAL056, ESCAL062, ESCAL070, 17 more | **39** |
| `H-PATIENT-AGE` | threshold | `80` | AGE_FACTORS | ESCAL056, ESCAL062, ESCAL070, 17 more | **39** |
| `PPS-RTC` | default | `53` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **32** |
| `H-BUN-LOW-VOL-MULTIPLIER` | default | `1.000` | OTHER | ESCAL117, ESCAL122, ESCAL130, 10 more | **26** |
| `H-PATIENT-AGE` | threshold | `13` | AGE_FACTORS | ESCAL117, ESCAL122, ESCAL130, 10 more | **26** |
| `ONSET-DATE` | threshold | `120` | DATES | ESCAL117, ESCAL122, ESCAL130, 10 more | **26** |
| `B-PATIENT-HGT` | threshold | `300.00` | BODY_METRICS | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `B-PATIENT-WGT` | threshold | `500.00` | BODY_METRICS | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `55` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `54` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `71` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `52` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `72` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `56` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `58` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `PPS-RTC` | default | `57` | RETURN_CODES | ESCAL056, ESCAL062, ESCAL070, 17 more | **20** |
| `P-GEO-CBSA` | threshold | `100` | BODY_METRICS | ESCAL160, ESCAL170, ESCAL171, 5 more | **16** |
| `H-BMI` | threshold | `18.5` | BODY_METRICS | ESCAL056, ESCAL062, ESCAL070, 10 more | **13** |
| `H-BMI-FACTOR` | default | `1.000` | BODY_METRICS | ESCAL056, ESCAL062, ESCAL070, 10 more | **13** |
| `H-BSA-FACTOR` | default | `1.000` | BODY_METRICS | ESCAL056, ESCAL062, ESCAL070, 10 more | **13** |
| `H-BUN-BMI` | threshold | `18.5` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-BMI  ROUNDED` | constant | `10000` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-BMI-FACTOR` | default | `1.000` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-BSA  ROUNDED` | constant | `.725` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-BSA  ROUNDED` | constant | `.007184` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-BSA  ROUNDED` | constant | `.425` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-BSA-FACTOR` | default | `1.000` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-BSA-FACTOR  ROUNDED` | constant | `.1` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-BUN-ONSET-FACTOR` | default | `1.000` | RATE_FACTORS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-COMORBID-MULTIPLIER` | default | `1.000` | OTHER | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BMI` | threshold | `18.5` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BMI  ROUNDED` | constant | `10000` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BMI-FACTOR` | default | `1.000` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BSA  ROUNDED` | constant | `.725` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BSA  ROUNDED` | constant | `.425` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BSA  ROUNDED` | constant | `.007184` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BSA-FACTOR` | default | `1.000` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-BSA-FACTOR  ROUNDED` | constant | `.1` | BODY_METRICS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` | constant | `18` | RATE_FACTORS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` | constant | `17` | RATE_FACTORS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-ONSET-FACTOR` | default | `1.000` | RATE_FACTORS | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-PAYMENT  ROUNDED` | constant | `17` | PAYMENT | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |
| `H-OUT-PAYMENT  ROUNDED` | constant | `18` | PAYMENT | ESCAL117, ESCAL122, ESCAL130, 10 more | **13** |

## Rules by Category

### AGE_FACTORS (22 unique values)

| Field | Kind | Value | Occurrences |
|---|---|---|---|
| `H-PATIENT-AGE` | threshold | `18` | 141 |
| `H-PATIENT-AGE` | threshold | `17` | 140 |
| `H-PATIENT-AGE` | threshold | `60` | 39 |
| `H-PATIENT-AGE` | threshold | `70` | 39 |
| `H-PATIENT-AGE` | threshold | `45` | 39 |
| `H-PATIENT-AGE` | threshold | `80` | 39 |
| `H-PATIENT-AGE` | threshold | `13` | 26 |
| `H-2006-WAGE-ADJ-PYMT ROUNDED` | constant | `2006` | 8 |
| `H-AGE-FACTOR` | default | `1.055` | 7 |
| `H-AGE-FACTOR` | default | `1.094` | 7 |
| `H-AGE-FACTOR` | default | `1.620` | 7 |
| `H-AGE-FACTOR` | default | `1.000` | 7 |
| `H-AGE-FACTOR` | default | `1.223` | 7 |
| `H-AGE-FACTOR` | default | `1.174` | 7 |
| `H-PATIENT-AGE` | threshold | `59` | 7 |
| `H-PATIENT-AGE` | threshold | `44` | 7 |
| `H-PATIENT-AGE` | threshold | `79` | 7 |
| `H-PATIENT-AGE` | threshold | `69` | 7 |
| `H-2007-WAGE-ADJ-PYMT ROUNDED` | constant | `2007` | 4 |
| `H-2007-WAGE-ADJ-PYMT ROUNDED` | constant | `2006` | 4 |
| `H-2008-WAGE-ADJ-PYMT ROUNDED` | constant | `2007` | 2 |
| `H-2008-WAGE-ADJ-PYMT ROUNDED` | constant | `2008` | 2 |

### BODY_METRICS (42 unique values)

| Field | Kind | Value | Occurrences |
|---|---|---|---|
| `B-PATIENT-HGT` | threshold | `300.00` | 20 |
| `B-PATIENT-WGT` | threshold | `500.00` | 20 |
| `P-GEO-CBSA` | threshold | `100` | 16 |
| `H-BMI` | threshold | `18.5` | 13 |
| `H-BMI-FACTOR` | default | `1.000` | 13 |
| `H-BSA-FACTOR` | default | `1.000` | 13 |
| `H-BUN-BMI` | threshold | `18.5` | 13 |
| `H-BUN-BMI  ROUNDED` | constant | `10000` | 13 |
| `H-BUN-BMI-FACTOR` | default | `1.000` | 13 |
| `H-BUN-BSA  ROUNDED` | constant | `.725` | 13 |
| `H-BUN-BSA  ROUNDED` | constant | `.007184` | 13 |
| `H-BUN-BSA  ROUNDED` | constant | `.425` | 13 |
| `H-BUN-BSA-FACTOR` | default | `1.000` | 13 |
| `H-BUN-BSA-FACTOR  ROUNDED` | constant | `.1` | 13 |
| `H-OUT-BMI` | threshold | `18.5` | 13 |
| `H-OUT-BMI  ROUNDED` | constant | `10000` | 13 |
| `H-OUT-BMI-FACTOR` | default | `1.000` | 13 |
| `H-OUT-BSA  ROUNDED` | constant | `.725` | 13 |
| `H-OUT-BSA  ROUNDED` | constant | `.425` | 13 |
| `H-OUT-BSA  ROUNDED` | constant | `.007184` | 13 |
| `H-OUT-BSA-FACTOR` | default | `1.000` | 13 |
| `H-OUT-BSA-FACTOR  ROUNDED` | constant | `.1` | 13 |
| `H-BMI ROUNDED` | constant | `10000` | 7 |
| `H-BMI-FACTOR` | default | `1.112` | 7 |
| `H-BSA ROUNDED` | constant | `.425` | 7 |
| `H-BSA ROUNDED` | constant | `.007184` | 7 |
| `H-BSA ROUNDED` | constant | `.725` | 7 |
| `H-BSA-FACTOR ROUNDED` | constant | `.1` | 7 |
| `H-BSA-FACTOR ROUNDED` | constant | `1.84` | 7 |
| `H-BSA-FACTOR ROUNDED` | constant | `1.037` | 7 |
| `H-BMI  ROUNDED` | constant | `10000` | 6 |
| `H-BSA  ROUNDED` | constant | `.725` | 6 |
| `H-BSA  ROUNDED` | constant | `.425` | 6 |
| `H-BSA  ROUNDED` | constant | `.007184` | 6 |
| `H-BSA-FACTOR  ROUNDED` | constant | `.1` | 6 |
| `H-BSA-FACTOR  ROUNDED` | constant | `1.87` | 5 |
| `H-BUN-BSA-FACTOR  ROUNDED` | constant | `1.87` | 5 |
| `H-OUT-BSA-FACTOR  ROUNDED` | constant | `1.87` | 5 |
| `BUN-CBSA-W-INDEX ROUNDED` | constant | `0.95` | 1 |
| `H-BSA-FACTOR  ROUNDED` | constant | `1.84` | 1 |
| `H-BUN-BSA-FACTOR  ROUNDED` | constant | `1.90` | 1 |
| `H-OUT-BSA-FACTOR  ROUNDED` | constant | `1.90` | 1 |

### DATES (2 unique values)

| Field | Kind | Value | Occurrences |
|---|---|---|---|
| `ONSET-DATE` | threshold | `120` | 26 |
| `B-THRU-YEAR-CODE` | constant | `10` | 1 |

### OTHER (18 unique values)

| Field | Kind | Value | Occurrences |
|---|---|---|---|
| `H-OUT-COMORBID-MULTIPLIER` | default | `1.000` | 52 |
| `H-BUN-COMORBID-MULTIPLIER` | default | `1.000` | 39 |
| `H-BUN-LOW-VOL-MULTIPLIER` | default | `1.000` | 26 |
| `H-COMORBID-MULTIPLIER` | default | `1.000` | 13 |
| `H-OUT-PREDICTED-MAP  ROUNDED` | constant | `17` | 13 |
| `H-OUT-PREDICTED-MAP  ROUNDED` | constant | `18` | 13 |
| `H-LV-OUT-PREDICTED-MAP  ROUNDED` | constant | `18` | 12 |
| `H-LV-OUT-PREDICTED-MAP  ROUNDED` | constant | `17` | 12 |
| `QIP-REDUCTION` | default | `0.980` | 12 |
| `QIP-REDUCTION` | default | `0.995` | 12 |
| `QIP-REDUCTION` | default | `0.990` | 12 |
| `QIP-REDUCTION` | default | `0.985` | 12 |
| `QIP-REDUCTION` | default | `1.000` | 12 |
| `H-BUN-RURAL-MULTIPLIER` | default | `1.000` | 8 |
| `H-OUT-RURAL-MULTIPLIER` | default | `1.000` | 8 |
| `H-ESRD-SUPP-WI-RATIO` | threshold | `-0.05` | 1 |
| `H-NETWORK-REDUCTION` | default | `0.50` | 1 |
| `H-NETWORK-REDUCTION` | default | `0.21` | 1 |

### PAYMENT (8 unique values)

| Field | Kind | Value | Occurrences |
|---|---|---|---|
| `H-OUT-PAYMENT  ROUNDED` | constant | `17` | 13 |
| `H-OUT-PAYMENT  ROUNDED` | constant | `18` | 13 |
| `H-LV-OUT-PAYMENT  ROUNDED` | constant | `17` | 12 |
| `H-LV-OUT-PAYMENT  ROUNDED` | constant | `18` | 12 |
| `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` | constant | `74` | 12 |
| `H-PPS-FINAL-PAY-AMT  ROUNDED` | constant | `74` | 11 |
| `H-PYMT-AMT ROUNDED` | constant | `49` | 1 |
| `H-TPNIES-PAYMENT` | constant | `0.65` | 1 |

### RATE_FACTORS (13 unique values)

| Field | Kind | Value | Occurrences |
|---|---|---|---|
| `H-BUN-ONSET-FACTOR` | threshold | `120` | 51 |
| `H-BUN-ONSET-FACTOR` | default | `1.000` | 13 |
| `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` | constant | `18` | 13 |
| `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` | constant | `17` | 13 |
| `H-OUT-ONSET-FACTOR` | default | `1.000` | 13 |
| `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` | constant | `18` | 12 |
| `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` | constant | `17` | 12 |
| `PPS-2011-BLEND-COMP-RATE    ROUNDED` | constant | `2011` | 12 |
| `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` | constant | `2011` | 12 |
| `PPS-2011-BLEND-PPS-RATE     ROUNDED` | constant | `2011` | 12 |
| `PPS-2011-FULL-COMP-RATE     ROUNDED` | constant | `2011` | 12 |
| `PPS-2011-FULL-OUTLIER-RATE  ROUNDED` | constant | `2011` | 12 |
| `PPS-2011-FULL-PPS-RATE      ROUNDED` | constant | `2011` | 10 |

### RETURN_CODES (53 unique values)

| Field | Kind | Value | Occurrences |
|---|---|---|---|
| `PPS-RTC` | default | `53` | 32 |
| `PPS-RTC` | default | `55` | 20 |
| `PPS-RTC` | default | `54` | 20 |
| `PPS-RTC` | default | `71` | 20 |
| `PPS-RTC` | default | `52` | 20 |
| `PPS-RTC` | default | `72` | 20 |
| `PPS-RTC` | default | `56` | 20 |
| `PPS-RTC` | default | `58` | 20 |
| `PPS-RTC` | default | `57` | 20 |
| `PPS-RTC` | default | `22` | 13 |
| `PPS-RTC` | default | `34` | 13 |
| `PPS-RTC` | default | `20` | 13 |
| `PPS-RTC` | default | `10` | 13 |
| `PPS-RTC` | default | `75` | 13 |
| `PPS-RTC` | default | `76` | 13 |
| `PPS-RTC` | default | `15` | 13 |
| `PPS-RTC` | default | `23` | 13 |
| `PPS-RTC` | default | `07` | 13 |
| `PPS-RTC` | default | `32` | 13 |
| `PPS-RTC` | default | `31` | 13 |
| `PPS-RTC` | default | `35` | 13 |
| `PPS-RTC` | default | `73` | 13 |
| `PPS-RTC` | default | `81` | 13 |
| `PPS-RTC` | default | `74` | 13 |
| `PPS-RTC` | default | `06` | 13 |
| `PPS-RTC` | default | `12` | 13 |
| `PPS-RTC` | default | `17` | 13 |
| `PPS-RTC` | default | `26` | 13 |
| `PPS-RTC` | default | `05` | 13 |
| `PPS-RTC` | default | `27` | 13 |
| `PPS-RTC` | default | `09` | 13 |
| `PPS-RTC` | default | `21` | 13 |
| `PPS-RTC` | default | `16` | 13 |
| `PPS-RTC` | default | `19` | 13 |
| `PPS-RTC` | default | `11` | 13 |
| `PPS-RTC` | default | `14` | 13 |
| `PPS-RTC` | default | `30` | 13 |
| `PPS-RTC` | default | `03` | 13 |
| `PPS-RTC` | default | `25` | 13 |
| `PPS-RTC` | default | `02` | 13 |
| `PPS-RTC` | default | `08` | 13 |
| `PPS-RTC` | default | `29` | 13 |
| `PPS-RTC` | default | `24` | 13 |
| `PPS-RTC` | default | `18` | 13 |
| `PPS-RTC` | default | `28` | 13 |
| `PPS-RTC` | default | `33` | 13 |
| `PPS-RTC` | default | `04` | 13 |
| `PPS-RTC` | threshold | `50` | 7 |
| `PPS-RTC` | default | `60` | 5 |
| `PPS-RTC` | default | `01` | 2 |
| `PPS-RTC` | default | `98` | 2 |
| `PPS-RTC` | default | `61` | 2 |
| `PPS-RTC` | default | `50` | 1 |

## Divergences - Inconsistent Values Across Programs

> These fields have **different hardcoded values** in different programs.
> This may indicate version drift, regulatory inconsistency, or copy-paste errors.

| Field | Kind | Value | Programs using this value |
|---|---|---|---|
| `H-PATIENT-AGE` | threshold | `18` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100, ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-PATIENT-AGE` | threshold | `17` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100, ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-PATIENT-AGE` | threshold | `60` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100, ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-PATIENT-AGE` | threshold | `70` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100, ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-PATIENT-AGE` | threshold | `45` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100, ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-PATIENT-AGE` | threshold | `80` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100, ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-PATIENT-AGE` | threshold | `13` | ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-PATIENT-AGE` | threshold | `59` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100 |
| `H-PATIENT-AGE` | threshold | `44` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100 |
| `H-PATIENT-AGE` | threshold | `79` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100 |
| `H-PATIENT-AGE` | threshold | `69` | ESCAL056, ESCAL062, ESCAL070, ESCAL071, ESCAL080, ESCAL091, ESCAL100 |
| `H-BSA-FACTOR  ROUNDED` | constant | `.1` | ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160 |
| `H-BSA-FACTOR  ROUNDED` | constant | `1.87` | ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160 |
| `H-BSA-FACTOR  ROUNDED` | constant | `1.84` | ESCAL117 |
| `H-BUN-BSA-FACTOR  ROUNDED` | constant | `.1` | ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-BUN-BSA-FACTOR  ROUNDED` | constant | `1.87` | ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151 |
| `H-BUN-BSA-FACTOR  ROUNDED` | constant | `1.90` | ESCAL160 |
| `H-OUT-BSA-FACTOR  ROUNDED` | constant | `.1` | ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151, ESCAL160, ESCAL170, ESCAL171, ESCAL180, ESCAL191, ESCAL200, ESCAL202, ESCAL212 |
| `H-OUT-BSA-FACTOR  ROUNDED` | constant | `1.87` | ESCAL117, ESCAL122, ESCAL130, ESCAL140, ESCAL151 |
| `H-OUT-BSA-FACTOR  ROUNDED` | constant | `1.90` | ESCAL160 |

