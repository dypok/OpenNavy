# ADR-0002: Hexagonal and Modular Architecture for Open-Source Maintainability

## Status
Accepted

## Context
Open-source codebases suffer when tight coupling exists between the presentation layer (UI/API), core domain logic (AST parsing, course plotting), and infrastructure dependencies (Ollama, SQLite, WebSockets). External contributors struggle to submit parsers for new programming languages or swap inference providers without breaking the system core.

## Decision Drivers
* Strict independence from web frameworks and external inference libraries.
* Isolated, deterministic testability of topological graph logic without requiring external database or AI services.
* Low barrier to entry for community contributors adding language-specific Tree-sitter parsers.

## Decision
A modular architecture based on Ports and Adapters (Hexagonal Architecture) is adopted:

1. **Domain / Code Analyzers (Core):**
   * Universal AST engine built on Tree-sitter (`treesitter_engine.py`).
   * Topological dependency and Strongly Connected Components analyzer using Tarjan's algorithm (`dependency_graph.py`).
   * Completely agnostic of HTTP transport, persistence models, or LLM clients.
2. **Application Services (Application Layer):**
   * Course Plotting Service (`CoursePlotterService`): Correlates issue requirements with AST coordinates.
   * Fleet Sonar Service (`FleetSonarManager`): Coordinates peer presence and topological proximity evaluation.
3. **Infrastructure Adapters (Adapters):**
   * Ollama Adapter (`ChatOllamaLocal`): Local inference adapter.
   * SQLite Repository (`SQLAlchemy`): Metadata persistence and exploration caching.
   * WebSocket Adapter: Real-time network transport on FastAPI.
4. **Presentation Layer (Frontend):**
   * Decoupled React 18 + Vite SPA communicating strictly via typed REST endpoints and WebSocket protocols defined in TypeScript.

## Consequences
* Positive: High cohesion and loose coupling. New languages supported by Tree-sitter can be integrated without modifying the API or UI.
* Positive: Sub-millisecond deterministic unit testing of the analysis engine without network mocks.
* Negative: Additional structural layers compared to a single monolithic script.
