# 2026 Hackathon — Exposure Territory / team121

This branch contains the team121 strategy package and v2 strategy notes/helpers.

## v1 package

[Download v1 ZIP](./exposure-territory-team121.zip)

## v2 source added

- [Strategy notes](./exposure-territory-team121-v2/STRATEGY_NOTES.md)
- [Strategy helper implementation](./exposure-territory-team121-v2/strategy_helpers.py)
- [Helper tests](./exposure-territory-team121-v2/tests/test_strategy_helpers.py)

The v2 helpers provide legal-command filtering, BFS first-step routing, weighted territory value, exposed-edge counting, and a score estimate. They are reference components and still need to be integrated with the official SDK adapter.

## Validation caveat

The official `player-kit.zip` has not been run against this repository's v2 helpers. Use the official engine as source of truth for movement, closure, and match scoring. The helper tests are not tournament-engine tests.

No strategy can guarantee first place against unknown opponents and maps. Validate both seats over many seeds before submitting.
