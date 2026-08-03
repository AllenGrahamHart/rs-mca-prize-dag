# PRE-REGISTRATION — ESCAPE-1 GATE-CLEAN REALIZABILITY (channel (ii))

Pilot: Opus 5, 2026-08-03. Directory
`notes/pilots_20260803/escape1_realizability/`.
**Written and timestamped BEFORE any computation was run.** Everything
below is hand-derivation from the two sibling reports
(`k_escape_unification`, `zero_escape_collapse`) plus the banked node
`background/nodes/xr_support4_structure`. No script had been executed at
the time of writing; the fixtures and their predicted numbers are stated
here in full so that every prediction is falsifiable by the verifier.

## 0. The question (as commissioned)

Does there exist a ray system `Sigma = ((z_a, S_a))_{a=1..V}`,
`|S_a| = A = k+h`, `z_a` distinct in `P^1(F_q)`, that is **gate-clean**

* (T) k-packing gate: `|S_a ^ S_b ^ S_c| <= k-1` for all triples,
* pairwise-intersecting: `|S_a ^ S_b| >= k+1` for all pairs,

whose `(3, k+1)`-core `(K, T^inf)` (Phi = shrink to the triple locus of
the live sub-family AND drop rays with `<= k` surviving points, iterated
to the greatest fixed point; `T^inf_a = S_a ^ W_infinity`) is **nonempty**
and contains a ray with **escape exactly 1**: `|S_a \ T^inf_a| = 1`?

Follow-up that matters: can such a core ray defeat per-ray charge 2, i.e.
`rank = Vh - dim Rel < 2V`, or does a floor protect the heart there?

## 1. PREDICTIONS

**PR-1 (REALIZABILITY): YES — and not marginally.** I predict a
gate-clean fixture in which the core is ALL rays and EVERY ray has escape
exactly 1. Named fixture **E1**:

```text
U = B_1 u ... u B_V  u  Y            (disjoint), plus a common block A_0
|B_a| = s, Y = {y_1..y_p}, V = 2p,   i(a) = ceil(a/2)  (a matching of rays)
S_a = A_0 u (u_{b != a} B_b) u {y_{i(a)}}
```

so `y_i` lies in exactly the two rays of its matched pair (multiplicity 2
= escaped), every `B`-point has multiplicity `V-1`, every `A_0`-point
multiplicity `V`. Parameters `h = 4, s = 2, p = 6, V = 12, k = 19,
|A_0| = 0`. Predicted exactly:

| quantity | predicted |
|---|---|
| `A = |S_a|` | 23 = k+h |
| `n = |U|` | 30 |
| `m = |U| - k` | 11 |
| pairwise core, unmatched pair | 20 = k+1 |
| pairwise core, matched pair | 21 = k+2 (depth 2 = h-2, band proper) |
| every triple intersection | 18 = k-1 (gate SATURATED, not violated) |
| every 4-wise intersection | 16 (k-packing on cores holds) |
| multiplicities | 2 (the `y`), 11 (the `B`-points) |
| core `K` | all 12 rays |
| escape vector | `(1,1,1,1,1,1,1,1,1,1,1,1)` |

**PR-2 (CHARGE): an escape-1 core ray CAN defeat per-ray charge 2.**
`Row <= C_U x C_U` (banked S4-14 upper half) forces `rank <= 2m = 22`,
while `2V = 24`. Predicted `rank = 22` exactly (generic slopes), so
per-ray charge `= 22/12 = 1.833... < 2`. Channel (ii) is therefore a
GENUINE counterexample channel, not closable.

**PR-3 (the sharp sub-case is nevertheless PROTECTED).** I predict a new
floor, proved by hand before running (the *3-drop kernel floor*): since a
relation of ray-support `<= 3` is zero ((T) + MDS), `Rel` meets every
3-fold sub-sum `(+)_{a in X} C_{T^inf_a}` trivially, so

```text
dim Rel <= sum_{a in K} (h - esc_a)  -  max_{X <= K, |X|=3} sum_{a in X} (h - esc_a)
rank    >= sum_{a not in K} h  +  sum_{a in K} esc_a  +  G3 ,
           G3 := max_{|X|=3} sum_{a in X} (h - esc_a).
```

Consequences predicted: (a) ONE escape-1 core ray with all other core
rays escaping `>= 2` can NEVER defeat charge 2 (`G3 >= 3 > 1`); charge 2
survives unless `2 n_0 + n_1 > G3 + surplus`, so with `n_0 = 0` at least
`3h - 2` escape-1 core rays are needed. (b) The floor is TIGHT on the
banked U-mechanism `(k,h,d,V) = (3,5,1,4)`: escapes `(4,4,4,4)`,
`sum (h-esc) = 4`, `G3 = 3`, so `dim Rel <= 1` — the recorded value.

**PR-4 (structure lemmas).** For gate-clean systems with `V >= 3`:
`h >= 3` is FORCED (`|S_a^S_b^S_c| >= 2(k+1) - (k+h) = k+2-h <= k-1`);
and the core satisfies `|K| = 0` or `|K| >= 4` (`|K| <= 3` would give
`|T^inf_a| <= |S_a^S_b^S_c| <= k-1 < k+1`).

