# Program Detail - Part 5/6

---

# COBOL Program: `ESCAL180`

**Source:** `ESCAL180`  
**Lines:** 2054 total / 1218 code / 719 comments

## Inter-Service Narrative (ISN)

> **ESCAL180 - 12 paragraphs, 48 return codes, 1 state flags, 3 external copybooks**

COBOL program `ESCAL180` orchestrates a 1-step business flow. It emits 47 distinct return-code value(s) across 48 assignment site(s), driven by 1 state-machine flag group(s). Depends on 3 external copybook(s): RTCCPY, BILLCPY, WAGECPY.

**Entry point:** `0000-PROCEDURE-START`

**Top decision points (most branched paragraphs):**

- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches - sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' / PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE / PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
- `9000-SET-RETURN-CODE` - 32 branches - sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN / PPS-RTC=16 when TRAINING-TRACK = "Y" THEN / PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
- `2500-CALC-OUTLIER-FACTORS` - 28 branches
- `2100-CALC-COMORBID-ADJUST` - 7 branches

**Return-code catalog (value -> emission sites):**

| RC | Sites | Variables | Sample condition |
|---|---|---|---|
| **02** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **03** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **04** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **05** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **06** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **07** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **08** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **09** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **10** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **11** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **12** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **14** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **15** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **16** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **17** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **18** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **19** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **20** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **21** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **22** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **23** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **24** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **25** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **26** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **27** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **28** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **29** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **30** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **31** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **32** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **33** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **34** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **35** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **52** | 1 | `PPS-RTC` | P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE |
| **53** | 2 | `PPS-RTC` | P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN |
| **54** | 1 | `PPS-RTC` | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN |
| **55** | 1 | `PPS-RTC` | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| **56** | 1 | `PPS-RTC` | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| **57** | 1 | `PPS-RTC` | B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| **58** | 1 | `PPS-RTC` | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' |
| **71** | 1 | `PPS-RTC` | B-PATIENT-HGT > 300.00 |
| **72** | 1 | `PPS-RTC` | B-PATIENT-WGT > 500.00 THEN |
| **73** | 1 | `PPS-RTC` | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NU? |
| **74** | 1 | `PPS-RTC` | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC) THEN |
| **75** | 1 | `PPS-RTC` | (B-DIALYSIS-START-DATE NOT NUMERIC) THEN |
| **76** | 1 | `PPS-RTC` | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| **81** | 1 | `PPS-RTC` | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN ? |

## Stats

- Paragraphs: **12**
- PERFORM/CALL edges: **12**
- COPY references: **3**
- WORKING-STORAGE items: **168**, LINKAGE items: **198**
- Return code assignments: **48**, State machines: **1**
- Cyclomatic complexity (est): **170**

## Business Rules (Magic Numbers)

**Total:** 142 rules (41 thresholds, 71 defaults)

| Type | Key | Value | Paragraph | Line |
|------|-----|-------|-----------|------|
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `58` | `1000-VALIDATE-BILL-ELEMENTS` | 698 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `52` | `1000-VALIDATE-BILL-ELEMENTS` | 705 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 713 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `54` | `1000-VALIDATE-BILL-ELEMENTS` | 719 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `55` | `1000-VALIDATE-BILL-ELEMENTS` | 725 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `56` | `1000-VALIDATE-BILL-ELEMENTS` | 733 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `57` | `1000-VALIDATE-BILL-ELEMENTS` | 741 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 750 |
| ?? threshold | `1000_validate_bill_elements.b_patient_hgt.threshold` | `300.00` | `1000-VALIDATE-BILL-ELEMENTS` | 760 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `71` | `1000-VALIDATE-BILL-ELEMENTS` | 760 |
| ?? threshold | `1000_validate_bill_elements.b_patient_wgt.threshold` | `500.00` | `1000-VALIDATE-BILL-ELEMENTS` | 768 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `72` | `1000-VALIDATE-BILL-ELEMENTS` | 768 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `73` | `1000-VALIDATE-BILL-ELEMENTS` | 781 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `74` | `1000-VALIDATE-BILL-ELEMENTS` | 788 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `75` | `1000-VALIDATE-BILL-ELEMENTS` | 795 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `76` | `1000-VALIDATE-BILL-ELEMENTS` | 801 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `81` | `1000-VALIDATE-BILL-ELEMENTS` | 818 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 851 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `1.000` | `2000-CALCULATE-BUNDLED-FACTORS` | 861 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.995` | `2000-CALCULATE-BUNDLED-FACTORS` | 861 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.990` | `2000-CALCULATE-BUNDLED-FACTORS` | 861 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.985` | `2000-CALCULATE-BUNDLED-FACTORS` | 861 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.980` | `2000-CALCULATE-BUNDLED-FACTORS` | 861 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `13` | `2000-CALCULATE-BUNDLED-FACTORS` | 978 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 978 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `45` | `2000-CALCULATE-BUNDLED-FACTORS` | 978 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `60` | `2000-CALCULATE-BUNDLED-FACTORS` | 978 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `70` | `2000-CALCULATE-BUNDLED-FACTORS` | 978 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `80` | `2000-CALCULATE-BUNDLED-FACTORS` | 978 |
| ?? constant | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` | `.007184` | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 |

_... +112 more rules in `--extract-rules` output_

## Business Logic (Computed Values & Lookups)

_What this program actually calculates: 49 formulas/lookups/loops/call-params across 9 paragraphs._

### `0000-START-TO-FINISH`

- **INITIALIZE** `PPS-DATA-ALL` (L661)
- **INITIALIZE** `BILL-DATA-TEST` (L669)
- **INITIALIZE** `COND-CD-73` (L669)

### `1200-INITIALIZATION`

- **INITIALIZE** `HOLD-COMP-RATE-PPS-COMPONENTS` (L830)
- **INITIALIZE** `HOLD-BUNDLED-PPS-COMPONENTS` (L831)
- **INITIALIZE** `HOLD-OUTLIER-PPS-COMPONENTS` (L832)
- **INITIALIZE** `PAID-RETURN-CODE-TRACKERS` (L833)
- **COMPUTE** `H-BUN-NAT-LABOR-AMT ROUNDED` = `(BUNDLED-BASE-PMT-RATE * BUN-NAT-LABOR-PCT) * BUN-CBSA-W-INDEX.` (L839)
- **COMPUTE** `H-BUN-NAT-NONLABOR-AMT ROUNDED` = `BUNDLED-BASE-PMT-RATE * BUN-NAT-NONLABOR-PCT` (L843)
- **COMPUTE** `H-BUN-BASE-WAGE-AMT ROUNDED` = `H-BUN-NAT-LABOR-AMT + H-BUN-NAT-NONLABOR-AMT.` (L843)

### `2000-CALCULATE-BUNDLED-FACTORS`

- **COMPUTE** `H-PATIENT-AGE` = `B-THRU-CCYY - B-DOB-CCYY` (L851)
- **COMPUTE** `H-PATIENT-AGE` = `H-PATIENT-AGE - 1` (L851)
- **COMPUTE** `H-BUN-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1019)
- **COMPUTE** `H-BUN-BSA-FACTOR  ROUNDED` = `CM-BSA ** ((H-BUN-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1019)
- **COMPUTE** `H-BUN-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1033)
- **COMPUTE** `INTEGER-LINE-ITEM-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1046)
- **COMPUTE** `INTEGER-DIALYSIS-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1046)
- **COMPUTE** `ONSET-DATE` = `(INTEGER-LINE-ITEM-DATE - INTEGER-DIALYSIS-DATE) + 1` (L1046)

### `2100-CALC-COMORBID-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1244)

### `2500-CALC-OUTLIER-FACTORS`

- **COMPUTE** `H-OUT-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1346)
- **COMPUTE** `H-OUT-BSA-FACTOR  ROUNDED` = `SB-BSA ** ((H-OUT-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1346)
- **COMPUTE** `H-OUT-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1360)
- **COMPUTE** `H-OUT-PREDICTED-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1452)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1464)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1464)
- **COMPUTE** `H-HEMO-EQUIV-DIAL-SESSIONS  ROUNDED` = `((B-CLAIM-NUM-DIALYSIS-SESSIONS * 3) / 7)` (L1478)
- **COMPUTE** `H-OUT-IMPUTED-MAP  ROUNDED` = `(B-TOT-PRICE-SB-OUTLIER / H-HEMO-EQUIV-DIAL-SESSIONS)` (L1478)

### `2600-CALC-COMORBID-OUT-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1543)

### `3000-LOW-VOL-FULL-PPS-PAYMENT`

- **COMPUTE** `H-LV-BUN-ADJUST-BASE-WAGE-AMT  ROUNDED` = `(H-BUN-BASE-WAGE-AMT * H-BUN-AGE-FACTOR)     * (H-BUN-BSA-FACTOR    * H-BUN-BMI-FACTOR)     * (H-BUN-ONSET-FACTOR  * H-B` (L1603)
- **COMPUTE** `H-BUN-WAGE-ADJ-TRAINING-AMT  ROUNDED` = `TRAINING-ADD-ON-PMT-AMT * BUN-CBSA-W-INDEX` (L1612)
- **COMPUTE** `H-CC-74-PER-DIEM-AMT  ROUNDED` = `(H-LV-BUN-ADJUST-BASE-WAGE-AMT * 3) / 7` (L1612)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-CC-74-PER-DIEM-AMT` (L1638)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-LV-BUN-ADJUST-BASE-WAGE-AMT + H-BUN-WAGE-ADJ-TRAINING-AMT` (L1638)

### `3100-LOW-VOL-OUT-PPS-PAYMENT`

