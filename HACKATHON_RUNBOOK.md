# Hackathon Runbook: Gemma 4 Server & Cloudflare Tunnel

Quick reference operational guide for local team deployments.

---

## 1. Starting the Central Host Server (One-Click)

On the host machine, open **PowerShell** in the project root and execute:

```powershell
.\scripts\start-server.ps1
```

* **What it does:**
  1. Starts the local Ollama daemon with `OLLAMA_ORIGINS=*` and `OLLAMA_KEEP_ALIVE=-1`.
  2. Pre-warms and pins `gemma4:e4b` in memory.
  3. Establishes a secure Cloudflare tunnel and outputs a public endpoint such as:
     `https://example-words-xyz.trycloudflare.com`

> **Note:** Copy the generated URL and distribute it across the team.

---

## 2. Developer Client Configuration

Each team member configures their environment variable to point to the shared host:

### In `.env` (Frontend or Backend):
```env
AI_SERVER_URL=https://your-cloudflare-tunnel.trycloudflare.com/v1
AI_MODEL_NAME=gemma4:e4b
AI_FALLBACK_MODEL=gemma4:e2b
AI_API_KEY=ollama
```

### Validate Connectivity via CLI:
```bash
python scripts/test-inference.py https://your-cloudflare-tunnel.trycloudflare.com
```

---

## 3. Dynamic Model Switching

Restarting the server is not required to switch between tiers. Simply pass the target model name in the JSON payload:
- For maximum reasoning depth / architecture synthesis: `"model": "gemma4:e4b"`
- For high-speed / latency-sensitive operations: `"model": "gemma4:e2b"`

---

## 4. Emergency Contingency Protocol ("Plan B")

In the event of hardware power failure or local Wi-Fi interruption:
1. Navigate to [Google AI Studio](https://aistudio.google.com/) and obtain an API key.
2. In your `.env` file, update the following variables:
   ```env
   AI_SERVER_URL=https://generativelanguage.googleapis.com/v1beta/openai/
   AI_API_KEY=YOUR_GEMINI_API_KEY
   AI_MODEL_NAME=gemini-2.5-flash
   ```
3. Due to OpenAI SDK compatibility standards, all downstream code continues functioning without modifications.

---

## 5. Hackathon Operational Timeline

- **09:00 - 10:00:** Host server initialized, endpoint shared, architecture baseline locked.
- **10:00 - 13:00:** Core deterministic engine and Gemma 4 prompt engineering.
- **13:00 - 13:30:** Integration testing (streaming responses verified).
- **13:30 - 15:30:** Frontend cockpit connection and visual ergonomics.
- **15:30:** **FEATURE FREEZE** (Strictly no new features).
- **15:30 - 16:30:** Happy path verification and backup demo screencast recording.
- **16:30 - 17:30:** Pitch deck review and presentation rehearsal.
