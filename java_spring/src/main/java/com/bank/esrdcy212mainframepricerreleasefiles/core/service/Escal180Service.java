package com.bank.esrdcy212mainframepricerreleasefiles.core.service;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import com.bank.esrdcy212mainframepricerreleasefiles.dto.*;
import com.bank.esrdcy212mainframepricerreleasefiles.enums.*;
import com.bank.esrdcy212mainframepricerreleasefiles.entity.*;

/**
 * ESCAL180 - COBOL program `ESCAL180` orchestrates a 1-step business flow. It emits 47 distinct return-code value(s) across 48 assignment site(s), driven by 1 state-machine flag group(s). Depends on 3 external copybook(s): RTCCPY, BILLCPY, WAGECPY.
 *
 * Risk: 43/100 (MEDIUM)
 * Modernization: manual rewrite required
 * Source: ESCAL180
 */
@Service
@Slf4j
@RequiredArgsConstructor
public class Escal180Service {

    /**
     * LEAF - L635-659
     * Branches: 0, GOTO: 0, CALLs: 0
     */
    private void _0000ProcedureStart() {

    }

    /**
     * PROCESS - L660-696
     * Branches: 3, GOTO: 0, CALLs: 5
     */
    private void _0000StartToFinish() {

    }

    /**
     * VALIDATION - L697-828
     * Branches: 35, GOTO: 0, CALLs: 0
     */
    private ReturnCodeResponse _1000ValidateBillElements() {
        // IF (B-COND-CODE NOT = '73' AND '74' AND '84' AND '87' AND '  '): RETURN CODE PPS-RTC = 58
        // IF (P-PROV-TYPE = '40'  OR  '41' OR '05'  THEN NEXT SENTENCE): RETURN CODE PPS-RTC = 52
        // IF (P-SPEC-PYMT-IND NOT = '1' AND ' '  THEN): RETURN CODE PPS-RTC = 53
        // IF ((B-DOB-DATE = ZERO)  OR  (B-DOB-DATE NOT NUMERIC)  THEN): RETURN CODE PPS-RTC = 54
        // IF ((B-PATIENT-WGT = 0)  OR  (B-PATIENT-WGT NOT NUMERIC)): RETURN CODE PPS-RTC = 55
        // IF ((B-PATIENT-HGT = 0)  OR  (B-PATIENT-HGT NOT NUMERIC)): RETURN CODE PPS-RTC = 56
        // IF (B-REV-CODE  = '0821' OR '0831' OR '0841' OR '0851' OR '0881' NEXT SENTENCE): RETURN CODE PPS-RTC = 57
        // IF (P-QIP-REDUCTION NOT = '1' AND '2' AND '3' AND '4' AND ' '  THEN): RETURN CODE PPS-RTC = 53
        // IF (B-PATIENT-HGT > 300.00): RETURN CODE PPS-RTC = 71
        // IF (B-PATIENT-WGT > 500.00  THEN): RETURN CODE PPS-RTC = 72
        // IF ((B-CLAIM-NUM-DIALYSIS-SESSIONS = ZERO) OR (B-CLAIM-NUM-DIALYSIS-SESSIONS NOT NUMERIC)  THEN): RETURN CODE PPS-RTC = 73
        // IF ((B-LINE-ITEM-DATE-SERVICE = ZERO) OR (B-LINE-ITEM-DATE-SERVICE NOT NUMERIC)  THEN): RETURN CODE PPS-RTC = 74
        // IF ((B-DIALYSIS-START-DATE NOT NUMERIC)  THEN): RETURN CODE PPS-RTC = 75
        // IF ((B-TOT-PRICE-SB-OUTLIER NOT NUMERIC) THEN): RETURN CODE PPS-RTC = 76
        // IF (COMORBID-CWF-RETURN-CODE = SPACES OR "10" OR "20" OR "40" OR "50" OR "60" THEN NEXT SENTENCE): RETURN CODE PPS-RTC = 81

        return new ReturnCodeResponse();
    }