- **COMPUTE** `H-LV-OUT-PREDICT-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1655)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1665)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1665)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-LT-18` (L1681)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-LT-18` (L1681)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-GT-17` (L1681)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-GT-17` (L1681)
- **COMPUTE** `H-LV-OUT-PAYMENT ROUNDED` = `H-LV-OUT-PAYMENT * (((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)` (L1708)

### `9100-MOVE-RESULTS`

- **COMPUTE** `H-OUT-PAYMENT ROUNDED` = `H-OUT-PAYMENT / B-CLAIM-NUM-DIALYSIS-SESSIONS` (L1939)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `H-PYMT-AMT              *  COM-CBSA-BLEND-PCT` (L1945)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `H-PPS-FINAL-PAY-AMT     *  BUN-CBSA-BLEND-PCT` (L1945)
- **COMPUTE** `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` = `H-OUT-PAYMENT           *  BUN-CBSA-BLEND-PCT` (L1945)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `PPS-2011-BLEND-COMP-RATE    *  QIP-REDUCTION` (L1970)
- **COMPUTE** `PPS-2011-FULL-COMP-RATE     ROUNDED` = `PPS-2011-FULL-COMP-RATE     *  QIP-REDUCTION` (L1970)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `PPS-2011-BLEND-PPS-RATE     *  QIP-REDUCTION` (L1970)
- **COMPUTE** `PPS-2011-FULL-PPS-RATE      ROUNDED` = `PPS-2011-FULL-PPS-RATE      *  QIP-REDUCTION` (L1970)

## Copybooks

- `RTCCPY`
- `BILLCPY`
- `WAGECPY`

## Paragraphs (Action Graph)

| Paragraph | Lines | PERFORM | CALL | GO TO | IF | RC set |
|---|---|---|---|---|---|---|
| `0000-PROCEDURE-START` | 635-659 | 0 | 0 | 0 | 0 | 0 |
| `0000-START-TO-FINISH` | 660-696 | 5 | 0 | 0 | 3 | 0 |
| `1000-VALIDATE-BILL-ELEMENTS` | 697-828 | 0 | 0 | 0 | 35 | 15 |
| `1200-INITIALIZATION` | 829-848 | 0 | 0 | 0 | 0 | 0 |
| `2000-CALCULATE-BUNDLED-FACTORS` | 849-1231 | 4 | 0 | 0 | 40 | 0 |
| `2100-CALC-COMORBID-ADJUST` | 1232-1300 | 1 | 0 | 0 | 7 | 0 |
| `2500-CALC-OUTLIER-FACTORS` | 1301-1529 | 1 | 0 | 0 | 28 | 0 |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1530-1599 | 1 | 0 | 0 | 7 | 0 |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1600-1651 | 0 | 0 | 0 | 4 | 0 |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1652-1718 | 0 | 0 | 0 | 5 | 0 |
| `9000-SET-RETURN-CODE` | 1719-1900 | 0 | 0 | 0 | 32 | 33 |
| `9100-MOVE-RESULTS` | 1901-2054 | 0 | 0 | 0 | 7 | 0 |

## Execution Logic Summary (ELS)

_Auto-generated narrative per paragraph - what each routine does, which branches it evaluates, and which side effects it produces._

### `0000-PROCEDURE-START` (L635-659)

Main control routine - leaf logic block.


### `0000-START-TO-FINISH` (L660-696)

Main control routine - orchestrates 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 9000-SET-RETURN-CODE (+1 more). Contains 3 IF/branchs.

- **Calls:** `1000-VALIDATE-BILL-ELEMENTS`, `1200-INITIALIZATION`, `2000-CALCULATE-BUNDLED-FACTORS`, `9000-SET-RETURN-CODE`, `9100-MOVE-RESULTS`

### `1000-VALIDATE-BILL-ELEMENTS` (L697-828)

Validation routine - assigns return codes based on input state. Contains 35 IF/branchs. Sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '; PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE; PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN (+12 more).

- **Side effects:**
  - PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '
  - PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE
  - PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
  - PPS-RTC=54 when (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN
  - PPS-RTC=55 when (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC)
  - PPS-RTC=56 when (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC)
  - PPS-RTC=57 when B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENT?
  - PPS-RTC=53 when P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' ' THEN
  - PPS-RTC=71 when B-PATIENT-HGT > 300.00
  - PPS-RTC=72 when B-PATIENT-WGT > 500.00 THEN
  - PPS-RTC=73 when (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSI?
  - PPS-RTC=74 when (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NU?
  - PPS-RTC=75 when (B-DIALYSIS-START-DATE NOT NUMERIC) THEN
  - PPS-RTC=76 when (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN
  - PPS-RTC=81 when COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR ?

### `1200-INITIALIZATION` (L829-848)

Initialization routine - leaf logic block.


### `2000-CALCULATE-BUNDLED-FACTORS` (L849-1231)

Calculation routine - orchestrates 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT. Contains 40 IF/branchs.

- **Calls:** `2100-CALC-COMORBID-ADJUST`, `2500-CALC-OUTLIER-FACTORS`, `3000-LOW-VOL-FULL-PPS-PAYMENT`, `3100-LOW-VOL-OUT-PPS-PAYMENT`

### `2100-CALC-COMORBID-ADJUST` (L1232-1300)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `2500-CALC-OUTLIER-FACTORS` (L1301-1529)

Calculation routine - orchestrates 2600-CALC-COMORBID-OUT-ADJUST. Contains 28 IF/branchs.

- **Calls:** `2600-CALC-COMORBID-OUT-ADJUST`

### `2600-CALC-COMORBID-OUT-ADJUST` (L1530-1599)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `3000-LOW-VOL-FULL-PPS-PAYMENT` (L1600-1651)

Business routine - evaluates 4 branch conditions. Contains 4 IF/branchs.


### `3100-LOW-VOL-OUT-PPS-PAYMENT` (L1652-1718)

Business routine - evaluates 5 branch conditions. Contains 5 IF/branchs.


### `9000-SET-RETURN-CODE` (L1719-1900)

Business routine - assigns return codes based on input state. Contains 32 IF/branchs. Sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN; PPS-RTC=16 when TRAINING-TRACK = "Y" THEN; PPS-RTC=15 when TRAINING-TRACK = "Y" THEN (+30 more).

- **Side effects:**
  - PPS-RTC=17 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=16 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=14 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=24 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=19 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=29 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=23 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=18 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=30 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=28 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=34 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=35 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=33 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=07 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=06 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=09 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=03 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=26 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=21 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=12 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=25 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=20 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=32 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=10 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=27 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=22 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=11 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=08 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=04 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=05 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=31 when LOW-BMI-TRACK = "Y" THEN
  - PPS-RTC=02 when LOW-BMI-TRACK = "Y" THEN

### `9100-MOVE-RESULTS` (L1901-2054)

Business routine - evaluates 7 branch conditions. Contains 7 IF/branchs.


## TSB Risk Metric Summary (Technical & Structural Breakdown Risk)

**Average risk:** [W] 43 / 100 (MEDIUM)  
**Max paragraph risk:** [E] 100 / 100 (CRITICAL)  
**Distribution:** 4 CRITICAL ?. 0 HIGH ?. 1 MEDIUM ?. 7 LOW (of 12 paragraphs)

### Top 10 risky paragraphs

| Paragraph | Lines | Score | Category | Top factors |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 697-828 | **100** | [E] CRITICAL | 35 IF/EVAL branches, 15 return-code emissions, 131 lines (size penalty) |
| `2000-CALCULATE-BUNDLED-FACTORS` | 849-1231 | **100** | [E] CRITICAL | 40 IF/EVAL branches, 382 lines (size penalty), 4 PERFORM calls |
| `2500-CALC-OUTLIER-FACTORS` | 1301-1529 | **100** | [E] CRITICAL | 28 IF/EVAL branches, 228 lines (size penalty), 1 PERFORM calls |
| `9000-SET-RETURN-CODE` | 1719-1900 | **100** | [E] CRITICAL | 33 return-code emissions, 32 IF/EVAL branches, 181 lines (size penalty) |
| `9100-MOVE-RESULTS` | 1901-2054 | **31** | [W] MEDIUM | 7 IF/EVAL branches, 153 lines (size penalty) |
| `2100-CALC-COMORBID-ADJUST` | 1232-1300 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1530-1599 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1652-1718 | **15** | [OK] LOW | 5 IF/EVAL branches |
| `0000-START-TO-FINISH` | 660-696 | **14** | [OK] LOW | 3 IF/EVAL branches, 5 PERFORM calls |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1600-1651 | **12** | [OK] LOW | 4 IF/EVAL branches |

## Issues

- [W] **WARNING**  `escal180.cbl:L660`: Potential state leak: Flag `P-PROV-WAIVE-BLEND-PAY-INDIC` is set to 'Y' in paragraph `0000-START-TO-FINISH` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L849`: Potential state leak: Flag `LOW-BMI-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L849`: Potential state leak: Flag `H-BUN-ONSET-FACTOR` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L849`: Potential state leak: Flag `PEDIATRIC-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L849`: Potential state leak: Flag `MOVED-CORMORBIDS` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L849`: Potential state leak: Flag `ONSET-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L849`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L849`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1232`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1232`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1301`: Potential state leak: Flag `H-OUT-ONSET-FACTOR` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1301`: Potential state leak: Flag `H-OUT-LOW-VOL-MULTIPLIER` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1301`: Potential state leak: Flag `OUTLIER-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1301`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1530`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1530`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal180.cbl:L1600`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `3000-LOW-VOL-FULL-PPS-PAYMENT` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.

> **Call Graph:** Structure identical to `ESCAL170` - diagram not repeated.


## Call Graph Edges

```
          0000-START-TO-FINISH  --PERFORM-->  1000-VALIDATE-BILL-ELEMENTS (L677)
          0000-START-TO-FINISH  --PERFORM-->  1200-INITIALIZATION (L679)
          0000-START-TO-FINISH  --PERFORM-->  2000-CALCULATE-BUNDLED-FACTORS (L679)
          0000-START-TO-FINISH  --PERFORM-->  9000-SET-RETURN-CODE (L679)
          0000-START-TO-FINISH  --PERFORM-->  9100-MOVE-RESULTS (L679)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2100-CALC-COMORBID-ADJUST (L1074)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2500-CALC-OUTLIER-FACTORS (L1204)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3000-LOW-VOL-FULL-PPS-PAYMENT (L1209)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3100-LOW-VOL-OUT-PPS-PAYMENT (L1209)
     2100-CALC-COMORBID-ADJUST  --PERFORM-->   (L1244)
     2500-CALC-OUTLIER-FACTORS  --PERFORM-->  2600-CALC-COMORBID-OUT-ADJUST (L1390)
 2600-CALC-COMORBID-OUT-ADJUST  --PERFORM-->   (L1543)
```

## Return Codes (Trigger Summary)

| Paragraph | Line | RC Var | Value | Condition |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 698 | `PPS-RTC` | **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `1000-VALIDATE-BILL-ELEMENTS` | 705 | `PPS-RTC` | **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 713 | `PPS-RTC` | **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 719 | `PPS-RTC` | **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 725 | `PPS-RTC` | **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 733 | `PPS-RTC` | **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 741 | `PPS-RTC` | **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 750 | `PPS-RTC` | **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 760 | `PPS-RTC` | **71** | B-PATIENT-HGT > 300.00 |
| `1000-VALIDATE-BILL-ELEMENTS` | 768 | `PPS-RTC` | **72** | B-PATIENT-WGT > 500.00  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 781 | `PPS-RTC` | **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NUM |
| `1000-VALIDATE-BILL-ELEMENTS` | 788 | `PPS-RTC` | **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC)  THE |
| `1000-VALIDATE-BILL-ELEMENTS` | 795 | `PPS-RTC` | **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 801 | `PPS-RTC` | **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 818 | `PPS-RTC` | **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN N |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **17** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **16** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **15** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **14** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **30** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **28** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **09** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **03** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **32** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **10** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **08** | ONSET-TRACK               = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **31** | LOW-BMI-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1770 | `PPS-RTC` | **02** | LOW-BMI-TRACK = "Y"  THEN |

## State Machines (88-level)

### `IS-HIGH-COMORBID-FOUND`

- **'Y'** = HIGH-COMORBID-FOUND (L467)

---

# COBOL Program: `ESCAL191`

**Source:** `ESCAL191`  
**Lines:** 2069 total / 1218 code / 734 comments

## Inter-Service Narrative (ISN)

> **ESCAL191 - 12 paragraphs, 48 return codes, 1 state flags, 3 external copybooks**

COBOL program `ESCAL191` orchestrates a 1-step business flow. It emits 47 distinct return-code value(s) across 48 assignment site(s), driven by 1 state-machine flag group(s). Depends on 3 external copybook(s): RTCCPY, BILLCPY, WAGECPY.

**Entry point:** `0000-PROCEDURE-START`

**Top decision points (most branched paragraphs):**

- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches - sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' / PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE / PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
- `9000-SET-RETURN-CODE` - 32 branches - sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN / PPS-RTC=16 when TRAINING-TRACK = "Y" THEN / PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
- `2500-CALC-OUTLIER-FACTORS` - 28 branches
- `2100-CALC-COMORBID-ADJUST` - 7 branches

**Return-code catalog (value -> emission sites):**

| RC | Sites | Variables | Sample condition |
|---|---|---|---|
| **02** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **03** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **04** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **05** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **06** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **07** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **08** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **09** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **10** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **11** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **12** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **14** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **15** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **16** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **17** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **18** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **19** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **20** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **21** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **22** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **23** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **24** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **25** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **26** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **27** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **28** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **29** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **30** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **31** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **32** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **33** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **34** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **35** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **52** | 1 | `PPS-RTC` | P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE |
| **53** | 2 | `PPS-RTC` | P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN |
| **54** | 1 | `PPS-RTC` | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN |
| **55** | 1 | `PPS-RTC` | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| **56** | 1 | `PPS-RTC` | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| **57** | 1 | `PPS-RTC` | B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| **58** | 1 | `PPS-RTC` | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' |
| **71** | 1 | `PPS-RTC` | B-PATIENT-HGT > 300.00 |
| **72** | 1 | `PPS-RTC` | B-PATIENT-WGT > 500.00 THEN |
| **73** | 1 | `PPS-RTC` | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NU? |
| **74** | 1 | `PPS-RTC` | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC) THEN |
| **75** | 1 | `PPS-RTC` | (B-DIALYSIS-START-DATE NOT NUMERIC) THEN |
| **76** | 1 | `PPS-RTC` | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| **81** | 1 | `PPS-RTC` | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN ? |

## Stats

- Paragraphs: **12**
- PERFORM/CALL edges: **12**
- COPY references: **3**
- WORKING-STORAGE items: **168**, LINKAGE items: **198**
- Return code assignments: **48**, State machines: **1**
- Cyclomatic complexity (est): **170**

## Business Rules (Magic Numbers)

**Total:** 142 rules (41 thresholds, 71 defaults)

| Type | Key | Value | Paragraph | Line |
|------|-----|-------|-----------|------|
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `58` | `1000-VALIDATE-BILL-ELEMENTS` | 713 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `52` | `1000-VALIDATE-BILL-ELEMENTS` | 720 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 728 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `54` | `1000-VALIDATE-BILL-ELEMENTS` | 734 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `55` | `1000-VALIDATE-BILL-ELEMENTS` | 740 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `56` | `1000-VALIDATE-BILL-ELEMENTS` | 748 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `57` | `1000-VALIDATE-BILL-ELEMENTS` | 756 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 765 |
| ?? threshold | `1000_validate_bill_elements.b_patient_hgt.threshold` | `300.00` | `1000-VALIDATE-BILL-ELEMENTS` | 775 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `71` | `1000-VALIDATE-BILL-ELEMENTS` | 775 |
| ?? threshold | `1000_validate_bill_elements.b_patient_wgt.threshold` | `500.00` | `1000-VALIDATE-BILL-ELEMENTS` | 783 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `72` | `1000-VALIDATE-BILL-ELEMENTS` | 783 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `73` | `1000-VALIDATE-BILL-ELEMENTS` | 796 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `74` | `1000-VALIDATE-BILL-ELEMENTS` | 803 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `75` | `1000-VALIDATE-BILL-ELEMENTS` | 810 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `76` | `1000-VALIDATE-BILL-ELEMENTS` | 816 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `81` | `1000-VALIDATE-BILL-ELEMENTS` | 833 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 866 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `1.000` | `2000-CALCULATE-BUNDLED-FACTORS` | 876 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.995` | `2000-CALCULATE-BUNDLED-FACTORS` | 876 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.990` | `2000-CALCULATE-BUNDLED-FACTORS` | 876 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.985` | `2000-CALCULATE-BUNDLED-FACTORS` | 876 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.980` | `2000-CALCULATE-BUNDLED-FACTORS` | 876 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `13` | `2000-CALCULATE-BUNDLED-FACTORS` | 993 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 993 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `45` | `2000-CALCULATE-BUNDLED-FACTORS` | 993 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `60` | `2000-CALCULATE-BUNDLED-FACTORS` | 993 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `70` | `2000-CALCULATE-BUNDLED-FACTORS` | 993 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `80` | `2000-CALCULATE-BUNDLED-FACTORS` | 993 |
| ?? constant | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` | `.007184` | `2000-CALCULATE-BUNDLED-FACTORS` | 1034 |

_... +112 more rules in `--extract-rules` output_

## Business Logic (Computed Values & Lookups)

_What this program actually calculates: 49 formulas/lookups/loops/call-params across 9 paragraphs._

### `0000-START-TO-FINISH`

- **INITIALIZE** `PPS-DATA-ALL` (L676)
- **INITIALIZE** `BILL-DATA-TEST` (L684)
- **INITIALIZE** `COND-CD-73` (L684)

### `1200-INITIALIZATION`

- **INITIALIZE** `HOLD-COMP-RATE-PPS-COMPONENTS` (L845)
- **INITIALIZE** `HOLD-BUNDLED-PPS-COMPONENTS` (L846)
- **INITIALIZE** `HOLD-OUTLIER-PPS-COMPONENTS` (L847)
- **INITIALIZE** `PAID-RETURN-CODE-TRACKERS` (L848)
- **COMPUTE** `H-BUN-NAT-LABOR-AMT ROUNDED` = `(BUNDLED-BASE-PMT-RATE * BUN-NAT-LABOR-PCT) * BUN-CBSA-W-INDEX.` (L854)
- **COMPUTE** `H-BUN-NAT-NONLABOR-AMT ROUNDED` = `BUNDLED-BASE-PMT-RATE * BUN-NAT-NONLABOR-PCT` (L858)
- **COMPUTE** `H-BUN-BASE-WAGE-AMT ROUNDED` = `H-BUN-NAT-LABOR-AMT + H-BUN-NAT-NONLABOR-AMT.` (L858)

### `2000-CALCULATE-BUNDLED-FACTORS`

- **COMPUTE** `H-PATIENT-AGE` = `B-THRU-CCYY - B-DOB-CCYY` (L866)
- **COMPUTE** `H-PATIENT-AGE` = `H-PATIENT-AGE - 1` (L866)
- **COMPUTE** `H-BUN-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1034)
- **COMPUTE** `H-BUN-BSA-FACTOR  ROUNDED` = `CM-BSA ** ((H-BUN-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1034)
- **COMPUTE** `H-BUN-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1048)
- **COMPUTE** `INTEGER-LINE-ITEM-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1061)
- **COMPUTE** `INTEGER-DIALYSIS-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1061)
- **COMPUTE** `ONSET-DATE` = `(INTEGER-LINE-ITEM-DATE - INTEGER-DIALYSIS-DATE) + 1` (L1061)

### `2100-CALC-COMORBID-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1259)

### `2500-CALC-OUTLIER-FACTORS`

- **COMPUTE** `H-OUT-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1361)
- **COMPUTE** `H-OUT-BSA-FACTOR  ROUNDED` = `SB-BSA ** ((H-OUT-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1361)
- **COMPUTE** `H-OUT-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1375)
- **COMPUTE** `H-OUT-PREDICTED-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1467)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1479)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1479)
- **COMPUTE** `H-HEMO-EQUIV-DIAL-SESSIONS  ROUNDED` = `((B-CLAIM-NUM-DIALYSIS-SESSIONS * 3) / 7)` (L1493)
- **COMPUTE** `H-OUT-IMPUTED-MAP  ROUNDED` = `(B-TOT-PRICE-SB-OUTLIER / H-HEMO-EQUIV-DIAL-SESSIONS)` (L1493)

