# Proof

Notation as in `statement.md`. **Inputs consumed, not re-derived**
(hard law 5):

- **(L1)** `dim C_S = |S|-K` and `dim(C_S ^ C_T) = max(0, |S^T|-K)` —
  `background/nodes/xr_two_slope_cost_theorem/proof.md:7-23`.
- **(L2)** `RS_K x RS_K` lies in the kernel of every condition row, and a
  non-degenerate realisation forces `rank <= 2(n-K)-1` —
  `background/nodes/xr_two_slope_cost_theorem/proof.md:96-108`.

Both are recapped in one line each below, at the point of use, so this
file reads standalone; neither is re-proved.

## Claim 0 (Lemma 0: transversality — CORRECTED)

By L1, `C_{S_a} ^ C_{S_b} = C_{S_a ^ S_b}`, of dimension
`max(0, |S_a ^ S_b| - K)`. Hence

```text
C_{S_a} ^ C_{S_b} = 0    <=>    |S_a ^ S_b| <= K.
```

Spreadness is `|S_a ^ S_b| <= K - 1`, which is strictly stronger. So
**spread implies pairwise transversality, and the converse fails exactly
on the core-`K` stratum.** QED (0)

**CORRECTION TO THE RECORD (flagged, not silently adopted).** The P-B
lane states this as an equivalence: "spread <=> pairwise-transverse
condition spaces (dual distance K+1)" (`pb_h4_hunt/REPORT.md:29`). As
written that is one-directional. The discrepancy is exactly the pairs at
core `= K`, which the P-B budget puts in `Gamma_hi`, not `Gamma_lo` — so
the distinction is load-bearing for the lane and must not be quoted
loosely. The verifier exhibits explicit core-`K` transverse pairs. Note
that **nothing downstream in this node uses the false direction**:
Claim 1 needs only independence, which is stronger than transversality
anyway.

## Claim 1 (THEOREM 1: the ceiling)

**Recap of L2 (consumed).** For `f, g in RS_K` and `c in C_S`,
`<c, f> = 0` by definition of the shortened dual; every condition row is
`(c, zc)` with `c in C_S` for some `S`; so `(f,g)` satisfies every row.
Hence `RS_K x RS_K` (dimension `2K`) lies in the kernel of the whole
system. If the family is realised by some `(u,v) NOT in RS_K x RS_K`,
the kernel strictly contains `RS_K x RS_K`, so

```text
2n - rank >= 2K + 1,    i.e.    rank <= 2(n-K) - 1 = 2r - 1.
```

**The ceiling.** The row space of the family is
`sum_{a=1..M} G_{z_a}(C_{S_a})`. By hypothesis the family is
INDEPENDENT, i.e. this sum is direct with
`dim G_{z_a}(C_{S_a}) = dim C_{S_a} = h` (L1), so

```text
rank = M h.
```

Combining, `M h <= 2r - 1`, i.e. `M <= (2r-1)/h`, and since `M` is an
integer, `M <= floor((2r-1)/h)`. QED (1)

**Six-row arithmetic.** With `r = n-K` at the pinned rows (RowC
`n = 1024`, `K = 256/128/64`, `h = 5/5/3`; prize `n = 2^41`,
`K = 2^39/2^38/2^37`, `h = 2^33+1/2^33+1/2^32+1`):

```text
floor((2r-1)/h) = 307 / 358 / 639   (RowC)   and   383 / 447 / 959   (prize).
```

All six recomputed as exact integers by the verifier. These are the same
integers as the banked node's per-RAY column
(`xr_two_slope_cost_theorem/proof.md:133`) — as they must be: a P-B
witness `(z,S)` **is** a ray. The P-B content is the gauge (single
supports, spread families) and what follows next.

## Claim 2 (COROLLARY: forcedness)

Let `F` be a family realised non-degenerately with `|F| > 8n^3` members
(a P-B counterexample). Choose a maximal INDEPENDENT sub-family
`F_0 <= F` — i.e. a basis-like selection whose row blocks are
independent; every remaining member's block lies in the span of `F_0`'s
(that is what maximality means), so those members are **forced**: their
witness conditions are implied by `F_0`'s. `F_0` satisfies Claim 1, so

```text
|F_0| <= floor((2r-1)/h)  <=  959      (max over the six rows),
```

and therefore

```text
|F_0| / |F|  <  960 / 8n^3.
```

At the six rows `8n^3 = 2^33` (RowC, `n = 1024`) and
`8 (2^41)^3 = 2^126` (prize). The worst (largest) ratio is at RowC
`1/16`, where `639 / 2^33 = 2^-23.68`. Hence every P-B counterexample is
at least `1 - 2^-23.68 > 1 - 2^-23` **forced**. QED (2)

