# Infrastructure Evidence

*Best-effort static detection of external system dependencies: DB2, CICS, VSAM, IMS, JCL.*

**Limitations:** Table names are extracted heuristically. Dynamic SQL, CICS transaction routing, and JCL member resolution require additional analysis. See 04-LIMITATIONS.md for details.

> DB2: 0 SQL statements | CICS: 0 transactions | VSAM: 0 files | IMS: 0 calls | JCL: 0 hints | 0 programs with external dependencies

**No external infrastructure dependencies detected in this portfolio.** This may indicate a standalone batch-processing system or that external dependencies are in separate JCL/PROC members not included in the COBOL source directory.

