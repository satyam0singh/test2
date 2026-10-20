# Decision Log — add a readme file in the code

## ADR-001: No filesystem writes before explicit plan approval

- Status: confirmed
- Rationale: The build engine can write to the user's local folder, so every write is gated behind the human-in-the-loop confirmation step.

