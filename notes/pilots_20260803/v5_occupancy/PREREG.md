# Pre-registration (written BEFORE any computation), 2026-08-03

Pilot: **the `V >= 5` zero-escape occupancy question**. Anchor:
`notes/pilots_20260803/zero_escape_collapse/REPORT.md` section 9 item 4 +
`FABLE_AUDIT.md` "Surfaced decisions"; channel (i) of the re-posed heart
(`notes/BAND_LANE_DEFINITIONS.md` addenda 2 and 3).

**Question.** For `V >= 5` ray systems that are zero-escape,
pairwise-intersecting (`|S_a ^ S_b| >= k+1`), k-packing-gated
(`(T)`: all triples `<= k-1`), and BELOW the Corollary-3b kill threshold
(`(V-3)t + |A_0| <= k-1`): does `rank >= 2V` (per-ray charge `>= 2`)
always hold?

**Pre-registered falsifier (the brief's):** a system in that class with
`rank < 2V`.

Attack route: route (1) of the brief — extend THEOREM 4 to `V >= 5` by
normalising `p_1 = p_2 = 0` and counting the constraints honestly.

---

## 0. The class, parametrised (definitions fixed before running)

A **zero-escape block system** `B(V, t, t_0, k)` over `F_q`:

```text
U = A_0 |_| A_1 |_| ... |_| A_V   (disjoint),  |A_0| = t_0, |A_a| = t
S_a = U \ A_a ,  a = 1..V ,  slopes z_a in F_q pairwise distinct
|U| = t_0 + V t ,  A = |S_a| = t_0 + (V-1) t ,  h = A - k ,  m = |U| - k
sigma := |S_a ^ S_b ^ S_c| = t_0 + (V-3) t   (same for every triple)
e := k - sigma
```

This is the shape in which Corollary 3b's threshold is stated ("block
systems"), and it is the strongest form of zero escape: every point has
multiplicity `V-1` or `V`, so zero escape is automatic for `V >= 4`.

**Derived identities (claimed here, to be machine-checked):**

```text
m = t + h ,        e = 2t - h ,        2m - 3h = e
pairwise |S_a ^ S_b| = k + (h - t)  ->  ">= k+1"  <=>  h >= t+1
gate (T)  sigma <= k-1              <=>  e >= 1   <=>  h <= 2t-1
```

so the admissible parameter set is exactly

```text
t >= 2 ,   t + 1 <= h <= 2t - 1 ,   t_0 >= 0 ,   V >= 4 ,
k = t_0 + (V-1)t - h            (determined by the rest)
```

Note `V` is **unconstrained** by the gates.

## 1. The theory, stated before any computation

**Normalisation.** Subtract `(P + z_a Q)` to force `p_1 = p_2 = 0`
(solvable, `z_1 != z_2`, `deg < k`; the normalised representative is
unique). Then on `S_1 ^ S_2 = U \ (A_1 u A_2)` both `lambda` and `mu`
vanish, so `(lambda, mu)` is supported on `A_1 u A_2`, with
`lambda = -z_2 mu` on `A_1` and `lambda = -z_1 mu` on `A_2`. Writing
`nu := mu|_{A_1 u A_2}`, for every `a >= 3`

```text
p_a = 0 on A_0 u (union_{j>=3, j!=a} A_j)      [sigma points]
p_a = (z_a - z_2) nu on A_1 ,  p_a = (z_a - z_1) nu on A_2
```

and conversely any such family is an annihilator. `Ann ~ {valid nu}`.

**PREDICTION T-B (injectivity floor).** `p_3` alone determines `nu`
(hence `Ann`), and `p_3` lies in a space of dimension `(k - sigma)^+`,
so

```text
dim Ann <= e = 2t - h  and  rank >= 2m - e = 3h .
```

(For `V = 4` this is exactly the banked bound (*) `(k - |A_0| - t)^+`.)

**PREDICTION T-A (ceiling).** `m = t + h <= 3t - 1`, hence

```text
rank <= 2m = 2(t + h) <= 6t - 2   INDEPENDENT OF V .
```

**PREDICTION T-C (the `V >= 5` construction).** Let `<w, w'>` be a
base-point-free degree-`t` pencil and let `A_1..A_V` be `V` full fibres
with parameters `c_1..c_V` (`B_a = w - c_a w'`), `A_0` any disjoint
extra set. Put `p_a := kappa_a D prod_{j>=3, j!=a} B_j` with
`D = prod_{A_0}(X - x)`; `deg p_a = sigma <= k-1` — the below-threshold
condition is EXACTLY what makes this fit under degree `k`. Eliminating
`nu` gives ONE scalar condition per `a >= 3`:

```text
(c_a - c_1)(z_a - z_2) / [(c_a - c_2)(z_a - z_1)] = const  for all a>=3
   <=>   c_a = psi(z_a) for a single Mobius psi and ALL a = 1..V .
```

For `V = 4` this is one cross-ratio equation — the banked THEOREM 4(c)
(`CR(c_1..c_4) = CR(z_1..z_4)`). For `V >= 5` it is `V - 3` simultaneous
equations, but the slopes are FREE, so it is solvable for every `V`:
take `z_a := psi^{-1}(c_a)`. Predicted exact dimension (all `q_a`
forced proportional because `deg q_a < e <= t-1 < t = |A_a|`):

```text
dim Ann = e  if (c_a) ~ (z_a) under Mobius,   0 otherwise.
```

So the pencil-fibre family attains the floor: `rank = 2m - e = 3h`.

**PREDICTION T-D (trichotomy — the answer to the question).** In the
class `B(V,t,t_0,k)`, `3h <= rank <= 2m = 2(t+h)`, hence

```text
2V <= 3h            =>  charge >= 2 ALWAYS (proved by T-B)
2V >  2(t + h)      =>  charge <  2 ALWAYS (proved by T-A; V > m)
3h < 2V <= 2(t+h)   =>  charge >= 2 generically but FAILS on the
                        pencil-fibre family with Mobius slopes (T-C)
```

**Predicted verdicts:** (1) the collapse is FALSE at every `V >= 5`;
(2) `rank >= 2V` is FALSE at `V >= 5` — by TWO independent mechanisms;
(3) the RowC clique sits deep in the ceiling regime.

---

## 2. Pre-registered predictions and falsifiers

Fixtures (all fixed here, before running):

| id | q | t | h | t_0 | V | k | \|U\| | m | e | blocks | slopes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Y1** | 11 | 2 | 3 | 0 | 5 | 5 | 10 | 5 | 1 | fibres of `X^2` over `{1,3,4,5,9}` | `z_a = c_a` |
| **Y2** | 11 | 2 | 3 | 0 | 5 | 5 | 10 | 5 | 1 | same as Y1 | `(1,3,4,5,2)` (off-Mobius) |
| **Y2b** | 11 | 2 | 3 | 0 | 5 | 5 | 10 | 5 | 1 | non-pencil pairing | `(1,3,4,5,9)` |
| **Y3** | 13 | 2 | 3 | 0 | 6 | 7 | 12 | 5 | 1 | non-pencil pairing | `(1,2,3,4,5,6)` |
| **Y3'** | 13 | 2 | 3 | 0 | 6 | 7 | 12 | 5 | 1 | fibres of `X^2` over the 6 squares | `z_a = c_a` |
| **Y4** | 41 | 4 | 5 | 1 | 10 | 32 | 41 | 9 | 3 | fibres of `X^4`, `A_0={0}` | `z_a = c_a` |
| **Y5** | 269 | 4 | 5 | 1 | 66 | 256 | 265 | 9 | 3 | 66 fibres of `X^4`, `A_0={0}` | `z_a = c_a` |
| **Y6** | 269 | 4 | 5 | 1 | 66 | 256 | 265 | 9 | 3 | same as Y5 | one slope moved off-Mobius |

**Y5 is the RowC 1/4 clique's recorded shape EXACTLY**
(`|U| = 265, k = 256, |A_a| = 4, V = 66`, triples `253`, and hence
`h = 5, m = 9, e = 3`).

* **Q1 (the `V = 5` counterexample).** Y1 is gate-clean
  (`|S_a| = 8`, pairwise `= 6 = k+1`, triples `= 4 = k-1`, zero escape,
  4-wise `= 2`), `dim Ann = 1`, `rank = 9 = 3h = 2m - 1 < 10 = 2V`.
  Per-ray charge `1.8`.
  FALSIFIER: `rank = 10`, or any gate off these numbers.
* **Q2 (Mobius is the exact criterion, `V = 5`).** Y2 (same supports,
  off-Mobius slopes) has `dim Ann = 0`, `rank = 2m = 10 = 2V`. Y2b
  (non-pencil supports, on-parameter slopes) has `dim Ann = 0`,
  `rank = 10`.
  FALSIFIER: either has `dim Ann != 0`.
* **Q3 (exact slope locus).** For the Y1 supports, sweeping ALL slope
  tuples with `z_1 = 0, z_2 = 1` (affine normalisation), the set with
  `dim Ann > 0` is EXACTLY `{(psi(c_a))_a : psi in PGL_2(F_11),
  psi(c_1)=0, psi(c_2)=1, all values finite and distinct}`. Same for a
  sample of other pencil pairings; for NON-pencil pairings the set is
  EMPTY over the whole sweep.
  FALSIFIER: any off-locus tuple with `dim Ann > 0`, any on-locus tuple
  with `dim Ann = 0`, or any non-pencil pairing with `dim Ann > 0`.
* **Q4 (the ceiling counterexample — no annihilator needed).** Y3 has
  `dim Ann = 0` and `rank = 2m = 10 < 12 = 2V`: a **collapsing**
  gate-clean system that still violates charge 2. Y3' has
  `dim Ann = 1`, `rank = 9 = 3h < 12`.
  FALSIFIER: `rank > 10` at Y3 (impossible if `rank <= 2m` holds), or
  Y3 failing a gate.
* **Q5 (RowC invariants at verifiable size).** Y4: `dim Ann = 3`,
  `rank = 15 = 3h`, `2m = 18`, `2V = 20`; so `rank < 2V` and even the
  collapse value `2m` is `< 2V`. Charge `1.5`.
  FALSIFIER: `dim Ann != 3` or `rank != 15`.
* **Q6 (the RowC clique's own shape).** Y5: `dim Ann = 3`,
  `rank = 15 = 3h`; Y6: `dim Ann = 0`, `rank = 18 = 2m`. Both are
  astronomically below `2V = 132`.
  FALSIFIER: either rank off its predicted value.
* **Q7 (reformulation lemma, used to reach `V = 66`).** With
  `B_a = prod_{x in A_a}(X - x)`, `rank(Row) = dim span
  {(B_a X^i, z_a B_a X^i) : a = 1..V, 0 <= i < h}` inside
  `F_q[X]_{<m}^2`. Verified against the banked brute-force
  `rank_row` on every small fixture.
  FALSIFIER: any disagreement.
* **Q8 (retro-explanation of the banked deficits).** The banked
  counterexamples X1/X2/X3 have `e = k - sigma = 1, 1, 2` and
  `rank = 3h = 9, 21, 12` — i.e. the previously MEASURED deficits
  (flag F6 of the collapse pilot: "no deficit bound beyond (*)") are
  exactly `e`, and their ranks are exactly `3h`.
  FALSIFIER: any mismatch with the banked table.
* **Q9 (arithmetic of T-A/T-B/T-D).** Over all admissible
  `(t, h, t_0, V)` in a box (`t <= 12`, `t_0 <= 12`, `V <= 40`):
  `m = t+h`, `e = 2t-h >= 1`, pairwise `= k+h-t >= k+1`,
  `sigma = k-e <= k-1`, `3h <= 2m`, and `V > m` is admissible for every
  `t, h` (so the ceiling refutation is not a small-parameter accident).
  FALSIFIER: any admissible tuple violating an identity.
* **Q10 (`V = 5` general zero escape, not just blocks).** For `V = 5`,
  zero escape forces `U = S_a u S_b u S_c` for every triple, hence
  `m <= 3h - 4` by inclusion-exclusion with pairwise `>= k+1` and
  `(T)`. Checked on random `V = 5` zero-escape systems.
  FALSIFIER: a `V = 5` gate-clean zero-escape system with `m > 3h - 4`.

## 2b. Addendum, same session, STILL BEFORE ANY COMPUTATION

Added after reading the record for how the RowC kill consumes the
collapse (`notes/pilots_20260802/support4_relation/stage5_escape.py`
section D + `.json`, `background/nodes/xr_support4_structure/proof.md`
:140-145). No computation of my own has been run at this point; the two
predictions below are therefore also pre-registered.

The record's escape-clique model is `u = k + 2h - d`,
`Vmax = u // (h - d)`, `m = 2h - d`, `charge = 2m / Vmax`, and the
"secondary exact criterion" is `charge >= 2  <=>  k <= 2h^2` (recorded
`k <= 2h^2 - 5h + 2`).

* **Q11 (the record's clique model IS this class).** That model is
  exactly `B(V, t, t_0, k)` with `t = h - d`; i.e.
  `m = t + h = 2h - d`, `e = 2t - h = h - 2d`, `Vmax = |U| / t` is the
  block-disjointness bound, and admissibility `h >= t+1`, `h <= 2t-1`
  is `d >= 1`, `h >= 2d + 1`. In particular fixture **Y1** is the
  record's own clique at `(k, h, d) = (5, 3, 1)` with `V = Vmax = 5`,
  and RowC 1/4 has `(h, d) = (5, 1)`, `t = 4`, `e = 3`, `m = 9`.
  FALSIFIER: any of these identities failing against the JSON.
* **Q12 (the secondary criterion is REFUTED, and its correction).**
  `charge = 2m/Vmax` is an UPPER bound on `rank/V`, so `2m/Vmax >= 2`
  cannot imply `charge >= 2`. Prediction: **Y1 has `k = 5 <= 2h^2 = 18`
  yet per-ray charge `1.8 < 2`** — a direct counterexample to
  "the zero-escape channel can reach per-ray charge `< 2` only when
  `k > 2h^2`". The correct criterion is the tight floor of T-B:
  `charge >= 2` is guaranteed **iff `2V <= 3h`**. Prediction on the
  consequences: at the three PRIZE rows the corrected criterion still
  holds with an enormous margin (`Vmax` is 66/34/34 while `3h/2` is
  about `1.3e10 / 1.3e10 / 6.4e9`), so the prize-row conclusion
  SURVIVES but on a different and now proved footing; at the three
  RowC rows it fails (as the record already concedes, charge ceiling
  `0.27 / 0.53 / 0.29`).
  FALSIFIER: Y1 having charge `>= 2`; or a prize row with
  `2 * Vmax > 3h`; or a RowC row with `2 * Vmax <= 3h`.

## 3. Honesty rules fixed in advance

* MEASURED != PROVED. Anything checked only on fixtures is labelled
  MEASURED; T-A, T-B, T-C, T-D are to be delivered with complete proofs
  or downgraded to MEASURED.
* The three sub-questions (collapse at `V>=5` / `rank >= 2V` at
  `V>=5` / the RowC instance) get **separate** verdicts.
* Realisability: these fixtures satisfy the **combinatorial** gates
  (the same quantification the banked X1/X2/X3 refutation used). Any
  full band-gate `(u,v)`-realisation is NOT claimed and will be
  flagged, not asserted.
* Slopes finite and pairwise distinct throughout; the `z = (0:1)` case
  is inherited from the banked section 8 argument and not swept.
* No node, `dag.json`, `critical/`, `background/` or `tools/` file is
  edited. Upstream consequences are FLAGGED only.