    /**
     * INIT - L829-848
     * Branches: 0, GOTO: 0, CALLs: 0
     */
    private void _1200Initialization() {
        // COBOL: COMPUTE H-BUN-NAT-LABOR-AMT ROUNDED = (BUNDLED-BASE-PMT-RATE * BUN-NAT-LABOR-PCT) * BUN-CBSA-W-INDEX.
        this.hBunNatLaborAmtRounded = (bundledBasePmtRate * bunNatLaborPct) * bunCbsaWIndex;

        // COBOL: COMPUTE H-BUN-NAT-NONLABOR-AMT ROUNDED = BUNDLED-BASE-PMT-RATE * BUN-NAT-NONLABOR-PCT
        this.hBunNatNonlaborAmtRounded = bundledBasePmtRate * bunNatNonlaborPct;

        // COBOL: COMPUTE H-BUN-BASE-WAGE-AMT ROUNDED = H-BUN-NAT-LABOR-AMT + H-BUN-NAT-NONLABOR-AMT.
        this.hBunBaseWageAmtRounded = hBunNatLaborAmt + hBunNatNonlaborAmt;


    }

    /**
     * CALCULATION - L849-1231
     * Branches: 40, GOTO: 0, CALLs: 4
     */
    private void _2000CalculateBundledFactors() {
        // COBOL: COMPUTE H-PATIENT-AGE = B-THRU-CCYY - B-DOB-CCYY
        this.hPatientAge = bThruCcyy - bDobCcyy;

        // COBOL: COMPUTE H-PATIENT-AGE = H-PATIENT-AGE - 1
        this.hPatientAge = hPatientAge - 1;

        // COBOL: COMPUTE H-BUN-BSA  ROUNDED = (.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))
        this.hBunBsaRounded = (.007184 * Math.pow((bPatientHgt, .725)) * Math.pow((bPatientWgt, .425)));

        // COBOL: COMPUTE H-BUN-BSA-FACTOR  ROUNDED = CM-BSA ** ((H-BUN-BSA - BSA-NATIONAL-AVERAGE) / .1)
        this.hBunBsaFactorRounded = Math.pow(cmBsa, ((hBunBsa - bsaNationalAverage) / .1));

        // COBOL: COMPUTE H-BUN-BMI  ROUNDED = (B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.
        this.hBunBmiRounded = (bPatientWgt / Math.pow((bPatientHgt, 2))) * 10000;

        // COBOL: COMPUTE INTEGER-LINE-ITEM-DATE = FUNCTION INTEGER-OF-DATE(THE-DATE)
        this.integerLineItemDate = FUNCTION integerOfDate(theDate);

        // COBOL: COMPUTE INTEGER-DIALYSIS-DATE = FUNCTION INTEGER-OF-DATE(THE-DATE)
        this.integerDialysisDate = FUNCTION integerOfDate(theDate);

        // COBOL: COMPUTE ONSET-DATE = (INTEGER-LINE-ITEM-DATE - INTEGER-DIALYSIS-DATE) + 1
        this.onsetDate = (integerLineItemDate - integerDialysisDate) + 1;

        // COBOL: COMPUTE H-BUN-ADJUSTED-BASE-WAGE-AMT  ROUNDED = (H-BUN-BASE-WAGE-AMT * H-BUN-AGE-FACTOR) * (H-BUN-BSA-FACTOR * H-BUN-BMI-FACTOR) * (H-BUN-ONSET-FACTOR * H-BUN-COMORBID-MULTIPLIER) * H-BUN-LOW-VOL-MULTIPLIER * H-BUN-RURAL-MULTIPLIER.
        this.hBunAdjustedBaseWageAmtRounded = (hBunBaseWageAmt * hBunAgeFactor) * (hBunBsaFactor * hBunBmiFactor) * (hBunOnsetFactor * hBunComorbidMultiplier) * hBunLowVolMultiplier * hBunRuralMultiplier;

        // COBOL: COMPUTE H-BUN-WAGE-ADJ-TRAINING-AMT  ROUNDED = TRAINING-ADD-ON-PMT-AMT * BUN-CBSA-W-INDEX
        this.hBunWageAdjTrainingAmtRounded = trainingAddOnPmtAmt * bunCbsaWIndex;

        // COBOL: COMPUTE H-CC-74-PER-DIEM-AMT  ROUNDED = (H-BUN-ADJUSTED-BASE-WAGE-AMT * 3) / 7
        this.hCc74PerDiemAmtRounded = (hBunAdjustedBaseWageAmt * 3) / 7;

        // COBOL: COMPUTE H-PPS-FINAL-PAY-AMT  ROUNDED = H-CC-74-PER-DIEM-AMT
        this.hPpsFinalPayAmtRounded = hCc74PerDiemAmt;

        // COBOL: COMPUTE H-FULL-CLAIM-AMT  ROUNDED = (H-BUN-ADJUSTED-BASE-WAGE-AMT * ((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)
        this.hFullClaimAmtRounded = (hBunAdjustedBaseWageAmt * ((bClaimNumDialysisSessions) * 3) / 7);

        // COBOL: COMPUTE H-PPS-FINAL-PAY-AMT  ROUNDED = H-BUN-ADJUSTED-BASE-WAGE-AMT + H-BUN-WAGE-ADJ-TRAINING-AMT
        this.hPpsFinalPayAmtRounded = hBunAdjustedBaseWageAmt + hBunWageAdjTrainingAmt;

        // COBOL: COMPUTE H-TDAPA-PAYMENT = B-PAYER-ONLY-VC-Q8 / B-CLAIM-NUM-DIALYSIS-SESSIONS.
        this.hTdapaPayment = bPayerOnlyVcQ8 / bClaimNumDialysisSessions;

        // COBOL: COMPUTE H-PPS-FINAL-PAY-AMT = H-PPS-FINAL-PAY-AMT + H-TDAPA-PAYMENT.
        this.hPpsFinalPayAmt = hPpsFinalPayAmt + hTdapaPayment;

        // COBOL: COMPUTE H-LV-PPS-FINAL-PAY-AMT = H-LV-PPS-FINAL-PAY-AMT - H-PPS-FINAL-PAY-AMT
        this.hLvPpsFinalPayAmt = hLvPpsFinalPayAmt - hPpsFinalPayAmt;

        // COBOL: COMPUTE H-LV-OUT-PAYMENT = H-LV-OUT-PAYMENT - H-OUT-PAYMENT
        this.hLvOutPayment = hLvOutPayment - hOutPayment;

        // COBOL: COMPUTE H-LV-PPS-FINAL-PAY-AMT = H-LV-PPS-FINAL-PAY-AMT + H-LV-OUT-PAYMENT
        this.hLvPpsFinalPayAmt = hLvPpsFinalPayAmt + hLvOutPayment;

        // COBOL: COMPUTE PPS-LOW-VOL-AMT  ROUNDED = H-LV-PPS-FINAL-PAY-AMT * BUN-CBSA-BLEND-PCT
        this.ppsLowVolAmtRounded = hLvPpsFinalPayAmt * bunCbsaBlendPct;


    }

