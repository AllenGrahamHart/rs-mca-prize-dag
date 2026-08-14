# Cycle 309: MCA rank-11 31-anchor C/S/A/E router (2026-08-14)

The new proved node `rate_half_mca_rank11_anchor_star_sae_router` globalizes
the local order-32 interfaces without changing support locators between
tuples.

Fix the eighteen dense-pair records and one off-pair-line record. Complete
them to a 31-record deck using the heavy-pair component basis. For basis size
`t<=6`, double every basis pair and fill to 31. For `7<=t<=10`, remove one
second record from the Cycle-307 schedule. The number of singly represented
cores is

```text
0,0,0,0,0,0,1,3,5,7,
```

so the fixed deck's exact common support is at most

```text
(K-4923)+7*387 = K-2214.
```

For every other post-near record `z`, the tuple `A_* union {z}` has 32
records, is non-affine, and has slope degree `18..31`. Exact cancellation,
support-collapsed extraction, and lift return to the same original locators.
Thus every pair of target tuples shares the identical 31 indexed
explanation/support-locator triples.

Outside named exceptions, collision rigidity makes all primitive root-free
rational certificates projectively identical, producing one coherent atom
owner `(A)`. A primitive high-complexity tuple gives `(S)`; pure locator,
denominator root, extension, quotient, clone, field-drop, nonprimitive
collision, or near-sunflower gives `(E)`.

The semantic audit found one necessary extra output. If a target tuple has a
nonempty maximal common agreement set, cancellation produces a punctured
domain, on which the deployed spread theorem cannot be assumed. This is
retained explicitly as `(C)`, not hidden inside `(E)`. Hence the exact route
is

```text
(C) local maximal-common residual
or (S) primitive spread
or (A) coherent rational owner
or (E) named exception.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_ANCHOR_STAR_CSAE_ROUTER_PASS
  core=1046362 singles=7 g31=1083345 toyQ=1 controls=7/7
RATE_HALF_MCA_RANK11_ANCHOR_STAR_CSAE_ROUTER_AUDIT_PASS
  core=1046362 g31=1083345 routes=4 controls=5/5
```

No Modal computation was used. The canonical Fable tree remained clean at
`659319780`; its earlier whole-line global-core audit confirms that `(C)` is
an unpaid shortened-family residual.

```text
start:                   2444ce8d6
DAG delta:               +1 PROVED anchor-star globalization router,
                         +4 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: rank-eleven-specific selector/coherence closed
                         outside one explicit common-core residual
delta-star movement:     none
compute:                 exact local arithmetic and GF(17) control only
next route action:       attack the local common-core star residual first;
                         S/A/E remain the shared upstream terminals
```