### `2600-CALC-COMORBID-OUT-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1558)

### `3000-LOW-VOL-FULL-PPS-PAYMENT`

- **COMPUTE** `H-LV-BUN-ADJUST-BASE-WAGE-AMT  ROUNDED` = `(H-BUN-BASE-WAGE-AMT * H-BUN-AGE-FACTOR)     * (H-BUN-BSA-FACTOR    * H-BUN-BMI-FACTOR)     * (H-BUN-ONSET-FACTOR  * H-B` (L1618)
- **COMPUTE** `H-BUN-WAGE-ADJ-TRAINING-AMT  ROUNDED` = `TRAINING-ADD-ON-PMT-AMT * BUN-CBSA-W-INDEX` (L1627)
- **COMPUTE** `H-CC-74-PER-DIEM-AMT  ROUNDED` = `(H-LV-BUN-ADJUST-BASE-WAGE-AMT * 3) / 7` (L1627)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-CC-74-PER-DIEM-AMT` (L1653)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-LV-BUN-ADJUST-BASE-WAGE-AMT + H-BUN-WAGE-ADJ-TRAINING-AMT` (L1653)

### `3100-LOW-VOL-OUT-PPS-PAYMENT`

- **COMPUTE** `H-LV-OUT-PREDICT-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1670)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1680)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1680)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-LT-18` (L1696)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-LT-18` (L1696)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-GT-17` (L1696)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-GT-17` (L1696)
- **COMPUTE** `H-LV-OUT-PAYMENT ROUNDED` = `H-LV-OUT-PAYMENT * (((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)` (L1723)

### `9100-MOVE-RESULTS`

- **COMPUTE** `H-OUT-PAYMENT ROUNDED` = `H-OUT-PAYMENT / B-CLAIM-NUM-DIALYSIS-SESSIONS` (L1954)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `H-PYMT-AMT              *  COM-CBSA-BLEND-PCT` (L1960)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `H-PPS-FINAL-PAY-AMT     *  BUN-CBSA-BLEND-PCT` (L1960)
- **COMPUTE** `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` = `H-OUT-PAYMENT           *  BUN-CBSA-BLEND-PCT` (L1960)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `PPS-2011-BLEND-COMP-RATE    *  QIP-REDUCTION` (L1985)
- **COMPUTE** `PPS-2011-FULL-COMP-RATE     ROUNDED` = `PPS-2011-FULL-COMP-RATE     *  QIP-REDUCTION` (L1985)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `PPS-2011-BLEND-PPS-RATE     *  QIP-REDUCTION` (L1985)
- **COMPUTE** `PPS-2011-FULL-PPS-RATE      ROUNDED` = `PPS-2011-FULL-PPS-RATE      *  QIP-REDUCTION` (L1985)

## Copybooks

- `RTCCPY`
- `BILLCPY`
- `WAGECPY`

## Paragraphs (Action Graph)

| Paragraph | Lines | PERFORM | CALL | GO TO | IF | RC set |
|---|---|---|---|---|---|---|
| `0000-PROCEDURE-START` | 650-674 | 0 | 0 | 0 | 0 | 0 |
| `0000-START-TO-FINISH` | 675-711 | 5 | 0 | 0 | 3 | 0 |
| `1000-VALIDATE-BILL-ELEMENTS` | 712-843 | 0 | 0 | 0 | 35 | 15 |
| `1200-INITIALIZATION` | 844-863 | 0 | 0 | 0 | 0 | 0 |
| `2000-CALCULATE-BUNDLED-FACTORS` | 864-1246 | 4 | 0 | 0 | 40 | 0 |
| `2100-CALC-COMORBID-ADJUST` | 1247-1315 | 1 | 0 | 0 | 7 | 0 |
| `2500-CALC-OUTLIER-FACTORS` | 1316-1544 | 1 | 0 | 0 | 28 | 0 |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1545-1614 | 1 | 0 | 0 | 7 | 0 |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1615-1666 | 0 | 0 | 0 | 4 | 0 |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1667-1733 | 0 | 0 | 0 | 5 | 0 |
| `9000-SET-RETURN-CODE` | 1734-1915 | 0 | 0 | 0 | 32 | 33 |
| `9100-MOVE-RESULTS` | 1916-2069 | 0 | 0 | 0 | 7 | 0 |

## Execution Logic Summary (ELS)

_Auto-generated narrative per paragraph - what each routine does, which branches it evaluates, and which side effects it produces._

### `0000-PROCEDURE-START` (L650-674)

Main control routine - leaf logic block.


### `0000-START-TO-FINISH` (L675-711)

Main control routine - orchestrates 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 9000-SET-RETURN-CODE (+1 more). Contains 3 IF/branchs.

- **Calls:** `1000-VALIDATE-BILL-ELEMENTS`, `1200-INITIALIZATION`, `2000-CALCULATE-BUNDLED-FACTORS`, `9000-SET-RETURN-CODE`, `9100-MOVE-RESULTS`

### `1000-VALIDATE-BILL-ELEMENTS` (L712-843)

Validation routine - assigns return codes based on input state. Contains 35 IF/branchs. Sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '; PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE; PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN (+12 more).

- **Side effects:**
  - PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '
  - PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE
  - PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
  - PPS-RTC=54 when (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN
  - PPS-RTC=55 when (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC)
  - PPS-RTC=56 when (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC)
  - PPS-RTC=57 when B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENT?
  - PPS-RTC=53 when P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' ' THEN
  - PPS-RTC=71 when B-PATIENT-HGT > 300.00
  - PPS-RTC=72 when B-PATIENT-WGT > 500.00 THEN
  - PPS-RTC=73 when (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSI?
  - PPS-RTC=74 when (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NU?
  - PPS-RTC=75 when (B-DIALYSIS-START-DATE NOT NUMERIC) THEN
  - PPS-RTC=76 when (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN
  - PPS-RTC=81 when COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR ?

### `1200-INITIALIZATION` (L844-863)

Initialization routine - leaf logic block.


### `2000-CALCULATE-BUNDLED-FACTORS` (L864-1246)

Calculation routine - orchestrates 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT. Contains 40 IF/branchs.

- **Calls:** `2100-CALC-COMORBID-ADJUST`, `2500-CALC-OUTLIER-FACTORS`, `3000-LOW-VOL-FULL-PPS-PAYMENT`, `3100-LOW-VOL-OUT-PPS-PAYMENT`

### `2100-CALC-COMORBID-ADJUST` (L1247-1315)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `2500-CALC-OUTLIER-FACTORS` (L1316-1544)

Calculation routine - orchestrates 2600-CALC-COMORBID-OUT-ADJUST. Contains 28 IF/branchs.

- **Calls:** `2600-CALC-COMORBID-OUT-ADJUST`

### `2600-CALC-COMORBID-OUT-ADJUST` (L1545-1614)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `3000-LOW-VOL-FULL-PPS-PAYMENT` (L1615-1666)

Business routine - evaluates 4 branch conditions. Contains 4 IF/branchs.


### `3100-LOW-VOL-OUT-PPS-PAYMENT` (L1667-1733)

Business routine - evaluates 5 branch conditions. Contains 5 IF/branchs.


### `9000-SET-RETURN-CODE` (L1734-1915)

Business routine - assigns return codes based on input state. Contains 32 IF/branchs. Sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN; PPS-RTC=16 when TRAINING-TRACK = "Y" THEN; PPS-RTC=15 when TRAINING-TRACK = "Y" THEN (+30 more).

- **Side effects:**
  - PPS-RTC=17 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=16 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=14 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=24 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=19 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=29 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=23 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=18 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=30 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=28 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=34 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=35 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=33 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=07 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=06 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=09 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=03 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=26 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=21 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=12 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=25 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=20 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=32 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=10 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=27 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=22 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=11 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=08 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=04 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=05 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=31 when LOW-BMI-TRACK = "Y" THEN
  - PPS-RTC=02 when LOW-BMI-TRACK = "Y" THEN

### `9100-MOVE-RESULTS` (L1916-2069)

Business routine - evaluates 7 branch conditions. Contains 7 IF/branchs.


## TSB Risk Metric Summary (Technical & Structural Breakdown Risk)

**Average risk:** [W] 43 / 100 (MEDIUM)  
**Max paragraph risk:** [E] 100 / 100 (CRITICAL)  
**Distribution:** 4 CRITICAL ?. 0 HIGH ?. 1 MEDIUM ?. 7 LOW (of 12 paragraphs)

### Top 10 risky paragraphs

| Paragraph | Lines | Score | Category | Top factors |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 712-843 | **100** | [E] CRITICAL | 35 IF/EVAL branches, 15 return-code emissions, 131 lines (size penalty) |
| `2000-CALCULATE-BUNDLED-FACTORS` | 864-1246 | **100** | [E] CRITICAL | 40 IF/EVAL branches, 382 lines (size penalty), 4 PERFORM calls |
| `2500-CALC-OUTLIER-FACTORS` | 1316-1544 | **100** | [E] CRITICAL | 28 IF/EVAL branches, 228 lines (size penalty), 1 PERFORM calls |
| `9000-SET-RETURN-CODE` | 1734-1915 | **100** | [E] CRITICAL | 33 return-code emissions, 32 IF/EVAL branches, 181 lines (size penalty) |
| `9100-MOVE-RESULTS` | 1916-2069 | **31** | [W] MEDIUM | 7 IF/EVAL branches, 153 lines (size penalty) |
| `2100-CALC-COMORBID-ADJUST` | 1247-1315 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1545-1614 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1667-1733 | **15** | [OK] LOW | 5 IF/EVAL branches |
| `0000-START-TO-FINISH` | 675-711 | **14** | [OK] LOW | 3 IF/EVAL branches, 5 PERFORM calls |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1615-1666 | **12** | [OK] LOW | 4 IF/EVAL branches |

## Issues

- [W] **WARNING**  `escal191.cbl:L675`: Potential state leak: Flag `P-PROV-WAIVE-BLEND-PAY-INDIC` is set to 'Y' in paragraph `0000-START-TO-FINISH` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L864`: Potential state leak: Flag `H-BUN-ONSET-FACTOR` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L864`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L864`: Potential state leak: Flag `ONSET-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L864`: Potential state leak: Flag `LOW-BMI-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L864`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L864`: Potential state leak: Flag `PEDIATRIC-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L864`: Potential state leak: Flag `MOVED-CORMORBIDS` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1247`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1247`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1316`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1316`: Potential state leak: Flag `H-OUT-ONSET-FACTOR` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1316`: Potential state leak: Flag `H-OUT-LOW-VOL-MULTIPLIER` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1316`: Potential state leak: Flag `OUTLIER-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1545`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1545`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal191.cbl:L1615`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `3000-LOW-VOL-FULL-PPS-PAYMENT` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.

> **Call Graph:** Structure identical to `ESCAL170` - diagram not repeated.


## Call Graph Edges

```
          0000-START-TO-FINISH  --PERFORM-->  1000-VALIDATE-BILL-ELEMENTS (L692)
          0000-START-TO-FINISH  --PERFORM-->  1200-INITIALIZATION (L694)
          0000-START-TO-FINISH  --PERFORM-->  2000-CALCULATE-BUNDLED-FACTORS (L694)
          0000-START-TO-FINISH  --PERFORM-->  9000-SET-RETURN-CODE (L694)
          0000-START-TO-FINISH  --PERFORM-->  9100-MOVE-RESULTS (L694)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2100-CALC-COMORBID-ADJUST (L1089)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2500-CALC-OUTLIER-FACTORS (L1219)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3000-LOW-VOL-FULL-PPS-PAYMENT (L1224)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3100-LOW-VOL-OUT-PPS-PAYMENT (L1224)
     2100-CALC-COMORBID-ADJUST  --PERFORM-->   (L1259)
     2500-CALC-OUTLIER-FACTORS  --PERFORM-->  2600-CALC-COMORBID-OUT-ADJUST (L1405)
 2600-CALC-COMORBID-OUT-ADJUST  --PERFORM-->   (L1558)
```

## Return Codes (Trigger Summary)

| Paragraph | Line | RC Var | Value | Condition |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 713 | `PPS-RTC` | **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `1000-VALIDATE-BILL-ELEMENTS` | 720 | `PPS-RTC` | **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 728 | `PPS-RTC` | **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 734 | `PPS-RTC` | **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 740 | `PPS-RTC` | **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 748 | `PPS-RTC` | **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 756 | `PPS-RTC` | **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 765 | `PPS-RTC` | **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 775 | `PPS-RTC` | **71** | B-PATIENT-HGT > 300.00 |
| `1000-VALIDATE-BILL-ELEMENTS` | 783 | `PPS-RTC` | **72** | B-PATIENT-WGT > 500.00  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 796 | `PPS-RTC` | **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NUM |
| `1000-VALIDATE-BILL-ELEMENTS` | 803 | `PPS-RTC` | **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC)  THE |
| `1000-VALIDATE-BILL-ELEMENTS` | 810 | `PPS-RTC` | **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 816 | `PPS-RTC` | **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 833 | `PPS-RTC` | **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN N |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **17** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **16** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **15** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **14** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **30** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **28** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **09** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **03** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **32** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **10** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **08** | ONSET-TRACK               = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **31** | LOW-BMI-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1785 | `PPS-RTC` | **02** | LOW-BMI-TRACK = "Y"  THEN |

## State Machines (88-level)

### `IS-HIGH-COMORBID-FOUND`

- **'Y'** = HIGH-COMORBID-FOUND (L482)

---

# COBOL Program: `ESCAL200`

**Source:** `ESCAL200`  
**Lines:** 2084 total / 1218 code / 749 comments

## Inter-Service Narrative (ISN)

> **ESCAL200 - 12 paragraphs, 48 return codes, 1 state flags, 3 external copybooks**

COBOL program `ESCAL200` orchestrates a 1-step business flow. It emits 47 distinct return-code value(s) across 48 assignment site(s), driven by 1 state-machine flag group(s). Depends on 3 external copybook(s): RTCCPY, BILLCPY, WAGECPY.

**Entry point:** `0000-PROCEDURE-START`

**Top decision points (most branched paragraphs):**

- `2000-CALCULATE-BUNDLED-FACTORS` - 40 branches
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches - sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' / PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE / PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
- `9000-SET-RETURN-CODE` - 32 branches - sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN / PPS-RTC=16 when TRAINING-TRACK = "Y" THEN / PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
- `2500-CALC-OUTLIER-FACTORS` - 28 branches
- `2100-CALC-COMORBID-ADJUST` - 7 branches

**Return-code catalog (value -> emission sites):**

| RC | Sites | Variables | Sample condition |
|---|---|---|---|
| **02** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **03** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **04** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **05** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **06** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **07** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **08** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **09** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **10** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **11** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **12** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **14** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **15** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **16** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **17** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **18** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **19** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **20** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **21** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **22** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **23** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **24** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **25** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **26** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **27** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **28** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **29** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **30** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **31** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **32** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **33** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **34** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **35** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **52** | 1 | `PPS-RTC` | P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE |
| **53** | 2 | `PPS-RTC` | P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN |
| **54** | 1 | `PPS-RTC` | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN |
| **55** | 1 | `PPS-RTC` | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| **56** | 1 | `PPS-RTC` | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| **57** | 1 | `PPS-RTC` | B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| **58** | 1 | `PPS-RTC` | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' |
| **71** | 1 | `PPS-RTC` | B-PATIENT-HGT > 300.00 |
| **72** | 1 | `PPS-RTC` | B-PATIENT-WGT > 500.00 THEN |
| **73** | 1 | `PPS-RTC` | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NU? |
| **74** | 1 | `PPS-RTC` | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC) THEN |
| **75** | 1 | `PPS-RTC` | (B-DIALYSIS-START-DATE NOT NUMERIC) THEN |
| **76** | 1 | `PPS-RTC` | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| **81** | 1 | `PPS-RTC` | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN ? |

## Stats

- Paragraphs: **12**
- PERFORM/CALL edges: **12**
- COPY references: **3**
- WORKING-STORAGE items: **168**, LINKAGE items: **198**
- Return code assignments: **48**, State machines: **1**
- Cyclomatic complexity (est): **170**

## Business Rules (Magic Numbers)

**Total:** 142 rules (41 thresholds, 71 defaults)

| Type | Key | Value | Paragraph | Line |
|------|-----|-------|-----------|------|
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `58` | `1000-VALIDATE-BILL-ELEMENTS` | 728 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `52` | `1000-VALIDATE-BILL-ELEMENTS` | 735 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 743 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `54` | `1000-VALIDATE-BILL-ELEMENTS` | 749 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `55` | `1000-VALIDATE-BILL-ELEMENTS` | 755 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `56` | `1000-VALIDATE-BILL-ELEMENTS` | 763 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `57` | `1000-VALIDATE-BILL-ELEMENTS` | 771 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 780 |
| ?? threshold | `1000_validate_bill_elements.b_patient_hgt.threshold` | `300.00` | `1000-VALIDATE-BILL-ELEMENTS` | 790 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `71` | `1000-VALIDATE-BILL-ELEMENTS` | 790 |
| ?? threshold | `1000_validate_bill_elements.b_patient_wgt.threshold` | `500.00` | `1000-VALIDATE-BILL-ELEMENTS` | 798 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `72` | `1000-VALIDATE-BILL-ELEMENTS` | 798 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `73` | `1000-VALIDATE-BILL-ELEMENTS` | 811 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `74` | `1000-VALIDATE-BILL-ELEMENTS` | 818 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `75` | `1000-VALIDATE-BILL-ELEMENTS` | 825 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `76` | `1000-VALIDATE-BILL-ELEMENTS` | 831 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `81` | `1000-VALIDATE-BILL-ELEMENTS` | 848 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 881 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `1.000` | `2000-CALCULATE-BUNDLED-FACTORS` | 891 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.995` | `2000-CALCULATE-BUNDLED-FACTORS` | 891 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.990` | `2000-CALCULATE-BUNDLED-FACTORS` | 891 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.985` | `2000-CALCULATE-BUNDLED-FACTORS` | 891 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.980` | `2000-CALCULATE-BUNDLED-FACTORS` | 891 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `13` | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `45` | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `60` | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `70` | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `80` | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 |
| ?? constant | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` | `.007184` | `2000-CALCULATE-BUNDLED-FACTORS` | 1049 |

_... +112 more rules in `--extract-rules` output_

## Business Logic (Computed Values & Lookups)

_What this program actually calculates: 49 formulas/lookups/loops/call-params across 9 paragraphs._

### `0000-START-TO-FINISH`

- **INITIALIZE** `PPS-DATA-ALL` (L691)
- **INITIALIZE** `BILL-DATA-TEST` (L699)
- **INITIALIZE** `COND-CD-73` (L699)

### `1200-INITIALIZATION`

- **INITIALIZE** `HOLD-COMP-RATE-PPS-COMPONENTS` (L860)
- **INITIALIZE** `HOLD-BUNDLED-PPS-COMPONENTS` (L861)
- **INITIALIZE** `HOLD-OUTLIER-PPS-COMPONENTS` (L862)
- **INITIALIZE** `PAID-RETURN-CODE-TRACKERS` (L863)
- **COMPUTE** `H-BUN-NAT-LABOR-AMT ROUNDED` = `(BUNDLED-BASE-PMT-RATE * BUN-NAT-LABOR-PCT) * BUN-CBSA-W-INDEX.` (L869)
- **COMPUTE** `H-BUN-NAT-NONLABOR-AMT ROUNDED` = `BUNDLED-BASE-PMT-RATE * BUN-NAT-NONLABOR-PCT` (L873)
- **COMPUTE** `H-BUN-BASE-WAGE-AMT ROUNDED` = `H-BUN-NAT-LABOR-AMT + H-BUN-NAT-NONLABOR-AMT.` (L873)

### `2000-CALCULATE-BUNDLED-FACTORS`

- **COMPUTE** `H-PATIENT-AGE` = `B-THRU-CCYY - B-DOB-CCYY` (L881)
- **COMPUTE** `H-PATIENT-AGE` = `H-PATIENT-AGE - 1` (L881)
- **COMPUTE** `H-BUN-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1049)
- **COMPUTE** `H-BUN-BSA-FACTOR  ROUNDED` = `CM-BSA ** ((H-BUN-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1049)
- **COMPUTE** `H-BUN-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1063)
- **COMPUTE** `INTEGER-LINE-ITEM-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1076)
- **COMPUTE** `INTEGER-DIALYSIS-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1076)
- **COMPUTE** `ONSET-DATE` = `(INTEGER-LINE-ITEM-DATE - INTEGER-DIALYSIS-DATE) + 1` (L1076)

### `2100-CALC-COMORBID-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1274)

### `2500-CALC-OUTLIER-FACTORS`

- **COMPUTE** `H-OUT-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1376)
- **COMPUTE** `H-OUT-BSA-FACTOR  ROUNDED` = `SB-BSA ** ((H-OUT-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1376)
- **COMPUTE** `H-OUT-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1390)
- **COMPUTE** `H-OUT-PREDICTED-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1482)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1494)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1494)
- **COMPUTE** `H-HEMO-EQUIV-DIAL-SESSIONS  ROUNDED` = `((B-CLAIM-NUM-DIALYSIS-SESSIONS * 3) / 7)` (L1508)
- **COMPUTE** `H-OUT-IMPUTED-MAP  ROUNDED` = `(B-TOT-PRICE-SB-OUTLIER / H-HEMO-EQUIV-DIAL-SESSIONS)` (L1508)

