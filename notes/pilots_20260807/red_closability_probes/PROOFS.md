# PROOFS — RED CLOSABILITY PROBES (round 21)

Opus pilot, `notes/pilots_20260807/red_closability_probes/`. Every claim
below was registered in `PREREG.md` §P0–P8 **before** computation.
Machine checks: `probe1_verify.py` (stages `hyp / rank1 / fold / box /
banked / tight / poscontrol / catch / hfb` + `failclosed`) and
`probe2_verify.py` (stages `region / functional / endpoint` +
`failclosed`). Totals: **137 checks, 0 failures**; both `failclosed`
controls exit 1. Stdlib only, all runs under `tools/ramguard`.

**Both probes return NO.** Neither red is closable by the named recent
theorem. Each "no" is delivered as an exact gap, and in both cases the
obstruction is *structural and already banked* — not a missing
computation.

---

# PROBE 1 — `integer_code_distance_cert` vs THEOREM Z-1 / THEOREM Z-2

## 1.1 The node's obligation, quoted

`critical/nodes/integer_code_distance_cert/node.json:6`:

> `"title": "THE RESIDUE: certify min ternary distance > 2l' for the explicit k x N' system"`

`critical/nodes/integer_code_distance_cert/statement.md:11-14`:

> pin the prime field, quotient order and root, class cell and its exact
> cardinality, support bound `2l'`, explicit integer kernel matrix, and
> allowed cyclotomic-relation basis. Then bank a machine-checkable
> certificate that no non-cyclotomic ternary kernel vector of weight at
> most `2l'` remains

## 1.2 The explicit system, quoted

`critical/nodes/weight_graded_mitm/proof.md:26` (the `(K)` display), and
identically `critical/nodes/kernel_lattice_reframing/proof.md:25`:

> ```
> K_p = { v in Z^{N'} : sum_x v_x zeta^x = 0  in F_p },                       (K)
> ```

with `p = 1 (mod N')` and `zeta in F_p` of exact order `N'`
(`weight_graded_mitm/proof.md:20`), `v` ternary, `supp(v) <= 2 l'`
(`ibid.:22`), modulo the antipodal cyclotomic sublattice `R`
(`ibid.:29-32`).

`l' = rho N' + 1` (`critical/nodes/acl_count/statement.md:9`;
`critical/nodes/qfloor_exact/statement.md:13`).

## 1.3 The instruments, quoted

THEOREM Z-2, `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:200-209`:

> **THEOREM Z-2 (`l1` extension).** Let `F` have characteristic `0` or
> `> w`, let `omega in F` have exact order `2N`, and let `c in Z^N` be
> nonzero, indexed by `e in {0,...,N-1}`, with **`l1`-weight**
> `w := sum_e |c_e|`. If
> `sum_e c_e omega^{(2j-1)e} = 0   for j = 1,...,ell     and   w <= 2ell,`
> then `c = 0`

THEOREM Z-1, `ibid.:96-101`: on the admissible object every nonzero
ternary vector of `L^perp` has `wt >= 2R + 1`; SCOPE at `ibid.:116-124`
— shift 0 only, 43 shifted counterexamples banked.

## 1.4 Hypothesis match, term by term

The fold of `kernel_lattice_reframing` (PROVED) puts the node's system
into exactly Z-2's shape: with `N := N'/2` and `omega := zeta` of exact
order `2N = N'`, a ternary `v` folds to `w_x = v_x - v_{x+N'/2}` in
`{-2..2}`, indexed by `e in {0,...,N-1}`. So:

| Z-1/Z-2 hypothesis | the node's system | verdict |
|---|---|---|
| (H1) `char F = 0` or `char F > w` | `p >= 2^167` at every pinned exhibit; `w <= 2l' <= 2N'` | **HOLDS** |
| (H2) `omega` of exact order `2N` | `zeta` of exact order `N' = 2N` | **HOLDS** |
| (H3) exponents distinct in `{0..N-1}` | the fold gives exactly `e in {0..N'/2-1}` | **HOLDS** |
| (H4) vanishing at the first `ell` odd powers, `w <= 2ell` | **`ell = 1`**: the system is a SINGLE `F_p`-linear functional | **FAILS** |

