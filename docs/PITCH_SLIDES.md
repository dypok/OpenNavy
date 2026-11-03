---
marp: true
theme: uncover
paginate: true
backgroundColor: #0A1128
color: #F8FAFC
style: |
  section {
    font-family: 'Inter', system-ui, sans-serif;
    text-align: left;
    padding: 40px 60px;
  }
  h1 {
    color: #38BDF8;
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
  }
  h2 {
    color: #94A3B8;
    font-size: 1.4rem;
    margin-top: 0;
  }
  .highlight {
    color: #FACC15;
    font-weight: bold;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
  }
  .card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 12px;
    padding: 16px 20px;
  }
  .badge {
    background: #0284C7;
    color: white;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 600;
  }
---

<!-- _class: lead -->
![width:180px](../assets/logo_opennavy.svg)

# OPENNAVY
### The Sovereign Fleet Navigator for Open Source Codebases

<span class="badge">MLH Hacktoberfest 2026</span>
<span class="badge">Google DeepMind Gemma 4</span>
<span class="badge">MIT License</span>

**Team:** Daniel Echeverría · Brandon Carranza · Dylan Gamero

---

# 1. The Challenge: Compliance Walls and Code Disorientation

<div class="grid">
  <div class="card">
    <h3 style="color: #F87171; margin-top:0;">The Compliance Wall</h3>
    <p>In banking, defense, and healthcare, <b>Cursor and Copilot are prohibited</b> because streaming proprietary code to external clouds violates SOC2 and GDPR.</p>
  </div>
  <div class="card">
    <h3 style="color: #FB923C; margin-top:0;">Open-Source Attrition</h3>
    <p>Over <b>80% of newcomers abandon</b> contributions because deciphering 50,000+ lines of unfamiliar architecture takes days.</p>
  </div>
</div>

<div class="card" style="margin-top: 20px; border-color: #38BDF8;">
  <p style="margin: 0; font-size: 1.15rem;">
    <b>The OpenNavy Solution:</b> A sovereign, local-first cockpit driven by <b>Google Gemma 4</b> and an air-gapped LAN multiplayer radar.
  </p>
</div>

---

# 2. Technology Trilogy: Live Demonstration

<div class="grid">
  <div class="card">
    <h3 style="color: #38BDF8; margin-top:0;">Multimodal Course Plotter</h3>
    <p>Ingests issue descriptions or UI error screenshots. <b>Gemma 4 Vision</b> reasons locally (<code>&lt;|think|&gt;</code>) and emits <b>exact waypoints</b> verified by Tree-sitter.</p>
  </div>
  <div class="card">
    <h3 style="color: #4ADE80; margin-top:0;">Fleet Sonar (LAN Mesh)</h3>
    <p>FastAPI WebSockets over local Wi-Fi. Detects <b>architectural collisions</b> via <b>Tarjan's SCC Algorithm</b> before developers commit code.</p>
  </div>
</div>

<p style="margin-top: 25px; text-align: center; color: #94A3B8;">
  <i>0 ms cloud latency · 100% Sovereign · Zero telemetry or external accounts</i>
</p>

---

# 3. Robust Architecture and Business Strategy

<div class="grid">
  <div class="card">
    <h3 style="color: #38BDF8; margin-top:0;">Hexagonal Architecture</h3>
    <ul>
      <li>Tree-sitter universal AST parser</li>
      <li>Tarjan SCC (linear cycle detection)</li>
      <li>Google Gemma 4 (<code>e4b</code> / <code>e2b</code>)</li>
      <li>FastAPI + React 18 / Tailwind CSS</li>
    </ul>
  </div>
  <div class="card">
    <h3 style="color: #FACC15; margin-top:0;">Open-Core Strategy</h3>
    <ul>
      <li><b>Community Edition (MIT):</b> $0, free forever for Hacktoberfest and developers.</li>
      <li><b>Enterprise Fleet:</b> $35 / seat / month. On-premise for regulated sectors with ISO 5055 audit reports.</li>
    </ul>
  </div>
</div>

<div style="text-align: center; margin-top: 30px;">
  <span style="font-size: 1.3rem; color: #38BDF8; font-weight: bold;">
    OpenNavy: The sovereign compass and fleet radar for modern software engineering.
  </span>
</div>