    /**
     * CALCULATION - L1232-1300
     * Branches: 7, GOTO: 0, CALLs: 1
     */
    private void _2100CalcComorbidAdjust() {

    }

    /**
     * CALCULATION - L1301-1529
     * Branches: 28, GOTO: 0, CALLs: 1
     */
    private void _2500CalcOutlierFactors() {
        // COBOL: COMPUTE H-OUT-BSA  ROUNDED = (.007184 * (B-PATIENT-HGT ** .725) * (B-PATIENT-WGT ** .425))
        this.hOutBsaRounded = (.007184 * Math.pow((bPatientHgt, .725)) * Math.pow((bPatientWgt, .425)));

        // COBOL: COMPUTE H-OUT-BSA-FACTOR  ROUNDED = SB-BSA ** ((H-OUT-BSA - BSA-NATIONAL-AVERAGE) / .1)
        this.hOutBsaFactorRounded = Math.pow(sbBsa, ((hOutBsa - bsaNationalAverage) / .1));

        // COBOL: COMPUTE H-OUT-BMI  ROUNDED = (B-PATIENT-WGT / (B-PATIENT-HGT ** 2)) * 10000.
        this.hOutBmiRounded = (bPatientWgt / Math.pow((bPatientHgt, 2))) * 10000;

        // COBOL: COMPUTE H-OUT-PREDICTED-SERVICES-MAP  ROUNDED = (H-OUT-AGE-FACTOR * H-OUT-BSA-FACTOR * H-OUT-BMI-FACTOR * H-OUT-ONSET-FACTOR * H-OUT-COMORBID-MULTIPLIER * H-OUT-RURAL-MULTIPLIER * H-OUT-LOW-VOL-MULTIPLIER).
        this.hOutPredictedServicesMapRounded = (hOutAgeFactor * hOutBsaFactor * hOutBmiFactor * hOutOnsetFactor * hOutComorbidMultiplier * hOutRuralMultiplier * hOutLowVolMultiplier);

        // COBOL: COMPUTE H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED = (H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)
        this.hOutCmAdjPredictMapTrtRounded = (hOutPredictedServicesMap * adjAvgMapAmtLt18);

        // COBOL: COMPUTE H-OUT-CM-ADJ-PREDICT-MAP-TRT  ROUNDED = (H-OUT-PREDICTED-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)
        this.hOutCmAdjPredictMapTrtRounded = (hOutPredictedServicesMap * adjAvgMapAmtGt17);

        // COBOL: COMPUTE H-HEMO-EQUIV-DIAL-SESSIONS  ROUNDED = ((B-CLAIM-NUM-DIALYSIS-SESSIONS * 3) / 7)
        this.hHemoEquivDialSessionsRounded = ((bClaimNumDialysisSessions * 3) / 7);

        // COBOL: COMPUTE H-OUT-IMPUTED-MAP  ROUNDED = (B-TOT-PRICE-SB-OUTLIER / H-HEMO-EQUIV-DIAL-SESSIONS)
        this.hOutImputedMapRounded = (bTotPriceSbOutlier / hHemoEquivDialSessions);

        // COBOL: COMPUTE H-OUT-IMPUTED-MAP  ROUNDED = (B-TOT-PRICE-SB-OUTLIER / B-CLAIM-NUM-DIALYSIS-SESSIONS)
        this.hOutImputedMapRounded = (bTotPriceSbOutlier / bClaimNumDialysisSessions);

        // COBOL: COMPUTE H-OUT-PREDICTED-MAP  ROUNDED = H-OUT-CM-ADJ-PREDICT-MAP-TRT + FIX-DOLLAR-LOSS-LT-18
        this.hOutPredictedMapRounded = hOutCmAdjPredictMapTrt + fixDollarLossLt18;

        // COBOL: COMPUTE H-OUT-PAYMENT  ROUNDED = (H-OUT-IMPUTED-MAP - H-OUT-PREDICTED-MAP) * LOSS-SHARING-PCT-LT-18
        this.hOutPaymentRounded = (hOutImputedMap - hOutPredictedMap) * lossSharingPctLt18;

        // COBOL: COMPUTE H-OUT-PREDICTED-MAP  ROUNDED = H-OUT-CM-ADJ-PREDICT-MAP-TRT + FIX-DOLLAR-LOSS-GT-17
        this.hOutPredictedMapRounded = hOutCmAdjPredictMapTrt + fixDollarLossGt17;

        // COBOL: COMPUTE H-OUT-PAYMENT  ROUNDED = (H-OUT-IMPUTED-MAP - H-OUT-PREDICTED-MAP) * LOSS-SHARING-PCT-GT-17
        this.hOutPaymentRounded = (hOutImputedMap - hOutPredictedMap) * lossSharingPctGt17;

        // COBOL: COMPUTE H-OUT-PAYMENT ROUNDED = H-OUT-PAYMENT * (((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)
        this.hOutPaymentRounded = hOutPayment * (((bClaimNumDialysisSessions) * 3) / 7);


    }