**The registered prediction (P3) is confirmed, and the shift check
passes.** The single exponent is `j = 1`, i.e. the first odd power, so
the window starts at `l = 1` and the 43 banked shifted counterexamples
are *not* what blocks this node. The scope check that the brief called
"the whole probe" is clean. The probe dies one slot later, at (H4)'s
`ell`.

## 1.5 Why `ell = 1` is permanent, not incidental

Two independent reasons, one already banked as a refutation:

**(a) Banked.** `background/nodes/multi_multiplier_reduction/node.json:8`,
status `REFUTED`, verbatim:

> `"REFUTED (wave-1 packet, Lemma 1): the k-multiplier residue matrix is an OUTER PRODUCT mod p — rank 1 for every k — so the stacked ternary kernel equals the single relation's kernel and the GV counting presupposed independence that never holds."`

This is precisely the statement that `ell` cannot be raised above 1 by
stacking rows. It is the node's *own* `evidence_for` edge
(`ibid.:16-21`). **The node's title still advertises "the explicit
k x N' system", a phrase minted by that refuted supplier
(`ibid.:6`).** The live system, after the refutation, is `k = 1`; see
`critical/nodes/weight_graded_mitm/proof.md:50-53`:

> No auxiliary multiplier polynomial is introduced: because `zeta in F_p`
> (`p = 1 mod N'`), the sums `s(a)` are elements of the prime field computed
> directly, so the earlier multiplier-based reduction is unnecessary

*Verified* (`probe1_verify.py rank1`, 30 checks): the stacked
`k x N'` residue matrix has rank exactly 1 over `F_p` for
`k in {1,2,3,5,10}` at six cells.

**(b) Structural.** Because `zeta in F_p`, the substitutions
`zeta -> zeta^a` are **not** induced by field automorphisms of `F_p`, so
no further vanishing conditions are free. *Verified*
(`probe1_verify.py catch`): an explicit `v in K_p` at `N'=8, p=17` whose
index-multiplication by `a=3` leaves `K_p`.

## 1.6 THE GAP, exactly

At the rate-1/2 prize cell `N' = 128`, `l' = 65`:

```
Z-1/Z-2 floor at ell conditions :  2*ell + 1
node's threshold                :  > 2l' = 130
smallest ell that suffices      :  ell = 65
ell the system supplies         :  ell = 1        (rank 1 for every k, PROVED)
MISSING CONDITIONS              :  64
Z-2's actual output at ell = 1  :  min l1 weight >= 3
WEIGHT GAP                      :  131 - 3 = 128 units of l1 weight
```

**Z-1/Z-2 give this node literally nothing.** At `ell = 1` the
conclusion "no nonzero `c` with `l1`-weight `<= 2`" says exactly
`zeta^a != +-zeta^b` for distinct `a,b in {0..N-1}` — which is immediate
from `zeta` having exact order `N' = 2N` and is already assumed by the
node. *Verified* (`probe1_verify.py box`, 36 checks): the `ell=1` floor
holds at all 17 cells, and *(`tight`)* it is **attained** at
`N'=8, p=17` (min folded `l1` = 3), so no sharpening at `ell = 1` can
ever exceed 3.

**Is a bounded amount of new work enough? No.** Closing the gap means
manufacturing 64 further independent odd-power vanishing conditions on
the same ternary vector. The only named mechanism for that
(`multi_multiplier_reduction`) is REFUTED by a rank argument that holds
*for every k*. No banked object supplies them. This is not a compute
gap; it is a rank gap with a proof of impossibility already on file.

