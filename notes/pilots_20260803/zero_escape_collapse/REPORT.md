# Zero-escape collapse — pilot report (2026-08-03)

(Persisted verbatim by the coordinator from the pilot's final message;
the pilot's own REPORT.md write was harness-blocked. Pilot: Opus 5.)

## VERDICT: both named open sub-items are REFUTED, not proved

- **PRIMARY — the zero-escape collapse (`rank = 2m` exactly) is FALSE.**
  Explicit counterexamples X1/X2/X3: zero-escape, pairwise-intersecting,
  uniform-depth, k-packing-**saturated** ray systems with `rank = 2m-1`
  (X1, X2) and `rank = 2m-2` (X3). The 3,876 + 8,855-tuple measurement
  is *not* contradicted: it swept **slopes at fixed supports**, and the
  obstruction is a property of the **supports**.
- **SECONDARY — "non-collapsing => `V <= m/2`" is FALSE.** X1 has
  `V=4 > m/2=2.5` with `rank 9 < 2m=10`; X3 has `V=4 > 3.5` with
  `rank 12 < 14`.
- **Route (2) (duality) is what worked**, and its exact boundary is *the
  k-packing gate itself*: the duality argument closes the collapse
  **iff some triple intersection has >= k points**, i.e. iff gate (T)
  `|S_a^S_b^S_c| <= k-1` **fails**. On the gate, the collapse is false.

Falsifiers P1-P7 were pre-registered in `PREREG.md` **before** any
computation; all seven came out as pre-registered.

## 1. Notation

`Row = Sum_a G_{z_a}(C_{S_a})`, `G_z(W)={(c,zc)}`, `U=union S_a`,
`m=|U|-k`, `A_a=U\S_a`, `I_ab=S_a^S_b`, `|S_a|=A=k+h`. Zero escape =
every point of every support lies in >= 3 supports. Sections 2-6 assume
finite slopes (section 8 handles infinity). Since all `|S_a|=A`, all
blocks of a `V=4` system have one size `t`; `A_0` = points in all
supports.

## 2. THEOREM 1 (duality) — PROVED

`rank(Row) = 2m - dim Ann`, where

```text
Ann = {(lambda,mu) in (F^U)^2 : forall a exists p_a, deg p_a < k,
       lambda(x)+z_a mu(x)=p_a(x) on S_a} / (RS_k|_U)^2
```

so **collapse <=> Ann = 0**.

*Proof.* `C_U` pairs with `F^U` with radical `RS_k|_U`, so
`C_U* = F^U/RS_k|_U` has dim `m`. `(lambda,mu)` kills `Row` iff
`<lambda+z_a mu, c>=0` for all `c in C_{S_a}`. Shortening `C` at
`U\S_a` gives `C_{S_a}|_{S_a} = (RS_k|_{S_a})^perp`, so the condition
is exactly `(lambda+z_a mu)|_{S_a} in RS_k|_{S_a}`. QED

**THEOREM 1' (subspace form).** With `W := F^U/RS_k|_U` (dim `m`) and
`W_a :=` image of `F^{A_a}` (dim `|A_a|`):
`Ann = {(lambda,mu) in W x W : lambda + z_a mu in W_a forall a}`.
Projectively: a nonzero `(lambda,mu)` spans a 2-plane `P <= W`; the
condition says `P` meets every `W_a` **at the prescribed parameter
`z_a`**. Identifying `P(W) = P^{m-1}` so the classes `e_x` lie on a
rational normal curve of degree `m-1` (any `m` independent — MDS), each
`W_a` is the secant space spanned by block `A_a`. So: *the collapse
fails iff a line of `P^{m-1}` meets the block secant spaces at
prescribed parameters.*

**THEOREM 1'' (collinearity form).** If every point of `U` has
multiplicity >= 2 then `Ann ~ Z/T`,
`Z = {(p_a) in (F_q[X]_{<k})^V : forall x in U the points
(z_a,p_a(x)) over a containing x are collinear}`,
`T = {(P+z_aQ)_a}` (dim `2k`).

Checked in `verify.py` section A (38 random systems: dimensions agree
**and** every solution really interpolates to deg<k polys) and B.

## 3. THEOREM 2 (MDS-chain criterion) — PROVED => collapse

If the `I_ab` with `|I_ab| >= k` cover `U` and the graph joining
`{a,b} ~ {c,d}` when `|I_ab ^ I_cd| >= k` is connected, then
`rank = 2m`.

*Proof.* `(c,z_ac)-(c,z_bc) = (0,(z_a-z_b)c)`, so
`K := {v : (0,v) in Row} >= C_{I_ab}`. The MDS sum lemma plus the
connectivity chain give `Sum C_{I_ab} = C_U`, hence `Row >= 0 x C_U`
and `pi_1(Row) >= C_U`. QED (Dual proof: `mu` equals the deg<k poly
`(p_a-p_b)/(z_a-z_b)` on `I_ab`; two pairs overlapping in >= k points
force equality.)

**PROPOSITION 5 (improved unconditional floor) — PROVED.**
`rank = m + dim K >= m + dim Sum_{a<b} C_{I_ab}`, strictly better than
the banked `rank >= m`: floors 8/20/10 vs banked 5/11/7 on X1/X2/X3.

## 4. THEOREM 3 (triple-cover criterion) — PROVED => collapse for every slope tuple

If two rays `a,b` satisfy `|S_a^S_b^S_j| >= k` for all other `j`, then
`Ann = 0`.

*Proof.* Normalise `p_a=p_b=0` (subtract `P+z_cQ`; the 2x2 slope
system is invertible). On `I_ab`, `lambda+z_a mu = 0 = lambda+z_b mu`
=> `lambda=mu=0` there. So each `p_j` vanishes on `S_j^I_ab`, >= k
points, and `deg p_j < k` => `p_j=0`. Then `lambda+z_j mu=0` on every
`S_j`, and multiplicity >= 2 everywhere gives `lambda=mu=0`. QED

**COROLLARY 3b (block form).** `(V-3)t + |A_0| >= k => collapse, for
every slope tuple.`

**COROLLARY 3c.** The band-mint fixture `(3,5,3,5)` has all triples
`=4 >= k=3` and `(V-3)t = 4 > k-1 = 2`: **its collapse is now a
theorem, not a measurement.** (`verify.py` section E adds an
exhaustive-modulo-affine sweep of that shape over `F_11` — 504 tuples,
`rank=2m` always; section H replays the node's own 60 tuples through
the node's own `Row`/`relation_space`/`peel`, 57 non-degenerate, all
`rank=14`.)

**The sting:** both criteria need a triple intersection >= k, i.e. they
fire **only when k-packing fails**. Every fixture on which the collapse
was measured is of that kind.

## 5. THEOREM 4 (V=4: complete classification) — PROVED

With `alpha=z_4-z_2, beta=z_3-z_2, gamma=z_4-z_1, delta=z_3-z_1`,
`Delta=alpha delta-beta gamma=(z_3-z_4)(z_1-z_2) != 0`:

**(a)** `Ann ~ {(p_3,p_4) in (F_q[X]_{<k})^2 :` `p_3=0` on `A_0 u A_4`;
`p_4=0` on `A_0 u A_3`; `alpha p_3-beta p_4=0` on `A_0 u A_1`;
`gamma p_3-delta p_4=0` on `A_0 u A_2}`.

**(b)** Every nonzero solution has `p_3,p_4` independent, so
`M := span(p_3,p_4)` is a **2-dimensional pencil** of deg<k
polynomials, whose four members `w_4=p_3, w_3=p_4,
w_1=alpha p_3-beta p_4, w_2=gamma p_3-delta p_4` are pairwise
non-proportional with `w_i` vanishing on `A_0 u A_i`.

**(c)** Conversely such a pencil yields a nonzero annihilator **iff**
`CR([w_1],[w_2],[w_3],[w_4]) = CR(z_3,z_4,z_1,z_2)`,
`CR(a,b,c,d)=((a-c)(b-d))/((a-d)(b-c))`.

*Proof.* (a) Normalise `p_1=p_2=0`. For `x in A_0 u A_3 u A_4` rays
1,2 both contain `x` => `lambda(x)=mu(x)=0`, giving the first two
vanishing conditions. For `x in A_1` (rays 2,3,4), `lambda+z_2 mu=0`
=> `p_3(x)=(z_3-z_2)mu(x)`, `p_4(x)=(z_4-z_2)mu(x)` =>
`alpha p_3-beta p_4=0` at `x`; `x in A_2` similarly with `z_1`.
Converse: a solution defines `(lambda,mu)` pointwise (multiplicity
>= 3, 2x2 system invertible).
(b) If `p_3=0` then `w_1=-beta p_4, w_2=-delta p_4` with
`beta,delta != 0`, so `p_4` vanishes on
`A_0 u A_1 u A_2 u A_3 = S_4` of size `k+h > k-1` => `p_4=0`;
symmetrically for `p_4=0`. If `p_4=rho p_3 != 0`, then
`alpha-beta rho` and `gamma-delta rho` cannot both vanish (else
`Delta=0`), so `p_3` vanishes on `A_0 u A_3 u A_4` plus `A_0 u A_1` or
`A_0 u A_2`, i.e. on a set containing `S_2` or `S_1` => `p_3=0`,
contradiction. Hence `dim M=2` and the directions
`[1:0],[0:1],[alpha:-beta],[gamma:-delta]` are pairwise distinct.
(c) In the affine coordinate `tau=u/s` on `P(M)`: `tau_4=0,
tau_3=infty, tau_1=-beta/alpha, tau_2=-delta/gamma`, so
`CR(tau_1,tau_2,tau_3,tau_4)=tau_2/tau_1
=((z_3-z_1)(z_4-z_2))/((z_3-z_2)(z_4-z_1))=CR(z_3,z_4,z_1,z_2)`.
Conversely set `p_3:=w_4, p_4:=c w_3`; `c` can be chosen to satisfy
the first equation, and the second is then exactly the (c-independent)
cross-ratio equality. QED

This is the **dual-side analogue of the banked S4-4 Mobius
criterion**: there the slope cross-ratio matches the four dual classes
in `P(L)`; here it matches the four **pencil directions of the
annihilator**.

**Injectivity bound (used by PROP 6):** each of `p_3,p_4,w_1,w_2`
alone determines the solution, and `w_i` vanishes on `A_0 u A_i`, so
`dim Ann <= (k - |A_0| - t)^+`.  (*)

### 5.1 The counterexample family (construction)

Let `M=<w,w'> <= F_q[X]_{<k}` be base-point-free, i.e. a degree-`t`
map `phi=(w:w') : P^1 -> P^1` with `t <= k-1`. Take four distinct
**full fibres** `A_1..A_4` with pencil parameters `c_1..c_4`; set
`U = disjoint union A_i`, `S_i=U\A_i`, and solve

```text
R_1=(c_3-c_1)/(c_4-c_1),  R_2=(c_3-c_2)/(c_4-c_2)
z_1=1/(1-R_2),  z_2=1/(1-R_1),  z_3=0,  z_4=1
(then translate; rank is PGL_2-invariant)
```

These `z_i` are automatically finite and distinct. If `2t >= k+1` the
system is zero-escape, pairwise-intersecting of uniform depth
`d=2t-k >= 1`, all triples `= t <= k-1` (**k-packing saturated, not
violated**), and `rank <= 2m-1`. Feasibility `(k+1)/2 <= t <= k-1` is
nonempty for every `k >= 3`; e.g. `M=<X^t,1>` when `t | q-1`,
`q-1 >= 4t` (for `t=2` the blocks are the orbits of an involution of
`P^1`).

| fixture | q | k | t | h | V | \|U\| | m | Vh | 2m | **rank** | deficit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **X1** `<X^2,1>` | 17 | 3 | 2 | 3 | 4 | 8 | 5 | 12 | 10 | **9** | 1 |
| **X2** `<X^4,1>` | 17 | 5 | 4 | 7 | 4 | 16 | 11 | 28 | 22 | **21** | 1 |
| **X3** `<X^3,1>` | 13 | 5 | 3 | 4 | 4 | 12 | 7 | 16 | 14 | **12** | 2 |

X1 in full: `U={1,16,6,11,2,15,5,12} <= F_17` (fibres of `x^2` over
`c=1,2,4,8`), `S_i=U\A_i`, slopes `(12,8,2,3)`. The verifier extracts
the annihilator, normalises it and **certifies** `p_3 ~ X^2-8`,
`p_4 ~ X^2-4`, `E_1 ~ X^2-1`, `E_2 ~ X^2-2` — four members of
`<X^2,1>` — with `CR(c)=CR(z_3,z_4,z_1,z_2)=11`.

### 5.2 Why the measurement could not see it

- **Slope sweeps are blind to it.** With X1's supports fixed, an
  exhaustive sweep modulo the affine group drops the rank on **exactly
  14 tuples — precisely the cross-ratio locus** of THEOREM 4(c). Slope
  codimension 1, exactly as in S4-4.
- **CONTROL.** Identical combinatorial shape (`k=3, V=4`, blocks of 2,
  `q=17`) with *consecutive* evaluation points — blocks not fibres of a
  common degree-2 pencil — has `rank = 2m` for **every** slope tuple,
  exhaustively modulo the affine group.
- The record's two exhaustively swept fixtures
  (`k=9,V=4,|U|=16,|A_i|=3,|A_0|=4` and `k=11`) are **not** covered by
  THEOREM 3 (triples `=7 < k=9`); their collapse is exactly the
  statement that those blocks are not four fibres of a pencil of degree
  `<= k-1-|A_0|` — a **support** property a slope sweep cannot see.

## 6. PROPOSITION 6 (the occupancy floor survives at V=4) — PROVED

For `V=4`, zero escape, equal supports, pairwise `|I_ab| >= k+1`,
k-packing `<= k-1`: `t >= 2` and
`rank >= 2m - (k-|A_0|-t)^+ >= min(3t+3, 4t+2) >= 9 > 8 = 2V`.

*Proof.* `t_0+2t >= k+1` (pairwise) and `t_0+t <= k-1` (k-packing)
give `t >= 2` and `k <= t_0+2t-1`. By (*),
`rank >= 2(t_0+4t-k) - (k-t_0-t)^+`; if `k-t_0-t >= 0` this is
`3t_0+9t-3k >= 3t+3`, else it is `2m >= 4t+2`. QED (Machine-checked
over all **1,575** admissible `(k,|A_0|,t)` with
`k<=30, |A_0|<=30, t<=15`.)

So the refutation does **not** kill the occupancy heart — it kills the
two named routes to it. X1/X2/X3 have per-ray charges
**2.25 / 5.25 / 3.00**, all >= 2. This directly answers flag 5 of the
round-7 addendum: the *escape-0 channel cannot defeat charge 2 at
V=4*.

## 7. Exact boundary (honesty)

- The duality route closes the collapse **exactly when some triple
  intersection has >= k points** — i.e. exactly when gate (T) fails.
  Under the gate the collapse is false.
- The pairwise threshold `>= k` vs `>= k+1` is **not** the boundary:
  X1/X2/X3 all have `|I_ab| >= k+1` (depths 1, 3, 1). Strengthening
  pairwise does not restore the collapse.
- `V` is a boundary: for `V >= 5` complete block systems, COROLLARY 3b
  kills the annihilator once `(V-3)t+|A_0| >= k` — which is why the
  record's `V=5` fixture collapses for every slope tuple. For `V >= 5`
  with `(V-3)t+|A_0| <= k-1` the question is **open**; THEOREM 4 is a
  `V=4` classification only.
- `dim Ann` is **not** bounded by 1 (X3 has deficit 2); no deficit
  bound is claimed beyond (*). Deficit values are MEASURED; THEOREMS
  1-4 and PROPS 5-6 are proved.

## 8. Infinite slope

With `e(z_a)=(s_a,t_a)` pairwise independent, THEOREM 1 reads
`(s_a lambda+t_a mu)|_{S_a} in RS_k|_{S_a}` and all proofs go through
verbatim (only pairwise independence was used; cross-ratios are
`P^1`-valued). All sweeps used finite slopes.

## 9. Upstream consequences / next targets

1. `xr_support4_structure` **claim 7 must be restated**: the collapse
   is false in general; what is true is THEOREMS 2/3 + COR 3b (which
   cover every fixture the node cites) plus the THEOREM 4
   classification. The node's PROVED claims 1-6, 8 are untouched —
   nothing depended on claim 7. Its falsifier list already anticipated
   this find.
2. The **T3-type consequence** ("at `rank=2m` any realising pair is
   jointly explained on the union — a single deep pair, not a family")
   **does not follow from zero escape alone**; it needs a collapse
   certificate.
3. **Highest-value follow-up:** the record's "at the RowC toy rows
   `k > 2h^2` holds and THE COLLAPSE is the load-bearing kill there"
   is now **unsupported**. The RowC 1/4 clique has
   `|U|=265, k=256, |A_a|=4, V <= 66`; THEOREM 3 needs triples >= 256
   and gets >= 253 — **it misses by 3**. That row now rests on
   `V >= 5` support conditions that are open.
4. Strike "non-collapsing => `V <= m/2`". Its role is better served by
   PROP 6 and its `V >= 5` analogue — the natural next target:
   *`V >= 5` zero-escape + pairwise-intersecting + k-packing =>
   `rank >= 2V`?* Pre-registered falsifier: such a system with
   `rank < 2V`. (The pencil family never produces one: it always gives
   `rank >= 3t+3`.)
5. New unconditional tool: PROP 5's floor
   `rank >= m + dim Sum C_{I_ab}`.

## 10. FLAGS

- **F1 (upstream status change).** `xr_support4_structure` claim 7 is
  REFUTED as a general statement; needs a dated addendum. I edited
  **no** node, `dag.json`, `critical/`, `background/` or `tools/` —
  surfaced, not applied.
- **F2 (a consumer loses its support).** Any argument citing "the
  collapse" as the load-bearing kill at the RowC toy rows is now
  unsupported. I re-priced nothing.
- **F3 (named conjecture struck).** "non-collapsing => `V <= m/2`" is
  false; two independent counterexamples.
- **F4 (realisability unchecked).** X1/X2/X3 satisfy the
  **combinatorial** gates (sizes, uniform depth, `depth <= h-2`,
  k-packing, zero escape) — the same quantification the measured claim
  used — but I did **not** exhibit a realising `(u,v)` pair through
  the full band gate, and the fields are toy (`q=13,17`). A larger-`q`
  full-gate realisation is a COMPUTE REQUEST, not run.
- **F5 (scope).** THEOREM 4 is `V=4` only.
- **F6 (deficit).** No upper bound beyond (*); X3 shows deficit 2
  occurs.
- **F7 (external read).** `verify.py` imports
  `background/nodes/xr_support4_structure/verify.py` read-only, as
  instructed ("reuse, don't copy"). 57 of 60 tuples are non-degenerate
  — the node's own filter drops 3, matching its behaviour.
- **F8 (compute).** All under `tools/ramguard tiny`, 0.4 s. No Modal,
  no network.
- **F9 (git side-effect, not mine).** Commit `1aba2bd5` (another
  agent, 10:36) swept `PREREG.md` and the first version of `verify.py`
  into the repo; later verifier edits (PROP 5, PROP 6, renumbering)
  were uncommitted at report time.