Per-row bit margins `lg(8n^3) - lg(floor((2r-1)/h))`:
`24.74 / 24.52 / 23.68` (RowC), `117.42 / 117.20 / 116.09` (prize).
*(The pilot quotes `2^23.1 .. 2^117.4`, computed from the FREE-slope
ceiling `383/447/959` — on the RowC triple those are
`24.42 / 24.20 / 23.09`. Under the PROVED prescribed form the margins are
the slightly better numbers above; the prize triple is unchanged because
`h` is so large there that the two ceilings coincide. Both readings give
"`<= ~960` designable" and "`>= 1 - 2^-23` forced". See AUDIT_CHECKLIST
F3.b.)*

## Claim 3 (THEOREM 2: the free-slope form is not proved)

With the slope of each witness left free, the condition on `(u,v)` is
that the `2 x h` syndrome matrix `[sigma_{S_a}(u); sigma_{S_a}(v)]` has
rank `<= 1`. That is `h-1` determinantal equations (the `2 x 2` minors),
not `h` linear ones. Counting naively, `M` witnesses cost `M(h-1)`
conditions and the same argument as Claim 1 would give
`M <= (2r-1)/(h-1)`.

**The gap.** This step needs the `M` determinantal loci to meet
PROPERLY (codimensions adding). That is a general-position assumption of
exactly the type Claim 4 refutes: the `mu_n`-orbit family has `M = 20`
witnesses with free slopes at `n = 20, K = 4, h = 3`, where
`(2r-1)/(h-1) = 15`. So the naive count is false for that family, and no
argument in the record repairs it. The source itself writes "the true
ceiling **SHOULD** be" (`pb_h4_hunt/expC.py:352-364`) and "the
determinantal count" (`:19-21`).

**Book-keeping note (subtraction).** The banked node's proved table has
`floor((2r-1)/(2h-2)) = 191/223/479` on both triples — the per-DATUM
free-slope form, a datum being an unordered pair of rays. Per SUPPORT
that would read `2 * 191 = 382`, whereas `floor((2r-1)/(h-1)) = 383`.
The two integers differ; the per-support form is not a corollary of the
banked per-datum entry. Recorded, not claimed. QED (3, as a
non-claim)

## Claim 4 (THEOREM 3: the refutation)

Take `q = 41`, `D = mu_20 <= F_41^*` (`20 | 40`), `K = 4`, `h = 3`,
`A = 7`, `r = 16`, `2r = 32`. Let

```text
U = X^7,   V = -X^6,    u_i = x_i^7,   v_i = -x_i^6   (x_i in D).
```

**Invariance.** For `omega` a primitive 20th root of unity, the
substitution `x -> omega x` scales `u` by `omega^7` and `v` by
`omega^6`. A support `S` is a witness at slope `z` iff
`(u + zv)|_S in RS_K|_S`; applying the substitution, `omega S` is a
witness at slope `omega z`... — the precise statement the verifier
establishes (and all this proof needs) is the **machine fact**: the
witness set is closed under the index shift `i -> i+1 (mod 20)`, so it is
a union of `mu_20`-orbits.

**The exhibit.** Scanning **all** `C(20,7) = 77,520` supports
exhaustively (the verifier does this from scratch):

- the witness set has `40` members with `40` distinct supports, splitting
  into `2` full orbits of size `20`;
- one full orbit is **spread**: its maximum pairwise core is `3 = K-1`,
  so `Gamma_lo` contains all `20` of its members and there is **zero
  self-collision**;
- that orbit carries `20` **distinct** slopes;
- its condition system has `M h = 20 * 3 = 60` rows of rank exactly
  `31 = 2r - 1`, so `2n - rank = 40 - 31 = 9 > 2K = 8`: the kernel
  strictly contains `RS_K x RS_K` and the family IS realised
  non-degenerately (by the very pair `(u,v)` it was built from).

Hence `M = 20` with `Mh = 60 > 31 = 2r-1`: Claim 1's conclusion fails,
so its hypothesis must fail — the family is NOT independent (deficit
`60 - 31 = 29`). Both ceilings (`10` prescribed, `15` free) are
exceeded by a **realised, spread, zero-collision** family. QED (4)

**Consequences recorded (not claimed).** "Rank deficit forces
self-collision" is FALSE. Symmetry buys deficit, not excess: this class
produces `40` witnesses against a mean supply `C(n,A)/q^{h-1} = 46.115`,
i.e. **deficit without excess** (`pb_h4_hunt/REPORT.md:14`).

## Honest scope

- Claims 1 and 2 are linear algebra plus exact integer arithmetic, valid
  at every scale. Claim 4 is a single exhibit, verified exhaustively at
  its own shape; its role is to refute a universal statement, for which
  one exhibit suffices.
- Every number quoted from the pilot record was **re-derived from
  scratch** in `verify.py` and cross-checked against the persisted
  checkpoints (`EXPC_lemma/rank/orbit/extend.json`, `OFFICIAL.json`),
  never against prose alone. The single exception is the pilot's
  official-scale `nu`/selector arithmetic, which this node does not use
  and does not restate.
- What this node does **not** attempt: the non-split-fibre concentration
  half of (H4); the RowC 1/4 q-scope decision; the word-model exhaustive
  search (out of reach — `REPORT.md:57`).
