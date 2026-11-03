# ADR-0003: Sovereign Local-First Inference with Google Gemma 4

## Status
Accepted

## Context
Developers collaborating on open-source projects or working within privacy-regulated environments (finance, healthcare, defense) cannot transmit proprietary source code to public cloud APIs (such as OpenAI or Anthropic). Concurrently, the platform requires advanced architectural reasoning to interpret incoming issues and correlate them with the repository AST.

## Considered Options
1. **Cloud Commercial Models (OpenAI GPT-4o / Claude 3.5 Sonnet):** High reasoning output, but breaches data sovereignty requirements, incurs per-token recurring costs, and mandates persistent internet connectivity.
2. **70B+ Parameter Open Models:** Impractical for commodity developer laptops during local hackathons or off-grid sprints without enterprise multi-GPU hardware.
3. **Google Gemma 4 (e4b and e2b Variants):** Open-weights architectures featuring native reasoning traces (`<|think|>`), multimodal vision capabilities, and modest memory footprints (3.5 GB to 6.6 GB).

## Decision
Adopt **Google Gemma 4** executed locally via **Ollama** using the following hierarchy:
* **Primary Tier:** `gemma4:e4b` (Q4_K_M quantization). Balances deep architectural reasoning, strict JSON contract compliance, and local CPU/GPU throughput.
* **Fallback Tier:** `gemma4:e2b`. For resource-constrained hardware or memory profiles under 8 GB RAM.
* **Server Daemon Settings:** `OLLAMA_ORIGINS=*`, `OLLAMA_KEEP_ALIVE=-1` (maintains active model in RAM across requests), and `OLLAMA_NUM_PARALLEL=2`.

## Consequences
* Positive: Zero external telemetry. Complete compliance with air-gapped environments.
* Positive: Zero operational subscription or inference token costs.
* Positive: Direct visibility into the model's intermediate reasoning trace in the cockpit UI.
* Negative: Token generation rate is tied to local host hardware specs (10-15 tokens/s on modern CPU, 30-50 tokens/s on GPU).