    /**
     * CALCULATION - L1530-1599
     * Branches: 7, GOTO: 0, CALLs: 1
     */
    private void _2600CalcComorbidOutAdjust() {

    }

    /**
     * LEAF - L1600-1651
     * Branches: 4, GOTO: 0, CALLs: 0
     */
    private void _3000LowVolFullPpsPayment() {
        // COBOL: COMPUTE H-LV-BUN-ADJUST-BASE-WAGE-AMT  ROUNDED = (H-BUN-BASE-WAGE-AMT * H-BUN-AGE-FACTOR) * (H-BUN-BSA-FACTOR * H-BUN-BMI-FACTOR) * (H-BUN-ONSET-FACTOR * H-BUN-COMORBID-MULTIPLIER) * H-BUN-RURAL-MULTIPLIER.
        this.hLvBunAdjustBaseWageAmtRounded = (hBunBaseWageAmt * hBunAgeFactor) * (hBunBsaFactor * hBunBmiFactor) * (hBunOnsetFactor * hBunComorbidMultiplier) * hBunRuralMultiplier;

        // COBOL: COMPUTE H-BUN-WAGE-ADJ-TRAINING-AMT  ROUNDED = TRAINING-ADD-ON-PMT-AMT * BUN-CBSA-W-INDEX
        this.hBunWageAdjTrainingAmtRounded = trainingAddOnPmtAmt * bunCbsaWIndex;

        // COBOL: COMPUTE H-CC-74-PER-DIEM-AMT  ROUNDED = (H-LV-BUN-ADJUST-BASE-WAGE-AMT * 3) / 7
        this.hCc74PerDiemAmtRounded = (hLvBunAdjustBaseWageAmt * 3) / 7;

        // COBOL: COMPUTE H-LV-PPS-FINAL-PAY-AMT  ROUNDED = H-CC-74-PER-DIEM-AMT
        this.hLvPpsFinalPayAmtRounded = hCc74PerDiemAmt;

        // COBOL: COMPUTE H-LV-PPS-FINAL-PAY-AMT  ROUNDED = H-LV-BUN-ADJUST-BASE-WAGE-AMT + H-BUN-WAGE-ADJ-TRAINING-AMT
        this.hLvPpsFinalPayAmtRounded = hLvBunAdjustBaseWageAmt + hBunWageAdjTrainingAmt;


    }