### `2600-CALC-COMORBID-OUT-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1573)

### `3000-LOW-VOL-FULL-PPS-PAYMENT`

- **COMPUTE** `H-LV-BUN-ADJUST-BASE-WAGE-AMT  ROUNDED` = `(H-BUN-BASE-WAGE-AMT * H-BUN-AGE-FACTOR)     * (H-BUN-BSA-FACTOR    * H-BUN-BMI-FACTOR)     * (H-BUN-ONSET-FACTOR  * H-B` (L1633)
- **COMPUTE** `H-BUN-WAGE-ADJ-TRAINING-AMT  ROUNDED` = `TRAINING-ADD-ON-PMT-AMT * BUN-CBSA-W-INDEX` (L1642)
- **COMPUTE** `H-CC-74-PER-DIEM-AMT  ROUNDED` = `(H-LV-BUN-ADJUST-BASE-WAGE-AMT * 3) / 7` (L1642)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-CC-74-PER-DIEM-AMT` (L1668)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-LV-BUN-ADJUST-BASE-WAGE-AMT + H-BUN-WAGE-ADJ-TRAINING-AMT` (L1668)

### `3100-LOW-VOL-OUT-PPS-PAYMENT`

- **COMPUTE** `H-LV-OUT-PREDICT-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1685)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1695)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1695)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-LT-18` (L1711)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-LT-18` (L1711)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-GT-17` (L1711)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-GT-17` (L1711)
- **COMPUTE** `H-LV-OUT-PAYMENT ROUNDED` = `H-LV-OUT-PAYMENT * (((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)` (L1738)

### `9100-MOVE-RESULTS`

- **COMPUTE** `H-OUT-PAYMENT ROUNDED` = `H-OUT-PAYMENT / B-CLAIM-NUM-DIALYSIS-SESSIONS` (L1969)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `H-PYMT-AMT              *  COM-CBSA-BLEND-PCT` (L1975)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `H-PPS-FINAL-PAY-AMT     *  BUN-CBSA-BLEND-PCT` (L1975)
- **COMPUTE** `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` = `H-OUT-PAYMENT           *  BUN-CBSA-BLEND-PCT` (L1975)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `PPS-2011-BLEND-COMP-RATE    *  QIP-REDUCTION` (L2000)
- **COMPUTE** `PPS-2011-FULL-COMP-RATE     ROUNDED` = `PPS-2011-FULL-COMP-RATE     *  QIP-REDUCTION` (L2000)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `PPS-2011-BLEND-PPS-RATE     *  QIP-REDUCTION` (L2000)
- **COMPUTE** `PPS-2011-FULL-PPS-RATE      ROUNDED` = `PPS-2011-FULL-PPS-RATE      *  QIP-REDUCTION` (L2000)

## Copybooks

- `RTCCPY`
- `BILLCPY`
- `WAGECPY`

## Paragraphs (Action Graph)

| Paragraph | Lines | PERFORM | CALL | GO TO | IF | RC set |
|---|---|---|---|---|---|---|
| `0000-PROCEDURE-START` | 665-689 | 0 | 0 | 0 | 0 | 0 |
| `0000-START-TO-FINISH` | 690-726 | 5 | 0 | 0 | 3 | 0 |
| `1000-VALIDATE-BILL-ELEMENTS` | 727-858 | 0 | 0 | 0 | 35 | 15 |
| `1200-INITIALIZATION` | 859-878 | 0 | 0 | 0 | 0 | 0 |
| `2000-CALCULATE-BUNDLED-FACTORS` | 879-1261 | 4 | 0 | 0 | 40 | 0 |
| `2100-CALC-COMORBID-ADJUST` | 1262-1330 | 1 | 0 | 0 | 7 | 0 |
| `2500-CALC-OUTLIER-FACTORS` | 1331-1559 | 1 | 0 | 0 | 28 | 0 |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1560-1629 | 1 | 0 | 0 | 7 | 0 |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1630-1681 | 0 | 0 | 0 | 4 | 0 |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1682-1748 | 0 | 0 | 0 | 5 | 0 |
| `9000-SET-RETURN-CODE` | 1749-1930 | 0 | 0 | 0 | 32 | 33 |
| `9100-MOVE-RESULTS` | 1931-2084 | 0 | 0 | 0 | 7 | 0 |

## Execution Logic Summary (ELS)

_Auto-generated narrative per paragraph - what each routine does, which branches it evaluates, and which side effects it produces._

### `0000-PROCEDURE-START` (L665-689)

Main control routine - leaf logic block.


### `0000-START-TO-FINISH` (L690-726)

Main control routine - orchestrates 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 9000-SET-RETURN-CODE (+1 more). Contains 3 IF/branchs.

- **Calls:** `1000-VALIDATE-BILL-ELEMENTS`, `1200-INITIALIZATION`, `2000-CALCULATE-BUNDLED-FACTORS`, `9000-SET-RETURN-CODE`, `9100-MOVE-RESULTS`

### `1000-VALIDATE-BILL-ELEMENTS` (L727-858)

Validation routine - assigns return codes based on input state. Contains 35 IF/branchs. Sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '; PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE; PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN (+12 more).

- **Side effects:**
  - PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '
  - PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE
  - PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
  - PPS-RTC=54 when (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN
  - PPS-RTC=55 when (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC)
  - PPS-RTC=56 when (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC)
  - PPS-RTC=57 when B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENT?
  - PPS-RTC=53 when P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' ' THEN
  - PPS-RTC=71 when B-PATIENT-HGT > 300.00
  - PPS-RTC=72 when B-PATIENT-WGT > 500.00 THEN
  - PPS-RTC=73 when (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSI?
  - PPS-RTC=74 when (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NU?
  - PPS-RTC=75 when (B-DIALYSIS-START-DATE NOT NUMERIC) THEN
  - PPS-RTC=76 when (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN
  - PPS-RTC=81 when COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR ?

### `1200-INITIALIZATION` (L859-878)

Initialization routine - leaf logic block.


### `2000-CALCULATE-BUNDLED-FACTORS` (L879-1261)

Calculation routine - orchestrates 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT. Contains 40 IF/branchs.

- **Calls:** `2100-CALC-COMORBID-ADJUST`, `2500-CALC-OUTLIER-FACTORS`, `3000-LOW-VOL-FULL-PPS-PAYMENT`, `3100-LOW-VOL-OUT-PPS-PAYMENT`

### `2100-CALC-COMORBID-ADJUST` (L1262-1330)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `2500-CALC-OUTLIER-FACTORS` (L1331-1559)

Calculation routine - orchestrates 2600-CALC-COMORBID-OUT-ADJUST. Contains 28 IF/branchs.

- **Calls:** `2600-CALC-COMORBID-OUT-ADJUST`

### `2600-CALC-COMORBID-OUT-ADJUST` (L1560-1629)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `3000-LOW-VOL-FULL-PPS-PAYMENT` (L1630-1681)

Business routine - evaluates 4 branch conditions. Contains 4 IF/branchs.


### `3100-LOW-VOL-OUT-PPS-PAYMENT` (L1682-1748)

Business routine - evaluates 5 branch conditions. Contains 5 IF/branchs.


### `9000-SET-RETURN-CODE` (L1749-1930)

Business routine - assigns return codes based on input state. Contains 32 IF/branchs. Sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN; PPS-RTC=16 when TRAINING-TRACK = "Y" THEN; PPS-RTC=15 when TRAINING-TRACK = "Y" THEN (+30 more).

- **Side effects:**
  - PPS-RTC=17 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=16 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=14 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=24 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=19 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=29 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=23 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=18 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=30 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=28 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=34 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=35 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=33 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=07 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=06 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=09 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=03 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=26 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=21 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=12 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=25 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=20 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=32 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=10 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=27 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=22 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=11 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=08 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=04 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=05 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=31 when LOW-BMI-TRACK = "Y" THEN
  - PPS-RTC=02 when LOW-BMI-TRACK = "Y" THEN

### `9100-MOVE-RESULTS` (L1931-2084)

Business routine - evaluates 7 branch conditions. Contains 7 IF/branchs.


## TSB Risk Metric Summary (Technical & Structural Breakdown Risk)

**Average risk:** [W] 43 / 100 (MEDIUM)  
**Max paragraph risk:** [E] 100 / 100 (CRITICAL)  
**Distribution:** 4 CRITICAL ?. 0 HIGH ?. 1 MEDIUM ?. 7 LOW (of 12 paragraphs)

### Top 10 risky paragraphs

| Paragraph | Lines | Score | Category | Top factors |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 727-858 | **100** | [E] CRITICAL | 35 IF/EVAL branches, 15 return-code emissions, 131 lines (size penalty) |
| `2000-CALCULATE-BUNDLED-FACTORS` | 879-1261 | **100** | [E] CRITICAL | 40 IF/EVAL branches, 382 lines (size penalty), 4 PERFORM calls |
| `2500-CALC-OUTLIER-FACTORS` | 1331-1559 | **100** | [E] CRITICAL | 28 IF/EVAL branches, 228 lines (size penalty), 1 PERFORM calls |
| `9000-SET-RETURN-CODE` | 1749-1930 | **100** | [E] CRITICAL | 33 return-code emissions, 32 IF/EVAL branches, 181 lines (size penalty) |
| `9100-MOVE-RESULTS` | 1931-2084 | **31** | [W] MEDIUM | 7 IF/EVAL branches, 153 lines (size penalty) |
| `2100-CALC-COMORBID-ADJUST` | 1262-1330 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1560-1629 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1682-1748 | **15** | [OK] LOW | 5 IF/EVAL branches |
| `0000-START-TO-FINISH` | 690-726 | **14** | [OK] LOW | 3 IF/EVAL branches, 5 PERFORM calls |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1630-1681 | **12** | [OK] LOW | 4 IF/EVAL branches |

## Issues

- [W] **WARNING**  `escal200.cbl:L690`: Potential state leak: Flag `P-PROV-WAIVE-BLEND-PAY-INDIC` is set to 'Y' in paragraph `0000-START-TO-FINISH` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L879`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L879`: Potential state leak: Flag `PEDIATRIC-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L879`: Potential state leak: Flag `H-BUN-ONSET-FACTOR` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L879`: Potential state leak: Flag `MOVED-CORMORBIDS` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L879`: Potential state leak: Flag `ONSET-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L879`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L879`: Potential state leak: Flag `LOW-BMI-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1262`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1262`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1331`: Potential state leak: Flag `H-OUT-ONSET-FACTOR` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1331`: Potential state leak: Flag `OUTLIER-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1331`: Potential state leak: Flag `H-OUT-LOW-VOL-MULTIPLIER` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1331`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1560`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1560`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal200.cbl:L1630`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `3000-LOW-VOL-FULL-PPS-PAYMENT` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.

> **Call Graph:** Structure identical to `ESCAL170` - diagram not repeated.


## Call Graph Edges

```
          0000-START-TO-FINISH  --PERFORM-->  1000-VALIDATE-BILL-ELEMENTS (L707)
          0000-START-TO-FINISH  --PERFORM-->  1200-INITIALIZATION (L709)
          0000-START-TO-FINISH  --PERFORM-->  2000-CALCULATE-BUNDLED-FACTORS (L709)
          0000-START-TO-FINISH  --PERFORM-->  9000-SET-RETURN-CODE (L709)
          0000-START-TO-FINISH  --PERFORM-->  9100-MOVE-RESULTS (L709)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2100-CALC-COMORBID-ADJUST (L1104)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2500-CALC-OUTLIER-FACTORS (L1234)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3000-LOW-VOL-FULL-PPS-PAYMENT (L1239)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3100-LOW-VOL-OUT-PPS-PAYMENT (L1239)
     2100-CALC-COMORBID-ADJUST  --PERFORM-->   (L1274)
     2500-CALC-OUTLIER-FACTORS  --PERFORM-->  2600-CALC-COMORBID-OUT-ADJUST (L1420)
 2600-CALC-COMORBID-OUT-ADJUST  --PERFORM-->   (L1573)
```

## Return Codes (Trigger Summary)

| Paragraph | Line | RC Var | Value | Condition |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 728 | `PPS-RTC` | **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `1000-VALIDATE-BILL-ELEMENTS` | 735 | `PPS-RTC` | **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 743 | `PPS-RTC` | **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 749 | `PPS-RTC` | **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 755 | `PPS-RTC` | **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 763 | `PPS-RTC` | **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 771 | `PPS-RTC` | **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 780 | `PPS-RTC` | **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 790 | `PPS-RTC` | **71** | B-PATIENT-HGT > 300.00 |
| `1000-VALIDATE-BILL-ELEMENTS` | 798 | `PPS-RTC` | **72** | B-PATIENT-WGT > 500.00  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 811 | `PPS-RTC` | **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NUM |
| `1000-VALIDATE-BILL-ELEMENTS` | 818 | `PPS-RTC` | **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC)  THE |
| `1000-VALIDATE-BILL-ELEMENTS` | 825 | `PPS-RTC` | **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 831 | `PPS-RTC` | **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 848 | `PPS-RTC` | **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN N |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **17** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **16** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **15** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **14** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **30** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **28** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **09** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **03** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **32** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **10** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **08** | ONSET-TRACK               = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **31** | LOW-BMI-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1800 | `PPS-RTC` | **02** | LOW-BMI-TRACK = "Y"  THEN |

## State Machines (88-level)

### `IS-HIGH-COMORBID-FOUND`

- **'Y'** = HIGH-COMORBID-FOUND (L497)

---

# COBOL Program: `ESCAL202`

**Source:** `ESCAL202`  
**Lines:** 2168 total / 1250 code / 787 comments

## Inter-Service Narrative (ISN)

> **ESCAL202 - 12 paragraphs, 48 return codes, 1 state flags, 3 external copybooks**

COBOL program `ESCAL202` orchestrates a 1-step business flow. It emits 47 distinct return-code value(s) across 48 assignment site(s), driven by 1 state-machine flag group(s). Depends on 3 external copybook(s): RTCCPY, BILLCPY, WAGECPY.

**Entry point:** `0000-PROCEDURE-START`

**Top decision points (most branched paragraphs):**

- `2000-CALCULATE-BUNDLED-FACTORS` - 41 branches
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches - sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' / PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE / PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
- `9000-SET-RETURN-CODE` - 32 branches - sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN / PPS-RTC=16 when TRAINING-TRACK = "Y" THEN / PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
- `2500-CALC-OUTLIER-FACTORS` - 28 branches
- `9100-MOVE-RESULTS` - 8 branches

**Return-code catalog (value -> emission sites):**

| RC | Sites | Variables | Sample condition |
|---|---|---|---|
| **02** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **03** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **04** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **05** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **06** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **07** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **08** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **09** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **10** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **11** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **12** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **14** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **15** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **16** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **17** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **18** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **19** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **20** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **21** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **22** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **23** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **24** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **25** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **26** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **27** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **28** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **29** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **30** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **31** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **32** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **33** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **34** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **35** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **52** | 1 | `PPS-RTC` | P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE |
| **53** | 2 | `PPS-RTC` | P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN |
| **54** | 1 | `PPS-RTC` | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN |
| **55** | 1 | `PPS-RTC` | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| **56** | 1 | `PPS-RTC` | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| **57** | 1 | `PPS-RTC` | B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| **58** | 1 | `PPS-RTC` | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' |
| **71** | 1 | `PPS-RTC` | B-PATIENT-HGT > 300.00 |
| **72** | 1 | `PPS-RTC` | B-PATIENT-WGT > 500.00 THEN |
| **73** | 1 | `PPS-RTC` | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NU? |
| **74** | 1 | `PPS-RTC` | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC) THEN |
| **75** | 1 | `PPS-RTC` | (B-DIALYSIS-START-DATE NOT NUMERIC) THEN |
| **76** | 1 | `PPS-RTC` | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| **81** | 1 | `PPS-RTC` | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN ? |

## Stats

- Paragraphs: **12**
- PERFORM/CALL edges: **12**
- COPY references: **3**
- WORKING-STORAGE items: **173**, LINKAGE items: **198**
- Return code assignments: **48**, State machines: **1**
- Cyclomatic complexity (est): **172**

## Business Rules (Magic Numbers)

**Total:** 140 rules (41 thresholds, 71 defaults)

| Type | Key | Value | Paragraph | Line |
|------|-----|-------|-----------|------|
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `58` | `1000-VALIDATE-BILL-ELEMENTS` | 755 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `52` | `1000-VALIDATE-BILL-ELEMENTS` | 762 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 770 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `54` | `1000-VALIDATE-BILL-ELEMENTS` | 776 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `55` | `1000-VALIDATE-BILL-ELEMENTS` | 782 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `56` | `1000-VALIDATE-BILL-ELEMENTS` | 790 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `57` | `1000-VALIDATE-BILL-ELEMENTS` | 798 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 807 |
| ?? threshold | `1000_validate_bill_elements.b_patient_hgt.threshold` | `300.00` | `1000-VALIDATE-BILL-ELEMENTS` | 817 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `71` | `1000-VALIDATE-BILL-ELEMENTS` | 817 |
| ?? threshold | `1000_validate_bill_elements.b_patient_wgt.threshold` | `500.00` | `1000-VALIDATE-BILL-ELEMENTS` | 825 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `72` | `1000-VALIDATE-BILL-ELEMENTS` | 825 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `73` | `1000-VALIDATE-BILL-ELEMENTS` | 838 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `74` | `1000-VALIDATE-BILL-ELEMENTS` | 845 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `75` | `1000-VALIDATE-BILL-ELEMENTS` | 852 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `76` | `1000-VALIDATE-BILL-ELEMENTS` | 858 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `81` | `1000-VALIDATE-BILL-ELEMENTS` | 875 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 908 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `1.000` | `2000-CALCULATE-BUNDLED-FACTORS` | 918 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.995` | `2000-CALCULATE-BUNDLED-FACTORS` | 918 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.990` | `2000-CALCULATE-BUNDLED-FACTORS` | 918 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.985` | `2000-CALCULATE-BUNDLED-FACTORS` | 918 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.980` | `2000-CALCULATE-BUNDLED-FACTORS` | 918 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `13` | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `45` | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `60` | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `70` | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `80` | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 |
| ?? constant | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` | `.007184` | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 |

_... +110 more rules in `--extract-rules` output_

## Business Logic (Computed Values & Lookups)

_What this program actually calculates: 49 formulas/lookups/loops/call-params across 9 paragraphs._

### `0000-START-TO-FINISH`

- **INITIALIZE** `PPS-DATA-ALL` (L718)
- **INITIALIZE** `BILL-DATA-TEST` (L726)
- **INITIALIZE** `COND-CD-73` (L726)

### `1200-INITIALIZATION`

- **INITIALIZE** `HOLD-COMP-RATE-PPS-COMPONENTS` (L887)
- **INITIALIZE** `HOLD-BUNDLED-PPS-COMPONENTS` (L888)
- **INITIALIZE** `HOLD-OUTLIER-PPS-COMPONENTS` (L889)
- **INITIALIZE** `PAID-RETURN-CODE-TRACKERS` (L890)
- **COMPUTE** `H-BUN-NAT-LABOR-AMT ROUNDED` = `(BUNDLED-BASE-PMT-RATE * BUN-NAT-LABOR-PCT) * BUN-CBSA-W-INDEX.` (L896)
- **COMPUTE** `H-BUN-NAT-NONLABOR-AMT ROUNDED` = `BUNDLED-BASE-PMT-RATE * BUN-NAT-NONLABOR-PCT` (L900)
- **COMPUTE** `H-BUN-BASE-WAGE-AMT ROUNDED` = `H-BUN-NAT-LABOR-AMT + H-BUN-NAT-NONLABOR-AMT.` (L900)

### `2000-CALCULATE-BUNDLED-FACTORS`

- **COMPUTE** `H-PATIENT-AGE` = `B-THRU-CCYY - B-DOB-CCYY` (L908)
- **COMPUTE** `H-PATIENT-AGE` = `H-PATIENT-AGE - 1` (L908)
- **COMPUTE** `H-BUN-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1076)
- **COMPUTE** `H-BUN-BSA-FACTOR  ROUNDED` = `CM-BSA ** ((H-BUN-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1076)
- **COMPUTE** `H-BUN-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1090)
- **COMPUTE** `INTEGER-LINE-ITEM-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1103)
- **COMPUTE** `INTEGER-DIALYSIS-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1103)
- **COMPUTE** `ONSET-DATE` = `(INTEGER-LINE-ITEM-DATE - INTEGER-DIALYSIS-DATE) + 1` (L1103)

### `2100-CALC-COMORBID-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1329)

### `2500-CALC-OUTLIER-FACTORS`

- **COMPUTE** `H-OUT-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1431)
- **COMPUTE** `H-OUT-BSA-FACTOR  ROUNDED` = `SB-BSA ** ((H-OUT-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1431)
- **COMPUTE** `H-OUT-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1445)
- **COMPUTE** `H-OUT-PREDICTED-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1537)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1549)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1549)
- **COMPUTE** `H-HEMO-EQUIV-DIAL-SESSIONS  ROUNDED` = `((B-CLAIM-NUM-DIALYSIS-SESSIONS * 3) / 7)` (L1563)
- **COMPUTE** `H-OUT-IMPUTED-MAP  ROUNDED` = `(B-TOT-PRICE-SB-OUTLIER / H-HEMO-EQUIV-DIAL-SESSIONS)` (L1563)

