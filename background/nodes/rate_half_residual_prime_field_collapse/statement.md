# Rate-half residual prime-field collapse

- **status:** PROVED
- **closure:** proof plus exact integer certificate
- **consumer:** `rate_half_band_closure`
- **dependency:** `rate_half_ca_hankel_minimal_index_budget`

Let

```text
N=2^41,       q=p^f,
B=floor(q/2^128) in {2^39,2^39+1},
N divides q-1,                                            (RPFC1)
```

where `p` is prime and `f>=1`. Then

```text
f=1.                                                      (RPFC2)
```

Thus every field in either unresolved rate-half residual budget is a prime
field. In particular,

```text
p=q>2^167>N,                                              (RPFC3)
```

so the characteristic exceeds the evaluation-domain size and every degree
in the Hankel and pair-Lagrange reductions.

Before the exact finite exclusion, LTE already forces

```text
f in {1,2,3,4},                                          (RPFC4)

f odd  ==> p=1 mod 2^41,
f=2    ==> p^2=1 mod 2^41,
f=4    ==> p^4=1 mod 2^41.                               (RPFC5)
```

For `f=2`, the two budget intervals contain respectively `24` and `22`
integers satisfying `(RPFC5)`; every one has the nontrivial divisor printed
in `quadratic_candidate_factors.tsv`. For `f=3` and `f=4`, neither interval
contains any integer in an admissible residue class. These statements are
complete exact interval censuses, not probable-prime tests.

## Round-31 addendum (2026-08-10, coordinator): the contrapositive, stated

(RPFC2) read contrapositively is a SEPARATION theorem, nowhere
previously stated in-repo: **on the admissible family (N = 2^41 |
q-1, q = p^f < 2^256), f >= 2 implies B = floor(q/2^128) is NOT in
{2^39, 2^39+1} — every admissible extension row lies OUTSIDE
[2^167, 2^167 + 2^129).** Independently verified by direct census
(round-31 rh_e_axis_audit, d2b replayed by the coordinator): 46
integer candidates at e = 2 in the window, 0 at e in {3,4,5,6},
0 of the 46 prime. Consequence of record: the residual-budget
window — the sole territory of the A=1/A=3 exceptional core and of
the only primality-using instrument in the band chain (the Legendre
router) — contains no extension rows; the e-axis widening of the
RH-AC pose cannot import an extension row into prime-field
machinery. STRATUM LEMMA riding with this addendum (replayed): for
n = 2^41 | q-1, 2^167 < q = p^e < 2^256: e in {1,2,3,4,5,6} exactly
(LTE + the cap), q odd, and p > n = 2^41 always (the only e with a
sub-2^41 congruence floor is e = 6, whose three candidates
2^40-1, 2^40+1, 2^41-1 are all composite) — so (RPFC3)'s
load-bearing consequence (char exceeds the domain size and every
reduction degree) holds on the whole widened family with primality
never needed. Mint candidate: this addendum as a background node.
