# OpenNavy Engineering Roadmap

## Vision
OpenNavy is a sovereign, local-first developer cockpit and architectural radar engineered to turn complex open-source codebases into navigable nautical charts without cloud leakage. 

This document outlines delivered milestones and active planned engineering work for upcoming releases.

---

## 1. Release Milestones Overview

| Milestone | Target | Focus Area | Status |
| :--- | :--- | :--- | :--- |
| **v1.0.0** | Current | Core AST topography, Tarjan SCC cycle detection, Course Plotter, Fleet Sonar LAN mesh | **Delivered** |
| **v1.1.0** | Next Sprint | Polyglot Tree-sitter parsers, CLI pre-commit linter, local vector cache | **Active / Planned (~15h)** |
| **v1.2.0** | Following | GitHub Action bot, E2E test harness, performance scaling for large monorepos | **Planned (~13h)** |

---

## 2. Delivered Features (v1.0.0 Baseline)

- **Universal AST Parsing (Tree-sitter):** Multi-language parser extracting functions, complexity, and dependencies for Python, TypeScript, and JavaScript.
- **Topological Risk Detection (Tarjan SCC):** Strongly Connected Components solver identifying cyclic dependencies and architectural reefs in under 1 second.
- **Course Plotter Engine:** Issue-to-waypoint planner with Gemma 4 reasoning, zero-hallucination source line citations, and pull request drafting.
- **Nautical Cockpit UI:** Split-pane AST file tree and code viewer with synchronized line jumps, clean light theme, and enriched Markdown rendering.
- **Fleet Sonar (LAN Multiplayer Mesh):** Real-time WebSocket hub broadcasting peer telemetry and proximity collision alerts between co-located developers.
- **Local-First Privacy Architecture:** 100% on-premise execution via Ollama without cloud telemetry or external API dependencies.

---

## 3. Upcoming Work Packages (28+ Hours Planned)

### Milestone v1.1.0: Extended Language Support, CLI Tools, and Offline Caching (~15 Hours)

#### Package 1.1: Polyglot Tree-sitter Language Extensions (Estimated: 6 Hours)
- **Objective:** Broaden AST extraction beyond Python and TypeScript to support Go, Rust, and Java.
- **Deliverables:**
  - Integrate `tree-sitter-go` and `tree-sitter-rust` parser bindings into `backend/app/analyzers/treesitter_engine.py`.
  - Implement language-specific import extractors for Go (`import (...)`) and Rust (`use ...;`).
  - Unit test AST node generation on real sample Go and Rust projects.

#### Package 1.2: Git Pre-Commit Hook & CLI Linter (Estimated: 4 Hours)
- **Objective:** Provide a fast, headless CLI utility that blocks commits introducing cyclic dependencies.
- **Deliverables:**
  - Build CLI entrypoint `opennavy check-cycles [--strict] [--path <repo>]`.
  - Provide `.pre-commit-hooks.yaml` for pre-commit framework integration.
  - Return exit code 1 with exact cyclic file chains if new Tarjan cycles are detected.

#### Package 1.3: Offline Embedding Cache & Hybrid Search (Estimated: 5 Hours)
- **Objective:** Eliminate RAG re-indexing latency across application restarts.
- **Deliverables:**
  - Replace in-memory chunk scanning with a local persistent vector store (LanceDB or SQLite-vec).
  - Implement incremental document hashing to re-index only modified markdown and ADR files.
  - Reduce technical query context retrieval latency to under 50 milliseconds.

---

### Milestone v1.2.0: Automation, E2E Testing, and Monorepo Scalability (~13 Hours)

#### Package 2.1: Course Plotter GitHub Action Bot (Estimated: 5 Hours)
- **Objective:** Automatically post Gemma 4 waypoints directly onto newly filed GitHub repository issues.
- **Deliverables:**
  - Create reusable GitHub Action (`.github/workflows/opennavy-course-plotter.yml`).
  - Listen for `issues: opened` events, run headless Course Plotter, and post an architectural triage comment with waypoints and reef warnings.
  - Provide fallback offline mode for air-gapped CI runners.

#### Package 2.2: End-to-End Automated Testing Harness (Estimated: 4 Hours)
- **Objective:** Prevent UI and WebSocket regressions across cockpit updates.
- **Deliverables:**
  - Setup Playwright test suite in `frontend/tests/e2e/`.
  - Test split-view file navigation, waypoint jumping, code block clipboard copying, and live WebSocket radar updates.
  - Integrate Playwright run into GitHub Actions CI pipeline.

#### Package 2.3: Monorepo Scalability and Memory Profiling (Estimated: 4 Hours)
- **Objective:** Maintain sub-second AST analysis on large repositories exceeding 100,000 lines of code.
- **Deliverables:**
  - Implement parallel file scanning using Python `multiprocessing` worker pools.
  - Add AST node chunking and memory footprint limits for dependency graph construction.
  - Benchmark performance against popular open-source repositories (such as FastAPI, Flask, and Vite).

---

## 4. Contributing to the Roadmap

We welcome community feedback, pull requests, and architectural proposals. All contributions follow our [Contributing Guidelines](README.md#8-contributing--gitflow-guidelines) and GitFlow workflow:
- Development branch: `develop`
- Releases: `main`
- Style policy: Conventional Commits, zero emojis.