### `2600-CALC-COMORBID-OUT-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1628)

### `3000-LOW-VOL-FULL-PPS-PAYMENT`

- **COMPUTE** `H-LV-BUN-ADJUST-BASE-WAGE-AMT  ROUNDED` = `(H-BUN-BASE-WAGE-AMT * H-BUN-AGE-FACTOR)     * (H-BUN-BSA-FACTOR    * H-BUN-BMI-FACTOR)     * (H-BUN-ONSET-FACTOR  * H-B` (L1688)
- **COMPUTE** `H-BUN-WAGE-ADJ-TRAINING-AMT  ROUNDED` = `TRAINING-ADD-ON-PMT-AMT * BUN-CBSA-W-INDEX` (L1697)
- **COMPUTE** `H-CC-74-PER-DIEM-AMT  ROUNDED` = `(H-LV-BUN-ADJUST-BASE-WAGE-AMT * 3) / 7` (L1697)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-CC-74-PER-DIEM-AMT` (L1723)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-LV-BUN-ADJUST-BASE-WAGE-AMT + H-BUN-WAGE-ADJ-TRAINING-AMT` (L1723)

### `3100-LOW-VOL-OUT-PPS-PAYMENT`

- **COMPUTE** `H-LV-OUT-PREDICT-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1740)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1750)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1750)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-LT-18` (L1766)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-LT-18` (L1766)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-GT-17` (L1766)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-GT-17` (L1766)
- **COMPUTE** `H-LV-OUT-PAYMENT ROUNDED` = `H-LV-OUT-PAYMENT * (((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)` (L1793)

### `9100-MOVE-RESULTS`

- **COMPUTE** `H-OUT-PAYMENT ROUNDED` = `H-OUT-PAYMENT / B-CLAIM-NUM-DIALYSIS-SESSIONS` (L2024)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `H-PYMT-AMT              *  COM-CBSA-BLEND-PCT` (L2030)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `H-PPS-FINAL-PAY-AMT     *  BUN-CBSA-BLEND-PCT` (L2030)
- **COMPUTE** `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` = `H-OUT-PAYMENT           *  BUN-CBSA-BLEND-PCT` (L2030)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `PPS-2011-BLEND-COMP-RATE    *  QIP-REDUCTION` (L2057)
- **COMPUTE** `PPS-2011-FULL-COMP-RATE     ROUNDED` = `PPS-2011-FULL-COMP-RATE     *  QIP-REDUCTION` (L2057)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `PPS-2011-BLEND-PPS-RATE     *  QIP-REDUCTION` (L2057)
- **COMPUTE** `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` = `PPS-2011-BLEND-OUTLIER-RATE *  QIP-REDUCTION` (L2057)

## Copybooks

- `RTCCPY`
- `BILLCPY`
- `WAGECPY`

## Paragraphs (Action Graph)

| Paragraph | Lines | PERFORM | CALL | GO TO | IF | RC set |
|---|---|---|---|---|---|---|
| `0000-PROCEDURE-START` | 692-716 | 0 | 0 | 0 | 0 | 0 |
| `0000-START-TO-FINISH` | 717-753 | 5 | 0 | 0 | 3 | 0 |
| `1000-VALIDATE-BILL-ELEMENTS` | 754-885 | 0 | 0 | 0 | 35 | 15 |
| `1200-INITIALIZATION` | 886-905 | 0 | 0 | 0 | 0 | 0 |
| `2000-CALCULATE-BUNDLED-FACTORS` | 906-1316 | 4 | 0 | 0 | 41 | 0 |
| `2100-CALC-COMORBID-ADJUST` | 1317-1385 | 1 | 0 | 0 | 7 | 0 |
| `2500-CALC-OUTLIER-FACTORS` | 1386-1614 | 1 | 0 | 0 | 28 | 0 |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1615-1684 | 1 | 0 | 0 | 7 | 0 |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1685-1736 | 0 | 0 | 0 | 4 | 0 |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1737-1803 | 0 | 0 | 0 | 5 | 0 |
| `9000-SET-RETURN-CODE` | 1804-1985 | 0 | 0 | 0 | 32 | 33 |
| `9100-MOVE-RESULTS` | 1986-2168 | 0 | 0 | 0 | 8 | 0 |

## Execution Logic Summary (ELS)

_Auto-generated narrative per paragraph - what each routine does, which branches it evaluates, and which side effects it produces._

### `0000-PROCEDURE-START` (L692-716)

Main control routine - leaf logic block.


### `0000-START-TO-FINISH` (L717-753)

Main control routine - orchestrates 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 9000-SET-RETURN-CODE (+1 more). Contains 3 IF/branchs.

- **Calls:** `1000-VALIDATE-BILL-ELEMENTS`, `1200-INITIALIZATION`, `2000-CALCULATE-BUNDLED-FACTORS`, `9000-SET-RETURN-CODE`, `9100-MOVE-RESULTS`

### `1000-VALIDATE-BILL-ELEMENTS` (L754-885)

Validation routine - assigns return codes based on input state. Contains 35 IF/branchs. Sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '; PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE; PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN (+12 more).

- **Side effects:**
  - PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '
  - PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE
  - PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
  - PPS-RTC=54 when (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN
  - PPS-RTC=55 when (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC)
  - PPS-RTC=56 when (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC)
  - PPS-RTC=57 when B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENT?
  - PPS-RTC=53 when P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' ' THEN
  - PPS-RTC=71 when B-PATIENT-HGT > 300.00
  - PPS-RTC=72 when B-PATIENT-WGT > 500.00 THEN
  - PPS-RTC=73 when (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSI?
  - PPS-RTC=74 when (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NU?
  - PPS-RTC=75 when (B-DIALYSIS-START-DATE NOT NUMERIC) THEN
  - PPS-RTC=76 when (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN
  - PPS-RTC=81 when COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR ?

### `1200-INITIALIZATION` (L886-905)

Initialization routine - leaf logic block.


### `2000-CALCULATE-BUNDLED-FACTORS` (L906-1316)

Calculation routine - orchestrates 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT. Contains 41 IF/branchs.

- **Calls:** `2100-CALC-COMORBID-ADJUST`, `2500-CALC-OUTLIER-FACTORS`, `3000-LOW-VOL-FULL-PPS-PAYMENT`, `3100-LOW-VOL-OUT-PPS-PAYMENT`

### `2100-CALC-COMORBID-ADJUST` (L1317-1385)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `2500-CALC-OUTLIER-FACTORS` (L1386-1614)

Calculation routine - orchestrates 2600-CALC-COMORBID-OUT-ADJUST. Contains 28 IF/branchs.

- **Calls:** `2600-CALC-COMORBID-OUT-ADJUST`

### `2600-CALC-COMORBID-OUT-ADJUST` (L1615-1684)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `3000-LOW-VOL-FULL-PPS-PAYMENT` (L1685-1736)

Business routine - evaluates 4 branch conditions. Contains 4 IF/branchs.


### `3100-LOW-VOL-OUT-PPS-PAYMENT` (L1737-1803)

Business routine - evaluates 5 branch conditions. Contains 5 IF/branchs.


### `9000-SET-RETURN-CODE` (L1804-1985)

Business routine - assigns return codes based on input state. Contains 32 IF/branchs. Sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN; PPS-RTC=16 when TRAINING-TRACK = "Y" THEN; PPS-RTC=15 when TRAINING-TRACK = "Y" THEN (+30 more).

- **Side effects:**
  - PPS-RTC=17 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=16 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=14 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=24 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=19 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=29 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=23 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=18 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=30 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=28 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=34 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=35 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=33 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=07 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=06 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=09 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=03 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=26 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=21 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=12 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=25 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=20 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=32 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=10 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=27 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=22 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=11 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=08 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=04 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=05 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=31 when LOW-BMI-TRACK = "Y" THEN
  - PPS-RTC=02 when LOW-BMI-TRACK = "Y" THEN

### `9100-MOVE-RESULTS` (L1986-2168)

Business routine - evaluates 8 branch conditions. Contains 8 IF/branchs.


## TSB Risk Metric Summary (Technical & Structural Breakdown Risk)

**Average risk:** [W] 43 / 100 (MEDIUM)  
**Max paragraph risk:** [E] 100 / 100 (CRITICAL)  
**Distribution:** 4 CRITICAL ?. 0 HIGH ?. 1 MEDIUM ?. 7 LOW (of 12 paragraphs)

### Top 10 risky paragraphs

| Paragraph | Lines | Score | Category | Top factors |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 754-885 | **100** | [E] CRITICAL | 35 IF/EVAL branches, 15 return-code emissions, 131 lines (size penalty) |
| `2000-CALCULATE-BUNDLED-FACTORS` | 906-1316 | **100** | [E] CRITICAL | 41 IF/EVAL branches, 410 lines (size penalty), 4 PERFORM calls |
| `2500-CALC-OUTLIER-FACTORS` | 1386-1614 | **100** | [E] CRITICAL | 28 IF/EVAL branches, 228 lines (size penalty), 1 PERFORM calls |
| `9000-SET-RETURN-CODE` | 1804-1985 | **100** | [E] CRITICAL | 33 return-code emissions, 32 IF/EVAL branches, 181 lines (size penalty) |
| `9100-MOVE-RESULTS` | 1986-2168 | **34** | [W] MEDIUM | 8 IF/EVAL branches, 182 lines (size penalty) |
| `2100-CALC-COMORBID-ADJUST` | 1317-1385 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1615-1684 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1737-1803 | **15** | [OK] LOW | 5 IF/EVAL branches |
| `0000-START-TO-FINISH` | 717-753 | **14** | [OK] LOW | 3 IF/EVAL branches, 5 PERFORM calls |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1685-1736 | **12** | [OK] LOW | 4 IF/EVAL branches |

## Issues

- [W] **WARNING**  `escal202.cbl:L717`: Potential state leak: Flag `P-PROV-WAIVE-BLEND-PAY-INDIC` is set to 'Y' in paragraph `0000-START-TO-FINISH` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L906`: Potential state leak: Flag `H-BUN-ONSET-FACTOR` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L906`: Potential state leak: Flag `LOW-BMI-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L906`: Potential state leak: Flag `ONSET-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L906`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L906`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L906`: Potential state leak: Flag `MOVED-CORMORBIDS` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L906`: Potential state leak: Flag `PEDIATRIC-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1317`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1317`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1386`: Potential state leak: Flag `OUTLIER-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1386`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1386`: Potential state leak: Flag `H-OUT-ONSET-FACTOR` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1386`: Potential state leak: Flag `H-OUT-LOW-VOL-MULTIPLIER` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1615`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1615`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal202.cbl:L1685`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `3000-LOW-VOL-FULL-PPS-PAYMENT` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.

> **Call Graph:** Structure identical to `ESCAL170` - diagram not repeated.


## Call Graph Edges

```
          0000-START-TO-FINISH  --PERFORM-->  1000-VALIDATE-BILL-ELEMENTS (L734)
          0000-START-TO-FINISH  --PERFORM-->  1200-INITIALIZATION (L736)
          0000-START-TO-FINISH  --PERFORM-->  2000-CALCULATE-BUNDLED-FACTORS (L736)
          0000-START-TO-FINISH  --PERFORM-->  9000-SET-RETURN-CODE (L736)
          0000-START-TO-FINISH  --PERFORM-->  9100-MOVE-RESULTS (L736)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2100-CALC-COMORBID-ADJUST (L1131)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2500-CALC-OUTLIER-FACTORS (L1289)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3000-LOW-VOL-FULL-PPS-PAYMENT (L1294)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3100-LOW-VOL-OUT-PPS-PAYMENT (L1294)
     2100-CALC-COMORBID-ADJUST  --PERFORM-->   (L1329)
     2500-CALC-OUTLIER-FACTORS  --PERFORM-->  2600-CALC-COMORBID-OUT-ADJUST (L1475)
 2600-CALC-COMORBID-OUT-ADJUST  --PERFORM-->   (L1628)
```

## Return Codes (Trigger Summary)

| Paragraph | Line | RC Var | Value | Condition |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 755 | `PPS-RTC` | **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `1000-VALIDATE-BILL-ELEMENTS` | 762 | `PPS-RTC` | **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 770 | `PPS-RTC` | **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 776 | `PPS-RTC` | **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 782 | `PPS-RTC` | **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 790 | `PPS-RTC` | **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 798 | `PPS-RTC` | **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 807 | `PPS-RTC` | **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 817 | `PPS-RTC` | **71** | B-PATIENT-HGT > 300.00 |
| `1000-VALIDATE-BILL-ELEMENTS` | 825 | `PPS-RTC` | **72** | B-PATIENT-WGT > 500.00  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 838 | `PPS-RTC` | **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NUM |
| `1000-VALIDATE-BILL-ELEMENTS` | 845 | `PPS-RTC` | **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC)  THE |
| `1000-VALIDATE-BILL-ELEMENTS` | 852 | `PPS-RTC` | **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 858 | `PPS-RTC` | **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 875 | `PPS-RTC` | **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN N |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **17** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **16** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **15** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **14** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **30** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **28** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **09** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **03** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **32** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **10** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **08** | ONSET-TRACK               = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **31** | LOW-BMI-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1855 | `PPS-RTC` | **02** | LOW-BMI-TRACK = "Y"  THEN |

## State Machines (88-level)

### `IS-HIGH-COMORBID-FOUND`

- **'Y'** = HIGH-COMORBID-FOUND (L520)

---

# COBOL Program: `ESCAL212`

**Source:** `ESCAL212`  
**Lines:** 2253 total / 1272 code / 841 comments

## Inter-Service Narrative (ISN)

> **ESCAL212 - 12 paragraphs, 48 return codes, 1 state flags, 3 external copybooks**

COBOL program `ESCAL212` orchestrates a 1-step business flow. It emits 47 distinct return-code value(s) across 48 assignment site(s), driven by 1 state-machine flag group(s). Depends on 3 external copybook(s): RTCCPY, BILLCPY, WAGECPY.

**Entry point:** `0000-PROCEDURE-START`

**Top decision points (most branched paragraphs):**

- `2000-CALCULATE-BUNDLED-FACTORS` - 43 branches
- `1000-VALIDATE-BILL-ELEMENTS` - 35 branches - sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' / PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE / PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
- `9000-SET-RETURN-CODE` - 32 branches - sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN / PPS-RTC=16 when TRAINING-TRACK = "Y" THEN / PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
- `2500-CALC-OUTLIER-FACTORS` - 28 branches
- `9100-MOVE-RESULTS` - 9 branches

**Return-code catalog (value -> emission sites):**

| RC | Sites | Variables | Sample condition |
|---|---|---|---|
| **02** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **03** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **04** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **05** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **06** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **07** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **08** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **09** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **10** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **11** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **12** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **14** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **15** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **16** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **17** | 1 | `PPS-RTC` | TRAINING-TRACK = "Y" THEN |
| **18** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **19** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **20** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **21** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **22** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **23** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **24** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **25** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **26** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **27** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **28** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **29** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **30** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **31** | 1 | `PPS-RTC` | LOW-BMI-TRACK = "Y" THEN |
| **32** | 1 | `PPS-RTC` | ONSET-TRACK = "Y" THEN |
| **33** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **34** | 1 | `PPS-RTC` | CHRONIC-COMORBID-TRACK = "Y" THEN |
| **35** | 1 | `PPS-RTC` | ACUTE-COMORBID-TRACK = "Y" THEN |
| **52** | 1 | `PPS-RTC` | P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE |
| **53** | 2 | `PPS-RTC` | P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN |
| **54** | 1 | `PPS-RTC` | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN |
| **55** | 1 | `PPS-RTC` | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| **56** | 1 | `PPS-RTC` | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| **57** | 1 | `PPS-RTC` | B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| **58** | 1 | `PPS-RTC` | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' ' |
| **71** | 1 | `PPS-RTC` | B-PATIENT-HGT > 300.00 |
| **72** | 1 | `PPS-RTC` | B-PATIENT-WGT > 500.00 THEN |
| **73** | 1 | `PPS-RTC` | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NU? |
| **74** | 1 | `PPS-RTC` | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC) THEN |
| **75** | 1 | `PPS-RTC` | (B-DIALYSIS-START-DATE NOT NUMERIC) THEN |
| **76** | 1 | `PPS-RTC` | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| **81** | 1 | `PPS-RTC` | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN ? |

## Stats

- Paragraphs: **12**
- PERFORM/CALL edges: **12**
- COPY references: **3**
- WORKING-STORAGE items: **175**, LINKAGE items: **198**
- Return code assignments: **48**, State machines: **1**
- Cyclomatic complexity (est): **175**

## Business Rules (Magic Numbers)

**Total:** 143 rules (41 thresholds, 73 defaults)

| Type | Key | Value | Paragraph | Line |
|------|-----|-------|-----------|------|
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `58` | `1000-VALIDATE-BILL-ELEMENTS` | 796 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `52` | `1000-VALIDATE-BILL-ELEMENTS` | 803 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 811 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `54` | `1000-VALIDATE-BILL-ELEMENTS` | 817 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `55` | `1000-VALIDATE-BILL-ELEMENTS` | 823 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `56` | `1000-VALIDATE-BILL-ELEMENTS` | 831 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `57` | `1000-VALIDATE-BILL-ELEMENTS` | 839 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `53` | `1000-VALIDATE-BILL-ELEMENTS` | 848 |
| ?? threshold | `1000_validate_bill_elements.b_patient_hgt.threshold` | `300.00` | `1000-VALIDATE-BILL-ELEMENTS` | 858 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `71` | `1000-VALIDATE-BILL-ELEMENTS` | 858 |
| ?? threshold | `1000_validate_bill_elements.b_patient_wgt.threshold` | `500.00` | `1000-VALIDATE-BILL-ELEMENTS` | 866 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `72` | `1000-VALIDATE-BILL-ELEMENTS` | 866 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `73` | `1000-VALIDATE-BILL-ELEMENTS` | 879 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `74` | `1000-VALIDATE-BILL-ELEMENTS` | 886 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `75` | `1000-VALIDATE-BILL-ELEMENTS` | 893 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `76` | `1000-VALIDATE-BILL-ELEMENTS` | 899 |
| ?????? default | `1000_validate_bill_elements.pps_rtc.default` | `81` | `1000-VALIDATE-BILL-ELEMENTS` | 916 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 949 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `1.000` | `2000-CALCULATE-BUNDLED-FACTORS` | 959 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.995` | `2000-CALCULATE-BUNDLED-FACTORS` | 959 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.990` | `2000-CALCULATE-BUNDLED-FACTORS` | 959 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.985` | `2000-CALCULATE-BUNDLED-FACTORS` | 959 |
| ?????? default | `2000_calculate_bundled_factors.qip_reduction.default` | `0.980` | `2000-CALCULATE-BUNDLED-FACTORS` | 959 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `13` | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `18` | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `45` | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `60` | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `70` | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 |
| ?? threshold | `2000_calculate_bundled_factors.h_patient_age.threshold` | `80` | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 |
| ?? constant | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` | `.007184` | `2000-CALCULATE-BUNDLED-FACTORS` | 1117 |

_... +113 more rules in `--extract-rules` output_

## Business Logic (Computed Values & Lookups)

_What this program actually calculates: 49 formulas/lookups/loops/call-params across 9 paragraphs._

### `0000-START-TO-FINISH`

- **INITIALIZE** `PPS-DATA-ALL` (L759)
- **INITIALIZE** `BILL-DATA-TEST` (L767)
- **INITIALIZE** `COND-CD-73` (L767)

### `1200-INITIALIZATION`

- **INITIALIZE** `HOLD-COMP-RATE-PPS-COMPONENTS` (L928)
- **INITIALIZE** `HOLD-BUNDLED-PPS-COMPONENTS` (L929)
- **INITIALIZE** `HOLD-OUTLIER-PPS-COMPONENTS` (L930)
- **INITIALIZE** `PAID-RETURN-CODE-TRACKERS` (L931)
- **COMPUTE** `H-BUN-NAT-LABOR-AMT ROUNDED` = `(BUNDLED-BASE-PMT-RATE * BUN-NAT-LABOR-PCT) * BUN-CBSA-W-INDEX.` (L937)
- **COMPUTE** `H-BUN-NAT-NONLABOR-AMT ROUNDED` = `BUNDLED-BASE-PMT-RATE * BUN-NAT-NONLABOR-PCT` (L941)
- **COMPUTE** `H-BUN-BASE-WAGE-AMT ROUNDED` = `H-BUN-NAT-LABOR-AMT + H-BUN-NAT-NONLABOR-AMT.` (L941)

### `2000-CALCULATE-BUNDLED-FACTORS`

- **COMPUTE** `H-PATIENT-AGE` = `B-THRU-CCYY - B-DOB-CCYY` (L949)
- **COMPUTE** `H-PATIENT-AGE` = `H-PATIENT-AGE - 1` (L949)
- **COMPUTE** `H-BUN-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1117)
- **COMPUTE** `H-BUN-BSA-FACTOR  ROUNDED` = `CM-BSA ** ((H-BUN-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1117)
- **COMPUTE** `H-BUN-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1131)
- **COMPUTE** `INTEGER-LINE-ITEM-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1144)
- **COMPUTE** `INTEGER-DIALYSIS-DATE` = `FUNCTION INTEGER-OF-DATE(THE-DATE)` (L1144)
- **COMPUTE** `ONSET-DATE` = `(INTEGER-LINE-ITEM-DATE - INTEGER-DIALYSIS-DATE) + 1` (L1144)

### `2100-CALC-COMORBID-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1395)

