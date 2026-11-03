# ADR-0004: LAN Multiplayer Mesh with WebSockets and Collision Detection

## Status
Accepted

## Context
During hackathons, in-person software sprints, or offline office environments without external internet connectivity, engineering teams frequently encounter code collisions and merge conflicts because they lack mutual visibility into which files or coupled modules their teammates are actively editing. Traditional collaborative tools rely on centralized cloud backends (Firebase, Supabase).

## Decision
Implement an air-gapped real-time WebSocket event hub on FastAPI (`/ws/sonar`) hosted on the local area network:
1. **Crew Presence Tracking:** Each local client connects to the WebSocket hub and announces navigational coordinates (`NAVIGATE`: file path and target issue ID).
2. **Topological Proximity Radar:** The backend continuously verifies whether Developer A's active file shares a circular dependency or import boundary with Developer B's file according to Tarjan's SCC matrix.
3. **Collision Course Alert:** Upon detecting tight coupling, a `COLLISION_ALERT` payload is instantly dispatched to both screens before developers save or commit code.

## Consequences
* Positive: Proactive pre-merge conflict prevention in real time.
* Positive: Zero cloud reliance; functions seamlessly over local Wi-Fi or offline access points.
* Positive: Sub-millisecond latency across the local mesh.
* Negative: Requires developers to remain connected to the host WebSocket during joint sessions.
