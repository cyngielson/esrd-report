# CobolIQ — Executive Overview & Enterprise Architecture

## Stop Migrating. Start Understanding Ground Truth.

---

### Slide 1: The Core Enterprise Challenge

- **50 Years of Accumulated Legacy Math**: Mainframe systems (COBOL, PL/I, HLASM, RPG) contain unwritten business formulas and complex edge cases.
- **The Failure of 1:1 Transpilation (JOBOL)**: Naive translation into Java creates unmaintainable legacy debt in a new language with 10% hallucination risk.
- **The Financial Risk**: Rip-and-replace cutovers fail when undocumented formulas get lost (e.g., TSB £380M disaster).

---

### Slide 2: The CobolIQ Ground-Truth Solution

- **Synaptic Logic Synthesizer (SLS Engine)**: High-speed Rust-based AST parser that isolates pure business algebra in <1 second with **0% LLM hallucination**.
- **3-Tier Outputs**:
  1. **Descriptive Business Algebra (100% English)**: Step-by-step mathematical reconstruction mapped to exact source code line numbers.
  2. **Interactive Web Calculators**: Standalone HTML/JS engines for instant tariff and logic validation without mainframe runtime.
  3. **Target Microservices**: Production-ready Python (Django) & Java (Spring Boot) clean starters.

---

### Slide 3: Enterprise Integration & User Experience Suite
- **Visual Desktop GUI (`coboliq-desktop v0.8.0`)**: Built with Tauri & Rust. Provides an intuitive, dark-mode native desktop dashboard for non-technical executives and actuaries—no terminal or CLI commands required.
- **VS Code LSP Extension (`coboliq-0.1.0.vsix`)**: Live inline formula previews, copybook lineage hover cards, and AST diagnostic warnings (`NUMERIC_TRUNCATION`, `STATE_LEAK`) directly in developers' IDEs.
- **Model Context Protocol (MCP Server)**: Standardized JSON-RPC integration feeding deterministic Ground Truth directly into AI coding agents.
- **100% Air-Gapped / US Cloud Compliance**: Zero network call-home dependencies. Deploys on-premise or within AWS GovCloud / US Telco Air-Gapped VPCs.

---

### Slide 4: Business Impact & FinOps ROI

- **10x Discovery Acceleration**: Complete logic extraction in 1 day instead of 18 months of manual analysis.
- **Zero Production Outage Risk**: Verified AST mathematical parity guarantees 100% financial accuracy before cloud cutover.
- **Founder-Owned Clean IP**: 100% European R&D (Poland, EU) with zero VC cap table friction — ready for OEM licensing & US Entity integration.

---

### Slide 5: Live Benchmark Proof & Deliverables

- **Federal CMS ESRD Pricer Audit**: 4,243 extracted pure business rules, interactive web calculator, and microservice starters available at:
  👉 **https://github.com/cyngielson/esrd-report**
