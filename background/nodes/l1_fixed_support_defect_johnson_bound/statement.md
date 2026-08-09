# L1 fixed-support defect Johnson bound

- **status:** PROVED
- **role:** pay every positive-Johnson exact support cell
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Fix one maximal-sunflower source chart. Let its ordered core be `C`, with

```text
N=|C|=k-1.
```

Let the chart have background capacity `0<=b<ell` and put
`g=ell-b>=1`. Fix one exact labelled petal-support pattern `X`, disjoint from
`C`, and put `h=|X|`. The list threshold gives `h>=d+g`. Let `Z` be the exact
saturated pairs compatible with this pattern:

```text
F=L_D monic,       D subset C,       |D|=d,
deg W<=d,          gcd(F,W)=1,
W(x)=alpha(x)F(x)  for every x in X.                       (JB1)
```

Define

```text
r_J=2d-h,       e=max(0,r_J+1).                            (JB2)
```

Then:

1. if `r_J<0`, then `|Z|<=1`;
2. if `r_J>=0`, the defect sets of two distinct members satisfy

   ```text
   |D_1 intersect D_2|<=r_J;                               (JB3)
   ```

3. whenever the Johnson denominator is positive,

   ```text
   d^2-N r_J>0,
   ```

   one has the field-independent bound

   ```text
   |Z|<=N(d-r_J)/(d^2-N r_J).                              (JB4)
   ```

For every fixed petal-polarity cap `p<=P`, the union of all cells satisfying
the positive-denominator condition is polynomial per source chart. An
explicit bound, after summing support patterns and defect degrees, is

```text
(P+1)n^(1/c_0+P+3).                                       (JB5)
```

Consequently, a bounded-polarity per-chart counterfamily may be restricted
to the sub-Johnson tail

```text
e>=1,       N(e-1)>=d^2.                                  (JB6)
```

Since `h>=d+g`, this tail also satisfies

```text
d^2<=N(d-g),       g=ell-b.                               (JB7)
```

It is empty when `g>N/4`; otherwise `d` lies between the two real roots of
`d^2-Nd+Ng`.

## Scope

This is a per-source-chart exact-support payment. It does not count the
nonpositive-denominator tail, sum non-intrinsic first-match charts, or handle
unbounded petal polarity. It uses exact defect and saturation essentially.

## Round-24 addendum (2026-08-08, coordinator-applied): (JB3) IS the t-petal overlap cap; two extensions drafted

Put h = t*ell: (JB3) is the t-petal overlap-cap lemma verbatim
(|D_1 cap D_2| <= r_J = e-1) and (JB4)'s denominator is the FPC5
J-sieve functional — this node legalizes the large-source sieve at
every t (see the round-24 correction on
l1_fpc5_large_source_payment). Two coordinator-replayed extensions
drafted at notes/pilots_20260808/t_petal_lemma/ (mint candidates):
(a) the X-disjoint-from-C hypothesis is FREE for primitive members
(gcd(F,W) = 1 forbids petal roots; machine-checked, 5671 members,
360 overlapping configs, 0 exceptions); (b) THE SLICE-DIMENSION
THEOREM: dim V = e+1 exactly at every t (kernel-line argument, no
syzygy rank; machine-checked 391 cells, 155 saturated, 0
exceptions).

## Round-25a addendum (2026-08-09, coordinator-applied on replay: the pr_harvest crosswalk + a new corollary)

**COROLLARY (ours, one line, not previously written):** with the
list threshold h >= d + g, d < g forces r_J = 2d - h <= d - g < 0,
hence |Z| <= 1 — per-pattern UNIQUENESS, field-independent,
ell-uniform, every chart.

**THE S_tau <-> h CROSSWALK (#1146 harvested as a complement, with
the standing citation discipline: "for the two parity supports",
never "for ell=11 exact-five"):** in the ell=11 exact-five family,
upstream's S_tau envelope is exactly the envelope of this node's
petal-agreement h (their own auditor computes S_h as the sum of the
h largest fibre values). Composed on their tau = 6 rows: their
S_6 <= 20 forces d <= 9 < 11 = g, so THIS node's corollary gives
per-pattern uniqueness outright; their theorem deletes exactly the
d in [11,19] tail where this node's functional is weak-or-vacuous.
NOT domination in either direction — exact complementarity, newly
visible only because (JB3)/(JB4) became the legal every-t sieve
(round 24). CAVEAT of record: the identification of their
coset-sunflower members with (JB1)'s (F, W) pairs is a CANDIDATE
chart mapping (deg W <= d and the labelling unverified);
primitivity DOES transfer (their note asserts primitive anchors).
Theorem J proper (the balanced clause) MISSES all ten of their
rows (clause 1 reduces to tau < 2; clause-2 deficits -2057 to
-7139) — confirming and extending the banked 08-07 domination
check. Source: notes/pilots_20260809/pr_harvest/ (jcheck
replayed; their parity auditor replayed PASS).
