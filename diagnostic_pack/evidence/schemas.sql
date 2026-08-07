-- Auto-generated from COBOL table definitions

CREATE TABLE wwd-entry (
    wwd-date VARCHAR(8),
    wwd-dtcd SMALLINT
);

CREATE TABLE wwm-entry (
    wwm-msa VARCHAR(4),
    wwm-ptr INTEGER
);

CREATE TABLE www-entry (
    www-dtcd SMALLINT,
    www-wart1 DECIMAL(6,2),
    www-wart2 DECIMAL(6,2)
);

CREATE TABLE com-date-entry (
    com-date VARCHAR(8),
    com-date-code SMALLINT
);

CREATE TABLE com-cbsa-entry (
    com-cbsa-value VARCHAR(5),
    com-ptr INTEGER
);

CREATE TABLE com-wi-entry (
    com-wi-date-code SMALLINT,
    com-wage-index DECIMAL(8,4)
);

CREATE TABLE bun-date-entry (
    bun-date VARCHAR(8),
    bun-date-code SMALLINT
);

CREATE TABLE bun-cbsa-entry (
    bun-cbsa-value VARCHAR(5),
    bun-ptr INTEGER
);

CREATE TABLE bun-wi-entry (
    bun-wi-date-code SMALLINT,
    bun-wage-index DECIMAL(8,4)
);

CREATE TABLE child-hosp-group (
    child-hosp-prov VARCHAR(6),
    child-hosp-swi DECIMAL(8,4)
);

