# Round-7 anchor: |K| (P-A1) vs the escape residual (band lane)

Pilot: Opus 5, 2026-08-03. Directory:
`notes/pilots_20260803/k_escape_unification/` (`verify.py`, `verify.json`).
Anchor pre-registered at `notes/pilots_20260802/CAMPAIGN_LEDGER.md:379`
("NEXT-ROUND ANCHOR: unify |K| with the escape residual"), sharpened by
`notes/pilots_20260802/support4_relation/FABLE_AUDIT.md:34-38`.

## VERDICT: UNIFIED AS ONE OPERATOR, SEPARATED AS SETS

Both residuals are fixed points of **one** monotone closure on ray
systems — the `(3, k+1)`-core of the ray/point incidence structure
(delete points covered `< 3` times; delete rays left with `<= k` points;
repeat). They are **not the same set**:

* the band lane's **escape residual is the FIRST iterate** of that
  operator (Theorem U1: the band peel, as written, terminates in one
  pass — the ray-death step is missing, and without it nothing further
  can happen);
* **P-A1's `|K|` is the greatest fixed point** of the same operator
  (Theorem U2: P-A1's peel *is* the full closure).

Consequently the kernel floor **dominates** the escape floor (U4) and the
domination is **strict** on explicit gate-clean fixtures (S1, S2). Both
proofs below are elementary and complete; the fixtures are machine-
verified. 18/18 checks, 0 FAIL, `ramguard tiny`.

---

## (a) The two residual objects in one notation

### Shared setting (definitions of record)

A **ray system** is `Sigma = ((z_a, S_a))_{a in V}` with `z_a` pairwise
distinct in `P^1(F_q)` and `|S_a| = A = k + h`; `C_S := {c : supp(c) <= S,
c _|_ RS_k}`, `dim C_S = (|S| - k)^+`;

```text
Rel(Sigma) = {(c_a) in (+)_a C_{S_a} : sum_a e(z_a) (x) c_a = 0},  e(z)=(1,z)
rank(Sigma) = |V| h - dim Rel(Sigma)          (per-ray accounting)
```

(`background/nodes/xr_support4_structure/statement.md:17-38`; per-ray
accounting = `notes/BAND_LANE_DEFINITIONS.md:45-48`, item 11).
**Multiplicity** `mult(x) = #{a : x in S_a}`; **triple locus**
`W = {x : mult(x) >= 3}`. Hypothesis **(T)** (triple gate):
`|S_a ^ S_b ^ S_c| <= k - 1`.

### Object 1 — the ESCAPE residual (band lane)

`background/nodes/xr_support4_structure/statement.md:92-104`, proof at
`proof.md:103-127`, implementation of record
`notes/pilots_20260802/support4_relation/stage5_escape.py:49-57` (peel)
and `:60-70` (bound):

```text
S_a^(0) = S_a ,  S_a^(i+1) = S_a^(i) ^ W^(i),  W^(i) = triple locus of {S_b^(i)}
dim Rel <= sum_a (|S_a^inf| - k)^+ ,  rank >= sum_a min(h, |S_a \ S_a^inf|)
```

(the ESCAPE floor, `proof.md:112-115`; the `min(h, .)` cap is
load-bearing). **Escape form of the occupancy heart**
(`statement.md:98-101`, `proof.md:123-127`,
`notes/BAND_LANE_DEFINITIONS.md:49-52` item 12): *every ray support has
`>= 2` points lying in at most two supports* `=>` `rank >= 2V`, i.e.
per-ray charge `>= 2`. This is the **single open input** of the band
TARGET (`critical/nodes/xr_graded_tangent_band_charge/statement.md:37`,
heart restated at `:52-66`).

### Object 2 — P-A1's `|K|` (exact-k lane)

`notes/pilots_20260802/exact_k_heart/REPORT.md:9-13` (the `d=0`
ceiling), `:20-24` (D0-2), `:70-74` (the residual); lemma statement at
`exact_k_heart/stage10_lemmas.py:4-11`; implementation of record
`exact_k_heart/stage4_scan.py:59-79`:

```text
D0-2 PEELING: a ray with >= h points of family-coverage <= 2 contributes
0 to every relation; drop it, recompute coverage on the survivors,
iterate.  The un-peelable core K is where it stops: every surviving ray
has >= k+1 points covered >= 3x.   P-A1(d=0) <= (2R-1)/h + |K|.
```

### The dictionary (the reason they look alike)

`|S_a| = A = k + h`, so for `T <= S_a`

```text
|S_a \ W| >= h   <=>   |S_a ^ W| <= k   <=>   C_{S_a ^ W} = 0
```

i.e. **"`>= h` points of coverage `<= 2`" (P-A1's death test) is exactly
"`<= k` points survive to the triple locus" (the band's escape test at
full charge)**. Both sides are the same predicate on the same object.

---

## (b) UNIFICATION THEOREM + SEPARATING EXAMPLE

### The operator

A **state** is a pair `(F, T)`, `F <= V`, `T_a <= S_a` for `a in F`.
Write `mult_{F,T}(x) = #{a in F : x in T_a}` and
`W(F,T) = {x : mult_{F,T}(x) >= 3}`. Define

```text
Phi(F, T) = (F', T'),   T''_a = T_a ^ W(F,T),
                        F'   = {a in F : |T''_a| >= k+1},   T'_a = T''_a .
```

`Phi` is monotone and deflationary, so `Phi^i(V, S)` descends to a
greatest fixed point `(K, T^inf)` — the **`(3, k+1)`-core** of the
ray/point incidence structure. Write

* **ESC** = `Phi` with the ray-drop disabled (`F == V`) — the band peel;
* **KER** = `Phi` with the support-shrink disabled (`T == S`, death test
  `|S_a ^ W| <= k`) — P-A1's peel.

### Lemma 0 (soundness of `Phi`). *Proved.*

For every `(c_a) in Rel` and every `i`: `c_a = 0` for `a not in F_i`, and
`supp(c_a) <= T^i_a` for `a in F_i`.

*Proof.* Induction; `i = 0` is trivial. Assume it at `i` and let `x`
satisfy `mult_{F_i,T^i}(x) <= 2`. Any `b` with `c_b(x) != 0` has
`b in F_i` (else `c_b = 0`) and `x in supp(c_b) <= T^i_b`, so at most 2
components are nonzero at `x`. Evaluating the relation at `x` gives
`sum_b c_b(x) e(z_b) = 0` in `F_q^2` with the `e(z_b)` pairwise
independent, so the number of nonzero terms is `0` or `>= 3`
(= S4-1, `statement.md:41-47`, `proof.md:9-24`; = D0-2's Vandermonde
step, `stage10_lemmas.py:4-11`) — hence `0`. So
`supp(c_b) <= T^i_b ^ W(F_i,T^i) = T^{i+1}_b`. If `|T^{i+1}_a| <= k`
then `c_a in C_{S_a}` has support of size `<= k`, while every nonzero
word of `C_{S_a}` has weight `>= k+1` (MDS; = S4-2',
`proof.md:26-32`), so `c_a = 0`. QED

### Theorem U1 (the band peel is ONE step). *Proved.*

With the ray-drop disabled, `T^2 = T^1`; i.e.
`S_a^inf = S_a ^ W_0`, `W_0 = W(V, S)`.

*Proof.* `mult_{V,T^1}(x) = #{a : x in S_a ^ W_0}` equals
`mult_{V,S}(x) >= 3` if `x in W_0`, and `0` otherwise. So
`W(V, T^1) = W_0` and `T^2_a = T^1_a ^ W_0 = T^1_a`. QED

*(Mechanism: a point leaves **every** support simultaneously or none, so
its multiplicity never changes before it is deleted. Nothing in the
node's claim 6 is affected — the recorded fixture values are reproduced
exactly — but "iterate to the stable limit" is a one-pass operation as
literally written. Recommended as a definitional addendum; no edit made.)*

### Theorem U2 (P-A1's peel IS the full closure). *Proved.*

Let `F^K_i` be P-A1's iteration (`stage4_scan.py:59-79`) and
`(F_i, T^i) = Phi^i(V, S)`. Put `W_i := W(F^K_i, S)`. Then for all `i`:

```text
F_i = F^K_i ,   W(F_i, T^i) = W_i ,   T^{i+1}_a = S_a ^ W_i ,   W_{i+1} <= W_i
```

and at the fixed point `K = F_infinity`, `T^inf_a = S_a ^ W_infinity`.

*Proof.* Induction. Nesting: `F_{i+1} <= F_i` gives
`mult_{F_{i+1},S} <= mult_{F_i,S}`, so `W_{i+1} <= W_i`. Assume
`F_i = F^K_i` and `T^i_a = S_a ^ W_{i-1}` (`W_{-1}` = everything). For
`x in W_{i-1}`: `mult_{F_i,T^i}(x) = mult_{F_i,S}(x)`. For
`x not in W_{i-1}`: `mult_{F_i,T^i}(x) = 0`, and
`mult_{F_i,S}(x) <= mult_{F_{i-1},S}(x) <= 2`, so `x` is in neither
locus. Hence `W(F_i,T^i) = W_i`. With `W_i <= W_{i-1}`,
`T^{i+1}_a = (S_a ^ W_{i-1}) ^ W_i = S_a ^ W_i`, so
`F_{i+1} = {a in F_i : |S_a ^ W_i| >= k+1} = F^K_{i+1}`. QED

**This is the unification.** One operator; the band lane runs it with the
death rule switched off (and therefore for exactly one pass), P-A1 runs
it to the fixed point. P-A1's `|K|` is the surviving **ray count** of the
core; the band's escape residual is the surviving **point set** of its
first layer. They are two readings of the same covering condition:
`K` is a covering design in which every ray keeps `>= k+1` points and
every kept point is covered `>= 3` times *within* `K`
(verbatim P-A1's phrasing, `exact_k_heart/REPORT.md:70-72`).

### Theorem U3 (KERNEL FLOOR). *Proved.*

With `T^*_a := T^inf_a` for `a in K` and `T^*_a := empty` otherwise,

```text
dim Rel <= sum_{a in K} (|T^inf_a| - k)^+ ,
rank    >= sum_{a in V} min( h, |S_a \ T^*_a| )        (the KERNEL FLOOR)
```

*Proof.* Lemma 0 at the fixed point embeds `Rel` in
`(+)_{a in K} C_{T^inf_a}`. Then `rank = Vh - dim Rel >=
sum_{a not in K} h + sum_{a in K} (h - (|T^inf_a| - k)^+)`, and for
`T <= S_a` with `|S_a| = k+h` one has
`h - (|T| - k)^+ = min(h, |S_a \ T|)`. QED

### Theorem U4 (domination, strict). *Proved + fixtures.*

`T^*_a <= S_a ^ W_0 = S_a^inf` for every `a`, so the KERNEL FLOOR is
`>=` the ESCAPE FLOOR term by term. Strictness is exhibited below.

### Corollary U5 (the heart, relaxed). *Proved.*

If `h >= 2` and every ray of the core `K` escapes `>= 2` points
(`|S_a \ T^inf_a| >= 2` for `a in K`), then `rank >= 2V`: dead rays
contribute `h >= 2` automatically. Since `W_infinity <= W_0`, this
hypothesis is **implied by, and strictly weaker than**, the escape form
of the occupancy heart (item 12).

### SEPARATING EXAMPLE (the two residuals are different sets)

**S1 — minimal, `(T)`-clean; the heart's hypothesis FAILS but the
conclusion HOLDS.** For `k = h = 2` (`A = 4`, `V = 5`, `n = 14`), points
`0..13`:

```text
S_1 = {0,1,2, 3}      S_2 = {0,1,2, 4}          (the two survivors)
S_3 = {0, 5,6,7}      S_4 = {1, 8,9,10}      S_5 = {2, 11,12,13}
```

`W_0 = {0,1,2}` (each covered by `S_1, S_2` and one doomed ray).
Round 1: `|S_j ^ W_0| = 1 <= k` for `j = 3,4,5` — they die;
`|S_1 ^ W_0| = |S_2 ^ W_0| = 3 = k+1` — they survive. Round 2: only
`S_1, S_2` remain, every point has multiplicity `<= 2`, so
`W_1 = empty` and both die. Hence `K = empty`, `dim Rel = 0`,
`rank = Vh = 10` (machine-verified over 4 slope tuples), and the KERNEL
FLOOR `= 10` is tight. But the one-step escapes are `(1,1,3,3,3)`: the
survivors escape only **one** point, so the escape form's hypothesis
FAILS, and the ESCAPE FLOOR is `1+1+2+2+2 = 8 < 10`. The conclusion
`rank >= 2V = 10` nevertheless holds — via the kernel, not the escape
residual. `(T)` holds (all triples `<= k-1 = 1`); the system is **not**
pairwise-intersecting.

Verified for `(k,h) in {(2,2), (3,3), (2,4), (4,2), (5,3)}`:

| `(k,h)` | `V` | `n` | escape floor | kernel floor `=` rank `= Vh` | one-step escapes |
|---|---|---|---|---|---|
| (2,2) | 5 | 14 | 8 | 10 | 1,1,3,3,3 |
| (3,3) | 5 | 20 | 11 | 15 | 1,1,4,4,5 |
| (2,4) | 7 | 32 | 22 | 28 | 1,1,5,5,5,5,5 |
| (4,2) | 4 | 14 | 6 | 8 | 1,1,3,4 |
| (5,3) | 4 | 18 | 8 | 12 | 1,1,4,5 |

**S2 — fully gate-clean (`(T)` *and* pairwise-intersecting): the floors
still separate.** Two survivors, each fed by a `(k+1)`-cycle of doomed
rays (each doomed ray supplies the third coverer of exactly 2 of the
survivor's `k+1` triple-locus points, so it holds `<= k` of them and dies
at round 1); pair fillers (2-covered) restore pairwise intersection and
padding equalises `|S_a| = A`, neither touching the triple locus.

| `k` | `V` | `n` | `A` | `h` | triples | pairs | escape floor | kernel floor `=` rank `= Vh` |
|---|---|---|---|---|---|---|---|---|
| 2 | 8 | 46 | 12 | 10 | `<= 1 = k-1` | `>= 2 = k` | 78 | 80 |
| 3 | 10 | 123 | 25 | 22 | `<= 1 <= k-1` | `>= 3 = k` | 218 | 220 |

So inside the band lane's own admissible class the refinement is real,
though here it improves the floor by 2 rather than rescuing a failed
hypothesis (see FLAG 5).

### Honest correlation note

On **both banked fixtures the two residuals coincide** — which is exactly
why the objects looked identical: the U-mechanism `(3,5,1,4)` has
`K =` all 4 rays and kernel floor `=` escape floor `= 16` (cap 4, rank
19), and `K_V (3,7,1,5)` has `K = empty` with both floors `= 35 = rank =
Vh`. Over the 99-system sweep the kernel floor is **strictly** better on
**26**; the one-step escape hypothesis holds on 19 systems, the kernel
escape hypothesis on 38. Where they agree, they agree because
`W_infinity = W_0`; nothing here is a coincidence of measurement.

---

## Machine verification

`verify.py` (this directory) imports — never copies — `s4lib.py` and
`stage5_escape.py` (`support4_relation`) and `stage4_scan.py`
(`exact_k_heart`); `verify.json` holds the record.
Run: `tools/ramguard tiny -- python3
notes/pilots_20260803/k_escape_unification/verify.py` -> **18 checks, 0
FAIL** (well inside 256M/60s; no COMPUTE REQUEST needed).

Coverage: banked-fixture replay (F7); 99 systems (90 random over
`k in {2,3,4}`, `h in {2,3,4}`, `V in {4,5,6}` + 9 structured: U-cliques,
`K_V`, cascades) for U1/U2/U3/U4/F6; 7 separating fixtures (F5). Every
system also cross-checks `rank = Vh - dim Rel` against an independent
`family_rank`.

---

## (c) Implications — stated conservatively, no status flip

1. **Band TARGET `xr_graded_tangent_band_charge`, single open input.**
   The heart's hypothesis may be replaced by its `Phi`-iterated form
   (Corollary U5) at no cost and with a strictly smaller residual class:
   only systems whose `(3,k+1)`-core is **nonempty** and contains a ray
   with `<= 1` escaped point **relative to `W_infinity`** can defeat
   per-ray charge 2. Systems that die under iteration — including S1,
   where the one-step hypothesis fails outright — are now covered. This
   does **not** prove the occupancy lemma and does not change any node
   status; it narrows what remains and strictly strengthens the floor.
2. **The residual is one covering-design condition, not two.** The band's
   surviving object and P-A1's `K` are the same `(3,k+1)`-core; the
   lanes differ only in what they *charge* (band: escaped points per
   ray; P-A1: number of surviving rays). Future work on either heart
   applies verbatim to the other — the sharpest available consequence of
   this round.
3. **P-A1's `|K|` term.** Unconditionally, the accounting
   `rank(F) = h|P| + rank(K)` (`exact_k_heart/REPORT.md:9-13`) upgrades
   to `rank >= h|P| + sum_{a in K} min(h, esc_a)`: every core ray now
   carries its own escape charge (Theorem U3). **Conditionally** — if
   the heart holds in the U5 form — combining with the banked ceiling
   `rank <= 2(|U|-k) - 1 <= 2R-1` (D0-3, `stage10_lemmas.py:13-19`;
   identical to S4-14's upper half, `xr_support4_structure/proof.md:84-101`)
   gives `h|P| + 2|K| <= 2R-1` and hence

   ```text
   Gamma_0 = |P| + |K| <= (2R - 1)/2 .
   ```

   That is the **first finite ceiling on the `|K|` term**, which today
   has no bound proved (`exact_k_heart/REPORT.md:70-74`). It is weaker
   than the peelable head `(2R-1)/h` by exactly the factor `h/2`, so it
   does **not** by itself deliver the P-A1(`d=0`) target — it converts an
   unbounded residual into a bounded one. FLAGGED conditional.
4. **The residual channel is now explicit for both lanes**: core rays of
   escape `0` (the zero-escape channel — already the node's named open
   sub-item, the measured collapse) and of escape `1` (new, named here).
   Nothing else can defeat per-ray charge 2.
5. **Duplicate spotted**: D0-3 (locality + death) and S4-14's upper half
   are the same inequality in the shared notation, derived independently
   in the two lanes. Recorded as concordance, not novelty.

---

## (d) FLAGS (every step I could not fully verify)

1. **Scope of the unification.** Theorems U1-U5 unify the two *residual
   objects* on the shared ray-system abstraction. They do **not** claim
   the two lanes' families are the same systems (P-A1: post-strip live
   rays with exact-`k` pair cores; band: depth-`d` selected supports).
   NOT VERIFIED, and nothing here should be read as transporting a
   hypothesis across lanes.
2. **`|S_a| = A` in the P-A1 reading** is taken from the record (live =
   exact-`A` agreement, `BAND_LANE_DEFINITIONS.md` item 7), not
   re-derived. The formula `h - (|T|-k)^+ = min(h, |S_a \ T|)` in U3 uses
   it; for supports of unequal size the floor must be re-stated per ray.
3. **The `Gamma_0 <= (2R-1)/2` bound is CONDITIONAL** on the unproved
   heart (U5 form) *and* on `rank <= 2R-1` as banked. Not a status flip,
   not a claim about the prize rows.
4. **U1 (one-step) is a definitional finding about the node's wording**,
   not a defect: claim 6's floor and its recorded fixture values
   (16/cap 4/rank 19; 35 = rank; uncapped 40 false) are reproduced
   exactly. I did **not** edit the node; an addendum is recommended.
5. **The gate-clean separation is a floor gap, not a hypothesis failure.**
   I could not build a fixture that is `(T)`-clean *and*
   pairwise-intersecting *and* has a survivor of one-step escape `<= 1`,
   and I have not proved that impossible. Only the escape-`0` case is
   settled: if two rays satisfy `S_a <= W_0` and some ray dies at round 1,
   then those two rays and the dying ray share `k > k-1` points and
   `(T)` fails. The escape-`1` case is OPEN — it decides whether S1's
   phenomenon reaches the band lane's admissible class.
6. **Toy scale only**: `n <= 123`, `q in {1009, 6421}`, `V <= 10`. No
   official-scale statement is made or implied.
7. **The sweep is evidence, not proof** — but U1-U5 carry complete
   elementary proofs above, so the sweep is a consistency check of proved
   statements (in particular F6 is a check of Corollary U5, not an
   independent measurement). The 99 systems are not exhaustive.
8. **`rank = Vh - dim Rel`** rests on the banked per-ray accounting
   (item 11), not re-proved here; it is machine-cross-checked against an
   independent rank computation on every system in the sweep.

### Pre-registered falsifiers (fixed before any run; `verify.py:29-45`)

F1 kernel floor `>` rank (U3) · F2 escape floor `>` kernel floor (U4) ·
F3 ESC needing `>= 2` effective iterations (U1) · F4 `Phi` `!=`
`stage4_scan.peel` (U2) · F5 the separating fixtures failing (`K`
nonempty, `rank != Vh`, or escape floor `>= rank`) · F6 all kernel
escapes `>= 2` yet `rank < 2V` (U5) · F7 banked replay disagreeing with
the node's recorded numbers.
**All seven survived: 0 hits in 18 checks.**