### `2500-CALC-OUTLIER-FACTORS`

- **COMPUTE** `H-OUT-BSA  ROUNDED` = `(.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))` (L1497)
- **COMPUTE** `H-OUT-BSA-FACTOR  ROUNDED` = `SB-BSA ** ((H-OUT-BSA - BSA-NATIONAL-AVERAGE) / .1)` (L1497)
- **COMPUTE** `H-OUT-BMI  ROUNDED` = `(B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.` (L1511)
- **COMPUTE** `H-OUT-PREDICTED-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1603)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1615)
- **COMPUTE** `H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED` = `(H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1615)
- **COMPUTE** `H-HEMO-EQUIV-DIAL-SESSIONS  ROUNDED` = `((B-CLAIM-NUM-DIALYSIS-SESSIONS * 3) / 7)` (L1629)
- **COMPUTE** `H-OUT-IMPUTED-MAP  ROUNDED` = `(B-TOT-PRICE-SB-OUTLIER / H-HEMO-EQUIV-DIAL-SESSIONS)` (L1629)

### `2600-CALC-COMORBID-OUT-ADJUST`

- **PERFORM** `` UNTIL SUB   >  6   OR   HIGH-COMORBID-FOUND (L1694)

### `3000-LOW-VOL-FULL-PPS-PAYMENT`

