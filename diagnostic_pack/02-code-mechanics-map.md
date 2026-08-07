# CobolIQ Code Mechanics Map

*Source-cited explanation of how the COBOL system executes, moves data, sets state, handles exceptions and exposes modernization candidates.*

---

## 1. Machine Overview

**System type:** General COBOL Application

- **Programs:** 21
- **Copybooks:** 0
- **Total code lines:** 18714
- **Paragraphs:** 232
- **Call graph edges:** 212
- **Dialect:** Mixed / GnuCOBOL free-format

### Programs

| Program | Lines | Paragraphs | Edges | cc~ | Risk |
|---------|-------|------------|-------|-----|------|
| `ESCAL056` | 263 | 8 | 6 | 37 | CRITICAL |
| `ESCAL062` | 279 | 8 | 6 | 36 | CRITICAL |
| `ESCAL070` | 279 | 8 | 6 | 36 | CRITICAL |
| `ESCAL071` | 285 | 8 | 6 | 36 | CRITICAL |
| `ESCAL080` | 290 | 8 | 6 | 36 | CRITICAL |
| `ESCAL091` | 270 | 8 | 6 | 36 | CRITICAL |
| `ESCAL100` | 272 | 8 | 6 | 36 | CRITICAL |
| `ESCAL117` | 1173 | 11 | 11 | 165 | CRITICAL |
| `ESCAL122` | 1321 | 13 | 13 | 183 | CRITICAL |
| `ESCAL130` | 1321 | 13 | 13 | 183 | CRITICAL |
| `ESCAL140` | 1322 | 13 | 13 | 183 | CRITICAL |
| `ESCAL151` | 1322 | 13 | 13 | 183 | CRITICAL |
| `ESCAL160` | 1267 | 13 | 13 | 174 | CRITICAL |
| `ESCAL170` | 1208 | 12 | 12 | 169 | CRITICAL |
| `ESCAL171` | 1211 | 12 | 12 | 170 | CRITICAL |
| `ESCAL180` | 1218 | 12 | 12 | 170 | CRITICAL |
| `ESCAL191` | 1218 | 12 | 12 | 170 | CRITICAL |
| `ESCAL200` | 1218 | 12 | 12 | 170 | CRITICAL |
| `ESCAL202` | 1250 | 12 | 12 | 172 | CRITICAL |
| `ESCAL212` | 1272 | 12 | 12 | 175 | CRITICAL |
| `ESDRV212` | 455 | 16 | 10 | 54 | CRITICAL |

## 2. Entry & Ignition

### `ESCAL056`

**Entry paragraph:** `0000-PROCEDURE-START` [L134-158]

### `ESCAL062`

**Entry paragraph:** `0000-PROCEDURE-START` [L144-169]

### `ESCAL070`

**Entry paragraph:** `0000-PROCEDURE-START` [L136-161]

### `ESCAL071`

**Entry paragraph:** `0000-PROCEDURE-START` [L147-172]

### `ESCAL080`

**Entry paragraph:** `0000-PROCEDURE-START` [L192-217]

### `ESCAL091`

**Entry paragraph:** `0000-PROCEDURE-START` [L211-236]

### `ESCAL100`

**Entry paragraph:** `0000-PROCEDURE-START` [L222-247]

### `ESCAL117`

**Entry paragraph:** `0000-PROCEDURE-START` [L416-442]

### `ESCAL122`

**Entry paragraph:** `0000-PROCEDURE-START` [L454-480]

### `ESCAL130`

**Entry paragraph:** `0000-PROCEDURE-START` [L483-509]

### `ESCAL140`

**Entry paragraph:** `0000-PROCEDURE-START` [L526-552]

### `ESCAL151`

**Entry paragraph:** `0000-PROCEDURE-START` [L559-585]

### `ESCAL160`

**Entry paragraph:** `0000-PROCEDURE-START` [L591-617]

### `ESCAL170`

**Entry paragraph:** `0000-PROCEDURE-START` [L616-640]

### `ESCAL171`

**Entry paragraph:** `0000-PROCEDURE-START` [L619-643]

### `ESCAL180`

**Entry paragraph:** `0000-PROCEDURE-START` [L635-659]

### `ESCAL191`

**Entry paragraph:** `0000-PROCEDURE-START` [L650-674]

### `ESCAL200`

**Entry paragraph:** `0000-PROCEDURE-START` [L665-689]

### `ESCAL202`

**Entry paragraph:** `0000-PROCEDURE-START` [L692-716]

### `ESCAL212`

**Entry paragraph:** `0000-PROCEDURE-START` [L733-757]

### `ESDRV212`

**Entry paragraph:** `0000-PROCEDURE-START` [L356-379]

## 3. Main Drive Train

### `ESCAL056`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L134-158]
```

**Decision points** (high branching):

- `1000-EDIT-THE-BILL-INFO` [L219-276] - 17 branches
- `1200-CALC-AGE` [L277-316] - 7 branches
- `3000-CALC-PAYMENT` [L349-383] - 3 branches
- `9000-MOVE-RESULTS` [L384-434] - 4 branches

**Processing phases:**

- Calculation / Processing (3 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL062`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L144-169]
```

**Decision points** (high branching):

- `1000-EDIT-THE-BILL-INFO` [L238-295] - 17 branches
- `1200-CALC-AGE` [L296-335] - 7 branches
- `3000-CALC-PAYMENT` [L366-411] - 3 branches
- `9000-MOVE-RESULTS` [L412-454] - 3 branches

**Processing phases:**

- Calculation / Processing (3 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL070`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L136-161]
```

**Decision points** (high branching):

- `1000-EDIT-THE-BILL-INFO` [L230-287] - 17 branches
- `1200-CALC-AGE` [L288-327] - 7 branches
- `3000-CALC-PAYMENT` [L358-403] - 3 branches
- `9000-MOVE-RESULTS` [L404-446] - 3 branches

**Processing phases:**

- Calculation / Processing (3 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL071`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L147-172]
```

**Decision points** (high branching):

- `1000-EDIT-THE-BILL-INFO` [L245-302] - 17 branches
- `1200-CALC-AGE` [L303-342] - 7 branches
- `3000-CALC-PAYMENT` [L373-418] - 3 branches
- `9000-MOVE-RESULTS` [L419-461] - 3 branches

**Processing phases:**

- Calculation / Processing (3 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL080`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L192-217]
```

**Decision points** (high branching):

- `1000-EDIT-THE-BILL-INFO` [L294-351] - 17 branches
- `1200-CALC-AGE` [L352-391] - 7 branches
- `3000-CALC-PAYMENT` [L422-467] - 3 branches
- `9000-MOVE-RESULTS` [L468-509] - 3 branches

**Processing phases:**

- Calculation / Processing (3 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL091`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L211-236]
```

**Decision points** (high branching):

- `1000-EDIT-THE-BILL-INFO` [L301-358] - 17 branches
- `1200-CALC-AGE` [L359-398] - 7 branches
- `3000-CALC-PAYMENT` [L429-472] - 3 branches
- `9000-MOVE-RESULTS` [L473-514] - 3 branches

**Processing phases:**

- Calculation / Processing (3 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL100`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L222-247]
```

**Decision points** (high branching):

- `1000-EDIT-THE-BILL-INFO` [L311-368] - 17 branches
- `1200-CALC-AGE` [L369-408] - 7 branches
- `3000-CALC-PAYMENT` [L439-483] - 3 branches
- `9000-MOVE-RESULTS` [L484-525] - 3 branches

**Processing phases:**

- Calculation / Processing (3 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL117`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L416-442]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L443-474] - 5 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L475-572] - 27 branches
- `1200-INITIALIZATION` [L573-684] - 7 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L685-902] - 26 branches
- `2100-CALC-COMORBID-ADJUST` [L903-971] - 11 branches
- `2500-CALC-OUTLIER-FACTORS` [L972-1188] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1189-1255] - 11 branches
- `5000-CALC-COMP-RATE-FACTORS` [L1256-1367] - 11 branches
- `9000-SET-RETURN-CODE` [L1368-1548] - 32 branches
- `9100-MOVE-RESULTS` [L1549-1678] - 5 branches

**Processing phases:**

- Calculation / Processing (6 paragraphs)
- General Processing (3 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL122`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L454-480]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L481-512] - 5 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L513-620] - 29 branches
- `1200-INITIALIZATION` [L621-755] - 11 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L756-997] - 28 branches
- `2100-CALC-COMORBID-ADJUST` [L998-1066] - 11 branches
- `2500-CALC-OUTLIER-FACTORS` [L1067-1283] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1284-1353] - 11 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1354-1404] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1405-1468] - 5 branches
- `5000-CALC-COMP-RATE-FACTORS` [L1469-1580] - 11 branches
- `9000-SET-RETURN-CODE` [L1581-1761] - 32 branches
- `9100-MOVE-RESULTS` [L1762-1909] - 6 branches

**Processing phases:**

- Calculation / Processing (6 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL130`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L483-509]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L510-541] - 5 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L542-649] - 29 branches
- `1200-INITIALIZATION` [L650-784] - 11 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L785-1026] - 28 branches
- `2100-CALC-COMORBID-ADJUST` [L1027-1095] - 11 branches
- `2500-CALC-OUTLIER-FACTORS` [L1096-1312] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1313-1382] - 11 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1383-1433] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1434-1497] - 5 branches
- `5000-CALC-COMP-RATE-FACTORS` [L1498-1609] - 11 branches
- `9000-SET-RETURN-CODE` [L1610-1790] - 32 branches
- `9100-MOVE-RESULTS` [L1791-1938] - 6 branches

**Processing phases:**

- Calculation / Processing (6 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL140`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L526-552]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L553-587] - 5 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L588-695] - 29 branches
- `1200-INITIALIZATION` [L696-830] - 11 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L831-1072] - 28 branches
- `2100-CALC-COMORBID-ADJUST` [L1073-1141] - 11 branches
- `2500-CALC-OUTLIER-FACTORS` [L1142-1358] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1359-1428] - 11 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1429-1479] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1480-1543] - 5 branches
- `5000-CALC-COMP-RATE-FACTORS` [L1544-1655] - 11 branches
- `9000-SET-RETURN-CODE` [L1656-1836] - 32 branches
- `9100-MOVE-RESULTS` [L1837-1984] - 6 branches

**Processing phases:**

- Calculation / Processing (6 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL151`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L559-585]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L586-620] - 5 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L621-728] - 29 branches
- `1200-INITIALIZATION` [L729-863] - 11 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L864-1105] - 28 branches
- `2100-CALC-COMORBID-ADJUST` [L1106-1174] - 11 branches
- `2500-CALC-OUTLIER-FACTORS` [L1175-1391] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1392-1461] - 11 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1462-1512] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1513-1576] - 5 branches
- `5000-CALC-COMP-RATE-FACTORS` [L1577-1688] - 11 branches
- `9000-SET-RETURN-CODE` [L1689-1869] - 32 branches
- `9100-MOVE-RESULTS` [L1870-2017] - 6 branches

**Processing phases:**

- Calculation / Processing (6 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL160`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L591-617]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L618-652] - 5 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L653-771] - 29 branches
- `1200-INITIALIZATION` [L772-907] - 10 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L908-1157] - 28 branches
- `2100-CALC-COMORBID-ADJUST` [L1158-1226] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1227-1454] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1455-1524] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1525-1576] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1577-1641] - 5 branches
- `5000-CALC-COMP-RATE-FACTORS` [L1642-1753] - 11 branches
- `9000-SET-RETURN-CODE` [L1754-1934] - 32 branches
- `9100-MOVE-RESULTS` [L1935-2082] - 6 branches

**Processing phases:**

- Calculation / Processing (6 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL170`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L616-640]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L641-672] - 3 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L673-801] - 34 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L822-1196] - 40 branches
- `2100-CALC-COMORBID-ADJUST` [L1197-1265] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1266-1494] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1495-1564] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1565-1616] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1617-1683] - 5 branches
- `9000-SET-RETURN-CODE` [L1684-1865] - 32 branches
- `9100-MOVE-RESULTS` [L1866-2014] - 7 branches

**Processing phases:**

- Calculation / Processing (5 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL171`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L619-643]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L644-675] - 3 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L676-807] - 35 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L828-1202] - 40 branches
- `2100-CALC-COMORBID-ADJUST` [L1203-1271] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1272-1500] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1501-1570] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1571-1622] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1623-1689] - 5 branches
- `9000-SET-RETURN-CODE` [L1690-1871] - 32 branches
- `9100-MOVE-RESULTS` [L1872-2020] - 7 branches

**Processing phases:**

- Calculation / Processing (5 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL180`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L635-659]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L660-696] - 3 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L697-828] - 35 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L849-1231] - 40 branches
- `2100-CALC-COMORBID-ADJUST` [L1232-1300] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1301-1529] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1530-1599] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1600-1651] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1652-1718] - 5 branches
- `9000-SET-RETURN-CODE` [L1719-1900] - 32 branches
- `9100-MOVE-RESULTS` [L1901-2054] - 7 branches

