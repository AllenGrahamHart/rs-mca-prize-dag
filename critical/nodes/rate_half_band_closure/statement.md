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