- **COMPUTE** `H-LV-BUN-ADJUST-BASE-WAGE-AMT  ROUNDED` = `(H-BUN-BASE-WAGE-AMT * H-BUN-AGE-FACTOR)     * (H-BUN-BSA-FACTOR    * H-BUN-BMI-FACTOR)     * (H-BUN-ONSET-FACTOR  * H-B` (L1754)
- **COMPUTE** `H-BUN-WAGE-ADJ-TRAINING-AMT  ROUNDED` = `TRAINING-ADD-ON-PMT-AMT * BUN-CBSA-W-INDEX` (L1763)
- **COMPUTE** `H-CC-74-PER-DIEM-AMT  ROUNDED` = `(H-LV-BUN-ADJUST-BASE-WAGE-AMT * 3) / 7` (L1763)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-CC-74-PER-DIEM-AMT` (L1789)
- **COMPUTE** `H-LV-PPS-FINAL-PAY-AMT  ROUNDED` = `H-LV-BUN-ADJUST-BASE-WAGE-AMT + H-BUN-WAGE-ADJ-TRAINING-AMT` (L1789)

### `3100-LOW-VOL-OUT-PPS-PAYMENT`

- **COMPUTE** `H-LV-OUT-PREDICT-SERVICES-MAP  ROUNDED` = `(H-OUT-AGE-FACTOR             * H-OUT-BSA-FACTOR             * H-OUT-BMI-FACTOR             * H-OUT-ONSET-FACTOR        ` (L1806)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)` (L1816)
- **COMPUTE** `H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED` = `(H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)` (L1816)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-LT-18` (L1832)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-LT-18` (L1832)
- **COMPUTE** `H-LV-OUT-PREDICTED-MAP  ROUNDED` = `H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-GT-17` (L1832)
- **COMPUTE** `H-LV-OUT-PAYMENT  ROUNDED` = `(H-OUT-IMPUTED-MAP  -  H-LV-OUT-PREDICTED-MAP)  * LOSS-SHARING-PCT-GT-17` (L1832)
- **COMPUTE** `H-LV-OUT-PAYMENT ROUNDED` = `H-LV-OUT-PAYMENT * (((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)` (L1859)

### `9100-MOVE-RESULTS`

- **COMPUTE** `H-OUT-PAYMENT ROUNDED` = `H-OUT-PAYMENT / B-CLAIM-NUM-DIALYSIS-SESSIONS` (L2090)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `H-PYMT-AMT              *  COM-CBSA-BLEND-PCT` (L2096)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `H-PPS-FINAL-PAY-AMT     *  BUN-CBSA-BLEND-PCT` (L2096)
- **COMPUTE** `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` = `H-OUT-PAYMENT           *  BUN-CBSA-BLEND-PCT` (L2096)
- **COMPUTE** `PPS-2011-BLEND-COMP-RATE    ROUNDED` = `PPS-2011-BLEND-COMP-RATE    *  QIP-REDUCTION` (L2133)
- **COMPUTE** `PPS-2011-FULL-COMP-RATE     ROUNDED` = `PPS-2011-FULL-COMP-RATE     *  QIP-REDUCTION` (L2133)
- **COMPUTE** `PPS-2011-BLEND-PPS-RATE     ROUNDED` = `PPS-2011-BLEND-PPS-RATE     *  QIP-REDUCTION` (L2133)
- **COMPUTE** `PPS-2011-BLEND-OUTLIER-RATE ROUNDED` = `PPS-2011-BLEND-OUTLIER-RATE *  QIP-REDUCTION` (L2133)

## Copybooks

- `RTCCPY`
- `BILLCPY`
- `WAGECPY`

## Paragraphs (Action Graph)

| Paragraph | Lines | PERFORM | CALL | GO TO | IF | RC set |
|---|---|---|---|---|---|---|
| `0000-PROCEDURE-START` | 733-757 | 0 | 0 | 0 | 0 | 0 |
| `0000-START-TO-FINISH` | 758-794 | 5 | 0 | 0 | 3 | 0 |
| `1000-VALIDATE-BILL-ELEMENTS` | 795-926 | 0 | 0 | 0 | 35 | 15 |
| `1200-INITIALIZATION` | 927-946 | 0 | 0 | 0 | 0 | 0 |
| `2000-CALCULATE-BUNDLED-FACTORS` | 947-1382 | 4 | 0 | 0 | 43 | 0 |
| `2100-CALC-COMORBID-ADJUST` | 1383-1451 | 1 | 0 | 0 | 7 | 0 |
| `2500-CALC-OUTLIER-FACTORS` | 1452-1680 | 1 | 0 | 0 | 28 | 0 |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1681-1750 | 1 | 0 | 0 | 7 | 0 |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1751-1802 | 0 | 0 | 0 | 4 | 0 |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1803-1869 | 0 | 0 | 0 | 5 | 0 |
| `9000-SET-RETURN-CODE` | 1870-2051 | 0 | 0 | 0 | 32 | 33 |
| `9100-MOVE-RESULTS` | 2052-2253 | 0 | 0 | 0 | 9 | 0 |

## Execution Logic Summary (ELS)

_Auto-generated narrative per paragraph - what each routine does, which branches it evaluates, and which side effects it produces._

### `0000-PROCEDURE-START` (L733-757)

Main control routine - leaf logic block.


### `0000-START-TO-FINISH` (L758-794)

Main control routine - orchestrates 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 9000-SET-RETURN-CODE (+1 more). Contains 3 IF/branchs.

- **Calls:** `1000-VALIDATE-BILL-ELEMENTS`, `1200-INITIALIZATION`, `2000-CALCULATE-BUNDLED-FACTORS`, `9000-SET-RETURN-CODE`, `9100-MOVE-RESULTS`

### `1000-VALIDATE-BILL-ELEMENTS` (L795-926)

Validation routine - assigns return codes based on input state. Contains 35 IF/branchs. Sets: PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '; PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE; PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN (+12 more).

- **Side effects:**
  - PPS-RTC=58 when B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND ' '
  - PPS-RTC=52 when P-PROV-TYPE = '40' OR '41' OR '05' THEN NEXT SENTENCE
  - PPS-RTC=53 when P-SPEC-PYMT-IND NOT = '1' AND ' ' THEN
  - PPS-RTC=54 when (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) THEN
  - PPS-RTC=55 when (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC)
  - PPS-RTC=56 when (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC)
  - PPS-RTC=57 when B-REV-CODE = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENT?
  - PPS-RTC=53 when P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' ' THEN
  - PPS-RTC=71 when B-PATIENT-HGT > 300.00
  - PPS-RTC=72 when B-PATIENT-WGT > 500.00 THEN
  - PPS-RTC=73 when (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSI?
  - PPS-RTC=74 when (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NU?
  - PPS-RTC=75 when (B-DIALYSIS-START-DATE NOT NUMERIC) THEN
  - PPS-RTC=76 when (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN
  - PPS-RTC=81 when COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR ?

### `1200-INITIALIZATION` (L927-946)

Initialization routine - leaf logic block.


### `2000-CALCULATE-BUNDLED-FACTORS` (L947-1382)

Calculation routine - orchestrates 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT. Contains 43 IF/branchs.

- **Calls:** `2100-CALC-COMORBID-ADJUST`, `2500-CALC-OUTLIER-FACTORS`, `3000-LOW-VOL-FULL-PPS-PAYMENT`, `3100-LOW-VOL-OUT-PPS-PAYMENT`

### `2100-CALC-COMORBID-ADJUST` (L1383-1451)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `2500-CALC-OUTLIER-FACTORS` (L1452-1680)

Calculation routine - orchestrates 2600-CALC-COMORBID-OUT-ADJUST. Contains 28 IF/branchs.

- **Calls:** `2600-CALC-COMORBID-OUT-ADJUST`

### `2600-CALC-COMORBID-OUT-ADJUST` (L1681-1750)

Calculation routine - orchestrates . Contains 7 IF/branchs.

- **Calls:** ``

### `3000-LOW-VOL-FULL-PPS-PAYMENT` (L1751-1802)

Business routine - evaluates 4 branch conditions. Contains 4 IF/branchs.


### `3100-LOW-VOL-OUT-PPS-PAYMENT` (L1803-1869)

Business routine - evaluates 5 branch conditions. Contains 5 IF/branchs.


### `9000-SET-RETURN-CODE` (L1870-2051)

Business routine - assigns return codes based on input state. Contains 32 IF/branchs. Sets: PPS-RTC=17 when TRAINING-TRACK = "Y" THEN; PPS-RTC=16 when TRAINING-TRACK = "Y" THEN; PPS-RTC=15 when TRAINING-TRACK = "Y" THEN (+30 more).

- **Side effects:**
  - PPS-RTC=17 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=16 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=15 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=14 when TRAINING-TRACK = "Y" THEN
  - PPS-RTC=24 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=19 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=29 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=23 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=18 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=30 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=28 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=34 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=35 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=33 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=07 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=06 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=09 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=03 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=26 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=21 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=12 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=25 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=20 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=32 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=10 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=27 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=22 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=11 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=08 when ONSET-TRACK = "Y" THEN
  - PPS-RTC=04 when ACUTE-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=05 when CHRONIC-COMORBID-TRACK = "Y" THEN
  - PPS-RTC=31 when LOW-BMI-TRACK = "Y" THEN
  - PPS-RTC=02 when LOW-BMI-TRACK = "Y" THEN

### `9100-MOVE-RESULTS` (L2052-2253)

Business routine - evaluates 9 branch conditions. Contains 9 IF/branchs.


## TSB Risk Metric Summary (Technical & Structural Breakdown Risk)

**Average risk:** [W] 44 / 100 (MEDIUM)  
**Max paragraph risk:** [E] 100 / 100 (CRITICAL)  
**Distribution:** 4 CRITICAL ?. 0 HIGH ?. 1 MEDIUM ?. 7 LOW (of 12 paragraphs)

### Top 10 risky paragraphs

| Paragraph | Lines | Score | Category | Top factors |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 795-926 | **100** | [E] CRITICAL | 35 IF/EVAL branches, 15 return-code emissions, 131 lines (size penalty) |
| `2000-CALCULATE-BUNDLED-FACTORS` | 947-1382 | **100** | [E] CRITICAL | 43 IF/EVAL branches, 435 lines (size penalty), 4 PERFORM calls |
| `2500-CALC-OUTLIER-FACTORS` | 1452-1680 | **100** | [E] CRITICAL | 28 IF/EVAL branches, 228 lines (size penalty), 1 PERFORM calls |
| `9000-SET-RETURN-CODE` | 1870-2051 | **100** | [E] CRITICAL | 33 return-code emissions, 32 IF/EVAL branches, 181 lines (size penalty) |
| `9100-MOVE-RESULTS` | 2052-2253 | **47** | [W] MEDIUM | 9 IF/EVAL branches, 201 lines (size penalty) |
| `2100-CALC-COMORBID-ADJUST` | 1383-1451 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `2600-CALC-COMORBID-OUT-ADJUST` | 1681-1750 | **22** | [OK] LOW | 7 IF/EVAL branches, 1 PERFORM calls |
| `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1803-1869 | **15** | [OK] LOW | 5 IF/EVAL branches |
| `0000-START-TO-FINISH` | 758-794 | **14** | [OK] LOW | 3 IF/EVAL branches, 5 PERFORM calls |
| `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1751-1802 | **12** | [OK] LOW | 4 IF/EVAL branches |

## Issues

- [W] **WARNING**  `escal212.cbl:L758`: Potential state leak: Flag `P-PROV-WAIVE-BLEND-PAY-INDIC` is set to 'Y' in paragraph `0000-START-TO-FINISH` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L947`: Potential state leak: Flag `LOW-BMI-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L947`: Potential state leak: Flag `ONSET-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L947`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L947`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L947`: Potential state leak: Flag `MOVED-CORMORBIDS` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L947`: Potential state leak: Flag `PEDIATRIC-TRACK` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L947`: Potential state leak: Flag `H-BUN-ONSET-FACTOR` is set to 'Y' in paragraph `2000-CALCULATE-BUNDLED-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1383`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1383`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2100-CALC-COMORBID-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1452`: Potential state leak: Flag `OUTLIER-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1452`: Potential state leak: Flag `H-OUT-LOW-VOL-MULTIPLIER` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1452`: Potential state leak: Flag `LOW-VOLUME-TRACK` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1452`: Potential state leak: Flag `H-OUT-ONSET-FACTOR` is set to 'Y' in paragraph `2500-CALC-OUTLIER-FACTORS` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1681`: Potential state leak: Flag `CHRONIC-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1681`: Potential state leak: Flag `ACUTE-COMORBID-TRACK` is set to 'Y' in paragraph `2600-CALC-COMORBID-OUT-ADJUST` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.
- [W] **WARNING**  `escal212.cbl:L1751`: Potential state leak: Flag `TRAINING-TRACK` is set to 'Y' in paragraph `3000-LOW-VOL-FULL-PPS-PAYMENT` but is never reset to 'N' or INITIALIZEd here. Subsequent paragraph calls will reuse the dirty state.

> **Call Graph:** Structure identical to `ESCAL170` - diagram not repeated.


## Call Graph Edges

```
          0000-START-TO-FINISH  --PERFORM-->  1000-VALIDATE-BILL-ELEMENTS (L775)
          0000-START-TO-FINISH  --PERFORM-->  1200-INITIALIZATION (L777)
          0000-START-TO-FINISH  --PERFORM-->  2000-CALCULATE-BUNDLED-FACTORS (L777)
          0000-START-TO-FINISH  --PERFORM-->  9000-SET-RETURN-CODE (L777)
          0000-START-TO-FINISH  --PERFORM-->  9100-MOVE-RESULTS (L777)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2100-CALC-COMORBID-ADJUST (L1172)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  2500-CALC-OUTLIER-FACTORS (L1355)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3000-LOW-VOL-FULL-PPS-PAYMENT (L1360)
2000-CALCULATE-BUNDLED-FACTORS  --PERFORM-->  3100-LOW-VOL-OUT-PPS-PAYMENT (L1360)
     2100-CALC-COMORBID-ADJUST  --PERFORM-->   (L1395)
     2500-CALC-OUTLIER-FACTORS  --PERFORM-->  2600-CALC-COMORBID-OUT-ADJUST (L1541)
 2600-CALC-COMORBID-OUT-ADJUST  --PERFORM-->   (L1694)
```

## Return Codes (Trigger Summary)

| Paragraph | Line | RC Var | Value | Condition |
|---|---|---|---|---|
| `1000-VALIDATE-BILL-ELEMENTS` | 796 | `PPS-RTC` | **58** | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `1000-VALIDATE-BILL-ELEMENTS` | 803 | `PPS-RTC` | **52** | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 811 | `PPS-RTC` | **53** | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 817 | `PPS-RTC` | **54** | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 823 | `PPS-RTC` | **55** | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 831 | `PPS-RTC` | **56** | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `1000-VALIDATE-BILL-ELEMENTS` | 839 | `PPS-RTC` | **57** | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE |
| `1000-VALIDATE-BILL-ELEMENTS` | 848 | `PPS-RTC` | **53** | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 858 | `PPS-RTC` | **71** | B-PATIENT-HGT > 300.00 |
| `1000-VALIDATE-BILL-ELEMENTS` | 866 | `PPS-RTC` | **72** | B-PATIENT-WGT > 500.00  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 879 | `PPS-RTC` | **73** | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NUM |
| `1000-VALIDATE-BILL-ELEMENTS` | 886 | `PPS-RTC` | **74** | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC)  THE |
| `1000-VALIDATE-BILL-ELEMENTS` | 893 | `PPS-RTC` | **75** | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 899 | `PPS-RTC` | **76** | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `1000-VALIDATE-BILL-ELEMENTS` | 916 | `PPS-RTC` | **81** | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN N |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **17** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **16** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **15** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **14** | TRAINING-TRACK                  = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **24** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **19** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **29** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **23** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **18** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **30** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **28** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **34** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **35** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **33** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **07** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **06** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **09** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **03** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **26** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **21** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **12** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **25** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **20** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **32** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **10** | ONSET-TRACK         = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **27** | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **22** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **11** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **08** | ONSET-TRACK               = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **04** | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **05** | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **31** | LOW-BMI-TRACK = "Y"  THEN |
| `9000-SET-RETURN-CODE` | 1921 | `PPS-RTC` | **02** | LOW-BMI-TRACK = "Y"  THEN |

## State Machines (88-level)

### `IS-HIGH-COMORBID-FOUND`

- **'Y'** = HIGH-COMORBID-FOUND (L559)