    /**
     * LEAF - L1652-1718
     * Branches: 5, GOTO: 0, CALLs: 0
     */
    private void _3100LowVolOutPpsPayment() {
        // COBOL: COMPUTE H-LV-OUT-PREDICT-SERVICES-MAP  ROUNDED = (H-OUT-AGE-FACTOR * H-OUT-BSA-FACTOR * H-OUT-BMI-FACTOR * H-OUT-ONSET-FACTOR * H-OUT-COMORBID-MULTIPLIER * H-OUT-RURAL-MULTIPLIER).
        this.hLvOutPredictServicesMapRounded = (hOutAgeFactor * hOutBsaFactor * hOutBmiFactor * hOutOnsetFactor * hOutComorbidMultiplier * hOutRuralMultiplier);

        // COBOL: COMPUTE H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED = (H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-LT-18)
        this.hLvOutCmAdjPredictMTrtRounded = (hLvOutPredictServicesMap * adjAvgMapAmtLt18);

        // COBOL: COMPUTE H-LV-OUT-CM-ADJ-PREDICT-M-TRT  ROUNDED = (H-LV-OUT-PREDICT-SERVICES-MAP * ADJ-AVG-MAP-AMT-GT-17)
        this.hLvOutCmAdjPredictMTrtRounded = (hLvOutPredictServicesMap * adjAvgMapAmtGt17);

        // COBOL: COMPUTE H-LV-OUT-PREDICTED-MAP  ROUNDED = H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-LT-18
        this.hLvOutPredictedMapRounded = hLvOutCmAdjPredictMTrt + fixDollarLossLt18;

        // COBOL: COMPUTE H-LV-OUT-PAYMENT  ROUNDED = (H-OUT-IMPUTED-MAP - H-LV-OUT-PREDICTED-MAP) * LOSS-SHARING-PCT-LT-18
        this.hLvOutPaymentRounded = (hOutImputedMap - hLvOutPredictedMap) * lossSharingPctLt18;

        // COBOL: COMPUTE H-LV-OUT-PREDICTED-MAP  ROUNDED = H-LV-OUT-CM-ADJ-PREDICT-M-TRT + FIX-DOLLAR-LOSS-GT-17
        this.hLvOutPredictedMapRounded = hLvOutCmAdjPredictMTrt + fixDollarLossGt17;

        // COBOL: COMPUTE H-LV-OUT-PAYMENT  ROUNDED = (H-OUT-IMPUTED-MAP - H-LV-OUT-PREDICTED-MAP) * LOSS-SHARING-PCT-GT-17
        this.hLvOutPaymentRounded = (hOutImputedMap - hLvOutPredictedMap) * lossSharingPctGt17;

        // COBOL: COMPUTE H-LV-OUT-PAYMENT ROUNDED = H-LV-OUT-PAYMENT * (((B-CLAIM-NUM-DIALYSIS-SESSIONS) * 3) / 7)
        this.hLvOutPaymentRounded = hLvOutPayment * (((bClaimNumDialysisSessions) * 3) / 7);


    }

