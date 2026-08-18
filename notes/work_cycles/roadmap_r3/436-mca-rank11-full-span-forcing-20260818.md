# Cycle 436: rank-eleven full-span forcing

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 0badb9680
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
relevant open PRs: #1173 (2788d5ec3), #1172, #1171, #1170
critical mandatory-open count: 28 TARGET nodes
```

The live open-PR search contains no successor to `#1173`; main and canonical
are unchanged. No source tree was modified.

## Action

Reoptimize the anchored rich-flat envelope with one common affine correction
cap at dimensions seven, eight, and nine. Determine whether all sub-full-span
survivors can be paid and print the exact dimension-ten route wall.

## Result: NARROWED

`rate_half_mca_rank11_full_span_residual_forcing` is PROVED. At
`(tau,h)=(1679,38384)`, the transverse envelope is
`209812758437679617`; the complete dimension-nine nontransverse union costs
`65157026870188671`; and the total `274969785307868288` is below budget by
`10942803526799`. Therefore every unsafe survivor has

```text
dim(V_nt)=dim(C')=10.
```

Its exact population floor is

```text
nontransverse mass >= 65167969673715471
represented row spaces >= 262093370
promoted rich containers >= 16384884
common zeros per container >= 38385.
```

The adjacent threshold `h=38385` is over by `2062328934603`. The globally
best dimension-ten one-container formula occurs at `tau=872,h=0` and is over
by `773076621594690156`; this payment family is exhausted.

## Burn-down

```text
node/workboard item: KoalaBear rank-eleven collective rich-flat span
result: NARROWED
DAG delta: +1 PROVED background node; critical open count remains 28
upstream delta: stronger exact continuation of live PR #1173; held for one consolidated packet
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: exploit full-span basis exchange or weighted rich-container incidence;
             do not optimize another bounded-span envelope
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_full_span_residual_forcing/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_full_span_residual_forcing/verify_audit.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_full_span_residual_forcing/verify.py --tamper-selftest
tools/ramguard local -- python3 tools/verify_prize_dag.py
```
