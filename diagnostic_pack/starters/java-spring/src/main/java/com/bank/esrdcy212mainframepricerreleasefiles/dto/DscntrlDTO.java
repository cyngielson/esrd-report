package com.bank.esrdcy212mainframepricerreleasefiles.dto;

import lombok.Data;
import lombok.Builder;

/**
 * DTO mapped from COBOL copybook: DSCNTRL
 */
@Data
@Builder
public class DscntrlDTO {

    private String bThruYearCode;
    private String bunCbsaDate;
    private String bunCbsaWIndex;
    private String bunSub;
    private String childHospSwiFoundSwitch;
    private String comCbsaDate;
    private String comCbsaWIndex;
    private String comCbsaWageRecord;
    private String comSub;
    private String ppsCalcVersCd;
    private String ppsFinalPayAmt;
    private String ppsRtc;
    private String wNewEffDate;
    private String wNewRate1Record;
    private String wNewRate2Record;
    private String wSub1;
    private String wSub2;
    private String wSub3;
    private String wwdSub;

}
