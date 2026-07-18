# rate_half_band_closure

- **status:** TARGET
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/flip_packets/rate_half_coverage_gap.md']

## Statement

Cover the 2,978,147-radius band at prize-max rate 1/2 (M_max = 2^33 vs sigma* = 8,592,912,738) by a new mechanism (quotient windows and integrality both fall short) — or the rate-1/2 determination lands bracket-grade there. Rates 1/4, 1/8, 1/16 need nothing (clean by margins < -121). THE rate-1/2 battlefield node.

## Attack surface

a third mechanism for the band: extended quotient scales, averaged conversion at giant M, or the B2b-style balance analysis

## Falsifier

a band radius provably uncoverable by any priced mechanism

## [LIST-SIDE RETIREMENT + MCA/CA RE-SCOPE (wave-8 audited, 2026-07-16)]

The GRAND-LIST-DECODING half of this obligation is RETIRED BY THEOREM:
`rate_half_cyclic_rotated_prefix_floor` (PROVED, imported; + background
`rate_half_fixed_tail_prefix_floor`) proves the entire residual band
2^33 < sigma <= sigma* list-unsafe at sigma* — the trigger count
> q/2^128 is exactly the prize's |Lambda(C^{==m})| <= 2^-128 |F| object
— for ordinary + every constant common-support arity, every admissible
q < 2^256 (margin 75.0796 bits at q=2^256; cap boundary 256.0366 > 256;
agreement = k+sigma* exact). With the banked safe side, the rate-1/2
LIST crossing is DETERMINED; list_adjacency_closing consumes the PROVED
node directly. REMAINING for this red: the support-wise MCA/CA crossing
only (trigger ~ q/k). GUARD (verbatim, audited): any MCA-side argument
must not reuse the list threshold q/2^128 as an MCA surrogate — the two
triggers are different objects (separation measured:
notes/rate_half_trigger_separation_modal.py).

## [CORRECTION to the wave-8 addendum above (2026-07-17, w9-C2 — our
## own overclaim, caught by the wave-9 audit via v4's scope audit)]

The sentence "With the banked safe side, the rate-1/2 LIST crossing is
DETERMINED" is WITHDRAWN. The "banked safe side above sigma*" was
planning prose, not an in-repo theorem (the Paper D pincer stops at
half distance; r2_clean_rates excludes rate 1/2), and the s = c-1
instantiation of the cyclic floor proves list-unsafety THROUGH
sigma_0 = 8,594,128,895 > sigma*. Corrected state: the LIST UNSAFE
side is proved through sigma_0 (the cyclic floor node, strengthened);
the LIST SAFE side is OPEN (field-dependent); the crossing is NOT
determined. The retirement claim narrows accordingly: what is retired
is the unsafety obligation on the band, not the crossing location.
This node's own open content remains the MCA/CA half — now re-posed by
the audited v4 work as (RH-ADJ): find field-dependent a_RH(q) >=
k + 8,594,128,896 with B_mca(a_RH) <= floor(q/2^128) < B_mca(a_RH - 1).

## FIXED-CROSSING REFUTATION + FIELD-DEPENDENT RE-POSE (wave-9 audited, 2026-07-17; pin statement body — master text above preserved per #104)


- **status:** TARGET
- **closure:** proof
- **current object:** rowwise support-wise MCA adjacent certificate
- **refs (legacy repo):** `experimental/notes/roadmaps/flip_packets/rate_half_coverage_gap.md`

## Statement

Let

```text
n=2^41,       k=2^40,       C=RS[F,D,k],
2^128<q=|F|<2^256,          n divides q-1,
B*(q)=floor(q/2^128),
```

where `D` is a multiplicative coset of order `n`. Produce an explicit
row-computable agreement `a_RH(q)` and prove the exact adjacent certificate

```text
B_mca(a_RH(q)) <= B*(q) < B_mca(a_RH(q)-1).              (RH-ADJ)
```

Here `B_mca(a)` is the maximum number of finite slopes carrying a failed
support-wise MCA witness with agreement at least `a`. Equivalently,
`B_mca(a)/q=epsilon_mca(C,1-a/n)` under the closed finite-slope convention.
The range `q<2^128` is the already-settled degenerate regime with grand
threshold zero; equality `q=2^128` cannot admit this order-`2^41`
multiplicative domain.

## Proved lower bracket and refutation

Put

```text
c=2^22,       d=2048,
sigma_0=dc+c-1=8,594,128,895.
```

The strengthened proved node `rate_half_cyclic_simple_pole_mca_floor` gives

```text
B_mca(k+sigma_0)>B*(q)                                    (RH-LOW)
```