**Processing phases:**

- Calculation / Processing (5 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL191`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L650-674]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L675-711] - 3 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L712-843] - 35 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L864-1246] - 40 branches
- `2100-CALC-COMORBID-ADJUST` [L1247-1315] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1316-1544] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1545-1614] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1615-1666] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1667-1733] - 5 branches
- `9000-SET-RETURN-CODE` [L1734-1915] - 32 branches
- `9100-MOVE-RESULTS` [L1916-2069] - 7 branches

**Processing phases:**

- Calculation / Processing (5 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL200`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L665-689]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L690-726] - 3 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L727-858] - 35 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L879-1261] - 40 branches
- `2100-CALC-COMORBID-ADJUST` [L1262-1330] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1331-1559] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1560-1629] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1630-1681] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1682-1748] - 5 branches
- `9000-SET-RETURN-CODE` [L1749-1930] - 32 branches
- `9100-MOVE-RESULTS` [L1931-2084] - 7 branches

**Processing phases:**

- Calculation / Processing (5 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL202`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L692-716]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L717-753] - 3 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L754-885] - 35 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L906-1316] - 41 branches
- `2100-CALC-COMORBID-ADJUST` [L1317-1385] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1386-1614] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1615-1684] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1685-1736] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1737-1803] - 5 branches
- `9000-SET-RETURN-CODE` [L1804-1985] - 32 branches
- `9100-MOVE-RESULTS` [L1986-2168] - 8 branches

**Processing phases:**

- Calculation / Processing (5 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESCAL212`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L733-757]
```

**Decision points** (high branching):

- `0000-START-TO-FINISH` [L758-794] - 3 branches
- `1000-VALIDATE-BILL-ELEMENTS` [L795-926] - 35 branches
- `2000-CALCULATE-BUNDLED-FACTORS` [L947-1382] - 43 branches
- `2100-CALC-COMORBID-ADJUST` [L1383-1451] - 7 branches
- `2500-CALC-OUTLIER-FACTORS` [L1452-1680] - 28 branches
- `2600-CALC-COMORBID-OUT-ADJUST` [L1681-1750] - 7 branches
- `3000-LOW-VOL-FULL-PPS-PAYMENT` [L1751-1802] - 4 branches
- `3100-LOW-VOL-OUT-PPS-PAYMENT` [L1803-1869] - 5 branches
- `9000-SET-RETURN-CODE` [L1870-2051] - 32 branches
- `9100-MOVE-RESULTS` [L2052-2253] - 9 branches

**Processing phases:**

- Calculation / Processing (5 paragraphs)
- General Processing (5 paragraphs)
- Initialization (1 paragraphs)
- Validation (1 paragraphs)

### `ESDRV212`

**Primary execution path:**

```
?- 0000-PROCEDURE-START [L356-379]
```

**Decision points** (high branching):

- `0100-ENTER-DRIVER` [L380-822] - 30 branches
- `0700-FIND-COMPOSITE-CBSA-WI` [L995-1022] - 3 branches
- `0800-FIND-BUNDLED-CBSA-WI` [L1045-1114] - 9 branches

**Processing phases:**

- Calculation / Processing (4 paragraphs)
- Cleanup / Exit (6 paragraphs)
- General Processing (6 paragraphs)

## 4. Data Lines

### `ESCAL056`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 14 items

**Copybooks:** BILLCPY, WAGECPY

### `ESCAL062`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 17 items

**Copybooks:** BILLCPY, WAGECPY

### `ESCAL070`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 17 items

**Copybooks:** BILLCPY, WAGECPY

### `ESCAL071`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 18 items

**Copybooks:** BILLCPY, WAGECPY

### `ESCAL080`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 19 items

**Copybooks:** BILLCPY, WAGECPY

### `ESCAL091`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 16 items

**Copybooks:** BILLCPY, WAGECPY

### `ESCAL100`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 18 items

**Copybooks:** BILLCPY, WAGECPY

### `ESCAL117`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 31 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL122`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 31 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL130`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 31 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL140`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 31 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL151`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 31 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL160`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 31 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL170`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 32 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL171`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 32 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL180`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 32 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL191`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 32 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL200`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 32 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL202`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 33 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESCAL212`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)
- `WAGE-NEW-RATE-RECORD` (PIC -)
- `COM-CBSA-WAGE-RECORD` (PIC -)
- `BUN-CBSA-WAGE-RECORD` (PIC -)

**WORKING-STORAGE:** 33 items

**Copybooks:** RTCCPY, BILLCPY, WAGECPY

### `ESDRV212`

**LINKAGE inputs:**

- `BILL-NEW-DATA` (PIC -)
- `PPS-DATA-ALL` (PIC -)

**WORKING-STORAGE:** 64 items, 10 with REDEFINES

**Copybooks:** DSCNTRL, ESWRT151, ESCOM151, ESBUN210, ESCHI151, WAGECPY, RTCCPY, BILLCPY

## 5. Control Switches

### `ESCAL117`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L257)

### `ESCAL122`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L293)

### `ESCAL130`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L322)

### `ESCAL140`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L365)

### `ESCAL151`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L398)

### `ESCAL160`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L427)

### `ESCAL170`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L449)

### `ESCAL171`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L452)

### `ESCAL180`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L467)

### `ESCAL191`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L482)

### `ESCAL200`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L497)

### `ESCAL202`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L520)

### `ESCAL212`

**`IS-HIGH-COMORBID-FOUND`** - 1 states:

- `'Y'` = HIGH-COMORBID-FOUND (L559)

**Total: 13 state values across all programs.**

## 6. Warning Lights - Return-Code Catalog

### `ESCAL056`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `0100-INITIAL-ROUTINE` | 188 | P-PROV-TYPE = '41' |
| `PPS-RTC` | **53** | `1000-EDIT-THE-BILL-INFO` | 221 | P-SPEC-PYMT-IND NOT = '1' AND ' ' |
| `PPS-RTC` | **54** | `1000-EDIT-THE-BILL-INFO` | 227 | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) |
| `PPS-RTC` | **55** | `1000-EDIT-THE-BILL-INFO` | 233 | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-EDIT-THE-BILL-INFO` | 239 | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-EDIT-THE-BILL-INFO` | 245 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0880' |
| `PPS-RTC` | **58** | `1000-EDIT-THE-BILL-INFO` | 254 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-EDIT-THE-BILL-INFO` | 260 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-EDIT-THE-BILL-INFO` | 266 | B-PATIENT-WGT > 500.00 |

### `ESCAL062`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `0100-INITIAL-ROUTINE` | 199 | P-PROV-TYPE = '41' |
| `PPS-RTC` | **53** | `1000-EDIT-THE-BILL-INFO` | 240 | P-SPEC-PYMT-IND NOT = '1' AND ' ' |
| `PPS-RTC` | **54** | `1000-EDIT-THE-BILL-INFO` | 246 | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) |
| `PPS-RTC` | **55** | `1000-EDIT-THE-BILL-INFO` | 252 | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-EDIT-THE-BILL-INFO` | 258 | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-EDIT-THE-BILL-INFO` | 264 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0880' |
| `PPS-RTC` | **58** | `1000-EDIT-THE-BILL-INFO` | 273 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-EDIT-THE-BILL-INFO` | 279 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-EDIT-THE-BILL-INFO` | 285 | B-PATIENT-WGT > 500.00 |

### `ESCAL070`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `0100-INITIAL-ROUTINE` | 191 | P-PROV-TYPE = '41' |
| `PPS-RTC` | **53** | `1000-EDIT-THE-BILL-INFO` | 232 | P-SPEC-PYMT-IND NOT = '1' AND ' ' |
| `PPS-RTC` | **54** | `1000-EDIT-THE-BILL-INFO` | 238 | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) |
| `PPS-RTC` | **55** | `1000-EDIT-THE-BILL-INFO` | 244 | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-EDIT-THE-BILL-INFO` | 250 | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-EDIT-THE-BILL-INFO` | 256 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0880' |
| `PPS-RTC` | **58** | `1000-EDIT-THE-BILL-INFO` | 265 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-EDIT-THE-BILL-INFO` | 271 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-EDIT-THE-BILL-INFO` | 277 | B-PATIENT-WGT > 500.00 |

### `ESCAL071`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `0100-INITIAL-ROUTINE` | 202 | P-PROV-TYPE = '41' |
| `PPS-RTC` | **53** | `1000-EDIT-THE-BILL-INFO` | 247 | P-SPEC-PYMT-IND NOT = '1' AND ' ' |
| `PPS-RTC` | **54** | `1000-EDIT-THE-BILL-INFO` | 253 | (B-DOB-DATE = ZERO) OR (B-DOB-DATE NOT NUMERIC) |
| `PPS-RTC` | **55** | `1000-EDIT-THE-BILL-INFO` | 259 | (B-PATIENT-WGT = 0) OR (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-EDIT-THE-BILL-INFO` | 265 | (B-PATIENT-HGT = 0) OR (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-EDIT-THE-BILL-INFO` | 271 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0880' |
| `PPS-RTC` | **58** | `1000-EDIT-THE-BILL-INFO` | 280 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-EDIT-THE-BILL-INFO` | 286 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-EDIT-THE-BILL-INFO` | 292 | B-PATIENT-WGT > 500.00 |

### `ESCAL080`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `0100-INITIAL-ROUTINE` | 247 | P-PROV-TYPE = '41'  THEN |
| `PPS-RTC` | **53** | `1000-EDIT-THE-BILL-INFO` | 296 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-EDIT-THE-BILL-INFO` | 302 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-EDIT-THE-BILL-INFO` | 308 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-EDIT-THE-BILL-INFO` | 314 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-EDIT-THE-BILL-INFO` | 320 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0880' |
| `PPS-RTC` | **58** | `1000-EDIT-THE-BILL-INFO` | 329 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-EDIT-THE-BILL-INFO` | 335 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-EDIT-THE-BILL-INFO` | 341 | B-PATIENT-WGT > 500.00  THEN |

### `ESCAL091`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `0100-INITIAL-ROUTINE` | 266 | P-PROV-TYPE = '41'  THEN |
| `PPS-RTC` | **53** | `1000-EDIT-THE-BILL-INFO` | 303 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-EDIT-THE-BILL-INFO` | 309 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-EDIT-THE-BILL-INFO` | 315 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-EDIT-THE-BILL-INFO` | 321 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-EDIT-THE-BILL-INFO` | 327 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0880' |
| `PPS-RTC` | **58** | `1000-EDIT-THE-BILL-INFO` | 336 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-EDIT-THE-BILL-INFO` | 342 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-EDIT-THE-BILL-INFO` | 348 | B-PATIENT-WGT > 500.00  THEN |

### `ESCAL100`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `0100-INITIAL-ROUTINE` | 276 | P-PROV-TYPE = '41'  THEN |
| `PPS-RTC` | **53** | `1000-EDIT-THE-BILL-INFO` | 313 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-EDIT-THE-BILL-INFO` | 319 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-EDIT-THE-BILL-INFO` | 325 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-EDIT-THE-BILL-INFO` | 331 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-EDIT-THE-BILL-INFO` | 337 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0880' |
| `PPS-RTC` | **58** | `1000-EDIT-THE-BILL-INFO` | 346 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-EDIT-THE-BILL-INFO` | 352 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-EDIT-THE-BILL-INFO` | 358 | B-PATIENT-WGT > 500.00  THEN |

### `ESCAL117`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 476 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 482 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 488 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 494 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 500 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 506 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 515 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 521 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 527 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 538 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 545 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 552 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 558 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 564 | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMORBID-CWF-RE |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1419 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1419 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1419 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1419 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1419 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1419 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1419 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1419 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1419 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1419 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1419 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1419 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1419 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1419 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1419 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL122`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 514 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 520 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 526 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 532 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 538 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 544 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 553 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 559 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 569 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 575 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 586 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 593 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 600 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 606 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 612 | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMORBID-CWF-RE |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1632 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1632 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1632 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1632 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1632 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1632 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1632 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1632 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1632 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1632 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1632 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1632 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1632 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1632 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1632 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL130`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 543 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 549 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 555 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 561 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 567 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 573 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 582 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 588 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 598 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 604 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 615 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 622 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 629 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 635 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 641 | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMORBID-CWF-RE |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1661 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1661 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1661 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1661 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1661 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1661 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1661 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1661 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1661 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1661 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1661 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1661 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1661 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1661 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1661 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL140`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 589 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 595 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 601 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 607 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 613 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 619 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 628 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 634 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 644 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 650 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 661 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 668 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 675 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 681 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 687 | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMORBID-CWF-RE |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1707 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1707 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1707 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1707 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1707 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1707 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1707 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1707 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1707 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1707 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1707 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1707 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1707 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1707 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1707 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL151`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 622 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 628 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 634 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 640 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 646 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 652 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 661 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 667 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 677 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 683 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 694 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 701 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 708 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 714 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 720 | (COMORBID-CWF-RETURN-CODE = SPACES) OR VALID-COMORBID-CWF-RE |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1740 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1740 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1740 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1740 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1740 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1740 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1740 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1740 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1740 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1740 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1740 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1740 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1740 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1740 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1740 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL160`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 654 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 660 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 666 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 672 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 678 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 684 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 693 | B-COND-CODE NOT = '73' AND '74' AND '  ' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 699 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 709 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 715 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 726 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 733 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 740 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 746 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 763 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1805 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1805 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1805 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1805 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1805 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1805 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1805 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1805 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1805 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1805 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1805 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1805 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1805 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1805 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1805 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL170`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 674 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 680 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 686 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 692 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 700 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 708 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 717 | B-COND-CODE NOT = '73' AND '74' AND '84' AND '  ' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 723 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 733 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 741 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 754 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 761 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 768 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 774 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 791 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1735 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1735 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1735 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1735 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1735 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1735 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1735 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1735 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1735 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1735 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1735 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1735 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1735 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1735 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1735 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL171`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 677 | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 684 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 692 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 698 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 704 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 712 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 720 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 729 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 739 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 747 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 760 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 767 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 774 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 780 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 797 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1741 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1741 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1741 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1741 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1741 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1741 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1741 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1741 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1741 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1741 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1741 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1741 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1741 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1741 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1741 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL180`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 698 | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 705 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 713 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 719 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 725 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 733 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 741 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 750 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 760 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 768 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 781 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 788 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 795 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 801 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 818 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1770 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1770 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1770 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1770 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1770 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1770 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1770 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1770 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1770 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1770 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1770 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1770 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1770 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1770 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1770 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL191`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 713 | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 720 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 728 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 734 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 740 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 748 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 756 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 765 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 775 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 783 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 796 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 803 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 810 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 816 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 833 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1785 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1785 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1785 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1785 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1785 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1785 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1785 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1785 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1785 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1785 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1785 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1785 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1785 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1785 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1785 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL200`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 728 | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 735 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 743 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 749 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 755 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 763 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 771 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 780 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 790 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 798 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 811 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 818 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 825 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 831 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 848 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1800 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1800 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1800 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1800 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1800 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1800 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1800 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1800 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1800 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1800 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1800 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1800 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1800 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1800 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1800 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL202`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 755 | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 762 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 770 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 776 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 782 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 790 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 798 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 807 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 817 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 825 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 838 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 845 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 852 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 858 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 875 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1855 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1855 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1855 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1855 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1855 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1855 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1855 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1855 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1855 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1855 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1855 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1855 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1855 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1855 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1855 | LOW-BMI-TRACK = "Y"  THEN |

### `ESCAL212`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 796 | B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  ' |
| `PPS-RTC` | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 803 | P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 811 | P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN |
| `PPS-RTC` | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 817 | (B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 823 | (B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC) |
| `PPS-RTC` | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 831 | (B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC) |
| `PPS-RTC` | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 839 | B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' |
| `PPS-RTC` | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 848 | P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  T |
| `PPS-RTC` | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 858 | B-PATIENT-HGT > 300.00 |
| `PPS-RTC` | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 866 | B-PATIENT-WGT > 500.00  THEN |
| `PPS-RTC` | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 879 | (B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALY |
| `PPS-RTC` | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 886 | (B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVI |
| `PPS-RTC` | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 893 | (B-DIALYSIS-START-DATE NOT NUMERIC)  THEN |
| `PPS-RTC` | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 899 | (B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN |
| `PPS-RTC` | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 916 | COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR |
| `PPS-RTC` | **17** | `9000-SET-RETURN-CODE` | 1921 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **16** | `9000-SET-RETURN-CODE` | 1921 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **15** | `9000-SET-RETURN-CODE` | 1921 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **14** | `9000-SET-RETURN-CODE` | 1921 | TRAINING-TRACK                  = "Y"  THEN |
| `PPS-RTC` | **24** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **19** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **29** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **23** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **18** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **30** | `9000-SET-RETURN-CODE` | 1921 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **28** | `9000-SET-RETURN-CODE` | 1921 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **34** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **35** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **33** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **07** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **06** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **09** | `9000-SET-RETURN-CODE` | 1921 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **03** | `9000-SET-RETURN-CODE` | 1921 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **26** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **21** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **12** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **25** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **20** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **32** | `9000-SET-RETURN-CODE` | 1921 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **10** | `9000-SET-RETURN-CODE` | 1921 | ONSET-TRACK         = "Y"  THEN |
| `PPS-RTC` | **27** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK    = "Y"  THEN |
| `PPS-RTC` | **22** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **11** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **08** | `9000-SET-RETURN-CODE` | 1921 | ONSET-TRACK               = "Y"  THEN |
| `PPS-RTC` | **04** | `9000-SET-RETURN-CODE` | 1921 | ACUTE-COMORBID-TRACK   = "Y"  THEN |
| `PPS-RTC` | **05** | `9000-SET-RETURN-CODE` | 1921 | CHRONIC-COMORBID-TRACK = "Y"  THEN |
| `PPS-RTC` | **31** | `9000-SET-RETURN-CODE` | 1921 | LOW-BMI-TRACK = "Y"  THEN |
| `PPS-RTC` | **02** | `9000-SET-RETURN-CODE` | 1921 | LOW-BMI-TRACK = "Y"  THEN |

### `ESDRV212`

| RC Variable | Value | Paragraph | Line | Condition |
|-------------|-------|-----------|------|-----------|
| `PPS-RTC` | **00** | `0100-ENTER-DRIVER` | 384 | unconditional |
| `PPS-RTC` | **98** | `0100-ENTER-DRIVER` | 397 | (B-THRU-DATE < 20050401) OR (B-THRU-DATE NOT NUMERIC) |
| `PPS-RTC` | **50** | `0100-ENTER-DRIVER` | 402 | P-ESRD-RATE NOT NUMERIC |
| `PPS-RTC` | **01** | `0100-ENTER-DRIVER` | 420 | (B-THRU-DATE < 20110101)  AND  (P-ESRD-RATE > ZERO) |
| `PPS-RTC` | **01** | `0100-ENTER-DRIVER` | 426 | (B-THRU-DATE > 20101231)        AND (B-THRU-DATE < 20140101) |
| `PPS-RTC` | **98** | `0100-ENTER-DRIVER` | 466 | (B-THRU-DATE > 20050331 AND B-THRU-DATE < 20060101)  THEN |
| `PPS-RTC` | **60** | `0500-FIND-MSA-WAGE-ADJ-RATE` | 964 | unconditional |
| `PPS-RTC` | **60** | `0700-FIND-COMPOSITE-CBSA-WI` | 1007 | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN |
| `PPS-RTC` | **61** | `0700-FIND-COMPOSITE-CBSA-WI` | 1007 | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN |
| `PPS-RTC` | **60** | `0800-FIND-BUNDLED-CBSA-WI` | 1078 | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN |
| `PPS-RTC` | **61** | `0800-FIND-BUNDLED-CBSA-WI` | 1078 | MAINFRAME-PC-SWITCH = DS-ERROR-CODE  THEN |
| `PPS-RTC` | **60** | `0800-FIND-BUNDLED-CBSA-WI` | 1098 | H-ESRD-SUPP-WI-RATIO < -0.05 |
| `PPS-RTC` | **60** | `0850-GET-BUNDLED-CBSA-RATE` | 1129 | W-SUB3 > BUN-PTR (BUN-INDX - 1) THEN |

**Total: 699 return-code assignments.** Each value is traceable to a specific source line. These are the diagnostic signals the system emits - understanding them is critical for integration testing and migration validation.

## 7. Hardcoded Calibration

*Magic numbers, thresholds, defaults, and coefficients embedded directly in COBOL source. These are candidates for external configuration.*

### `ESCAL056`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **52** | `0100-INITIAL-ROUTINE` | 188 | `0100_initial_routine.pps_rtc.default` |
| default | **53** | `1000-EDIT-THE-BILL-INFO` | 221 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **54** | `1000-EDIT-THE-BILL-INFO` | 227 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **55** | `1000-EDIT-THE-BILL-INFO` | 233 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **56** | `1000-EDIT-THE-BILL-INFO` | 239 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **57** | `1000-EDIT-THE-BILL-INFO` | 245 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **58** | `1000-EDIT-THE-BILL-INFO` | 254 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **300.00** | `1000-EDIT-THE-BILL-INFO` | 260 | `1000_edit_the_bill_info.b_patient_hgt.threshold` |
| default | **71** | `1000-EDIT-THE-BILL-INFO` | 260 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **500.00** | `1000-EDIT-THE-BILL-INFO` | 266 | `1000_edit_the_bill_info.b_patient_wgt.threshold` |
| default | **72** | `1000-EDIT-THE-BILL-INFO` | 266 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **18** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.620** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_age_factor.default` |
| threshold | **17** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **45** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.223** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_age_factor.default` |
| threshold | **44** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **60** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.055** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_age_factor.default` |
| threshold | **59** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **70** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.000** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_age_factor.default` |
| threshold | **69** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **80** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.094** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_age_factor.default` |
| threshold | **79** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.174** | `1200-CALC-AGE` | 292 | `1200_calc_age.h_age_factor.default` |
| constant | **.007184** | `2000-ASSEMBLE-PPS-VARIABLES` | 324 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.725** | `2000-ASSEMBLE-PPS-VARIABLES` | 324 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.425** | `2000-ASSEMBLE-PPS-VARIABLES` | 324 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **10000** | `2000-ASSEMBLE-PPS-VARIABLES` | 324 | `2000_assemble_pps_variables.h_bmi_rounded.constant` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 330 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| constant | **1.037** | `2000-ASSEMBLE-PPS-VARIABLES` | 330 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **1.84** | `2000-ASSEMBLE-PPS-VARIABLES` | 330 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **.1** | `2000-ASSEMBLE-PPS-VARIABLES` | 330 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 330 | `2000_assemble_pps_variables.h_bsa_factor.default` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 337 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| threshold | **18.5** | `2000-ASSEMBLE-PPS-VARIABLES` | 337 | `2000_assemble_pps_variables.h_bmi.threshold` |
| default | **1.112** | `2000-ASSEMBLE-PPS-VARIABLES` | 337 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 337 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| threshold | **50** | `9000-MOVE-RESULTS` | 386 | `9000_move_results.pps_rtc.threshold` |

### `ESCAL062`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| constant | **2006** | `0100-INITIAL-ROUTINE` | 199 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 199 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| default | **52** | `0100-INITIAL-ROUTINE` | 199 | `0100_initial_routine.pps_rtc.default` |
| default | **53** | `1000-EDIT-THE-BILL-INFO` | 240 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **54** | `1000-EDIT-THE-BILL-INFO` | 246 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **55** | `1000-EDIT-THE-BILL-INFO` | 252 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **56** | `1000-EDIT-THE-BILL-INFO` | 258 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **57** | `1000-EDIT-THE-BILL-INFO` | 264 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **58** | `1000-EDIT-THE-BILL-INFO` | 273 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **300.00** | `1000-EDIT-THE-BILL-INFO` | 279 | `1000_edit_the_bill_info.b_patient_hgt.threshold` |
| default | **71** | `1000-EDIT-THE-BILL-INFO` | 279 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **500.00** | `1000-EDIT-THE-BILL-INFO` | 285 | `1000_edit_the_bill_info.b_patient_wgt.threshold` |
| default | **72** | `1000-EDIT-THE-BILL-INFO` | 285 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **18** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.620** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_age_factor.default` |
| threshold | **17** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **45** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.223** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_age_factor.default` |
| threshold | **44** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **60** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.055** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_age_factor.default` |
| threshold | **59** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **70** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.000** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_age_factor.default` |
| threshold | **69** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **80** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.094** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_age_factor.default` |
| threshold | **79** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.174** | `1200-CALC-AGE` | 311 | `1200_calc_age.h_age_factor.default` |
| constant | **.007184** | `2000-ASSEMBLE-PPS-VARIABLES` | 341 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.725** | `2000-ASSEMBLE-PPS-VARIABLES` | 341 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.425** | `2000-ASSEMBLE-PPS-VARIABLES` | 341 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **10000** | `2000-ASSEMBLE-PPS-VARIABLES` | 341 | `2000_assemble_pps_variables.h_bmi_rounded.constant` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 347 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| constant | **1.037** | `2000-ASSEMBLE-PPS-VARIABLES` | 347 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **1.84** | `2000-ASSEMBLE-PPS-VARIABLES` | 347 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **.1** | `2000-ASSEMBLE-PPS-VARIABLES` | 347 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 347 | `2000_assemble_pps_variables.h_bsa_factor.default` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| threshold | **18.5** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_bmi.threshold` |
| default | **1.112** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| threshold | **50** | `9000-MOVE-RESULTS` | 414 | `9000_move_results.pps_rtc.threshold` |

### `ESCAL070`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| constant | **2006** | `0100-INITIAL-ROUTINE` | 191 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 191 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| default | **52** | `0100-INITIAL-ROUTINE` | 191 | `0100_initial_routine.pps_rtc.default` |
| default | **53** | `1000-EDIT-THE-BILL-INFO` | 232 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **54** | `1000-EDIT-THE-BILL-INFO` | 238 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **55** | `1000-EDIT-THE-BILL-INFO` | 244 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **56** | `1000-EDIT-THE-BILL-INFO` | 250 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **57** | `1000-EDIT-THE-BILL-INFO` | 256 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **58** | `1000-EDIT-THE-BILL-INFO` | 265 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **300.00** | `1000-EDIT-THE-BILL-INFO` | 271 | `1000_edit_the_bill_info.b_patient_hgt.threshold` |
| default | **71** | `1000-EDIT-THE-BILL-INFO` | 271 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **500.00** | `1000-EDIT-THE-BILL-INFO` | 277 | `1000_edit_the_bill_info.b_patient_wgt.threshold` |
| default | **72** | `1000-EDIT-THE-BILL-INFO` | 277 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **18** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.620** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_age_factor.default` |
| threshold | **17** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **45** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.223** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_age_factor.default` |
| threshold | **44** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **60** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.055** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_age_factor.default` |
| threshold | **59** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **70** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.000** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_age_factor.default` |
| threshold | **69** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **80** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.094** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_age_factor.default` |
| threshold | **79** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.174** | `1200-CALC-AGE` | 303 | `1200_calc_age.h_age_factor.default` |
| constant | **.007184** | `2000-ASSEMBLE-PPS-VARIABLES` | 333 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.725** | `2000-ASSEMBLE-PPS-VARIABLES` | 333 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.425** | `2000-ASSEMBLE-PPS-VARIABLES` | 333 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **10000** | `2000-ASSEMBLE-PPS-VARIABLES` | 333 | `2000_assemble_pps_variables.h_bmi_rounded.constant` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 339 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| constant | **1.037** | `2000-ASSEMBLE-PPS-VARIABLES` | 339 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **1.84** | `2000-ASSEMBLE-PPS-VARIABLES` | 339 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **.1** | `2000-ASSEMBLE-PPS-VARIABLES` | 339 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 339 | `2000_assemble_pps_variables.h_bsa_factor.default` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 346 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| threshold | **18.5** | `2000-ASSEMBLE-PPS-VARIABLES` | 346 | `2000_assemble_pps_variables.h_bmi.threshold` |
| default | **1.112** | `2000-ASSEMBLE-PPS-VARIABLES` | 346 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 346 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| threshold | **50** | `9000-MOVE-RESULTS` | 406 | `9000_move_results.pps_rtc.threshold` |

### `ESCAL071`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| constant | **2006** | `0100-INITIAL-ROUTINE` | 202 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 202 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| constant | **2007** | `0100-INITIAL-ROUTINE` | 202 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 202 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 202 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| constant | **2007** | `0100-INITIAL-ROUTINE` | 202 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| default | **52** | `0100-INITIAL-ROUTINE` | 202 | `0100_initial_routine.pps_rtc.default` |
| default | **53** | `1000-EDIT-THE-BILL-INFO` | 247 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **54** | `1000-EDIT-THE-BILL-INFO` | 253 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **55** | `1000-EDIT-THE-BILL-INFO` | 259 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **56** | `1000-EDIT-THE-BILL-INFO` | 265 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **57** | `1000-EDIT-THE-BILL-INFO` | 271 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **58** | `1000-EDIT-THE-BILL-INFO` | 280 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **300.00** | `1000-EDIT-THE-BILL-INFO` | 286 | `1000_edit_the_bill_info.b_patient_hgt.threshold` |
| default | **71** | `1000-EDIT-THE-BILL-INFO` | 286 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **500.00** | `1000-EDIT-THE-BILL-INFO` | 292 | `1000_edit_the_bill_info.b_patient_wgt.threshold` |
| default | **72** | `1000-EDIT-THE-BILL-INFO` | 292 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **18** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.620** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_age_factor.default` |
| threshold | **17** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **45** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.223** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_age_factor.default` |
| threshold | **44** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **60** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.055** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_age_factor.default` |
| threshold | **59** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **70** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.000** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_age_factor.default` |
| threshold | **69** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **80** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.094** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_age_factor.default` |
| threshold | **79** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.174** | `1200-CALC-AGE` | 318 | `1200_calc_age.h_age_factor.default` |
| constant | **.007184** | `2000-ASSEMBLE-PPS-VARIABLES` | 348 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.725** | `2000-ASSEMBLE-PPS-VARIABLES` | 348 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.425** | `2000-ASSEMBLE-PPS-VARIABLES` | 348 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **10000** | `2000-ASSEMBLE-PPS-VARIABLES` | 348 | `2000_assemble_pps_variables.h_bmi_rounded.constant` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| constant | **1.037** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **1.84** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **.1** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 354 | `2000_assemble_pps_variables.h_bsa_factor.default` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 361 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| threshold | **18.5** | `2000-ASSEMBLE-PPS-VARIABLES` | 361 | `2000_assemble_pps_variables.h_bmi.threshold` |
| default | **1.112** | `2000-ASSEMBLE-PPS-VARIABLES` | 361 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 361 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| threshold | **50** | `9000-MOVE-RESULTS` | 421 | `9000_move_results.pps_rtc.threshold` |

### `ESCAL080`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| constant | **2006** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| constant | **2007** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| constant | **2007** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2008_wage_adj_pymt_rounded.constant` |
| constant | **2008** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2008_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2006_wage_adj_pymt_rounded.constant` |
| constant | **2006** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| constant | **2007** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2007_wage_adj_pymt_rounded.constant` |
| constant | **2007** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2008_wage_adj_pymt_rounded.constant` |
| constant | **2008** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.h_2008_wage_adj_pymt_rounded.constant` |
| default | **52** | `0100-INITIAL-ROUTINE` | 247 | `0100_initial_routine.pps_rtc.default` |
| default | **53** | `1000-EDIT-THE-BILL-INFO` | 296 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **54** | `1000-EDIT-THE-BILL-INFO` | 302 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **55** | `1000-EDIT-THE-BILL-INFO` | 308 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **56** | `1000-EDIT-THE-BILL-INFO` | 314 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **57** | `1000-EDIT-THE-BILL-INFO` | 320 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **58** | `1000-EDIT-THE-BILL-INFO` | 329 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **300.00** | `1000-EDIT-THE-BILL-INFO` | 335 | `1000_edit_the_bill_info.b_patient_hgt.threshold` |
| default | **71** | `1000-EDIT-THE-BILL-INFO` | 335 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **500.00** | `1000-EDIT-THE-BILL-INFO` | 341 | `1000_edit_the_bill_info.b_patient_wgt.threshold` |
| default | **72** | `1000-EDIT-THE-BILL-INFO` | 341 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **18** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.620** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_age_factor.default` |
| threshold | **17** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **45** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.223** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_age_factor.default` |
| threshold | **44** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **60** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.055** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_age_factor.default` |
| threshold | **59** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **70** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.000** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_age_factor.default` |
| threshold | **69** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **80** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.094** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_age_factor.default` |
| threshold | **79** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.174** | `1200-CALC-AGE` | 367 | `1200_calc_age.h_age_factor.default` |
| constant | **.007184** | `2000-ASSEMBLE-PPS-VARIABLES` | 397 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.725** | `2000-ASSEMBLE-PPS-VARIABLES` | 397 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.425** | `2000-ASSEMBLE-PPS-VARIABLES` | 397 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **10000** | `2000-ASSEMBLE-PPS-VARIABLES` | 397 | `2000_assemble_pps_variables.h_bmi_rounded.constant` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 403 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| constant | **1.037** | `2000-ASSEMBLE-PPS-VARIABLES` | 403 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **1.84** | `2000-ASSEMBLE-PPS-VARIABLES` | 403 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **.1** | `2000-ASSEMBLE-PPS-VARIABLES` | 403 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 403 | `2000_assemble_pps_variables.h_bsa_factor.default` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| threshold | **18.5** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_bmi.threshold` |
| default | **1.112** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| threshold | **50** | `9000-MOVE-RESULTS` | 470 | `9000_move_results.pps_rtc.threshold` |

### `ESCAL091`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **52** | `0100-INITIAL-ROUTINE` | 266 | `0100_initial_routine.pps_rtc.default` |
| default | **53** | `1000-EDIT-THE-BILL-INFO` | 303 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **54** | `1000-EDIT-THE-BILL-INFO` | 309 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **55** | `1000-EDIT-THE-BILL-INFO` | 315 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **56** | `1000-EDIT-THE-BILL-INFO` | 321 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **57** | `1000-EDIT-THE-BILL-INFO` | 327 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **58** | `1000-EDIT-THE-BILL-INFO` | 336 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **300.00** | `1000-EDIT-THE-BILL-INFO` | 342 | `1000_edit_the_bill_info.b_patient_hgt.threshold` |
| default | **71** | `1000-EDIT-THE-BILL-INFO` | 342 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **500.00** | `1000-EDIT-THE-BILL-INFO` | 348 | `1000_edit_the_bill_info.b_patient_wgt.threshold` |
| default | **72** | `1000-EDIT-THE-BILL-INFO` | 348 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **18** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.620** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_age_factor.default` |
| threshold | **17** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **45** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.223** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_age_factor.default` |
| threshold | **44** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **60** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.055** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_age_factor.default` |
| threshold | **59** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **70** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.000** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_age_factor.default` |
| threshold | **69** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **80** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.094** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_age_factor.default` |
| threshold | **79** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.174** | `1200-CALC-AGE` | 374 | `1200_calc_age.h_age_factor.default` |
| constant | **.007184** | `2000-ASSEMBLE-PPS-VARIABLES` | 404 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.725** | `2000-ASSEMBLE-PPS-VARIABLES` | 404 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.425** | `2000-ASSEMBLE-PPS-VARIABLES` | 404 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **10000** | `2000-ASSEMBLE-PPS-VARIABLES` | 404 | `2000_assemble_pps_variables.h_bmi_rounded.constant` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| constant | **1.037** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **1.84** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **.1** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 410 | `2000_assemble_pps_variables.h_bsa_factor.default` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 417 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| threshold | **18.5** | `2000-ASSEMBLE-PPS-VARIABLES` | 417 | `2000_assemble_pps_variables.h_bmi.threshold` |
| default | **1.112** | `2000-ASSEMBLE-PPS-VARIABLES` | 417 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 417 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| threshold | **50** | `9000-MOVE-RESULTS` | 475 | `9000_move_results.pps_rtc.threshold` |

### `ESCAL100`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **52** | `0100-INITIAL-ROUTINE` | 276 | `0100_initial_routine.pps_rtc.default` |
| default | **53** | `1000-EDIT-THE-BILL-INFO` | 313 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **54** | `1000-EDIT-THE-BILL-INFO` | 319 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **55** | `1000-EDIT-THE-BILL-INFO` | 325 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **56** | `1000-EDIT-THE-BILL-INFO` | 331 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **57** | `1000-EDIT-THE-BILL-INFO` | 337 | `1000_edit_the_bill_info.pps_rtc.default` |
| default | **58** | `1000-EDIT-THE-BILL-INFO` | 346 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **300.00** | `1000-EDIT-THE-BILL-INFO` | 352 | `1000_edit_the_bill_info.b_patient_hgt.threshold` |
| default | **71** | `1000-EDIT-THE-BILL-INFO` | 352 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **500.00** | `1000-EDIT-THE-BILL-INFO` | 358 | `1000_edit_the_bill_info.b_patient_wgt.threshold` |
| default | **72** | `1000-EDIT-THE-BILL-INFO` | 358 | `1000_edit_the_bill_info.pps_rtc.default` |
| threshold | **18** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.620** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_age_factor.default` |
| threshold | **17** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **45** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.223** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_age_factor.default` |
| threshold | **44** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **60** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.055** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_age_factor.default` |
| threshold | **59** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **70** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.000** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_age_factor.default` |
| threshold | **69** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| threshold | **80** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.094** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_age_factor.default` |
| threshold | **79** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_patient_age.threshold` |
| default | **1.174** | `1200-CALC-AGE` | 384 | `1200_calc_age.h_age_factor.default` |
| constant | **.007184** | `2000-ASSEMBLE-PPS-VARIABLES` | 414 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.725** | `2000-ASSEMBLE-PPS-VARIABLES` | 414 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **.425** | `2000-ASSEMBLE-PPS-VARIABLES` | 414 | `2000_assemble_pps_variables.h_bsa_rounded.constant` |
| constant | **10000** | `2000-ASSEMBLE-PPS-VARIABLES` | 414 | `2000_assemble_pps_variables.h_bmi_rounded.constant` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 420 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| constant | **1.037** | `2000-ASSEMBLE-PPS-VARIABLES` | 420 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **1.84** | `2000-ASSEMBLE-PPS-VARIABLES` | 420 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| constant | **.1** | `2000-ASSEMBLE-PPS-VARIABLES` | 420 | `2000_assemble_pps_variables.h_bsa_factor_rounded.constant` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 420 | `2000_assemble_pps_variables.h_bsa_factor.default` |
| threshold | **17** | `2000-ASSEMBLE-PPS-VARIABLES` | 427 | `2000_assemble_pps_variables.h_patient_age.threshold` |
| threshold | **18.5** | `2000-ASSEMBLE-PPS-VARIABLES` | 427 | `2000_assemble_pps_variables.h_bmi.threshold` |
| default | **1.112** | `2000-ASSEMBLE-PPS-VARIABLES` | 427 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| default | **1.000** | `2000-ASSEMBLE-PPS-VARIABLES` | 427 | `2000_assemble_pps_variables.h_bmi_factor.default` |
| threshold | **50** | `9000-MOVE-RESULTS` | 486 | `9000_move_results.pps_rtc.threshold` |

### `ESCAL117`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| threshold | **18** | `0000-START-TO-FINISH` | 455 | `0000_start_to_finish.h_patient_age.threshold` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 476 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 482 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 488 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 494 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 500 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 506 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 515 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 521 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 521 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 527 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 527 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 538 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 545 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 552 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 558 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 564 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 689 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 689 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 689 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 689 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 689 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 689 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 730 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 730 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 730 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 730 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **1.87** | `2000-CALCULATE-BUNDLED-FACTORS` | 730 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 730 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 730 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 743 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 746 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 746 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 746 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 756 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 756 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 756 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 782 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 782 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 782 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 782 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 782 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 827 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 827 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 827 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 856 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 889 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 912 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 976 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 976 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 976 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 976 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 976 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 976 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1017 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1017 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1017 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1017 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **1.87** | `2500-CALC-OUTLIER-FACTORS` | 1017 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1017 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1017 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1030 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1033 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1033 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1033 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1042 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1042 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1042 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1059 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1059 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1059 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1059 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1059 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1098 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1123 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1123 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1123 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1151 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1151 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1151 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1151 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1151 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1199 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **18** | `5000-CALC-COMP-RATE-FACTORS` | 1260 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **45** | `5000-CALC-COMP-RATE-FACTORS` | 1260 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **60** | `5000-CALC-COMP-RATE-FACTORS` | 1260 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **70** | `5000-CALC-COMP-RATE-FACTORS` | 1260 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **80** | `5000-CALC-COMP-RATE-FACTORS` | 1260 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **.007184** | `5000-CALC-COMP-RATE-FACTORS` | 1286 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.725** | `5000-CALC-COMP-RATE-FACTORS` | 1286 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.425** | `5000-CALC-COMP-RATE-FACTORS` | 1286 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1286 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **1.84** | `5000-CALC-COMP-RATE-FACTORS` | 1286 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| constant | **.1** | `5000-CALC-COMP-RATE-FACTORS` | 1286 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1286 | `5000_calc_comp_rate_factors.h_bsa_factor.default` |
| constant | **10000** | `5000-CALC-COMP-RATE-FACTORS` | 1299 | `5000_calc_comp_rate_factors.h_bmi__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1302 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **18.5** | `5000-CALC-COMP-RATE-FACTORS` | 1302 | `5000_calc_comp_rate_factors.h_bmi.threshold` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1302 | `5000_calc_comp_rate_factors.h_bmi_factor.default` |
| constant | **49** | `5000-CALC-COMP-RATE-FACTORS` | 1330 | `5000_calc_comp_rate_factors.h_pymt_amt_rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1419 | `9000_set_return_code.pps_rtc.default` |

### `ESCAL122`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| threshold | **18** | `0000-START-TO-FINISH` | 493 | `0000_start_to_finish.h_patient_age.threshold` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 514 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 520 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 526 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 532 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 538 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 544 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 553 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 559 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 569 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 569 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 575 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 575 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 586 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 593 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 600 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 606 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 612 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **1.000** | `1200-INITIALIZATION` | 629 | `1200_initialization.qip_reduction.default` |
| default | **0.995** | `1200-INITIALIZATION` | 629 | `1200_initialization.qip_reduction.default` |
| default | **0.990** | `1200-INITIALIZATION` | 629 | `1200_initialization.qip_reduction.default` |
| default | **0.985** | `1200-INITIALIZATION` | 629 | `1200_initialization.qip_reduction.default` |
| default | **0.980** | `1200-INITIALIZATION` | 629 | `1200_initialization.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 760 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 760 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 760 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 760 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 760 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 760 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 801 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 801 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 801 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 801 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **1.87** | `2000-CALCULATE-BUNDLED-FACTORS` | 801 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 801 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 801 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 814 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 817 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 817 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 817 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 827 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 827 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 827 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 855 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 855 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 855 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 855 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 855 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 900 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 900 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 900 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 927 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 954 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1007 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1071 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1071 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1071 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1071 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1071 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1071 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1112 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1112 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1112 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1112 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **1.87** | `2500-CALC-OUTLIER-FACTORS` | 1112 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1112 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1112 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1125 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1128 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1128 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1128 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1137 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1137 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1137 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1154 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1154 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1154 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1154 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1154 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1193 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1218 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1218 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1218 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1246 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1246 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1246 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1246 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1246 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1294 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1365 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1391 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1417 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1417 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1417 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1433 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1433 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1433 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1433 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1433 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| threshold | **18** | `5000-CALC-COMP-RATE-FACTORS` | 1473 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **45** | `5000-CALC-COMP-RATE-FACTORS` | 1473 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **60** | `5000-CALC-COMP-RATE-FACTORS` | 1473 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **70** | `5000-CALC-COMP-RATE-FACTORS` | 1473 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **80** | `5000-CALC-COMP-RATE-FACTORS` | 1473 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **.007184** | `5000-CALC-COMP-RATE-FACTORS` | 1499 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.725** | `5000-CALC-COMP-RATE-FACTORS` | 1499 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.425** | `5000-CALC-COMP-RATE-FACTORS` | 1499 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1499 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **1.87** | `5000-CALC-COMP-RATE-FACTORS` | 1499 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| constant | **.1** | `5000-CALC-COMP-RATE-FACTORS` | 1499 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1499 | `5000_calc_comp_rate_factors.h_bsa_factor.default` |
| constant | **10000** | `5000-CALC-COMP-RATE-FACTORS` | 1512 | `5000_calc_comp_rate_factors.h_bmi__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1515 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **18.5** | `5000-CALC-COMP-RATE-FACTORS` | 1515 | `5000_calc_comp_rate_factors.h_bmi.threshold` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1515 | `5000_calc_comp_rate_factors.h_bmi_factor.default` |
| default | **17** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1632 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1830 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1830 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1830 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1830 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1830 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1830 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL130`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| threshold | **18** | `0000-START-TO-FINISH` | 522 | `0000_start_to_finish.h_patient_age.threshold` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 543 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 549 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 555 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 561 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 567 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 573 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 582 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 588 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 598 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 598 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 604 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 604 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 615 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 622 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 629 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 635 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 641 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **1.000** | `1200-INITIALIZATION` | 658 | `1200_initialization.qip_reduction.default` |
| default | **0.995** | `1200-INITIALIZATION` | 658 | `1200_initialization.qip_reduction.default` |
| default | **0.990** | `1200-INITIALIZATION` | 658 | `1200_initialization.qip_reduction.default` |
| default | **0.985** | `1200-INITIALIZATION` | 658 | `1200_initialization.qip_reduction.default` |
| default | **0.980** | `1200-INITIALIZATION` | 658 | `1200_initialization.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 789 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 789 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 789 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 789 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 789 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 789 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **1.87** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 843 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 846 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 846 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 846 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 856 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 856 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 856 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 884 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 884 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 884 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 884 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 884 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 929 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 929 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 929 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 956 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 983 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1036 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1100 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1100 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1100 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1100 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1100 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1100 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1141 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1141 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1141 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1141 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **1.87** | `2500-CALC-OUTLIER-FACTORS` | 1141 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1141 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1141 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1154 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1157 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1157 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1157 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1166 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1166 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1166 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1183 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1183 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1183 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1183 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1183 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1222 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1247 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1247 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1247 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1275 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1275 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1275 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1275 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1275 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1323 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1394 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1420 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1446 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1446 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1446 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1462 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1462 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1462 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1462 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1462 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| threshold | **18** | `5000-CALC-COMP-RATE-FACTORS` | 1502 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **45** | `5000-CALC-COMP-RATE-FACTORS` | 1502 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **60** | `5000-CALC-COMP-RATE-FACTORS` | 1502 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **70** | `5000-CALC-COMP-RATE-FACTORS` | 1502 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **80** | `5000-CALC-COMP-RATE-FACTORS` | 1502 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **.007184** | `5000-CALC-COMP-RATE-FACTORS` | 1528 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.725** | `5000-CALC-COMP-RATE-FACTORS` | 1528 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.425** | `5000-CALC-COMP-RATE-FACTORS` | 1528 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1528 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **1.87** | `5000-CALC-COMP-RATE-FACTORS` | 1528 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| constant | **.1** | `5000-CALC-COMP-RATE-FACTORS` | 1528 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1528 | `5000_calc_comp_rate_factors.h_bsa_factor.default` |
| constant | **10000** | `5000-CALC-COMP-RATE-FACTORS` | 1541 | `5000_calc_comp_rate_factors.h_bmi__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1544 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **18.5** | `5000-CALC-COMP-RATE-FACTORS` | 1544 | `5000_calc_comp_rate_factors.h_bmi.threshold` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1544 | `5000_calc_comp_rate_factors.h_bmi_factor.default` |
| default | **17** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1661 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1859 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1859 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1859 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1859 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1859 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1859 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL140`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| threshold | **18** | `0000-START-TO-FINISH` | 568 | `0000_start_to_finish.h_patient_age.threshold` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 589 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 595 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 601 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 607 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 613 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 619 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 628 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 634 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 644 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 644 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 650 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 650 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 661 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 668 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 675 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 681 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 687 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **1.000** | `1200-INITIALIZATION` | 704 | `1200_initialization.qip_reduction.default` |
| default | **0.995** | `1200-INITIALIZATION` | 704 | `1200_initialization.qip_reduction.default` |
| default | **0.990** | `1200-INITIALIZATION` | 704 | `1200_initialization.qip_reduction.default` |
| default | **0.985** | `1200-INITIALIZATION` | 704 | `1200_initialization.qip_reduction.default` |
| default | **0.980** | `1200-INITIALIZATION` | 704 | `1200_initialization.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 835 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 835 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 835 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 835 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 835 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 835 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **1.87** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 889 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 892 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 892 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 892 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 902 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 902 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 902 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 930 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 930 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 930 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 930 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 930 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 975 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 975 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 975 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1002 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1029 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1082 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1146 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1146 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1146 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1146 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1146 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1146 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1187 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1187 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1187 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1187 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **1.87** | `2500-CALC-OUTLIER-FACTORS` | 1187 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1187 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1187 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1200 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1203 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1203 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1203 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1212 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1212 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1212 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1229 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1229 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1229 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1229 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1229 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1268 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1293 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1293 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1293 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1321 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1321 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1321 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1321 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1321 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1369 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1440 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1466 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1492 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1492 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1492 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1508 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1508 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1508 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1508 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1508 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| threshold | **18** | `5000-CALC-COMP-RATE-FACTORS` | 1548 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **45** | `5000-CALC-COMP-RATE-FACTORS` | 1548 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **60** | `5000-CALC-COMP-RATE-FACTORS` | 1548 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **70** | `5000-CALC-COMP-RATE-FACTORS` | 1548 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **80** | `5000-CALC-COMP-RATE-FACTORS` | 1548 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **.007184** | `5000-CALC-COMP-RATE-FACTORS` | 1574 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.725** | `5000-CALC-COMP-RATE-FACTORS` | 1574 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.425** | `5000-CALC-COMP-RATE-FACTORS` | 1574 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1574 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **1.87** | `5000-CALC-COMP-RATE-FACTORS` | 1574 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| constant | **.1** | `5000-CALC-COMP-RATE-FACTORS` | 1574 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1574 | `5000_calc_comp_rate_factors.h_bsa_factor.default` |
| constant | **10000** | `5000-CALC-COMP-RATE-FACTORS` | 1587 | `5000_calc_comp_rate_factors.h_bmi__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1590 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **18.5** | `5000-CALC-COMP-RATE-FACTORS` | 1590 | `5000_calc_comp_rate_factors.h_bmi.threshold` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1590 | `5000_calc_comp_rate_factors.h_bmi_factor.default` |
| default | **17** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1707 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1905 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1905 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1905 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1905 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1905 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1905 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL151`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| threshold | **18** | `0000-START-TO-FINISH` | 601 | `0000_start_to_finish.h_patient_age.threshold` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 622 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 628 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 634 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 640 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 646 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 652 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 661 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 667 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 677 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 677 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 683 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 683 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 694 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 701 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 708 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 714 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 720 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **1.000** | `1200-INITIALIZATION` | 737 | `1200_initialization.qip_reduction.default` |
| default | **0.995** | `1200-INITIALIZATION` | 737 | `1200_initialization.qip_reduction.default` |
| default | **0.990** | `1200-INITIALIZATION` | 737 | `1200_initialization.qip_reduction.default` |
| default | **0.985** | `1200-INITIALIZATION` | 737 | `1200_initialization.qip_reduction.default` |
| default | **0.980** | `1200-INITIALIZATION` | 737 | `1200_initialization.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 868 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 868 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 868 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 868 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 868 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 868 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 909 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 909 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 909 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 909 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **1.87** | `2000-CALCULATE-BUNDLED-FACTORS` | 909 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 909 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 909 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 922 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 925 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 925 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 925 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 935 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 935 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 935 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 963 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 963 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 963 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 963 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 963 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1062 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1115 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1179 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1179 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1179 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1179 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1179 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1179 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1220 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1220 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1220 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1220 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **1.87** | `2500-CALC-OUTLIER-FACTORS` | 1220 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1220 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1220 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1233 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1236 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1236 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1236 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1245 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1245 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1245 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1262 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1262 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1262 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1262 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1262 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1301 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1326 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1326 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1326 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1354 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1354 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1354 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1354 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1354 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1402 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1473 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1499 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1525 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1525 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1525 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1541 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1541 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1541 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1541 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1541 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| threshold | **18** | `5000-CALC-COMP-RATE-FACTORS` | 1581 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **45** | `5000-CALC-COMP-RATE-FACTORS` | 1581 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **60** | `5000-CALC-COMP-RATE-FACTORS` | 1581 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **70** | `5000-CALC-COMP-RATE-FACTORS` | 1581 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **80** | `5000-CALC-COMP-RATE-FACTORS` | 1581 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **.007184** | `5000-CALC-COMP-RATE-FACTORS` | 1607 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.725** | `5000-CALC-COMP-RATE-FACTORS` | 1607 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.425** | `5000-CALC-COMP-RATE-FACTORS` | 1607 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1607 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **1.87** | `5000-CALC-COMP-RATE-FACTORS` | 1607 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| constant | **.1** | `5000-CALC-COMP-RATE-FACTORS` | 1607 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1607 | `5000_calc_comp_rate_factors.h_bsa_factor.default` |
| constant | **10000** | `5000-CALC-COMP-RATE-FACTORS` | 1620 | `5000_calc_comp_rate_factors.h_bmi__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1623 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **18.5** | `5000-CALC-COMP-RATE-FACTORS` | 1623 | `5000_calc_comp_rate_factors.h_bmi.threshold` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1623 | `5000_calc_comp_rate_factors.h_bmi_factor.default` |
| default | **17** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1740 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1938 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1938 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1938 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1938 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1938 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1938 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL160`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| threshold | **18** | `0000-START-TO-FINISH` | 633 | `0000_start_to_finish.h_patient_age.threshold` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 654 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 660 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 666 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 672 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 678 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 684 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 693 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 699 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 709 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 709 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 715 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 715 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 726 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 733 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 740 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 746 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 763 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **1.000** | `1200-INITIALIZATION` | 780 | `1200_initialization.qip_reduction.default` |
| default | **0.995** | `1200-INITIALIZATION` | 780 | `1200_initialization.qip_reduction.default` |
| default | **0.990** | `1200-INITIALIZATION` | 780 | `1200_initialization.qip_reduction.default` |
| default | **0.985** | `1200-INITIALIZATION` | 780 | `1200_initialization.qip_reduction.default` |
| default | **0.980** | `1200-INITIALIZATION` | 780 | `1200_initialization.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 912 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 912 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 912 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 912 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 912 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 912 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 953 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 953 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 953 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 953 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **1.90** | `2000-CALCULATE-BUNDLED-FACTORS` | 953 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 953 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 953 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 966 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 969 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 969 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 969 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 979 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 979 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 979 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1007 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1007 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1007 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1007 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1007 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1052 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1052 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1052 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1069 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1069 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1069 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1087 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1114 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1167 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1231 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1231 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1231 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1231 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1231 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1231 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1272 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1272 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1272 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1272 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **1.90** | `2500-CALC-OUTLIER-FACTORS` | 1272 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1272 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1272 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1285 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1288 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1288 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1288 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1297 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1297 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1297 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1315 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1315 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1315 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1315 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1315 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1354 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1369 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1369 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1369 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1389 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1389 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1389 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1417 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1417 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1417 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1417 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1417 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1465 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1537 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1563 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1590 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1590 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1590 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1606 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1606 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1606 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1606 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1606 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| threshold | **18** | `5000-CALC-COMP-RATE-FACTORS` | 1646 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **45** | `5000-CALC-COMP-RATE-FACTORS` | 1646 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **60** | `5000-CALC-COMP-RATE-FACTORS` | 1646 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **70** | `5000-CALC-COMP-RATE-FACTORS` | 1646 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **80** | `5000-CALC-COMP-RATE-FACTORS` | 1646 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **.007184** | `5000-CALC-COMP-RATE-FACTORS` | 1672 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.725** | `5000-CALC-COMP-RATE-FACTORS` | 1672 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| constant | **.425** | `5000-CALC-COMP-RATE-FACTORS` | 1672 | `5000_calc_comp_rate_factors.h_bsa__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1672 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| constant | **1.87** | `5000-CALC-COMP-RATE-FACTORS` | 1672 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| constant | **.1** | `5000-CALC-COMP-RATE-FACTORS` | 1672 | `5000_calc_comp_rate_factors.h_bsa_factor__rounded.constant` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1672 | `5000_calc_comp_rate_factors.h_bsa_factor.default` |
| constant | **10000** | `5000-CALC-COMP-RATE-FACTORS` | 1685 | `5000_calc_comp_rate_factors.h_bmi__rounded.constant` |
| threshold | **17** | `5000-CALC-COMP-RATE-FACTORS` | 1688 | `5000_calc_comp_rate_factors.h_patient_age.threshold` |
| threshold | **18.5** | `5000-CALC-COMP-RATE-FACTORS` | 1688 | `5000_calc_comp_rate_factors.h_bmi.threshold` |
| default | **1.000** | `5000-CALC-COMP-RATE-FACTORS` | 1688 | `5000_calc_comp_rate_factors.h_bmi_factor.default` |
| default | **17** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1805 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2003 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2003 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2003 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2003 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2003 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2003 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL170`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 674 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 680 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 686 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 692 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 700 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 708 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 717 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 723 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 733 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 733 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 741 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 741 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 754 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 761 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 768 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 774 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 791 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 824 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 834 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.995** | `2000-CALCULATE-BUNDLED-FACTORS` | 834 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.990** | `2000-CALCULATE-BUNDLED-FACTORS` | 834 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.985** | `2000-CALCULATE-BUNDLED-FACTORS` | 834 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.980** | `2000-CALCULATE-BUNDLED-FACTORS` | 834 | `2000_calculate_bundled_factors.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 951 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 951 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 951 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 951 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 951 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 951 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 992 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 992 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 992 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 992 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 992 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 992 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1006 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1009 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 1009 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1009 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1047 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1047 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1047 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1047 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1047 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1092 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1092 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1092 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1109 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1109 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1109 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1127 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1154 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1206 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1270 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1270 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1270 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1270 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1270 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1270 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1311 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1311 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1311 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1311 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1311 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1311 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1325 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1328 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1328 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1328 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1337 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1337 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1337 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1355 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1355 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1355 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1355 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1355 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1394 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1409 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1409 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1409 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1429 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1429 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1429 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1505 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1577 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1603 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1630 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1630 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1630 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1646 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1646 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1646 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1646 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1646 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1735 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1933 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1933 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1933 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1933 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1933 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1933 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL171`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 677 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 684 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 692 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 698 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 704 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 712 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 720 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 729 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 739 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 739 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 747 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 747 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 760 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 767 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 774 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 780 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 797 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 830 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 840 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.995** | `2000-CALCULATE-BUNDLED-FACTORS` | 840 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.990** | `2000-CALCULATE-BUNDLED-FACTORS` | 840 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.985** | `2000-CALCULATE-BUNDLED-FACTORS` | 840 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.980** | `2000-CALCULATE-BUNDLED-FACTORS` | 840 | `2000_calculate_bundled_factors.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 957 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 957 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 957 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 957 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 957 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 957 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 998 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 998 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 998 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 998 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 998 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 998 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1012 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1015 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 1015 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1015 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1025 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1025 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1025 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1053 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1053 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1053 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1053 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1053 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1098 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1098 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1098 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1115 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1115 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1115 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1133 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1160 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1212 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1276 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1276 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1276 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1276 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1276 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1276 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1317 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1317 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1317 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1317 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1317 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1317 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1331 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1334 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1334 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1334 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1343 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1343 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1343 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1400 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1415 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1415 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1415 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1435 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1435 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1435 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1463 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1463 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1463 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1463 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1463 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1511 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1583 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1609 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1636 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1636 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1636 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1652 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1652 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1652 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1652 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1652 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1741 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1939 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1939 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1939 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1939 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1939 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1939 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL180`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 698 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 705 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 713 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 719 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 725 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 733 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 741 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 750 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 760 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 760 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 768 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 768 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 781 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 788 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 795 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 801 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 818 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 851 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 861 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.995** | `2000-CALCULATE-BUNDLED-FACTORS` | 861 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.990** | `2000-CALCULATE-BUNDLED-FACTORS` | 861 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.985** | `2000-CALCULATE-BUNDLED-FACTORS` | 861 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.980** | `2000-CALCULATE-BUNDLED-FACTORS` | 861 | `2000_calculate_bundled_factors.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 978 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 978 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 978 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 978 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 978 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 978 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1019 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1033 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1036 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 1036 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1036 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1046 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1046 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1046 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1074 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1074 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1074 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1074 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1074 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1119 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1119 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1119 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1136 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1136 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1136 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1154 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1181 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1241 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1305 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1305 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1305 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1305 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1305 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1305 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1346 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1346 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1346 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1346 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1346 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1346 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1360 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1363 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1363 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1363 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1372 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1372 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1372 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1429 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1444 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1444 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1444 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1464 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1464 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1464 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1492 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1492 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1492 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1492 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1492 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1540 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1612 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1638 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1665 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1665 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1665 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1681 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1681 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1681 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1681 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1681 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1770 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1970 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1970 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1970 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1970 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1970 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1970 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL191`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 713 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 720 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 728 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 734 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 740 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 748 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 756 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 765 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 775 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 775 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 783 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 783 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 796 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 803 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 810 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 816 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 833 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 866 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.995** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.990** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.985** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.980** | `2000-CALCULATE-BUNDLED-FACTORS` | 876 | `2000_calculate_bundled_factors.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 993 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 993 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 993 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 993 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 993 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 993 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 1034 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 1034 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 1034 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1034 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 1034 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1034 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1048 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1051 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 1051 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1051 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1061 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1061 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1061 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1089 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1089 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1089 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1089 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1089 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1134 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1134 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1134 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1151 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1151 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1151 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1169 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1196 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1256 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1320 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1320 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1320 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1320 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1320 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1320 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1361 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1375 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1378 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1378 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1378 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1387 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1387 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1387 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1405 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1405 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1405 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1405 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1405 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1444 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1459 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1459 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1459 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1479 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1479 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1479 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1507 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1507 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1507 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1507 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1507 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1555 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1627 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1653 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1680 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1680 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1680 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1696 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1696 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1696 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1696 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1696 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1785 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1985 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1985 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1985 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1985 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1985 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 1985 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL200`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 728 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 735 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 743 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 749 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 755 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 763 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 771 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 780 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 790 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 790 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 798 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 798 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 811 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 818 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 825 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 831 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 848 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 881 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 891 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.995** | `2000-CALCULATE-BUNDLED-FACTORS` | 891 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.990** | `2000-CALCULATE-BUNDLED-FACTORS` | 891 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.985** | `2000-CALCULATE-BUNDLED-FACTORS` | 891 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.980** | `2000-CALCULATE-BUNDLED-FACTORS` | 891 | `2000_calculate_bundled_factors.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 1008 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 1049 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 1049 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 1049 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1049 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 1049 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1049 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1063 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1066 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 1066 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1066 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1104 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1104 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1104 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1104 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1104 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1149 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1149 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1149 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1166 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1166 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1166 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1184 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **74** | `2000-CALCULATE-BUNDLED-FACTORS` | 1211 | `2000_calculate_bundled_factors.h_pps_final_pay_amt__rounded.constant` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1271 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1335 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1335 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1335 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1335 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1335 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1335 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1376 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1376 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1376 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1376 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1376 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1376 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1393 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1393 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1393 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1402 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1402 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1402 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1420 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1420 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1420 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1420 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1420 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1459 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1474 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1474 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1474 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1494 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1494 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1494 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1522 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1522 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1522 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1522 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1522 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1570 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1642 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1668 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1695 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1695 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1695 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1711 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1711 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1711 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1711 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1711 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1800 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2000 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2000 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2000 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2000 | `9100_move_results.pps_2011_full_pps_rate______rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2000 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2000 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL202`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 755 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 762 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 770 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 776 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 782 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 790 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 798 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 807 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 817 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 817 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 825 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 825 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 838 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 845 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 852 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 858 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 875 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 908 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 918 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.995** | `2000-CALCULATE-BUNDLED-FACTORS` | 918 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.990** | `2000-CALCULATE-BUNDLED-FACTORS` | 918 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.985** | `2000-CALCULATE-BUNDLED-FACTORS` | 918 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.980** | `2000-CALCULATE-BUNDLED-FACTORS` | 918 | `2000_calculate_bundled_factors.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 1035 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1090 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1093 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 1093 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1093 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1103 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1103 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1103 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1131 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1131 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1131 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1131 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1131 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1176 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1176 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1176 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1193 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1193 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1193 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1211 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1326 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1390 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1431 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1431 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1431 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1431 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1431 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1431 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1445 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1448 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1448 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1448 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1457 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1475 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1475 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1475 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1475 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1475 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1514 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1529 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1529 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1529 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1549 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1549 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1549 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1577 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1577 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1577 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1577 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1577 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1625 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1697 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1723 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1750 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1750 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1750 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1766 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1766 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1766 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1766 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1766 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1855 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2057 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2057 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2057 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2057 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2057 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESCAL212`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **58** | `1000-VALIDATE-BILL-ELEMENTS` | 796 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **52** | `1000-VALIDATE-BILL-ELEMENTS` | 803 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 811 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **54** | `1000-VALIDATE-BILL-ELEMENTS` | 817 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **55** | `1000-VALIDATE-BILL-ELEMENTS` | 823 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **56** | `1000-VALIDATE-BILL-ELEMENTS` | 831 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **57** | `1000-VALIDATE-BILL-ELEMENTS` | 839 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **53** | `1000-VALIDATE-BILL-ELEMENTS` | 848 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **300.00** | `1000-VALIDATE-BILL-ELEMENTS` | 858 | `1000_validate_bill_elements.b_patient_hgt.threshold` |
| default | **71** | `1000-VALIDATE-BILL-ELEMENTS` | 858 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **500.00** | `1000-VALIDATE-BILL-ELEMENTS` | 866 | `1000_validate_bill_elements.b_patient_wgt.threshold` |
| default | **72** | `1000-VALIDATE-BILL-ELEMENTS` | 866 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **73** | `1000-VALIDATE-BILL-ELEMENTS` | 879 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **74** | `1000-VALIDATE-BILL-ELEMENTS` | 886 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **75** | `1000-VALIDATE-BILL-ELEMENTS` | 893 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **76** | `1000-VALIDATE-BILL-ELEMENTS` | 899 | `1000_validate_bill_elements.pps_rtc.default` |
| default | **81** | `1000-VALIDATE-BILL-ELEMENTS` | 916 | `1000_validate_bill_elements.pps_rtc.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 949 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 959 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.995** | `2000-CALCULATE-BUNDLED-FACTORS` | 959 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.990** | `2000-CALCULATE-BUNDLED-FACTORS` | 959 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.985** | `2000-CALCULATE-BUNDLED-FACTORS` | 959 | `2000_calculate_bundled_factors.qip_reduction.default` |
| default | **0.980** | `2000-CALCULATE-BUNDLED-FACTORS` | 959 | `2000_calculate_bundled_factors.qip_reduction.default` |
| threshold | **13** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **45** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **60** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **70** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **80** | `2000-CALCULATE-BUNDLED-FACTORS` | 1076 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.007184** | `2000-CALCULATE-BUNDLED-FACTORS` | 1117 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.725** | `2000-CALCULATE-BUNDLED-FACTORS` | 1117 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| constant | **.425** | `2000-CALCULATE-BUNDLED-FACTORS` | 1117 | `2000_calculate_bundled_factors.h_bun_bsa__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1117 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| constant | **.1** | `2000-CALCULATE-BUNDLED-FACTORS` | 1117 | `2000_calculate_bundled_factors.h_bun_bsa_factor__rounded.constant` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1117 | `2000_calculate_bundled_factors.h_bun_bsa_factor.default` |
| constant | **10000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1131 | `2000_calculate_bundled_factors.h_bun_bmi__rounded.constant` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1134 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2000-CALCULATE-BUNDLED-FACTORS` | 1134 | `2000_calculate_bundled_factors.h_bun_bmi.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1134 | `2000_calculate_bundled_factors.h_bun_bmi_factor.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1144 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1144 | `2000_calculate_bundled_factors.onset_date.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1144 | `2000_calculate_bundled_factors.h_bun_onset_factor.default` |
| threshold | **18** | `2000-CALCULATE-BUNDLED-FACTORS` | 1172 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1172 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1172 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1172 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1172 | `2000_calculate_bundled_factors.h_bun_comorbid_multiplier.default` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1217 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1217 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1217 | `2000_calculate_bundled_factors.h_bun_low_vol_multiplier.default` |
| threshold | **100** | `2000-CALCULATE-BUNDLED-FACTORS` | 1234 | `2000_calculate_bundled_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2000-CALCULATE-BUNDLED-FACTORS` | 1234 | `2000_calculate_bundled_factors.h_patient_age.threshold` |
| default | **1.000** | `2000-CALCULATE-BUNDLED-FACTORS` | 1234 | `2000_calculate_bundled_factors.h_bun_rural_multiplier.default` |
| threshold | **120** | `2000-CALCULATE-BUNDLED-FACTORS` | 1252 | `2000_calculate_bundled_factors.h_bun_onset_factor.threshold` |
| constant | **0.65** | `2000-CALCULATE-BUNDLED-FACTORS` | 1318 | `2000_calculate_bundled_factors.h_tpnies_payment.constant` |
| default | **0.21** | `2000-CALCULATE-BUNDLED-FACTORS` | 1347 | `2000_calculate_bundled_factors.h_network_reduction.default` |
| default | **0.50** | `2000-CALCULATE-BUNDLED-FACTORS` | 1347 | `2000_calculate_bundled_factors.h_network_reduction.default` |
| default | **1.000** | `2100-CALC-COMORBID-ADJUST` | 1392 | `2100_calc_comorbid_adjust.h_comorbid_multiplier.default` |
| threshold | **13** | `2500-CALC-OUTLIER-FACTORS` | 1456 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1456 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **45** | `2500-CALC-OUTLIER-FACTORS` | 1456 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **60** | `2500-CALC-OUTLIER-FACTORS` | 1456 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **70** | `2500-CALC-OUTLIER-FACTORS` | 1456 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **80** | `2500-CALC-OUTLIER-FACTORS` | 1456 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.007184** | `2500-CALC-OUTLIER-FACTORS` | 1497 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.725** | `2500-CALC-OUTLIER-FACTORS` | 1497 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| constant | **.425** | `2500-CALC-OUTLIER-FACTORS` | 1497 | `2500_calc_outlier_factors.h_out_bsa__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1497 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **.1** | `2500-CALC-OUTLIER-FACTORS` | 1497 | `2500_calc_outlier_factors.h_out_bsa_factor__rounded.constant` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1497 | `2500_calc_outlier_factors.h_out_bsa_factor.default` |
| constant | **10000** | `2500-CALC-OUTLIER-FACTORS` | 1511 | `2500_calc_outlier_factors.h_out_bmi__rounded.constant` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1514 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **18.5** | `2500-CALC-OUTLIER-FACTORS` | 1514 | `2500_calc_outlier_factors.h_out_bmi.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1514 | `2500_calc_outlier_factors.h_out_bmi_factor.default` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1523 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1523 | `2500_calc_outlier_factors.onset_date.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1523 | `2500_calc_outlier_factors.h_out_onset_factor.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1541 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1541 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **120** | `2500-CALC-OUTLIER-FACTORS` | 1541 | `2500_calc_outlier_factors.h_bun_onset_factor.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1541 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1541 | `2500_calc_outlier_factors.h_out_comorbid_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1580 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| threshold | **100** | `2500-CALC-OUTLIER-FACTORS` | 1595 | `2500_calc_outlier_factors.p_geo_cbsa.threshold` |
| threshold | **17** | `2500-CALC-OUTLIER-FACTORS` | 1595 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| default | **1.000** | `2500-CALC-OUTLIER-FACTORS` | 1595 | `2500_calc_outlier_factors.h_out_rural_multiplier.default` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1615 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1615 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1615 | `2500_calc_outlier_factors.h_out_cm_adj_predict_map_trt__rounded.constant` |
| threshold | **18** | `2500-CALC-OUTLIER-FACTORS` | 1643 | `2500_calc_outlier_factors.h_patient_age.threshold` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1643 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **18** | `2500-CALC-OUTLIER-FACTORS` | 1643 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1643 | `2500_calc_outlier_factors.h_out_predicted_map__rounded.constant` |
| constant | **17** | `2500-CALC-OUTLIER-FACTORS` | 1643 | `2500_calc_outlier_factors.h_out_payment__rounded.constant` |
| default | **1.000** | `2600-CALC-COMORBID-OUT-ADJUST` | 1691 | `2600_calc_comorbid_out_adjust.h_out_comorbid_multiplier.default` |
| threshold | **120** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1763 | `3000_low_vol_full_pps_payment.h_bun_onset_factor.threshold` |
| constant | **74** | `3000-LOW-VOL-FULL-PPS-PAYMENT` | 1789 | `3000_low_vol_full_pps_payment.h_lv_pps_final_pay_amt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1816 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1816 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1816 | `3100_low_vol_out_pps_payment.h_lv_out_cm_adj_predict_m_trt__rounded.constant` |
| threshold | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1832 | `3100_low_vol_out_pps_payment.h_patient_age.threshold` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1832 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **18** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1832 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1832 | `3100_low_vol_out_pps_payment.h_lv_out_predicted_map__rounded.constant` |
| constant | **17** | `3100-LOW-VOL-OUT-PPS-PAYMENT` | 1832 | `3100_low_vol_out_pps_payment.h_lv_out_payment__rounded.constant` |
| default | **17** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **16** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **15** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **14** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **24** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **19** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **29** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **23** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **18** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **30** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **28** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **34** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **35** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **33** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **07** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **06** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **09** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **03** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **26** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **21** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **12** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **25** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **20** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **32** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **10** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **27** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **22** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **11** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **08** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **04** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **05** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **31** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| default | **02** | `9000-SET-RETURN-CODE` | 1921 | `9000_set_return_code.pps_rtc.default` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2133 | `9100_move_results.pps_2011_blend_comp_rate____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2133 | `9100_move_results.pps_2011_full_comp_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2133 | `9100_move_results.pps_2011_blend_pps_rate_____rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2133 | `9100_move_results.pps_2011_blend_outlier_rate_rounded.constant` |
| constant | **2011** | `9100-MOVE-RESULTS` | 2133 | `9100_move_results.pps_2011_full_outlier_rate__rounded.constant` |

### `ESDRV212`

| Kind | Value | Paragraph | Line | Suggested Key |
|------|-------|-----------|------|---------------|
| default | **98** | `0100-ENTER-DRIVER` | 397 | `0100_enter_driver.pps_rtc.default` |
| default | **50** | `0100-ENTER-DRIVER` | 402 | `0100_enter_driver.pps_rtc.default` |
| default | **01** | `0100-ENTER-DRIVER` | 420 | `0100_enter_driver.pps_rtc.default` |
| default | **01** | `0100-ENTER-DRIVER` | 426 | `0100_enter_driver.pps_rtc.default` |
| default | **98** | `0100-ENTER-DRIVER` | 466 | `0100_enter_driver.pps_rtc.default` |
| default | **60** | `0500-FIND-MSA-WAGE-ADJ-RATE` | 964 | `0500_find_msa_wage_adj_rate.pps_rtc.default` |
| default | **60** | `0700-FIND-COMPOSITE-CBSA-WI` | 1007 | `0700_find_composite_cbsa_wi.pps_rtc.default` |
| default | **61** | `0700-FIND-COMPOSITE-CBSA-WI` | 1007 | `0700_find_composite_cbsa_wi.pps_rtc.default` |
| constant | **10** | `0800-FIND-BUNDLED-CBSA-WI` | 1072 | `0800_find_bundled_cbsa_wi.b_thru_year_code.constant` |
| default | **60** | `0800-FIND-BUNDLED-CBSA-WI` | 1078 | `0800_find_bundled_cbsa_wi.pps_rtc.default` |
| default | **61** | `0800-FIND-BUNDLED-CBSA-WI` | 1078 | `0800_find_bundled_cbsa_wi.pps_rtc.default` |
| threshold | **-0.05** | `0800-FIND-BUNDLED-CBSA-WI` | 1098 | `0800_find_bundled_cbsa_wi.h_esrd_supp_wi_ratio.threshold` |
| constant | **0.95** | `0800-FIND-BUNDLED-CBSA-WI` | 1098 | `0800_find_bundled_cbsa_wi.bun_cbsa_w_index_rounded.constant` |
| default | **60** | `0800-FIND-BUNDLED-CBSA-WI` | 1098 | `0800_find_bundled_cbsa_wi.pps_rtc.default` |
| default | **60** | `0850-GET-BUNDLED-CBSA-RATE` | 1129 | `0850_get_bundled_cbsa_rate.pps_rtc.default` |

**Total: 2224 hardcoded values** (671 thresholds, 1059 defaults).

These values are embedded directly in COBOL source. They are not external configuration. Before migration, review each one: some should be externalized to config files, others may be business constants that should remain in code with documentation.

## 8. Bypass & Emergency Paths

*GO TO statements, early exits, and exception handling flows that deviate from the main execution path.*

### `ESDRV212`

| From | To | Pattern | Line | Trigger Condition |
|------|----|---------|------|-------------------|
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 397 | Unconditional |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 402 | (B-THRU-DATE < 20050401) OR (B-THRU-DATE NOT NUMER |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 420 | P-ESRD-RATE NOT NUMERIC |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 426 | (B-THRU-DATE < 20110101) AND (P-ESRD-RATE > ZERO) |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 510 | (B-THRU-DATE > 20050331 AND B-THRU-DATE < 20060101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 520 | PPS-RTC > 00 THEN |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 536 | (B-THRU-DATE > 20201231 AND B-THRU-DATE < 20220101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 552 | (B-THRU-DATE > 20200630 AND B-THRU-DATE < 20210101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 568 | (B-THRU-DATE > 20191231 AND B-THRU-DATE < 20200701 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 583 | (B-THRU-DATE > 20181231 AND B-THRU-DATE < 20200101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 598 | (B-THRU-DATE > 20171231 AND B-THRU-DATE < 20190101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 613 | (B-THRU-DATE > 20170630 AND B-THRU-DATE < 20180101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 628 | (B-THRU-DATE > 20161231 AND B-THRU-DATE < 20170701 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 643 | (B-THRU-DATE > 20151231 AND B-THRU-DATE < 20170101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 658 | (B-THRU-DATE > 20141231 AND B-THRU-DATE < 20160101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 673 | (B-THRU-DATE > 20131231 AND B-THRU-DATE < 20150101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 689 | (B-THRU-DATE > 20121231 AND B-THRU-DATE < 20140101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 705 | (B-THRU-DATE > 20111231 AND B-THRU-DATE < 20130101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 721 | (B-THRU-DATE > 20101231 AND B-THRU-DATE < 20120101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 738 | (B-THRU-DATE > 20091231 AND B-THRU-DATE < 20110101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 753 | (B-THRU-DATE > 20081231 AND B-THRU-DATE < 20100101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 768 | (B-THRU-DATE > 20071231 AND B-THRU-DATE < 20090101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 783 | (B-THRU-DATE > 20070331 AND B-THRU-DATE < 20080101 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 798 | (B-THRU-DATE > 20061231 AND B-THRU-DATE < 20070401 |
| `0100-ENTER-DRIVER` | `0100-EXIT-DRIVER` | Unknown Flow | 813 | (B-THRU-DATE > 20051231 AND B-THRU-DATE < 20070101 |
| `0500-FIND-MSA-WAGE-ADJ-RATE` | `0500-FIND-EXIT` | Early Exit | 964 | Unconditional |
| `0550-N-GET-WAGE-RATE` | `0550-N-GET-WAGE-RATE` | Unknown Flow | 978 | Unconditional |
| `0700-FIND-COMPOSITE-CBSA-WI` | `0700-FIND-EXIT` | Early Exit | 996 | Unconditional |
| `0700-FIND-COMPOSITE-CBSA-WI` | `0700-FIND-EXIT` | Early Exit | 1007 | P-SPEC-PYMT-IND = '1' THEN |
| `0700-FIND-COMPOSITE-CBSA-WI` | `0700-FIND-EXIT` | Early Exit | 1007 | P-SPEC-PYMT-IND = '1' THEN |
| `0750-GET-COMP-CBSA-RATE` | `0750-GET-COMP-CBSA-RATE` | Unknown Flow | 1027 | Unconditional |
| `0800-FIND-BUNDLED-CBSA-WI` | `0800-FIND-EXIT` | Early Exit | 1046 | Unconditional |
| `0800-FIND-BUNDLED-CBSA-WI` | `0800-FIND-EXIT` | Early Exit | 1051 | P-SPEC-PYMT-IND = '1' THEN |
| `0800-FIND-BUNDLED-CBSA-WI` | `0800-FIND-EXIT` | Early Exit | 1078 | CHILD-HOSP-SWI-FOUND |
| `0800-FIND-BUNDLED-CBSA-WI` | `0800-FIND-EXIT` | Early Exit | 1078 | CHILD-HOSP-SWI-FOUND |
| `0800-FIND-BUNDLED-CBSA-WI` | `0800-FIND-EXIT` | Early Exit | 1098 | MAINFRAME-PC-SWITCH = DS-ERROR-CODE THEN |
| `0800-FIND-BUNDLED-CBSA-WI` | `0800-FIND-EXIT` | Early Exit | 1098 | MAINFRAME-PC-SWITCH = DS-ERROR-CODE THEN |
| `0850-GET-BUNDLED-CBSA-RATE` | `0850-GET-BUNDLED-CBSA-RATE` | Unknown Flow | 1129 | Unconditional |

**Critical paragraphs** (3+ exception paths): 0700-FIND-COMPOSITE-CBSA-WI, 0800-FIND-BUNDLED-CBSA-WI, 0100-ENTER-DRIVER

**Total: 38 GO TO statements** (10 early exits).

GO TO is not inherently bad, but each one is a departure from structured flow. Early exits (GO TO ...-EXIT) are usually validation guards - low risk. Cross-paragraph GO TOs require manual review before migration.

## 9. Reachability Map

*Which paragraphs are reachable from the entry point? Which are dead code?*

### `ESCAL056`

**1/8 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-MAINLINE-CONTROL, 0100-INITIAL-ROUTINE, 1000-EDIT-THE-BILL-INFO, 1200-CALC-AGE, 2000-ASSEMBLE-PPS-VARIABLES, 3000-CALC-PAYMENT, 9000-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 35 outputs

### `ESCAL062`

**1/8 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-MAINLINE-CONTROL, 0100-INITIAL-ROUTINE, 1000-EDIT-THE-BILL-INFO, 1200-CALC-AGE, 2000-ASSEMBLE-PPS-VARIABLES, 3000-CALC-PAYMENT, 9000-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 37 outputs

### `ESCAL070`

**1/8 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-MAINLINE-CONTROL, 0100-INITIAL-ROUTINE, 1000-EDIT-THE-BILL-INFO, 1200-CALC-AGE, 2000-ASSEMBLE-PPS-VARIABLES, 3000-CALC-PAYMENT, 9000-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 37 outputs

### `ESCAL071`

**1/8 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-MAINLINE-CONTROL, 0100-INITIAL-ROUTINE, 1000-EDIT-THE-BILL-INFO, 1200-CALC-AGE, 2000-ASSEMBLE-PPS-VARIABLES, 3000-CALC-PAYMENT, 9000-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 37 outputs

### `ESCAL080`

**1/8 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-MAINLINE-CONTROL, 0100-INITIAL-ROUTINE, 1000-EDIT-THE-BILL-INFO, 1200-CALC-AGE, 2000-ASSEMBLE-PPS-VARIABLES, 3000-CALC-PAYMENT, 9000-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 37 outputs

### `ESCAL091`

**1/8 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-MAINLINE-CONTROL, 0100-INITIAL-ROUTINE, 1000-EDIT-THE-BILL-INFO, 1200-CALC-AGE, 2000-ASSEMBLE-PPS-VARIABLES, 3000-CALC-PAYMENT, 9000-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 37 outputs

### `ESCAL100`

**1/8 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-MAINLINE-CONTROL, 0100-INITIAL-ROUTINE, 1000-EDIT-THE-BILL-INFO, 1200-CALC-AGE, 2000-ASSEMBLE-PPS-VARIABLES, 3000-CALC-PAYMENT, 9000-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 37 outputs

### `ESCAL117`

**1/11 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 5000-CALC-COMP-RATE-FACTORS, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 116 outputs

### `ESCAL122`

**1/13 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 5000-CALC-COMP-RATE-FACTORS, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 119 outputs

### `ESCAL130`

**1/13 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 5000-CALC-COMP-RATE-FACTORS, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 119 outputs

### `ESCAL140`

**1/13 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 5000-CALC-COMP-RATE-FACTORS, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 120 outputs

### `ESCAL151`

**1/13 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 5000-CALC-COMP-RATE-FACTORS, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 120 outputs

### `ESCAL160`

**1/13 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 5000-CALC-COMP-RATE-FACTORS, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 122 outputs

### `ESCAL170`

**1/12 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 114 outputs

### `ESCAL171`

**1/12 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 114 outputs

### `ESCAL180`

**1/12 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 115 outputs

### `ESCAL191`

**1/12 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 115 outputs

### `ESCAL200`

**1/12 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 115 outputs

### `ESCAL202`

**1/12 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 116 outputs

### `ESCAL212`

**1/12 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0000-START-TO-FINISH, 1000-VALIDATE-BILL-ELEMENTS, 1200-INITIALIZATION, 2000-CALCULATE-BUNDLED-FACTORS, 2100-CALC-COMORBID-ADJUST, 2500-CALC-OUTLIER-FACTORS, 2600-CALC-COMORBID-OUT-ADJUST, 3000-LOW-VOL-FULL-PPS-PAYMENT, 3100-LOW-VOL-OUT-PPS-PAYMENT, 9000-SET-RETURN-CODE, 9100-MOVE-RESULTS

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 119 outputs

### `ESDRV212`

**1/16 paragraphs reachable** from `0000-PROCEDURE-START`

**Unreachable paragraphs:** 0100-ENTER-DRIVER, 0100-EXIT-DRIVER, 0500-FIND-MSA-WAGE-ADJ-RATE, 0500-FIND-EXIT, 0550-N-GET-WAGE-RATE, 0550-N-EXIT, 0700-FIND-COMPOSITE-CBSA-WI, 0700-FIND-EXIT, 0750-GET-COMP-CBSA-RATE, 0750-COMP-EXIT, 0800-FIND-BUNDLED-CBSA-WI, 0800-FIND-EXIT, 0820-SEARCH-CHILD-HOSP-TABLE, 0850-GET-BUNDLED-CBSA-RATE, 0850-BUNDLED-EXIT

These may be dead code, or they may be called via PERFORM THRU ranges or dynamic calls not visible to static analysis.

**Dataflow:** 0 inputs, 19 outputs

## 10. Modernization Notes

### TSB Risk Metric Summary (Technical & Structural Breakdown Risk)

| Category | Programs |
|----------|----------|
| Critical | 0 |
| High | 1 |
| Medium | 13 |
| Low | 7 |

### Migration Recommendations

- **1 high-risk programs** - prioritize manual review before automated migration
- **38 GO TO statements** - refactor to structured flow where possible
- **2224 hardcoded values** - externalize to configuration files
- **699 return-code assignments** - map to modern error handling
- **13 state values** - convert to enums or state pattern

### Target Architecture

Based on the analysis above, the recommended modernization approach:

1. **Strangler Fig Pattern** - wrap COBOL in API layer, replace modules incrementally
2. **Test harness** - build regression tests from return-code catalog (Section 6)
3. **State machine migration** - convert 88-level switches to enums (Section 5)
4. **Data pipeline validation** - verify LINKAGE->WS->output flow (Section 4)
5. **Dead code removal** - eliminate unreachable paragraphs (Section 9)

---

*Generated by CobolIQ v0.4.0 - Code Mechanics Map*
*Analysis timestamp: 2026-08-06 18:43:02*
