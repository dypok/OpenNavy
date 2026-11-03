# ADR-0005: GitFlow Branching Model and Conventional Commits

## Status
Accepted

## Context
OpenNavy is released as an open-source project targeting high engineering standards. A disorganized Git history filled with vague messages ("fix everything", "update code") diminishes technical credibility when reviewed by open-source maintainers, community evaluators, and hackathon judges.

## Decision
Formally adopt the GitFlow workflow complemented by the Conventional Commits v1.0.0 specification:

### 1. Branching Model (GitFlow)
* **`main`:** Protected production release baseline. Contains only stable, tagged, release-ready deliverables.
* **`develop`:** Primary integration branch where completed and verified features converge.
* **`feature/<name>`:** Short-lived branches created from `develop` to implement discrete backlog user stories (e.g., `feature/course-plotter-ui`, `feature/sonar-collision-radar`).
* **`hotfix/<name>`:** Critical patches branched directly from `main`.

### 2. Commit Message Standards
Every commit must be atomic and follow the standard structure:
`<type>(<scope>): <concise description in lowercase>`

Allowed types:
* `feat`: New user-facing capability.
* `fix`: Bug or defect correction.
* `docs`: Technical documentation additions or modifications.
* `refactor`: Code reorganization without functional or behavioral changes.
* `test`: Adding or adjusting unit and integration test suites.
* `chore`: Build configuration or dependency maintenance.

### 3. Style Constraints
* Use of emojis in commit messages, technical documentation, and code contracts is strictly prohibited to maintain readability across terminal environments and CI/CD tools.

## Consequences
* Positive: Granular, professional audit trail for every increment of value.
* Positive: Automated generation of changelogs and release notes.
* Positive: Streamlined peer review process during Pull Request inspection.