for every field in scope. Consequently every valid adjacent certificate
must satisfy

```text
a_RH(q) >= k+sigma_0+1.                                  (RH-BRACKET)
```

This refutes the former fixed claim at

```text
k+8,592,912,738+1 <= k+sigma_0.
```

Thus `sigma*=8,592,912,738` is not the rate-half crossing, and the old
`(RH-SAFE)` statement must not be consumed downstream. The conjectural
corridor map that printed this point is also not an optimality certificate
for rate `1/2`.

## Exact safe-side reduction

For any proposed agreement `a`, the proved sparsification identity in
`rate_half_mca_sparse_layer_reduction` writes

```text
B_mca(a)=max(B_ca^far(a), S_sparse(a)).                   (RH-SPLIT)
```

Therefore the safe half of `(RH-ADJ)` is exactly the conjunction

```text
B_ca^far(a_RH(q)) <= B*(q),
S_sparse(a_RH(q)) <= B*(q).
```

The first term is the plain correlated-agreement upper problem for
column-far pairs. The second is the budget-restricted sparse mutual layer.
Neither is supplied by the deep or half-distance pincer at this
near-capacity radius.

The proved `rate_half_sparse_pinning_rigidity` theorem further reduces the
sparse term. At `a=k+tau`, every non-tangent bad slope requires support
`e>=tau+1`, a nonzero ambiguity polynomial with cofactor degree at most
`e-tau-1`, and at least `A-e+tau+1+u` active matches consistent with one
slope. For `q>=2^168`, all tangent slopes already fit `B*(q)`, so only this
coupled non-tangent system remains on the sparse side.

## Attack surface

Locate a candidate at or above `(RH-BRACKET)`, then prove both upper bounds in
`(RH-SPLIT)` and an adjacent lower witness. A complete first-match/profile
ledger may prove both upper terms; a stronger explicit lower family may move
the bracket farther before the upper work begins.

## Falsifier

For any proposed formula `A(q)`, either an admissible row with
`B_mca(A(q))>B*(q)` or failure to prove
`B_mca(A(q)-1)>B*(q)` falsifies that adjacent formula. The previously proposed
constant formula is already falsified by `(RH-LOW)`.

## QUADRATIC EXACT RANGE + SAFE BRACKETS + HANKEL SUITE + OPTIMIZED FLOOR (wave-10 audited, 2026-07-18 — the reconciled v4+v5 state; all previous poses preserved above)

**THE CROSSING IS DETERMINED for every admissible 2^128 < q < 2^167:** a_RH(q) = n - floor(q/2^128) + 1, unconditional. Composition: the quadratic staircase equality (mca_quadratic_prize_rows) covers B = floor(q/2^128) <= B_Q = 389,500,552,609 (~2^166.503); the (RQ4) equivalence reduces B_Q < B <= 2^39+1 to the single far-CA bound; the Hankel suite's unconditional layer B_ca^far(n-r) <= r+1 (every r <= 2^39-2) supplies it; the universal coordinate-tangent family (mca_full_agreement_endpoint, in-repo since wave-6) supplies the adjacent unsafe witness. The wave-9 PR4 q >= 2^168 caveat is bypassed below 2^167.

**EXACT RESIDUAL of (RH-ADJ):** budgets 2^39 (strict A=3, s=0, e in [2^37, floor((2^39-1)/3)]) and 2^39+1 (A=3 e >= 2^37+1, plus A=1 rows) — recorded per w10-H1 as the explicit open-budget set {2^39, 2^39+1}; beyond 2^167, brackets only: a_RH in [k+2^34, 3n/4] for q >= 2^169, [k+2^34, n] otherwise. The k+2^34 floor (v5's optimized re-instantiation, c=2^33, d=1, field-independent list 2^242.65) SUPERSEDES the former k+8,594,128,896 bracket lines and sigma_0 as the forward-facing constant (sigma_0 retained as history — forced-corrections authority, proved constant improvement).

**Hankel suite note (w10-H5):** the seven strict-endpoint nodes rigidify the residual profile at strict budget e=m only — they are NOT q-axis coverage progress. The five wave-9 guidance lines and the three pre-suite 'Remaining proof' lines are superseded, not deleted (w10-H2).

**LIST side (v5, audited):** the safe side is now OWNED by the TARGET pose rate_half_list_adjacent_crossing (the w9-C3 repair vehicle); the exact-integer Johnson anchor is PROVED; the list crossing is DETERMINED for budgets B* in {1,2} at a_L = 3n/4; the proved unsafe reach doubles to excess 2^34-1.
