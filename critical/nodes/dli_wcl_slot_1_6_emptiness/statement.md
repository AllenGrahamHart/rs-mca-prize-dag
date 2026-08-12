# WCL slot (1,6) emptiness

- **status:** TARGET (minted 2026-07-19 at the WCL amber ceremony)
- **consumer:** `dli_wcl_zone_coverage` (req)

At every official row, no reduced signed weight-6 polynomial vanishes at
an order-512 root (ell=1 window). Zero-event obligation. Evidence note:
(1,6)-shaped relations EXIST at non-ambient primes (the engineered
weight-6 witness) — the official-admissibility gate (v_2(q-1) >= 41) is
load-bearing. FALSIFIER: one official-admissible prime with such a
vanisher.

Finite exact evidence has two panels. The first 64 certified split-prime
characteristics, `q=k*2^41+1` for prime rows with `3<=k<=996`, exhaust all
normalized legal pair/triple splits and contain no vanisher. A second exact
panel exhausts 128 generated extension rows: 64 with exact `v_2(p-1)=39`
and `q=p^4`, and 64 with exact `v_2(p-1)=40` and `q=p^2`. Every extension
characteristic has a full-factorization Pocklington certificate, and four
class endpoints have independent sorted-pair replays. This does not alter
`TARGET`: later characteristics and nonsplit-on-`mu_512` extension classes
remain unclassified.

Structural router: aggregating the 32 sign lifts of each six-subset of
`mu_256` gives one symmetric degree-16 sign product with exactly the union of
their norm-prime supports. The affine-Galois quotient has `11,650,060`
unsigned orbits, split into `6,025,357` even-product and `5,624,703`
odd-product sectors. Aggregate factor control at the official gate remains
open. The pair-Heron refinement factors each aggregate into eight explicit
six-term conjugates, each owning four sign classes; prime control of those
factors remains open. Parity-adapted pairing places all eight factors directly
in `Q(zeta_256)` in the even sector and reduces the odd sector to four
explicit quadratic norms there. Prime control of these base-field factors
remains open, so this also leaves the node `TARGET`.

The conductor/block-gcd audit closes one proposed continuation negatively.
All-one-parity supports descend exactly to their maximal lower two-adic
conductor. At the resulting mixed-parity conductor, every even Heron block
norm is a product of two complete signed rational norms and every odd
quadratic block norm is a product of four. Hence gcds across different
pairings remain divisible by the complete norm of any sign class they share;
they cannot provide the independent-obstruction compression that closed the
`ell=2` lower weights. Individual minimal-conductor norm control or a genuinely
independent equation remains open.