**PR-5 (the sibling channel (i) also falls — reported, not claimed as my
anchor).** The same `rank <= 2m` mechanism refutes the OPEN `V >= 5`
zero-escape question with a *complete block system*: `U = A_0 u A_1 u ...
u A_V`, `S_a = U \ A_a`, `|A_a| = t`. Gates force `(h+1)/2 <= t <= h-1`,
`m = h+t`; any `V > h+t` breaks charge 2. Named fixture **Z1**:
`k = 7, h = 3, t = 2, |A_0| = 0, V = 6, n = 12, A = 10, m = 5`; predicted
pairwise `8 = k+1`, triples `6 = k-1`, zero escape (all multiplicities
5), `rank = 10 < 12 = 2V`, per-ray charge `1.667`.

**PR-6 (contrast — escape 1 alone is not the mechanism).** The same E1
family with `V <= m` does NOT defeat charge 2. Named fixture **E1safe**:
`h = 4, s = 2, p = 3, V = 6, k = 19, |A_0| = 12`, `n = 27, m = 8 >= V`;
all escapes 1, core all rays, predicted `rank = min(Vh, 2m) = 16 >= 12
= 2V`. So the counterexample mechanism is `V > m`, not escape 1 per se.

**PR-7 (family minimality).** Inside the E1 family the constraints are
`ceil(h/2) <= s <= h-2` (so `h >= 4`) and `V = 2p > m = h-1+s+p`, i.e.
`p >= h+s`; the smallest charge-defeating member is exactly
`h=4, s=2, p=6, V=12`. Predicted: an exhaustive scan of the family
parameters finds no smaller `V`.

## 2. FALSIFIERS (fixed now; any hit is reported as a hit, not dropped)

* **E-F1** E1 fails any gate (sizes `!= A`, some pair `< k+1`, some
  triple `> k-1`) → PR-1 dies (the fixture is not admissible).
* **E-F2** E1's core is not all 12 rays, or any escape `!= 1` → PR-1 dies
  (the fixture does not answer the commissioned question).
* **E-F3** `rank(E1) >= 2V = 24` → PR-2 dies; charge 2 survives channel
  (ii) and the answer to the follow-up flips to "a floor protects".
* **E-F4** `rank != Vh - dim Rel` on any fixture, or `rank > 2m`
  anywhere → the per-ray accounting / `Row <= C_U x C_U` reading is
  wrong and EVERY conclusion here dies.
* **E-F5** the 3-drop floor EXCEEDS the true rank on any system in the
  sweep → PR-3 refuted (the theorem is false).
* **E-F6** a gate-clean system with `V >= 3` and `h <= 2` appears
  anywhere → PR-4(a) refuted.
* **E-F7** a system with `1 <= |K| <= 3` appears anywhere → PR-4(b)
  refuted.
* **E-F8** `rank(Z1) >= 12` → PR-5 dies (channel (i) survives at V=6).
* **E-F9** `rank(E1safe) < 12` → PR-6 dies (the contrast is not a
  contrast; escape 1 would break charge even at `V <= m`).
* **E-F10** the 3-drop floor is not tight on the U-mechanism
  (`dim Rel != 1`, or floor `!= 19 = Vh - 1`) → PR-3(b) dies.
* **E-F11** the family scan finds a charge-defeating member with
  `V < 12` → PR-7 dies.
* **E-F12** any banked replay disagrees with the record (U-mechanism
  `rank 19`, escape floor 16 / cap 4; `K_V (3,7,1,5)` `rank 35 = Vh`) →
  the harness is wrong and nothing here is trustworthy.

## 3. SEARCH SPACE TO BE SWEPT

1. **Named fixtures**, all built from the hand-derived formulas above and
   fully re-derived by the verifier: E1 (`q=31`), E1deep
   (`h=4,s=2,p=10,V=20,k=35,n=50,q=53`), E1safe (`q=29`), Z1 (`q=13`),
   Z1big (`k=17,h=3,t=2,V=11`), and **X1p** — the escape-1 perturbation
   of the collapse pilot's X1/X2 pencil fixture (one point of one support
   swapped for a fresh private point), as an independent realizability
   witness with a *single* escape-1 ray.
2. **Banked replay**: U-mechanism `(3,5,1,4)` and `K_V (3,7,1,5)` via
   `s4lib.build_mobius_family` / the node's own numbers; S1 and S2 from
   the unification pilot (imported, not copied).
3. **Random (T)-clean sweep** for the 3-drop floor (PR-3): `>= 60`
   systems, `k in [2,5]`, `h in [2,5]`, `V in [4,7]`, supports drawn to
   satisfy (T); every system checks
   `rank >= 3-drop floor >= kernel floor >= escape floor` and
   `rank = Vh - dim Rel`, and records `|K|` and the escape vector.
4. **Family parameter scan** (PR-7): all `(h, s, p)` with `h <= 8`,
   `s <= h-2`, `p <= 12`, testing the gate inequalities and `V > m`.
5. **Boundary scan**: the interval predicted-but-not-realized between the
   3-drop threshold `n_1 = 3h-2 = 10` and the achieved counterexample
   `V = 12` at `h = 4` is expected to remain OPEN; I pre-register that I
   will report it as open rather than claim either way.

Compute: everything above is small linear algebra over prime fields
(`n <= 50`, `V <= 20`) and is expected to run inside
`tools/ramguard tiny` (256M/60s). If it does not, the run moves to
`tools/ramguard local` and that is reported.