**Positive control** (`probe1_verify.py poscontrol`, 9 checks): on the
*genuine* `ell`-condition system Z-2's conclusion holds exhaustively at
7 configurations, and the banked smallest shifted counterexample
(`2N=12, p=13, R=1, a=1`) is reproduced with `l1` weight `2 < 3`. The
mechanism of the shift failure is also pinned: the shifted generator
`omega^3` has exact order `4 < 2N = 12`, i.e. **the shift destroys (H2)**,
not (H4). Z-1/Z-2 are sound; it is the node's system that is short.

## 1.7 What the node's residual actually is (bonus, scoped)

`probe1_verify.py hfb`. The PROVED high-field branch
(`background/nodes/integer_code_distance_high_field_folded_box_exclusion/statement.md:17`,
`p > 253^32`) has threshold `log2(253^32) = 255.4558` bits. On the
rate-1/2 crossing lane's own prime-row window `log2 p in [245.1491, 256)`:

```
HFB covers   log2 p in (255.4558, 256.0000)   width 0.5442 bits =  5.02%
RESIDUAL     log2 p in [245.1491, 255.4558]   width 10.3067 bits = 94.98%
```

plus every quotient order `N' != 128`, plus the separate
cell-cardinality-vs-`B*` obligation. The four pinned Proth prize
exhibits (167–171 bits) sit **84.5 to 88.5 bits below** the threshold.

## 1.8 CATCH-P1 (mine) — the banked toy exemplar quotes the wrong support statistic

`critical/nodes/integer_code_distance_cert/notes/folded_certificate.md:19-20`:

> - N'=16, p=10177: 48 collisions, min support 5 -> falsifier fires (bad prime;
>   matches zone_b ratio 0.951).

`probe1_verify.py banked` (27 checks, exhaustive, all 8 primitive 16th
roots mod 10177):

```
folded kernel vectors in the box = 48        <- REPLICATES exactly
min folded HAMMING weight        = 5         <- this is the recorded "5"
min folded l1 weight             = 7
min UNFOLDED ternary support     = 7         <- what the node's threshold is about
    (exhaustive over supports 1..8: 0,0,0,0,0,0,128,0)
```

**Fold lemma** (proved here, verified at 6 cells in stage `fold` and
exhaustively at the real cell in stage `banked`): for a folded
`w in {-2..2}^{N'/2}`, the minimum support of a ternary preimage is
exactly `l1(w)` (use `(0,0) / (1,0) / (1,-1)` per coordinate). Hence
**min non-cyclotomic ternary support = min folded `l1` weight**, *not*
the folded Hamming weight. The recorded "min support 5" understates the
node-relevant quantity by 2 at that cell. The cell's *verdict*
(falsifier fires) is unaffected; the *number* is the wrong statistic and
would be wrong in a certificate. The other two banked toy verdicts
replicate exactly: `N'=16, p=60161` CERTIFIED (no non-cyclotomic vector
at all), and the C-4 anchor `N'=16, p=12289, w<=6` certified — our exact
min is 11, comfortably above 6
(`critical/nodes/integer_code_distance_cert/execution_report.md:16-27`).

## 1.9 CATCH-P2 (mine) — `weight_graded_mitm`'s speedup names the wrong mechanism

`critical/nodes/weight_graded_mitm/proof.md:110-114`:

> collisions are closed under `v |-> v^{(p)}` (index multiplication by
> `p mod N'`), so nonzero `v in K_p \ R` come in Frobenius orbits of size
> dividing `N'`, letting the search fix one orbit representative and divide
> `(COST)` by a factor `~ N' = 2^7`.

But the node's standing hypothesis is `p = 1 mod N'` (`ibid.:20`), so
`p mod N' = 1` and `v |-> v^{(p)}` is the **identity**: the Frobenius
orbit has size 1, not `N'`. *Verified* (stage `catch`, 6 checks).
Moreover index-multiplication by a general odd `a` is **not** a symmetry
of `K_p` at all (explicit counterexample above). The factor-`N'` saving
nevertheless survives, via a different mechanism: the **cyclic shift**
`v_x -> v_{x-1}` multiplies the sum by `zeta` and so does preserve
`K_p` (verified). Conclusion stands, stated justification does not.
Severity: cosmetic for the cost table, but the node is a *certificate*
node and the certificate's symmetry-reduction argument has to be right.