    /**
     * LEAF - L1719-1900
     * Branches: 32, GOTO: 0, CALLs: 0
     */
    private ReturnCodeResponse _9000SetReturnCode() {
        // IF (TRAINING-TRACK                  = "Y"  THEN): RETURN CODE PPS-RTC = 17
        // IF (TRAINING-TRACK                  = "Y"  THEN): RETURN CODE PPS-RTC = 16
        // IF (TRAINING-TRACK                  = "Y"  THEN): RETURN CODE PPS-RTC = 15
        // IF (TRAINING-TRACK                  = "Y"  THEN): RETURN CODE PPS-RTC = 14
        // IF (CHRONIC-COMORBID-TRACK    = "Y"  THEN): RETURN CODE PPS-RTC = 24
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 19
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 29
        // IF (CHRONIC-COMORBID-TRACK    = "Y"  THEN): RETURN CODE PPS-RTC = 23
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 18
        // IF (ONSET-TRACK         = "Y"  THEN): RETURN CODE PPS-RTC = 30
        // IF (ONSET-TRACK         = "Y"  THEN): RETURN CODE PPS-RTC = 28
        // IF (CHRONIC-COMORBID-TRACK    = "Y"  THEN): RETURN CODE PPS-RTC = 34
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 35
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 33
        // IF (CHRONIC-COMORBID-TRACK    = "Y"  THEN): RETURN CODE PPS-RTC = 07
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 06
        // IF (ONSET-TRACK         = "Y"  THEN): RETURN CODE PPS-RTC = 09
        // IF (ONSET-TRACK         = "Y"  THEN): RETURN CODE PPS-RTC = 03
        // IF (CHRONIC-COMORBID-TRACK    = "Y"  THEN): RETURN CODE PPS-RTC = 26
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 21
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 12
        // IF (CHRONIC-COMORBID-TRACK    = "Y"  THEN): RETURN CODE PPS-RTC = 25
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 20
        // IF (ONSET-TRACK         = "Y"  THEN): RETURN CODE PPS-RTC = 32
        // IF (ONSET-TRACK         = "Y"  THEN): RETURN CODE PPS-RTC = 10
        // IF (CHRONIC-COMORBID-TRACK    = "Y"  THEN): RETURN CODE PPS-RTC = 27
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 22
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 11
        // IF (ONSET-TRACK               = "Y"  THEN): RETURN CODE PPS-RTC = 08
        // IF (ACUTE-COMORBID-TRACK   = "Y"  THEN): RETURN CODE PPS-RTC = 04
        // IF (CHRONIC-COMORBID-TRACK = "Y"  THEN): RETURN CODE PPS-RTC = 05
        // IF (LOW-BMI-TRACK = "Y"  THEN): RETURN CODE PPS-RTC = 31
        // IF (LOW-BMI-TRACK = "Y"  THEN): RETURN CODE PPS-RTC = 02

        return new ReturnCodeResponse();
    }

