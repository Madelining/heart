# team121 v2 strategy core

This is a readable reference implementation of the v2 planning concepts. Integrate it with the official SDK adapter; it deliberately does not replace the HTTP gateway.

## Safety-first decision outline
1. Enumerate legal non-reverse commands.
2. Simulate each command against the official engine copy when available.
3. Reject actions that die immediately or leave a vulnerable trail when the opponent can cut it.
4. Score completed territory using cell value (ordinary=1, critical='*'=3) and exposed-edge penalty.
5. Prefer the best safe closure; otherwise stay near owned territory and pursue short loops.
6. Always return a legal command on exception.

The downloadable v2 ZIP includes the fuller multi-segment planner and regression suite. The official `player-kit` must be used to validate engine integration and tournament performance.
