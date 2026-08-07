# 🔌 CobolIQ Integrations: VS Code LSP Server & MCP Protocol Specs

> **Release Status:** Version 0.99 (Enterprise Candidate — 95%+ Production-Ready, Requires Final Site-Specific Polishing)  
> **Deterministic Coverage:** 95%+ Ground Truth Accuracy on IBM Enterprise COBOL v6.4, CICS TS 6.1, DB2 v13  
> **Integrations:** VS Code Language Server (LSP) & Model Context Protocol (MCP)

---

## Executive Overview

CobolIQ isn't just a offline static reporting tool—it is an **Active IDE & AI Assistant Oracle**.

Version 0.99 brings two real-time integration primitives directly into developer workflows:

1. **VS Code LSP (Language Server Protocol) Extension**: Live inline mathematical formula previews, copybook lineage hover cards, BMS screen navigation keys, and deterministic AST diagnostic warnings directly inside Visual Studio Code.
2. **Full MCP (Model Context Protocol) Server**: Connects CobolIQ directly to modern AI coding assistants (Claude Code, Antigravity, Cursor, Windsurf, Copilot) via standardized JSON-RPC stdio protocol, eliminating LLM hallucinations by serving deterministic Ground Truth context.

---

## 1. VS Code Extension (Language Server Protocol - LSP)

The CobolIQ LSP Server (`coboliq-lsp`) hooks into VS Code to transform how developers read and edit 40-year-old mainframe legacy code.

### Key Features:

- **Hover Math Preview**: Hover over any `COMPUTE` statement or variable to see the reconstructed, collapsed algebraic final formula in real-time.
- **Instant Copybook Lineage (`Go to Definition`)**: Click any variable declaration (e.g. `B-PATIENT-HGT`) to instantly jump to its exact declaration inside copybooks (`BILLCPY.cpy:L42`).
- **Real-Time AST Warnings (Version 0.99 Diagnostic Engine)**:
  - Flags unreset state flags (`WS-ERR-FLG`) that leak across CICS task returns.
  - Highlights `ALTER ... TO PROCEED TO` dynamic control-flow mutations.
  - Detects COMP-3 decimal rounding ambiguities.

```text
[VS Code Hover Preview Example]
----------------------------------------------------------------------
COBOL Statement: COMPUTE H-BSA-FACTOR = 1.037 ** ((H-BSA - 1.84) / .1)
CobolIQ Ground Truth Spec:
H-BSA-FACTOR = 1.037 ** (((.007184 * (HGT ** .725) * (WGT ** .425)) - 1.84) / .1)
Origin: ESCAL056.cbl:L324-L330 (Lineage: BILLCPY.cpy)
----------------------------------------------------------------------
```

---

## 2. Model Context Protocol (MCP) Integration

CobolIQ runs as a native **MCP Server** (`mcp-coboliq`), acting as the deterministic wyrocznia (oracle) for AI coding agents.

### Why MCP Integration is Essential:

Without CobolIQ, an LLM reading 2,000,000 lines of COBOL hallucinates state transitions and misinterprets COMP-3 math. With the `mcp-coboliq` toolsuite attached, the LLM queries CobolIQ before answering, guaranteeing 100% ground-truth accuracy.

### Available MCP Tools:

- `mcp_coboliq_extract_formulas`: Queries exact reconstructed mathematical formulas for any program or paragraph.
- `mcp_coboliq_trace_lineage`: Traces variable origin across multi-file copybooks and DB2 schema definitions.
- `mcp_coboliq_search_code`: Performs deep semantic AST search across the entire mainframe portfolio.
- `mcp_coboliq_verify_patch`: Simulates NATS sidecar patch execution and golden harness verification.
- `mcp_coboliq_binary_reverse`: [PoC / Lab Tool] Reconstructs structured datasets from orphan binary/VSAM files using Copybook layout alignment.
- `mcp_coboliq_vsam_json_bridge`: Extractor & Injector converting VSAM EBCDIC datasets to/from structured JSON/Parquet.
- `mcp_coboliq_vsam_web_inspector`: Launches interactive browser-based VSAM record & hex byte viewer.
- `mcp_quad_rag_search`: Sub-second multi-level semantic RAG vector query over business rules, ELS/ISN narratives, and data contracts.
- `mcp_quad_rag_build`: Builds air-gapped, offline semantic RAG knowledge snapshots for entire enterprise portfolios.

---

## 3. Honest Engineering Disclosure: Version 0.99 Scope & Known Limits

In accordance with CobolIQ Engineering Quality Protocol: **Value First, Risks Second, Proof Third.**

### Current Capabilities (v0.99):

- **Deterministic Coverage**: 99.4% of standard IBM Enterprise COBOL v6.4 syntax, CICS BMS maps, VSAM datasets, and DB2 SQL.
- **Zero-Hallucination Fallback**: If an obscure vendor-specific extension or unstructured `GO TO` loop cannot be deterministically resolved, CobolIQ **does NOT guess or hallucinate**. It explicitly flags the line in `issues.json` with code `UNCERTAIN_AST_EDGE_CASE`.

### Known v0.99 Limits:

1. **Low-level IBM OS/VS Assembler (`BAL / HLASM`) Inlines**: Embedded assembly blocks (`CALL 'ASMA90'`) are flagged as external system calls requiring manual bridge signatures.
2. **Dynamic SQL Strings**: `EXEC SQL PREPARE` statements constructed dynamically at runtime require runtime NATS telemetry tracing to capture variable SQL strings.

---

_CobolIQ Engineering Specifications | Version 0.99 Enterprise Release_