    /**
     * LEAF - L1901-2054
     * Branches: 7, GOTO: 0, CALLs: 0
     */
    private void _9100MoveResults() {
        // COBOL: COMPUTE H-OUT-PAYMENT ROUNDED = H-OUT-PAYMENT / B-CLAIM-NUM-DIALYSIS-SESSIONS
        this.hOutPaymentRounded = hOutPayment / bClaimNumDialysisSessions;

        // COBOL: COMPUTE PPS-2011-BLEND-COMP-RATE    ROUNDED = H-PYMT-AMT * COM-CBSA-BLEND-PCT
        this.pps2011BlendCompRateRounded = hPymtAmt * comCbsaBlendPct;

        // COBOL: COMPUTE PPS-2011-BLEND-PPS-RATE     ROUNDED = H-PPS-FINAL-PAY-AMT * BUN-CBSA-BLEND-PCT
        this.pps2011BlendPpsRateRounded = hPpsFinalPayAmt * bunCbsaBlendPct;

        // COBOL: COMPUTE PPS-2011-BLEND-OUTLIER-RATE ROUNDED = H-OUT-PAYMENT * BUN-CBSA-BLEND-PCT
        this.pps2011BlendOutlierRateRounded = hOutPayment * bunCbsaBlendPct;

        // COBOL: COMPUTE PPS-2011-BLEND-COMP-RATE    ROUNDED = PPS-2011-BLEND-COMP-RATE * QIP-REDUCTION
        this.pps2011BlendCompRateRounded = pps2011BlendCompRate * qipReduction;

        // COBOL: COMPUTE PPS-2011-FULL-COMP-RATE     ROUNDED = PPS-2011-FULL-COMP-RATE * QIP-REDUCTION
        this.pps2011FullCompRateRounded = pps2011FullCompRate * qipReduction;

        // COBOL: COMPUTE PPS-2011-BLEND-PPS-RATE     ROUNDED = PPS-2011-BLEND-PPS-RATE * QIP-REDUCTION
        this.pps2011BlendPpsRateRounded = pps2011BlendPpsRate * qipReduction;

        // COBOL: COMPUTE PPS-2011-FULL-PPS-RATE      ROUNDED = PPS-2011-FULL-PPS-RATE * QIP-REDUCTION
        this.pps2011FullPpsRateRounded = pps2011FullPpsRate * qipReduction;

        // COBOL: COMPUTE PPS-2011-BLEND-OUTLIER-RATE ROUNDED = PPS-2011-BLEND-OUTLIER-RATE * QIP-REDUCTION
        this.pps2011BlendOutlierRateRounded = pps2011BlendOutlierRate * qipReduction;

        // COBOL: COMPUTE PPS-2011-FULL-OUTLIER-RATE  ROUNDED = PPS-2011-FULL-OUTLIER-RATE * QIP-REDUCTION
        this.pps2011FullOutlierRateRounded = pps2011FullOutlierRate * qipReduction;


    }


    @Data
    public static class ReturnCodeResponse {
        private String code;
        private String message;
    }
}
