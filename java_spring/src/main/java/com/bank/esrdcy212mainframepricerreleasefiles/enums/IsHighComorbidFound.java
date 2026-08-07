package com.bank.esrdcy212mainframepricerreleasefiles.enums;

/** State machines from ESCAL212
 */
public enum IsHighComorbidFound {
    Y("HIGH-COMORBID-FOUND"),
    ;

    private final String cobolValue;

    IsHighComorbidFound(String cobolValue) { this.cobolValue = cobolValue; }
    public String getCobolValue() { return cobolValue; }
}