---

# PROBE 2 — `unsafe_crossing_family_instantiation` vs THEOREM BB

## 2.1 The universality quantifier, quoted exactly

`critical/nodes/unsafe_crossing_family_instantiation/statement.md:8-9`:

> For every admissible row and its proposed first-safe agreement `a_safe`, emit
> an exact certificate at `a_safe-1` in at least one of the following forms.

`node.json:12`:

> `"For every admissible row and its proposed safe agreement a_safe, supply an exact certificate at a_safe-1 of at least one of: (Q) ... (V) ... or (M) ..."`

The counted object is fixed by the falsifier, `statement.md:40`:

> An admissible row with exact `B_C(a_safe-1) <= B*` refutes this target

and by `claim_contract.md:8`:

> - the exact bad-slope count convention used by `mca_grand`.

`B_C` is defined at
`background/nodes/mca_quadratic_prize_rows/statement.md:9-10`:

> Let `C=RS[F,D,k]`, where `|D|=n`, and let `B_C(a)` be the maximum
> number of support-wise MCA-bad finite slopes at agreement at least `a`.

**"Universal" ranges over admissible rows, and the admissible family
provably contains both prime rows and tower rows**
(`critical/nodes/field_cap_check/statement.md:9`, PROVED: `k <= 2^40`,
`|F| < 2^256`; `critical/nodes/f1_case_tower/statement.md:13`: *"Family
CONFIRMED to include non-generating rows (any field < 2^256 incl.
extensions, n up to 2^41): the tower case is genuinely critical"*).

## 2.2 The instrument, quoted

`notes/pilots_20260806/gamma_shell/PROOFS.md:322-330`:

> **THEOREM BB (the budget break, at the DSA witness row).**
> At `p = 3·2^41+1`, `e = 6`, `q = p^6`, `n = 2^41`, `k = 2^40`, `w = 2^34`:
> `L_1(k + 2^34)  >=  max_gamma X_{2^34}(gamma)  >  B*,     by 72.0653 bits.`
> Consequently `a_L(C) > k + 2^34` at that row: **agreement `k + 2^34` is
> UNSAFE.**

`L_1(a) = max_u #{c in C: agr(c,u)>=a}`
(`critical/nodes/rate_half_list_adjacent_crossing/statement.md`, quoted at
`gamma_shell/PROOFS.md:49-59`).

## 2.3 The four registered gates (P5)

**(C1) SAME FUNCTIONAL — FAILS. This is the first and fatal obstruction,
exactly as predicted in P6.** BB bounds `L_1`, a count of *codewords for
one received word*. The node counts `B_C`, a count of *bad slopes on one
received pair*. No PROVED transfer exists; the entire
`rate_half_list_adjacent_crossing -> ... -> mca_grand` path is a chain of
`CONDITIONAL` nodes (`list_adjacency_closing`,
`f1_pole_list_threshold_location`, `f1_case_pole`, `f1_classification`,
`ext_lift`, `mca_safe`), i.e. a DAG dependency, **not** a count
inequality. The repo says so itself,
`notes/literature_map_20260726/target_mappings.json:133`:

> an MCA bad-slope count neither dominates nor is dominated by a worst-case list size

**Exact finite countermodel** (`probe2_verify.py functional`, 6 checks) —
`RS[F_5, |D|=4, k=2]`, `q = 5` finite slopes, 25 codewords, both counts
computed exhaustively:

| `a` | `L_1(a)` | `B_C(a)` |
|---|---|---|
| 1 | 17 | 5 |
| 2 | **6** | **5** |
| 3 | 1 | 5 |
| 4 | 1 | 5 |

Set `B* = 5`. Then `L_1(2) = 6 > B* = 5 >= B_C(2) = 5`: the implication
`L_1(a) > B*  =>  B_C(a) > B*` **is false**. The same countermodel at
`RS[F_7,|D|=6,k=2]`: `L_1(2) = 15 > 7 = q >= B_C(2)`. Structural reason:
`B_C(a) <= q` always (there are only `q` finite slopes), while `L_1(a)`
is bounded only by `|C|`.

*Two honest scope notes.*
(i) **Convention.** I used the **plain** MCA-bad predicate. The official
support-wise refinement
(`background/nodes/rate_half_arbitrary_line_syndrome_router/statement.md:8-16`,
PROVED) only *removes* slopes, so plain `B_C >= ` support-wise `B_C`, and
every `B_C` **upper** bound above — which is the whole countermodel — is
safe under the official convention. The *reverse* direction is not: at
`a in {3,4}` I measure `B_C^plain = 5 > 1 = L_1`, but those are lines
lying inside the code, exactly the case the support-wise clause
excludes, so I do **not** claim `B_C^sw > L_1` there. "Neither count
dominates" is asserted here only in the direction I verified, and
otherwise rests on the banked
`literature_map_20260726/target_mappings.json:133`.
(ii) **What the countermodel does and does not say.** It refutes the
*inference* `L_1(a) > B* => B_C(a) > B*` as a general implication, which
is all that is needed: BB's conclusion does not entail the node's. It is
**not** a claim about the prize row, where `B* = floor(q/2^128)` is far
below `q` and both counts are astronomically larger.

**(C2) ROW ADMISSIBILITY — FAILS on a non-empty part.**
`probe2_verify.py region` independently re-derives the live windows from
`log2 q in [245.1491, 256)` and `p >= 2^39+1` and reproduces
`gamma_shell/PROOFS.md:353-361` to four decimals:

```
e=1  [245.1491, 256.0000)   Cauchy-Schwarz VACUOUS at every delta_a
e=2  [122.5746, 128.0000)   partial
e=3  [ 81.7164,  85.3333)   full at delta_a=1
e=4  [ 61.2873,  64.0000)   full at delta_a=1
e=5  [ 49.0298,  51.2000)   full at delta_a=1
e=6  [ 40.8582,  42.6667)   full at delta_a=1
```

The admissible degree range is exactly `e in {1,...,6}` (`e >= 7` puts
the window below the prime floor). BB reaches 4 of 6 fully, 1 partially,
and **`e = 1` not at all** — and `gamma_shell/REPORT.md:91` states this
is not a compute limit: *"Prime rows untouched, and unreachable by this
method at any `v` in the bracket."*

**(C3) FORM — FAILS.** BB's output is a lower bound on a codeword count
`X_w(gamma)` at a `sig`-shell. The node's `V` form requires *"more than
`B*` pairwise-distinct ambient-field slopes, each bad at `a_safe-1` for
one received pair"* (`statement.md:22-23`). A list of codewords for a
single received word yields one slope, not `B*+1` slopes. BB is not a
`Q` payload (no `qfloor_exact` hypothesis set, no `Acl(N',ell')`) and not
an `M` payload (no post-paid support family, no `nu(A)`).

**(C4) ENDPOINT — FAILS.** `probe2_verify.py endpoint`: BB is stated at
`k + 2^34 = 1116691496960`; the node's two deployed endpoints are
`a_safe-1 = 1116047` (KoalaBear) and `1116023` (Mersenne-31)
(`critical/nodes/unsafe_crossing_family_instantiation/frontier.md:8-9`) —
a factor `1.001e+06` apart.

## 2.4 VERDICT: BB closes **no** part of this node

Not the node, not a named part, not a single row. All four gates fail,
and (C1) fails on its own: even restricted to the `e in {3,4,5,6}`
rows BB fully covers, the theorem bounds the wrong count.

**Lane wiring, verified by hand in `dag.json`** (not trusted from
search): `unsafe_crossing_family_instantiation` has exactly one
out-edge, `{"from": "unsafe_crossing_family_instantiation", "to":
"unsafe_at_crossing", "kind": "req"}` (MCA branch:
`unsafe_at_crossing -> mca_unsafe -> mca_grand`);
`rate_half_list_adjacent_crossing` has exactly one out-edge, to
`list_adjacency_closing` (LIST branch). They are different obligations.

## 2.5 CATCH-P3 (mine) — the roadmap files the MCA node under LIST

`notes/roadmap/LIST.md:16-17` lists, under "Current critical families":

> - Universal unsafe-crossing family instantiation.
> - The rate-half ordinary-list adjacent crossing.

The first is the MCA-branch node (single `req` out-edge to
`unsafe_at_crossing`), and `notes/roadmap/MCA.md:14-19` does not mention
it at all. This mis-filing is exactly the kind of thing that makes a
"BB may have closed it" hypothesis look plausible on the board when the
two nodes are on different branches. Navigational file only — no node
statement is affected.

## 2.6 The exact remainder, and what IS closed

What is already closed on this node (not by BB, and not by me):
a **finite deployed slice** — exact `V` payloads at the two deployed MCA
rows via `identity_prefix_flexible_budget_unsafe_floor`
(`frontier.md:7-12`, `result.md:6-9`), explicitly *"a finite slice, not
the universal row quantifier"*.

What remains open, precisely:
1. every admissible row outside those two, at all six degrees
   `e in {1,...,6}`;
2. on the pair-feasible branch the residual is *narrower than BB's
   region, not wider*: `dependency_subdag.md:105-110` records that
   *"Exact perfect-power interval checks also force extension degree one
   and `p=1 mod N`, so the prime-field kernel model is now correctly
   scoped to the residual target."* Extension degree **one** is exactly
   the row class BB provably cannot reach. So on that branch BB's
   coverage of the node is not merely incomplete — it is **disjoint**
   from the residual.
3. `(RHL-B12)` covers none of this: it is LIST-side
   (`critical/nodes/rate_half_list_adjacent_crossing/statement.md:75`,
   `L_1(3n/4)<=B*<L_1(3n/4-1)`), scoped to budgets `B* in {1,2}`, and
   scoped by budget rather than by field type — so it neither supplies a
   `B_C` payload nor covers the `e = 1` rows of this node.

**No certificate is written for a closable part, because there is no
closable part.** Per P8 that is the honest outcome, and per P2/P5 I do
not report a structural mismatch as a partial closure.

## 2.7 The one transferable thing (a lead, not a closure)

BB's *method* — pigeonhole over a concentration class (`N_acc/2L` across
`2L = 256` `sig`-shells) on top of a Cauchy–Schwarz accident lower bound
(THEOREM AC) — is the same shape the node's `M` route needs for
`nu(A) = E[N(A)] - (q/2) C_t(A) > B*`: an occupancy lower bound with an
exact overlap profile. The *objects* differ (window sets `W_w` under
`sig` vs. post-paid support families under the MCA line), and no
transfer is banked. Worth one scoping pass by whoever owns the `M`
route; it is not evidence about this node today.

---

## Rule compliance

- All computation under `tools/ramguard tiny|local -- python3`. My own
  draft-file patches were also executed as ramguard'd python scripts
  (`patch1.py`, `patch2.py`), and the `PREREG.md` append likewise. Draft
  `.py`/`.md` files were authored with the harness's own file tool,
  which runs no shell and no python; flagging the reading in case the
  coordinator wants it tightened.
- No `dag.json`, node, or tool file was edited. No git. No status flip.
- `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened. The
  quarantine clause was passed verbatim to the single search subagent
  dispatched, which confirmed it had not opened the file.
