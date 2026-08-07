```mermaid
graph LR
classDef date      fill:#f0a500,stroke:#c07800,color:#000
classDef validation fill:#e74c3c,stroke:#b03a2e,color:#fff
classDef rule      fill:#4a90d9,stroke:#2c6aa0,color:#fff
classDef calc      fill:#27ae60,stroke:#1e8449,color:#fff
classDef rc        fill:#8e44ad,stroke:#6c3483,color:#fff
classDef dispatch  fill:#e67e22,stroke:#d35400,color:#fff

    n0["ESCAL056: Processor"]
    n1["0000-MAINLINE-CONTROL: PPS-RTC = 00"]
    n0 --> n1
    n2["0100-INITIAL-ROUTINE: P-PROV-TYPE = '40'"]
    n0 --> n2
    n3["RC:PPS-RTC/52"]
    n2 --> n3
    n4["1000-EDIT-THE-BILL-INFO: PPS-RTC = 00"]
    n0 --> n4
    n5["RC:PPS-RTC/53,54,55,56,57,58,71,72"]
    n4 --> n5
    n6["1200-CALC-AGE: B-DOB-MM > B-THRU-MM"]
    n0 --> n6
    n7["2000-ASSEMBLE-PPS-VARIABLES: H-PATIENT-AGE > 17"]
    n0 --> n7
    n8["3000-CALC-PAYMENT: (B-COND-CODE = '73') AND (B-REV-CODE = '"]
    n0 --> n8
    n9["9000-MOVE-RESULTS: PPS-RTC < 50  THEN"]
    n0 --> n9
    n10["ESCAL062: Processor"]
    n11["0000-MAINLINE-CONTROL: PPS-RTC = 00"]
    n10 --> n11
    n12["0100-INITIAL-ROUTINE: P-PROV-TYPE = '40' OR '05'"]
    n10 --> n12
    n13["RC:PPS-RTC/52"]
    n12 --> n13
    n14["1000-EDIT-THE-BILL-INFO: PPS-RTC = 00"]
    n10 --> n14
    n15["RC:PPS-RTC/53,54,55,56,57,58,71,72"]
    n14 --> n15
    n16["1200-CALC-AGE: B-DOB-MM > B-THRU-MM"]
    n10 --> n16
    n17["2000-ASSEMBLE-PPS-VARIABLES: H-PATIENT-AGE > 17"]
    n10 --> n17
    n18["3000-CALC-PAYMENT: (B-COND-CODE = '73') AND (B-REV-CODE = '"]
    n10 --> n18
    n19["9000-MOVE-RESULTS: PPS-RTC < 50  THEN"]
    n10 --> n19
    n20["ESCAL070: Processor"]
    n21["0000-MAINLINE-CONTROL: PPS-RTC = 00"]
    n20 --> n21
    n22["0100-INITIAL-ROUTINE: P-PROV-TYPE = '40' OR '05'"]
    n20 --> n22
    n23["RC:PPS-RTC/52"]
    n22 --> n23
    n24["1000-EDIT-THE-BILL-INFO: PPS-RTC = 00"]
    n20 --> n24
    n25["RC:PPS-RTC/53,54,55,56,57,58,71,72"]
    n24 --> n25
    n26["1200-CALC-AGE: B-DOB-MM > B-THRU-MM"]
    n20 --> n26
    n27["2000-ASSEMBLE-PPS-VARIABLES: H-PATIENT-AGE > 17"]
    n20 --> n27
    n28["3000-CALC-PAYMENT: (B-COND-CODE = '73') AND (B-REV-CODE = '"]
    n20 --> n28
    n29["9000-MOVE-RESULTS: PPS-RTC < 50  THEN"]
    n20 --> n29
    n30["ESCAL071: Processor"]
    n31["0000-MAINLINE-CONTROL: PPS-RTC = 00"]
    n30 --> n31
    n32["0100-INITIAL-ROUTINE: P-PROV-TYPE = '40' OR '05'"]
    n30 --> n32
    n33["RC:PPS-RTC/52"]
    n32 --> n33
    n34["1000-EDIT-THE-BILL-INFO: PPS-RTC = 00"]
    n30 --> n34
    n35["RC:PPS-RTC/53,54,55,56,57,58,71,72"]
    n34 --> n35
    n36["1200-CALC-AGE: B-DOB-MM > B-THRU-MM"]
    n30 --> n36
    n37["2000-ASSEMBLE-PPS-VARIABLES: H-PATIENT-AGE > 17"]
    n30 --> n37
    n38["3000-CALC-PAYMENT: (B-COND-CODE = '73') AND (B-REV-CODE = '"]
    n30 --> n38
    n39["9000-MOVE-RESULTS: PPS-RTC < 50  THEN"]
    n30 --> n39
    n40["ESCAL080: Processor"]
    n41["0000-MAINLINE-CONTROL: PPS-RTC = 00  THEN"]
    n40 --> n41
    n42["0100-INITIAL-ROUTINE: P-PROV-TYPE = '40' OR '05'  THEN"]
    n40 --> n42
    n43["RC:PPS-RTC/52"]
    n42 --> n43
    n44["1000-EDIT-THE-BILL-INFO: PPS-RTC = 00  THEN"]
    n40 --> n44
    n45["RC:PPS-RTC/53,54,55,56,57,58,71,72"]
    n44 --> n45
    n46["1200-CALC-AGE: B-DOB-MM > B-THRU-MM  THEN"]
    n40 --> n46
    n47["2000-ASSEMBLE-PPS-VARIABLES: H-PATIENT-AGE > 17  THEN"]
    n40 --> n47
    n48["3000-CALC-PAYMENT: (B-COND-CODE = '73') AND (B-REV-CODE = '"]
    n40 --> n48
    n49["9000-MOVE-RESULTS: PPS-RTC < 50  THEN"]
    n40 --> n49
    n50["ESCAL091: Processor"]
    n51["0000-MAINLINE-CONTROL: PPS-RTC = 00  THEN"]
    n50 --> n51
    n52["0100-INITIAL-ROUTINE: P-PROV-TYPE = '40' OR '05'  THEN"]
    n50 --> n52
    n53["RC:PPS-RTC/52"]
    n52 --> n53
    n54["1000-EDIT-THE-BILL-INFO: PPS-RTC = 00  THEN"]
    n50 --> n54
    n55["RC:PPS-RTC/53,54,55,56,57,58,71,72"]
    n54 --> n55
    n56["1200-CALC-AGE: B-DOB-MM > B-THRU-MM  THEN"]
    n50 --> n56
    n57["2000-ASSEMBLE-PPS-VARIABLES: H-PATIENT-AGE > 17  THEN"]
    n50 --> n57
    n58["3000-CALC-PAYMENT: (B-COND-CODE = '73') AND (B-REV-CODE = '"]
    n50 --> n58
    n59["9000-MOVE-RESULTS: PPS-RTC < 50  THEN"]
    n50 --> n59
    n60["ESCAL100: Processor"]
    n61["0000-MAINLINE-CONTROL: PPS-RTC = 00  THEN"]
    n60 --> n61
    n62["0100-INITIAL-ROUTINE: P-PROV-TYPE = '40' OR '05'  THEN"]
    n60 --> n62
    n63["RC:PPS-RTC/52"]
    n62 --> n63
    n64["1000-EDIT-THE-BILL-INFO: PPS-RTC = 00  THEN"]
    n60 --> n64
    n65["RC:PPS-RTC/53,54,55,56,57,58,71,72"]
    n64 --> n65
    n66["1200-CALC-AGE: B-DOB-MM > B-THRU-MM  THEN"]
    n60 --> n66
    n67["2000-ASSEMBLE-PPS-VARIABLES: H-PATIENT-AGE > 17  THEN"]
    n60 --> n67
    n68["3000-CALC-PAYMENT: (B-COND-CODE = '73') AND (B-REV-CODE = '"]
    n60 --> n68
    n69["9000-MOVE-RESULTS: PPS-RTC < 50  THEN"]
    n60 --> n69
    n70["ESCAL117: Decision Engine"]
    n71["0000-START-TO-FINISH: BUNDLED-TEST  THEN"]
    n70 --> n71
    n72["1000-VALIDATE-BILL-ELEMENTS: P-PROV-TYPE = '40'  OR  '41' OR '05'  TH"]
    n70 --> n72
    n73["RC:PPS-RTC/52,53,54,55,56,57,58,71,72,73,74,75,76,81"]
    n72 --> n73
    n74["1200-INITIALIZATION: COMORBID-CWF-RETURN-CODE = SPACES  THEN "]
    n70 --> n74
    n75["2000-CALCULATE-BUNDLED-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n70 --> n75
    n76["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n70 --> n76
    n77["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n70 --> n77
    n78["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n70 --> n78
    n79["5000-CALC-COMP-RATE-FACTORS: H-PATIENT-AGE < 18  THEN"]
    n70 --> n79
    n80["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n70 --> n80
    n81["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n80 --> n81
    n82["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n70 --> n82
    n83["ESCAL122: Decision Engine"]
    n84["0000-START-TO-FINISH: BUNDLED-TEST  THEN"]
    n83 --> n84
    n85["1000-VALIDATE-BILL-ELEMENTS: P-PROV-TYPE = '40'  OR  '41' OR '05'  TH"]
    n83 --> n85
    n86["RC:PPS-RTC/52,53,54,55,56,57,58,53,71,72,73,74,75,76,81"]
    n85 --> n86
    n87["1200-INITIALIZATION: P-QIP-REDUCTION = ' '  THEN"]
    n83 --> n87
    n88["2000-CALCULATE-BUNDLED-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n83 --> n88
    n89["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n83 --> n89
    n90["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n83 --> n90
    n91["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n83 --> n91
    n92["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73'  THEN"]
    n83 --> n92
    n93["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n83 --> n93
    n94["5000-CALC-COMP-RATE-FACTORS: H-PATIENT-AGE < 18  THEN"]
    n83 --> n94
    n95["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n83 --> n95
    n96["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n95 --> n96
    n97["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n83 --> n97
    n98["ESCAL130: Decision Engine"]
    n99["0000-START-TO-FINISH: BUNDLED-TEST  THEN"]
    n98 --> n99
    n100["1000-VALIDATE-BILL-ELEMENTS: P-PROV-TYPE = '40'  OR  '41' OR '05'  TH"]
    n98 --> n100
    n101["RC:PPS-RTC/52,53,54,55,56,57,58,53,71,72,73,74,75,76,81"]
    n100 --> n101
    n102["1200-INITIALIZATION: P-QIP-REDUCTION = ' '  THEN"]
    n98 --> n102
    n103["2000-CALCULATE-BUNDLED-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n98 --> n103
    n104["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n98 --> n104
    n105["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n98 --> n105
    n106["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n98 --> n106
    n107["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73'  THEN"]
    n98 --> n107
    n108["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n98 --> n108
    n109["5000-CALC-COMP-RATE-FACTORS: H-PATIENT-AGE < 18  THEN"]
    n98 --> n109
    n110["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n98 --> n110
    n111["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n110 --> n111
    n112["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n98 --> n112
    n113["ESCAL140: Decision Engine"]
    n114["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n113 --> n114
    n115["1000-VALIDATE-BILL-ELEMENTS: P-PROV-TYPE = '40'  OR  '41' OR '05'  TH"]
    n113 --> n115
    n116["RC:PPS-RTC/52,53,54,55,56,57,58,53,71,72,73,74,75,76,81"]
    n115 --> n116
    n117["1200-INITIALIZATION: P-QIP-REDUCTION = ' '  THEN"]
    n113 --> n117
    n118["2000-CALCULATE-BUNDLED-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n113 --> n118
    n119["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n113 --> n119
    n120["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n113 --> n120
    n121["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n113 --> n121
    n122["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73'  THEN"]
    n113 --> n122
    n123["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n113 --> n123
    n124["5000-CALC-COMP-RATE-FACTORS: H-PATIENT-AGE < 18  THEN"]
    n113 --> n124
    n125["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n113 --> n125
    n126["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n125 --> n126
    n127["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n113 --> n127
    n128["ESCAL151: Decision Engine"]
    n129["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n128 --> n129
    n130["1000-VALIDATE-BILL-ELEMENTS: P-PROV-TYPE = '40'  OR  '41' OR '05'  TH"]
    n128 --> n130
    n131["RC:PPS-RTC/52,53,54,55,56,57,58,53,71,72,73,74,75,76,81"]
    n130 --> n131
    n132["1200-INITIALIZATION: P-QIP-REDUCTION = ' '  THEN"]
    n128 --> n132
    n133["2000-CALCULATE-BUNDLED-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n128 --> n133
    n134["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n128 --> n134
    n135["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n128 --> n135
    n136["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n128 --> n136
    n137["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73'  THEN"]
    n128 --> n137
    n138["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n128 --> n138
    n139["5000-CALC-COMP-RATE-FACTORS: H-PATIENT-AGE < 18  THEN"]
    n128 --> n139
    n140["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n128 --> n140
    n141["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n140 --> n141
    n142["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n128 --> n142
    n143["ESCAL160: Decision Engine"]
    n144["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n143 --> n144
    n145["1000-VALIDATE-BILL-ELEMENTS: P-PROV-TYPE = '40'  OR  '41' OR '05'  TH"]
    n143 --> n145
    n146["RC:PPS-RTC/52,53,54,55,56,57,58,53,71,72,73,74,75,76,81"]
    n145 --> n146
    n147["1200-INITIALIZATION: P-QIP-REDUCTION = ' '  THEN"]
    n143 --> n147
    n148["2000-CALCULATE-BUNDLED-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n143 --> n148
    n149["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n143 --> n149
    n150["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n143 --> n150
    n151["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n143 --> n151
    n152["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73'  THEN"]
    n143 --> n152
    n153["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n143 --> n153
    n154["5000-CALC-COMP-RATE-FACTORS: H-PATIENT-AGE < 18  THEN"]
    n143 --> n154
    n155["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n143 --> n155
    n156["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n155 --> n156
    n157["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n143 --> n157
    n158["ESCAL170: Decision Engine"]
    n159["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n158 --> n159
    n160["1000-VALIDATE-BILL-ELEMENTS: P-PROV-TYPE = '40'  OR  '41' OR '05'  TH"]
    n158 --> n160
    n161["RC:PPS-RTC/52,53,54,55,56,57,58,53,71,72,73,74,75,76,81"]
    n160 --> n161
    n162["2000-CALCULATE-BUNDLED-FACTORS: B-DOB-MM > B-THRU-MM  THEN"]
    n158 --> n162
    n163["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n158 --> n163
    n164["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n158 --> n164
    n165["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n158 --> n165
    n166["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73'  THEN"]
    n158 --> n166
    n167["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n158 --> n167
    n168["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n158 --> n168
    n169["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n168 --> n169
    n170["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n158 --> n170
    n171["ESCAL171: Decision Engine"]
    n172["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n171 --> n172
    n173["1000-VALIDATE-BILL-ELEMENTS: PPS-RTC = 00  THEN"]
    n171 --> n173
    n174["RC:PPS-RTC/58,52,53,54,55,56,57,53,71,72,73,74,75,76,81"]
    n173 --> n174
    n175["2000-CALCULATE-BUNDLED-FACTORS: B-DOB-MM > B-THRU-MM  THEN"]
    n171 --> n175
    n176["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n171 --> n176
    n177["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n171 --> n177
    n178["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n171 --> n178
    n179["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73' OR '87' THEN"]
    n171 --> n179
    n180["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n171 --> n180
    n181["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n171 --> n181
    n182["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n181 --> n182
    n183["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n171 --> n183
    n184["ESCAL180: Decision Engine"]
    n185["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n184 --> n185
    n186["1000-VALIDATE-BILL-ELEMENTS: PPS-RTC = 00  THEN"]
    n184 --> n186
    n187["RC:PPS-RTC/58,52,53,54,55,56,57,53,71,72,73,74,75,76,81"]
    n186 --> n187
    n188["2000-CALCULATE-BUNDLED-FACTORS: B-DOB-MM > B-THRU-MM  THEN"]
    n184 --> n188
    n189["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n184 --> n189
    n190["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n184 --> n190
    n191["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n184 --> n191
    n192["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73' OR '87' THEN"]
    n184 --> n192
    n193["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n184 --> n193
    n194["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n184 --> n194
    n195["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n194 --> n195
    n196["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n184 --> n196
    n197["ESCAL191: Decision Engine"]
    n198["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n197 --> n198
    n199["1000-VALIDATE-BILL-ELEMENTS: PPS-RTC = 00  THEN"]
    n197 --> n199
    n200["RC:PPS-RTC/58,52,53,54,55,56,57,53,71,72,73,74,75,76,81"]
    n199 --> n200
    n201["2000-CALCULATE-BUNDLED-FACTORS: B-DOB-MM > B-THRU-MM  THEN"]
    n197 --> n201
    n202["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n197 --> n202
    n203["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n197 --> n203
    n204["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n197 --> n204
    n205["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73' OR '87' THEN"]
    n197 --> n205
    n206["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n197 --> n206
    n207["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n197 --> n207
    n208["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n207 --> n208
    n209["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n197 --> n209
    n210["ESCAL200: Decision Engine"]
    n211["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n210 --> n211
    n212["1000-VALIDATE-BILL-ELEMENTS: PPS-RTC = 00  THEN"]
    n210 --> n212
    n213["RC:PPS-RTC/58,52,53,54,55,56,57,53,71,72,73,74,75,76,81"]
    n212 --> n213
    n214["2000-CALCULATE-BUNDLED-FACTORS: B-DOB-MM > B-THRU-MM  THEN"]
    n210 --> n214
    n215["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n210 --> n215
    n216["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n210 --> n216
    n217["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n210 --> n217
    n218["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73' OR '87' THEN"]
    n210 --> n218
    n219["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n210 --> n219
    n220["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n210 --> n220
    n221["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n220 --> n221
    n222["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n210 --> n222
    n223["ESCAL202: Decision Engine"]
    n224["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n223 --> n224
    n225["1000-VALIDATE-BILL-ELEMENTS: PPS-RTC = 00  THEN"]
    n223 --> n225
    n226["RC:PPS-RTC/58,52,53,54,55,56,57,53,71,72,73,74,75,76,81"]
    n225 --> n226
    n227["2000-CALCULATE-BUNDLED-FACTORS: B-DOB-MM > B-THRU-MM  THEN"]
    n223 --> n227
    n228["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n223 --> n228
    n229["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n223 --> n229
    n230["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n223 --> n230
    n231["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73' OR '87' THEN"]
    n223 --> n231
    n232["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n223 --> n232
    n233["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n223 --> n233
    n234["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n233 --> n234
    n235["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n223 --> n235
    n236["ESCAL212: Decision Engine"]
    n237["0000-START-TO-FINISH: BUNDLED-TEST THEN"]
    n236 --> n237
    n238["1000-VALIDATE-BILL-ELEMENTS: PPS-RTC = 00  THEN"]
    n236 --> n238
    n239["RC:PPS-RTC/58,52,53,54,55,56,57,53,71,72,73,74,75,76,81"]
    n238 --> n239
    n240["2000-CALCULATE-BUNDLED-FACTORS: B-DOB-MM > B-THRU-MM  THEN"]
    n236 --> n240
    n241["2100-CALC-COMORBID-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n236 --> n241
    n242["2500-CALC-OUTLIER-FACTORS: H-PATIENT-AGE < 13  THEN"]
    n236 --> n242
    n243["2600-CALC-COMORBID-OUT-ADJUST: COMORBID-DATA (SUB) = 'MA'  THEN"]
    n236 --> n243
    n244["3000-LOW-VOL-FULL-PPS-PAYMENT: B-COND-CODE = '73' OR '87' THEN"]
    n236 --> n244
    n245["3100-LOW-VOL-OUT-PPS-PAYMENT: H-PATIENT-AGE < 18  THEN"]
    n236 --> n245
    n246["9000-SET-RETURN-CODE: PEDIATRIC-TRACK                       = "]
    n236 --> n246
    n247["RC:PPS-RTC/17,16,15,14,24,19,29,23,18,30,28,34,35,33,07,06,09,03,26,21,12,25,20,32,10,27,22,11,08,04,05,31,02"]
    n246 --> n247
    n248["9100-MOVE-RESULTS: MOVED-CORMORBIDS = SPACES  THEN NEXT SEN"]
    n236 --> n248
    n249["ESDRV212: Decision Engine"]
    n250["0100-ENTER-DRIVER: (B-THRU-DATE < 20050401) OR (B-THRU-DATE"]
    n249 --> n250
    n251["RC:PPS-RTC./00,98,50,01,01,98"]
    n250 --> n251
    n252["0550-N-GET-WAGE-RATE: WWW-DTCD (W-SUB1) NOT > WWD-DTCD (WWD-SU"]
    n249 --> n252
    n253["0700-FIND-COMPOSITE-CBSA-WI: P-SPEC-PYMT-IND = '1'  THEN"]
    n249 --> n253
    n254["RC:PPS-RTC/60,61"]
    n253 --> n254
    n255["0750-GET-COMP-CBSA-RATE: COM-WI-DATE-CODE (W-SUB2) NOT > COM-DATE"]
    n249 --> n255
    n256["0800-FIND-BUNDLED-CBSA-WI: P-SPEC-PYMT-IND = '1'  THEN"]
    n249 --> n256
    n257["RC:PPS-RTC/60,61,60"]
    n256 --> n257
    n258["0820-SEARCH-CHILD-HOSP-TABLE: CHILD-HOSP-PROV (CHILD-HOSP-TABLE-SUB) ="]
    n249 --> n258
    n259["0850-GET-BUNDLED-CBSA-RATE: (BUN-WI-DATE-CODE (W-SUB3) = B-THRU-YEAR"]
    n249 --> n259
    n260["RC:PPS-RTC/60"]
    n259 --> n260
    n261["ESCAL056"]
    n249 -->|CALL| n261
    n262["ESCAL062"]
    n249 -->|CALL| n262
    n263["ESCAL070"]
    n249 -->|CALL| n263
    n264["ESCAL071"]
    n249 -->|CALL| n264
    n265["ESCAL080"]
    n249 -->|CALL| n265
    n266["ESCAL091"]
    n249 -->|CALL| n266
    n267["ESCAL100"]
    n249 -->|CALL| n267
    n268["ESCAL117"]
    n249 -->|CALL| n268
    n269["ESCAL122"]
    n249 -->|CALL| n269
    n270["ESCAL130"]
    n249 -->|CALL| n270
    n271["ESCAL140"]
    n249 -->|CALL| n271
    n272["ESCAL151"]
    n249 -->|CALL| n272
    n273["ESCAL160"]
    n249 -->|CALL| n273
    n274["ESCAL170"]
    n249 -->|CALL| n274
    n275["ESCAL171"]
    n249 -->|CALL| n275
    n276["ESCAL180"]
    n249 -->|CALL| n276
    n277["ESCAL191"]
    n249 -->|CALL| n277
    n278["ESCAL200"]
    n249 -->|CALL| n278
    n279["ESCAL202"]
    n249 -->|CALL| n279
    n280["ESCAL212"]
    n249 -->|CALL| n280
    class n0 dispatch
    class n1 rule
    class n2 rule
    class n3 rc
    class n4 validation
    class n5 rc
    class n6 calc
    class n7 rule
    class n8 calc
    class n9 rule
    class n10 dispatch
    class n11 rule
    class n12 rule
    class n13 rc
    class n14 validation
    class n15 rc
    class n16 calc
    class n17 rule
    class n18 calc
    class n19 rule
    class n20 dispatch
    class n21 rule
    class n22 rule
    class n23 rc
    class n24 validation
    class n25 rc
    class n26 calc
    class n27 rule
    class n28 calc
    class n29 rule
    class n30 dispatch
    class n31 rule
    class n32 rule
    class n33 rc
    class n34 validation
    class n35 rc
    class n36 calc
    class n37 rule
    class n38 calc
    class n39 rule
    class n40 dispatch
    class n41 rule
    class n42 rule
    class n43 rc
    class n44 validation
    class n45 rc
    class n46 calc
    class n47 rule
    class n48 calc
    class n49 rule
    class n50 dispatch
    class n51 rule
    class n52 rule
    class n53 rc
    class n54 validation
    class n55 rc
    class n56 calc
    class n57 rule
    class n58 calc
    class n59 rule
    class n60 dispatch
    class n61 rule
    class n62 rule
    class n63 rc
    class n64 validation
    class n65 rc
    class n66 calc
    class n67 rule
    class n68 calc
    class n69 rule
    class n70 dispatch
    class n71 rule
    class n72 validation
    class n73 rc
    class n74 rule
    class n75 calc
    class n76 calc
    class n77 calc
    class n78 calc
    class n79 calc
    class n80 rule
    class n81 rc
    class n82 rule
    class n83 dispatch
    class n84 rule
    class n85 validation
    class n86 rc
    class n87 rule
    class n88 calc
    class n89 calc
    class n90 calc
    class n91 calc
    class n92 rule
    class n93 rule
    class n94 calc
    class n95 rule
    class n96 rc
    class n97 rule
    class n98 dispatch
    class n99 rule
    class n100 validation
    class n101 rc
    class n102 rule
    class n103 calc
    class n104 calc
    class n105 calc
    class n106 calc
    class n107 rule
    class n108 rule
    class n109 calc
    class n110 rule
    class n111 rc
    class n112 rule
    class n113 dispatch
    class n114 rule
    class n115 validation
    class n116 rc
    class n117 rule
    class n118 calc
    class n119 calc
    class n120 calc
    class n121 calc
    class n122 rule
    class n123 rule
    class n124 calc
    class n125 rule
    class n126 rc
    class n127 rule
    class n128 dispatch
    class n129 rule
    class n130 validation
    class n131 rc
    class n132 rule
    class n133 calc
    class n134 calc
    class n135 calc
    class n136 calc
    class n137 rule
    class n138 rule
    class n139 calc
    class n140 rule
    class n141 rc
    class n142 rule
    class n143 dispatch
    class n144 rule
    class n145 validation
    class n146 rc
    class n147 rule
    class n148 calc
    class n149 calc
    class n150 calc
    class n151 calc
    class n152 rule
    class n153 rule
    class n154 calc
    class n155 rule
    class n156 rc
    class n157 rule
    class n158 dispatch
    class n159 rule
    class n160 validation
    class n161 rc
    class n162 calc
    class n163 calc
    class n164 calc
    class n165 calc
    class n166 rule
    class n167 rule
    class n168 rule
    class n169 rc
    class n170 rule
    class n171 dispatch
    class n172 rule
    class n173 validation
    class n174 rc
    class n175 calc
    class n176 calc
    class n177 calc
    class n178 calc
    class n179 rule
    class n180 rule
    class n181 rule
    class n182 rc
    class n183 rule
    class n184 dispatch
    class n185 rule
    class n186 validation
    class n187 rc
    class n188 calc
    class n189 calc
    class n190 calc
    class n191 calc
    class n192 rule
    class n193 rule
    class n194 rule
    class n195 rc
    class n196 rule
    class n197 dispatch
    class n198 rule
    class n199 validation
    class n200 rc
    class n201 calc
    class n202 calc
    class n203 calc
    class n204 calc
    class n205 rule
    class n206 rule
    class n207 rule
    class n208 rc
    class n209 rule
    class n210 dispatch
    class n211 rule
    class n212 validation
    class n213 rc
    class n214 calc
    class n215 calc
    class n216 calc
    class n217 calc
    class n218 rule
    class n219 rule
    class n220 rule
    class n221 rc
    class n222 rule
    class n223 dispatch
    class n224 rule
    class n225 validation
    class n226 rc
    class n227 calc
    class n228 calc
    class n229 calc
    class n230 calc
    class n231 rule
    class n232 rule
    class n233 rule
    class n234 rc
    class n235 rule
    class n236 dispatch
    class n237 rule
    class n238 validation
    class n239 rc
    class n240 calc
    class n241 calc
    class n242 calc
    class n243 calc
    class n244 rule
    class n245 rule
    class n246 rule
    class n247 rc
    class n248 rule
    class n249 dispatch
    class n250 rule
    class n251 rc
    class n252 rule
    class n253 calc
    class n254 rc
    class n255 calc
    class n256 rule
    class n257 rc
    class n258 rule
    class n259 rule
    class n260 rc
    class n261 dispatch
    class n262 dispatch
    class n263 dispatch
    class n264 dispatch
    class n265 dispatch
    class n266 dispatch
    class n267 dispatch
    class n268 dispatch
    class n269 dispatch
    class n270 dispatch
    class n271 dispatch
    class n272 dispatch
    class n273 dispatch
    class n274 dispatch
    class n275 dispatch
    class n276 dispatch
    class n277 dispatch
    class n278 dispatch
    class n279 dispatch
    class n280 dispatch
