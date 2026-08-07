# L1 FPC5 large-source payment

- **status:** TARGET
- **consumer:** `l1_full_petal_fpc5_payment`

After the official small-source sieve, the remaining large source scales are

```text
rate 1/2:   M>=5,
rate 1/4:   M>=5,
rate 1/8:   M>=7,
rate 1/16:  M>=15.
```

Every cell satisfies

```text
2<=t<2M-4,       d<ell(M-2),
max(0,2d+1-t ell)->infinity.
```

The target is one disjoint polynomial/profile allocation across first-owned
sources, touched-petal sets, defects, and exact owners. Raw enumeration of
sources or touched subsets is not an admissible payment.

## Round-23 diagnosis addendum (2026-08-07, coordinator-applied on replay: fpc5_diag)

**CLASSIFICATION: MYSTERY-HARD, and the LEAST DEFENDED of the three
FPC5 reds** (the registered exposure test FIRED as pre-registered —
an exposure, not a witness; the partition stands). Same wall (MF)
plus two missing pieces the m4 reds already have: (i) NO mu-basis /
overlap-cap theorem exists for t >= 4 (the three-petal theorems do
not generalize as stated; even the Johnson functional J is
undefined there); (ii) NO background-guard analogue at M >= 5.
Exact facts established: t <= M always (so the rate-quarter
uniqueness template applies exactly on the t = M, b <= 1 stratum
and nowhere else); touched-subset multiplicity is FREE
(binom(M,t) <= n^{1/c_0} by the layout-domination cutoff — the
attack note's first line aims at a non-obstruction); the exact
Johnson sieve at k = 2^40 leaves **408 residual rows** across the
four rates (all t at M >= 10), with e reaching n/3 — e.g. rate
1/2, M = 5, t = 2: a residual d-window of width 3.48e11.

**THE NAMED GATE (cheapest decisive probe):** prove the t-petal
overlap-cap lemma — for distinct primitive members of the t-petal
slice, |Z(F) cap Z(F')| <= e - 1 (the cofactor/syzygy determinant
argument, PROVED verbatim at t = 2 and t = 3). The moment it
lands, the entire J-sieve becomes legal and removes every
t < M, J > 0 cell at a stroke; the sieve table is already computed
and waiting (fpc5_exact.py). Second: port the m4_t2
background-guard collapse to general M — the codim = sigma
identity predicts the answer in advance.
Source: notes/pilots_20260807/fpc5_diag/.
