# Replay certificate

The verifier was shipped by content to Modal and replayed in app
`ap-fhAejZ8N8s1odZXvoM4kAo`. It returned

```text
XR_AFFINE_CORE_COGIRTH_RAY_BOUND_PASS
matroids=32280 equality=3960 affine_lines=624 max_pairs=5
rowc-r1_4:ambient_s<=4,rank4=closed
rowc-r1_8:ambient_s<=4,rank4=closed
rowc-r1_16:ambient_s<=3,rank4=closed
prize-r1_4:ambient_s<=11,rank4=closed
prize-r1_8:ambient_s<=11,rank4=closed
prize-r1_16:ambient_s<=10,rank4=closed
```

The matroid replay exhausts all full-rank `2 x 4` ternary and `3 x 5` binary
column systems. It verifies the cogirth basis lower bound in 32,280 cases,
including 3,960 equality cases. The affine replay exhausts 624 complete
transverse syndrome-line families for the length-four ternary repetition
code. A seven-slope nongeneric tangent family exceeds the `a=0` bound and is
rejected. Peak worker RSS was `57 MB`.

`ambient_s` is the largest affine selector rank paid on the full evaluation
domain. `rank4=closed` includes the RowC `1/16` handoff from the collision-line
self-localized chart of excess at most seven; the other rows are already paid
on the full domain or by a stronger collision-line branch.

After manifest refresh, the repository-wide Modal replay passed `128/128`
verifiers with no failures, timeouts, hash mismatches, or remote errors in app
`ap-IZqfGQD2KDhYQJwEl55Hb2`. The five integration gates passed in
`ap-Hk6TgSQLiV1chotFlgLlzX`, retaining exactly nine open critical truth leaves.
The critical orbit was rebuilt remotely in `ap-Bh4acgOozNjZejFSk5b2ZL`.

The exact local-envelope audit in `route_limit.md` was replayed in Modal app
`ap-3SsE1JL5IiiOkotzT89CcR`.  It returned the same paid P-A selector ranks
`4,4,4,11,11,10`; the third RowC rank includes the existing rank-four chart
handoff.  Therefore iterating the present cogirth and minimum-line-basis
bounds gives no additional official rank.


[w6 audit 2026-07-13: the paid ranges quoted here inherit catch #158 -- at RowC 1/16 the rank-4 handoff is conditional (line-admitting b <= 47 or line-covered hulls); the line-free/line-uncovered rank-4 sub-case remains open and is not fenced by this envelope, which presupposes the covering step; the rank-five kill is unconditional on the covered branch.]
