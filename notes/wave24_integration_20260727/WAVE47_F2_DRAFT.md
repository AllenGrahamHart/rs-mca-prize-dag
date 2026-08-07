# WAVE-47 AUDIT — F2 STREAM (Codex delta since pin 88238fd0)

- **Auditor:** Opus AUDIT agent, wave-47 F2 stream, 2026-08-06.
- **Worktree:** `/home/u2470931/smooth-read-solomin/prize-codex-resolution-v11-20260803`,
  branch `codex/full-prize-resolution-v11-20260803`.
- **Pin at mandate:** `48fc9efcf`. **Actual worktree HEAD at audit time:** `cf4699f77`
  (`f8ad8cb5e` "Record F2 selector transport handoff", then `cf4699f77`, the
  coordinator's own wave-47 launch commit replayed into the worktree). Also
  `75b97465c` "Exclude periodic selectors from F2 transport" touches the critical
  node. No F2 *result* changed past the pin; audit covers the mandated set.
- **Canonical:** `/home/u2470931/smooth-read-solomin/prize` @ `59cb2f627`
  (round-20 LAUNCH); rulings commit `85c9d1536`. NOT modified by this audit.
- **Write scope:** this file only.

---

## 0. HEADLINE

**The mathematics is sound.** I independently re-derived every load-bearing
identity and every printed constant in the delta — the collision identity, the
Fourier form, the sandwich, the flatness bridge, the Newton distance transport,
both order laws, all five witnesses, all nine compositeness divisors, and the
crossing benchmark — and **all of them hold**. All 13 verifiers replay clean.

**The wiring is not.** Three blocking findings, in descending order of severity:

- **CATCH-47F-1 (BLOCKING).** Codex **overwrote canonical's MINT-4 node
  `f2_admissible_object` in place**, `PROVED -> REFUTED`, deleting its statement
  of record and a `refutes` edge. *But the mathematics behind the overwrite is
  correct and is a maintainer-level catch against canonical:* canonical's minted
  **THEOREM G1/G2 ("generating classes are exactly three") is FALSE** — it omits
  the entire `p = 3 mod 4` branch. §2.
- **CATCH-47F-2 (BLOCKING, larger than the mandate anticipated).** The critical
  node `f2_conditional_close` is **not new** — it is canonical's existing
  CONDITIONAL node, rewritten. The rewrite flipped it `CONDITIONAL -> TARGET`,
  **demoted all seven `req` edges to `ev`**, and **moved five nodes out of
  `critical/` into `background/`** (critical census 246 -> 241). Codex's own
  `audit.md` discloses **only** the Myerson removal. §5.1.
- **CATCH-47F-3 (subtraction).** `(FLOOR-1)`, `2^m Z(A) = sum_v N(v)^2`, is
  presented as new but is **already banked in canonical** — which itself marks it
  as *not canonical's either* ("**BANKED — the collision identity is NOT ours**",
  `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:31`, sourced to
  `background/nodes/dli_c1_l1_block_owner_ledger/statement.md:15,18-19`). §6.

**And one finding the coordinator should act on before anything else:**

> **URGENT — the round-20 `f2_repose` pilot is running right now on a briefing
> that CATCH-47F-1 refutes.** Its PREREG cites the three-class census in three
> separate places (`f2_repose/PREREG.md:15`, `:19-20`, `:47-48`). §5.3.

### Verdicts

| package | verdict |
|---|---|
| `f2_admissible_generating_branch_classification` | **ADOPT** — highest-value item in the delta |
| `f2_admissible_degree_order_classification` | **ADOPT** |
| `f2_generated_field_ambient_invariance` | **ADOPT** — most board-moving |
| `f2_weighted_kernel_collision_floor` | **ADOPT-WITH-EDITS** (cite the banked identity) |
| `f2_admissible_weighted_prefix_l2_identity` | **ADOPT** |
| `f2_admissible_newton_signed_distance` | **ADOPT** |
| `f2_admissible_direct_sum_grs_reduction` | **ADOPT** |
| `f2_all_admissible_direct_sum_grs_reduction` | **ADOPT-WITH-EDITS** (retarget `refutes`) |
| `f2_all_admissible_o1_mass_bound` | **ADOPT-WITH-EDITS** (superseded by the rulings) |
| `f2_minus_branch_coupled_negacyclic_reduction` | **ADOPT-WITH-EDITS** (root-disjointness residual) |
| `f2_weighted_mass_max_fiber_sandwich` | **ADOPT-WITH-EDITS** (truncated sentence) |
| `f2_fixed_weight_flatness_mass_bridge` | **ADOPT-WITH-EDITS** (knife-edge scope note) |
| `rate_half_crossing_ideal_galois_multiplicity_exclusion` | **ADOPT** |
| `f2_antipodal_selector_prefix_transport` | **HOLD** — `f2_repose` collision |
| `f2_admissible_object` (clobbered) | **REJECT the edit**; re-land as forced correction |
| `critical/nodes/f2_conditional_close` | **HOLD** — needs ratification + pilot reconciliation |

---

## 1. REPLAY (compute law: `tools/ramguard tiny -- python3 ...`, from worktree root)

All 13 node verifiers exit 0:

```
critical/nodes/f2_conditional_close                     F2_CRITICAL_ROUTE_REPAIR_PASS statuses=9/9 edges=9/9
f2_admissible_weighted_prefix_l2_identity               ..._PASS rows=4 collisions=4688 kernel_words=404 list_fibers=753 dag=2/2
f2_admissible_direct_sum_grs_reduction                  ..._PASS canonical=373/373 classes<=4 grs=1 dag=1/1
f2_all_admissible_direct_sum_grs_reduction              ..._REFUTED_PASS witness=1 survivor=1 dag=1/1
f2_admissible_newton_signed_distance                    ..._PASS small_checks=328240 floor=8589934681 dag=3/3
f2_weighted_kernel_collision_floor                      ..._PASS cases=4 collisions=786 kernel_words=168 dag=1/1
f2_weighted_mass_max_fiber_sandwich                     ..._PASS checks=16 cases=4
f2_all_admissible_o1_mass_bound                         ..._REFUTED_PASS pocklington_base=5 field_cap=1 excess=5n/12 dag=2/2
rate_half_crossing_ideal_galois_multiplicity_exclusion  ..._PASS norm_checks=816 divisibility_checks=1104 first_excluded=170752922588 dag=2/2
f2_generated_field_ambient_invariance                   ..._PASS checks=321 types=12_to_5
f2_fixed_weight_flatness_mass_bridge                    ..._PASS checks=130 cases=4
f2_antipodal_selector_prefix_transport                  ..._PASS checks=29026 cases=3
f2_minus_branch_coupled_negacyclic_reduction            ..._PASS orders=4094 surrogate_orbits=28 top_orbits=15 official=1 dag=3/3
```

**What a PASS does not mean.** Every verifier ends with a `dag=N/N` clause reading
the **worktree's own** `dag.json`. They are self-referential: Codex's wiring
checked against Codex's wiring. Nine of nine status assertions and seven of nine
edge assertions in `critical/nodes/f2_conditional_close/verify.py` **fail against
canonical** (§5.2). Green in the worktree is not integration-readiness.

### 1.1 Independent re-derivation

Everything below I computed myself under ramguard, not taken from Codex:

- `p = 2^61-1`: prime; `q = p^2` = 122 bits `< 2^256`; `2^41 | q-1`;
  `v_2(p-1)=1`, `v_2(p+1)=61`; `ord_{2^41}(p) = 2 = e`; `gcd(2^41,p-1)=2`;
  `p = 3 mod 4`. So `(v_2(p-1), e, k) = (1,2,2)`.
- `p = 3*2^41+1`: prime; `p^6` exactly 256 bits, `< 2^256`; `2^41 | p-1`;
  Pocklington base 5 valid (`5^(p-1) = 1`, `gcd(5^((p-1)/2)-1,p) = 1`).
- Newton witness: `2R+1 = 8589934681 = 2^38/32 + 89`. Exact.
- **All five** generating witnesses prime with claimed valuation/order/cap:
  `3*2^41+1` (plus, 41, ord 1), `27*2^40+1` (plus, 40, ord 2),
  `5*2^39+1` (plus, 39, ord 4), `2^61-1` (minus, 61, ord 2),
  `25*2^39-1` (minus, 39, ord 4).
- `e=6, k=2` exclusion: `p^3 < 2^128` leaves exactly `c in {1,3,5}` (plus) and
  `(b,c) in {(40,1),(40,3),(40,5),(41,1),(41,3),(42,1)}` (minus);
  `(2^43-1)^3 > 2^128` closes `b >= 43`. **All nine printed divisors correct**
  (257, 7, 3 | 3, 144899, 179, 13367, 5, 3). Enumeration exhaustive.
- Crossing benchmark: bisecting `(IG4)` reproduces first excluded
  `w = 170752922588`, last unexcluded `170752922587`, **71.1641%** — to the digit.

---

## 2. CATCH-47F-1 — the `f2_admissible_object` clobber (and why canonical is wrong)

### 2.1 The clobber

Created by **canonical's** MINT-4 `207d49732`. Rewritten by Codex's `f6fba9ad5`:

```
-    "title": "The prize-admissible F2 object: ... the generating classes are exactly three ..."
-    "status": "PROVED",            +    "status": "REFUTED",
-    "closure": "proof",            +    "closure": "counterexample",
-  "refutes": [{ "to": "u2c_giant_tnull_dichotomy" }]
+  "evidence_for": [{ "to": "f2_conditional_close" }],  "refutes": []
```

Deleted from the record: LEMMA ADM-1/2/3 with the EXACT dimension, the depth
budget, THEOREM G1/G2, **THEOREM C1 (coset factor exactly 1)**, the THEOREM A
discharge percentage, the `(M3)`-vacuous line, the provenance block, and the
`refutes -> u2c_giant_tnull_dichotomy` edge. `statement.md` retains the historical
text under a "Scope correction" header (`:11-25`), but **the statement of record
lives in `node.json`** (per the mint-4 repair `5a8f0dba0`), and there it is gone.

### 2.2 …but canonical's THEOREM G1/G2 is FALSE

Canonical `background/nodes/f2_admissible_object/node.json:15`:

> "THEOREM G1/G2: generating classes are exactly (e_p,e,k) in
> {(>=41,1,1),(40,2,2),(39,4,4)}, all non-empty with Lucas p-1 certificates;
> e in {3,5,6} can never generate since ord mod 2^41 is a 2-power."

I derived the complete list independently. Write `a = v_2(p-1)`, `b = v_2(p+1)`;
`p` odd forces `min(a,b) = 1`. By LTE, for even `e`,
`v_2(p^e - 1) = a + b + v_2(e) - 1`:

- `e=1`: needs `a >= 41`. → `(>=41,1,1)` ✓ canonical
- `e=2`, `a >= 2` (so `b=1`): `a+1 >= 41`, `a <= 40` → `a = 40`. → `(40,2,2)` ✓ canonical
- `e=2`, `a = 1`: `1+b >= 41` → **`b >= 40`. MISSING from canonical.**
- `e=4`, `a >= 2`: `a+1+1 >= 41` → `a = 39`. → `(39,4,4)` ✓ canonical
- `e=4`, `a = 1`: `1+b+1 >= 41` → **`b = 39`. MISSING from canonical.**

**Five signed types, not three** — exactly Codex's classification, same two missing
rows, both with certified prime witnesses (`2^61-1`, `25*2^39-1`), both verified
prime by me. Canonical's error is that it ran `D = 41 - v_2(p-1)` throughout
(`node.json:15`: "for D = 41 - v_2(p-1) <= 2"), which is the `p = 1 mod 4` law
only; the `p = 3 mod 4` law runs on `v_2(p+1)`.

`p = 2^61-1`, `q = p^2` is an **official, admissible, generating** row that
canonical's three-class census does not contain. Codex names the defect exactly —
`f2_minus_branch_coupled_negacyclic_reduction/audit.md:3-4`:

> "1. The order law uses `v_2(p+1)`, not `v_2(p-1)`. This is the exact defect
> in canonical Rounds 17 and 18."

I confirm that reading. **This is the highest-value item in the delta.**

### 2.3 Recommended disposition

Reject the in-place rewrite; re-land the content as:

1. a **forced-correction addendum** on canonical's `f2_admissible_object`,
   narrowing LEMMA ADM-1/2/3 and THEOREM G1/G2 to `p = 1 mod 4` and pointing at
   the five-type classifier;
2. **keep the surviving components in the record** — field cap / 16-rung tower
   inadmissibility, the trace-rank `k = ord_n(p)` correction, THEOREM C1's coset
   factor of exactly 1, provenance. Codex concedes these survive ("The field-cap,
   trace-rank, and coset-invariance components survive only in their corrected
   scopes") and then deletes them anyway;
3. **do not silently drop** `refutes -> u2c_giant_tnull_dichotomy` — whether it
   survives the narrowing is a coordinator decision, not an edit side-effect;
4. adopt `f2_admissible_generating_branch_classification` (5 types) and
   `f2_admissible_degree_order_classification` (12 types) as the census of record.

**My reading on status:** the composite as written is false, but three of its five
components are untouched. **PROVED with a narrowed statement, plus a separate
REFUTED node carrying the counterexample**, is more honest than flipping the whole
composite. Codex already built that separate node
(`f2_all_admissible_direct_sum_grs_reduction`).

---

## 3. CONSISTENCY WITH THE 2026-08-06 SCOPE AND READING RULINGS

Codex merged canonical through `fed71a06b`; its F2 commits predate the rulings
commit `85c9d1536` (21:37) — by minutes, not days. Codex has not seen them.

### 3.1 Non-generating / tower rows are IN-FAMILY — **CONSISTENT, and helpful**

`notes/pilots_20260802/CAMPAIGN_LEDGER.md:1972-1976`:

> "**SCOPE RULING (spec-derived, no intent needed).** The frozen public spec
> ("for every choice of F, L, and k"; the pinned admissibility constraints)
> contains NO generation restriction — and our own stricter-reading clause points
> the same way. **Non-generating and tower rows ARE in the challenge family.**"

Codex never argues non-generating rows out of the family. It keeps them in and
*discharges* them by exact descent —
`f2_generated_field_ambient_invariance/statement.md:43-53`:

> "For the 12 official degree/order types, the seven non-generating types
> therefore descend exactly as follows: plus (k=1,e=2,3,4,5,6) -> plus (k=e=1),
> plus (k=2,e=4) -> plus (k=e=2), minus (k=2,e=4) -> minus (k=e=2).
> Thus the final F2 extras-plus-trades count and the associated kernel-mass
> problem on every official row reduce to the five signed generating types."

**This is the right shape of answer under the ruling** — rows stay in-family, the
obligation is reduced rather than scoped away. Mechanism checked: `S = gT` gives
`p_j(S) = g^j p_j(T)`, hence `A_D = diag(g^ell) A_{W_0}` (`statement.md:35`) with
the diagonal invertible, so kernel / rank / ternary weight enumerator / weighted
mass / fibers / max-fiber / collision sum are literally identical. Sound.

Codex does not over-claim — `audit.md:10-12`: "Ambient invariance of the final
combinatorial/kernel object does not imply invariance of `(O1)`, whose
normalization and averaging space depend on `e`."

**Net:** the largest board-relevant gain in the delta, and it survives the rulings
intact. Row surface 12 types -> 5.

### 3.2 `(O1)` as posed is FALSE across the board — **WEAKER, not in tension**

`CAMPAIGN_LEDGER.md:1995-1999`:

> "CONSEQUENCE ACCEPTED: **(O1) AS POSED IS FALSE on generating rows too** — the
> two-live-values bookkeeping collapses; the F2 lane's obligation of record is the
> minimal surviving form (E[T] = 2^{n/2}·Z_1^e) with the TAIL-COUNT criterion at
> tau = 1, which is where the mathematics already stands."

`f2_all_admissible_o1_mass_bound` kills `(O1)` only on non-generating rows
(`statement.md:10-16`, the row `p = 3*2^41+1`, `q = p^6`, `k=1<6=e`). Canonical now
kills it everywhere. **Subsumed, not contradicted.**

One snag to flag rather than paper over: Codex computes its refutation "under the
governing nested reading" with `m = n/2` (`proof.md:30-32`), whereas the ruling
pins **ensemble = THE SLICE (T\*)**. The conclusion coincides, so nothing unsound
follows, but the `5n/12` excess is a pre-ruling number and must not be quoted
post-ruling without re-derivation in the slice.

### 3.3 The MASS / tail-count obligation — **CONSISTENT in form, but NOT the same tail**

Codex's whole stack is mass-form, and no node re-poses the obligation in the old
`(O1)` first-moment form:

- `f2_weighted_kernel_collision_floor/statement.md:17-18`: `2^m Z = sum_v N(v)^2`, `Z >= max(1, 2^m/p^d)`;
- `f2_admissible_weighted_prefix_l2_identity/statement.md:34-36`: "`Z_1<=2^{o(S)}`
  is equivalent to `sum_v N(v)^2<=2^{S+o(S)}`";
- `f2_weighted_mass_max_fiber_sandwich/statement.md:17`: `M^2/2^m <= Z <= M`;
- `f2_fixed_weight_flatness_mass_bridge/statement.md:43-46`.

**CORRECTION worth stating plainly:** Codex's `T_G = sum_{b notin G} binom(S,b)`
is a tail over **Hamming weights**. Canonical's criterion of record
(`f2_z1_mass_knife_edge/statement.md:62-65`) is a tail over **Fourier modes**:

> "the true criterion is the TAIL-COUNT `|{u : P(u) >= 2^{cS}}| <= 2^{(1-c)S+46+o(S)}` for all c"

These are **different objects over different index sets**. Both are "tail counts";
they are not the same criterion, and Codex's bridge does not discharge canonical's.
Do not let the coincidence of vocabulary create a false sense of convergence.

**No tension found** — but no identity either.

---

## 4. PER-PACKAGE SOUNDNESS

### 4.1 `f2_weighted_kernel_collision_floor` — **ADOPT-WITH-EDITS**

Re-derived; all four claims correct. `(FLOOR-1)` via the bijection
`(S,T) -> (eps, U)`, `eps = 1_{S\T}-1_{T\S}`, `U = S∩T`, giving
`sum_eps 2^{m-wt(eps)}`. `(FLOOR-2)` from the diagonal and Cauchy–Schwarz over
`<= p^d` nonempty fibers. `(FLOOR-3)`: per-coordinate factor
`1 + (1/2)chi(x) + (1/2)chi(-x) = 1+cos(2πx/p)`, then `1+cos 2x = 2cos²x`. Exact.

**Two subtraction findings (see §6):**

- **CATCH-47F-3.** `(FLOOR-1)` is **already banked** and canonical explicitly marks
  it as not even canonical's own. Codex cites Z-FLOOR but not the identity. Add
  the citation to `dli_c1_l1_block_owner_ledger:15,18-19`.
- The framing in `result.md:10-12` / `audit.md:10-12` — "recovers the canonical
  Round-18 Z-FLOOR result without importing the false all-admissible
  proportionality-class classification" / "does not inherit its row
  classification" — is **hollow**. Canonical's Z-FLOOR was **already
  hypothesis-free**: `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:130-131`
  states it "For **every** `F_p`-subspace `L ⊆ F_p^m` (no MDS, no GRS, no
  genericity, no randomness)". There was no row classification to shed. Strike
  the claimed distinction.

**Credit where due.** The self-correction in `938039b62` is right and independent.
`audit.md:13-16`:

> "6. For the weighted mass the Fourier factor is `1+cos`, equivalently
> `2cos^2`. The factor `1+2cos` counts ternary words without the `2^-wt` weight
> and is not the prize terminal."

This is **exactly canonical's CATCH-B1** (round-19 `tern_route_b/PROOFS.md:113`,
ledger `:1902-1903`) — and Codex's commit **predates its merge of** `fed71a06b`,
the commit that banked CATCH-B1. Two agents found the same normalization error
blind and concurrently. That is a strong correctness signal for both. Note
canonical's erroneous line still stands, disclaimed, at
`z1_ternary_mass/PROOFS.md:394`; Codex's node gives the correct form as PROVED.

### 4.2 `f2_weighted_mass_max_fiber_sandwich` — **ADOPT-WITH-EDITS**

Correct: `sum_v N(v)^2 >= M^2` gives the left half; `N(v)^2 <= M N(v)` summed gives
`2^m Z <= M 2^m`. Exact, powers of two retained.

**EDIT — truncated sentence.** `statement.md:38-39`:

```
38	This theorem is an exact interface. It does not prove `(MF-2)`, quotient
39	In particular, upstream `def:q-row-atom` bounds a first-match residual family
```

Line 38 ends mid-clause on "quotient". Introduced by `8fbc0ded5`. Cosmetic — but
this is a **nonclaim fence**, and a lost half-sentence in a nonclaim fence is
exactly the kind of thing that later gets read as permission. Restore it.

### 4.3 `f2_admissible_weighted_prefix_l2_identity` — **ADOPT**

`(L2-1)`–`(L2-4)` re-derived, correct. Nonclaims exemplary: `statement.md:34-36`
states an *equivalence*, not an implication; `audit.md:10-11` warns "A max-fiber
bound implies an L2 bound, but the converse need not hold." `audit.md:16-18`
fences the list-recovery translation properly (agreement one, list size two, rate
`1-R/S`, explicit dyadic evaluation set — "Results for random or generic
evaluation points, or with a fixed gap from list-recovery capacity, do not
automatically apply"). That is the trap that kills most list-recovery transports,
and Codex sees it.

### 4.4 `f2_admissible_newton_signed_distance` — **ADOPT**

The content is a hypothesis match and it is clean: the kernel condition is
literally `P(zeta^{2j-1}) = 0`, `j=1..R` (`proof.md:22-23`); `ord(zeta)=2S | p-1`
forces `p >= 2S+1 > w`, so the characteristic hypothesis is automatic
(`audit.md:5-7`). Base case checked by hand: at `R=1`, weight 2 needs
`zeta^{a-b} = -1 = zeta^S` with `|a-b| < S` — impossible, so `w >= 3 = 2R+1`. ✓

**Residual now closed.** Canonical's `dli_wcl_newton_short_window_exclusion` is
PROVED with statement of record (`dag.json:10671`): *"In characteristic zero or
greater than w, a reduced signed relation satisfying the first ell odd-power
equations cannot have weight w<=2ell."* That matches Codex's usage exactly —
`N=S`, `ell=R`, signs, `char > w`, initial odd run. The transport is legitimate.

Honest about limits — `result.md:7-9`: "Distance alone does not supply the
required `Z_1<=2^{o(S)}` estimate."

### 4.5 `f2_admissible_direct_sum_grs_reduction` — **ADOPT**

The `p = 1 mod 4` restriction is now correctly load-bearing and prominent
(`statement.md:44-46`). The real step is class independence (`proof.md:22-26`):
for `D <= 2`, either the two-class ratio has dyadic order exceeding `2^{e_p}`, or
in the four-class case `1, y^l, y^{2l}, y^{3l}` is an `F_p`-basis of the
degree-four extension because `l` is odd. Correct. Vandermonde on distinct
`zeta^{2s}` gives rank `min(S,R)` and the `[S,S-R,R+1]_p` kernel. Correct.

The scope correction is dated and self-flagged (`audit.md:24-28`) — the right way
to record a narrowing.

### 4.6 `f2_all_admissible_direct_sum_grs_reduction` — **ADOPT-WITH-EDITS**

Counterexample correct (§1.1). The argument (`proof.md:20-29`) is the clean one:
`|G ∩ F_p^*| = gcd(n,p-1) = 2`, so the only possible ratio between retained
antipodal representatives is `±1`, and a transversal contains neither pair-mate —
all `2^40` positions are singleton classes, against `C <= 4`.

`audit.md:8-10` carries a non-obvious observation that stops the refutation
over-reaching:

> "4. Singleton proportionality classes do not imply independent prime-field
> equations: the Frobenius action couples the positions over `F_{p^2}`. Therefore
> the minus branch needs a different kernel model."

**EDIT:** `node.json:30-34` declares `"refutes": [{"to": "f2_admissible_object"}]` —
the wiring half of the clobber. Retarget to whatever narrowed object canonical
keeps, and confirm the convention for `refutes` edges emitted by REFUTED nodes.

### 4.7 `f2_all_admissible_o1_mass_bound` — **ADOPT-WITH-EDITS**

Arithmetic verified. Chain `E >= 4^m/p^{dim L} >= 2^{m(2-k/e)} = 2^{11m/6}` against
a `2^{m+o(n)}` target leaves `2^{5m/6} = 2^{5n/12}` at `m = n/2`. Internally correct.

**EDIT:** addendum recording that the 2026-08-06 rulings supersede this upward —
`(O1)` is false on generating rows too, so this is now a special case, and its
`5n/12` is a pre-ruling-ensemble constant (§3.2).

### 4.8 `f2_admissible_generating_branch_classification` — **ADOPT (highest value)**

Carries CATCH-47F-1. Five signed types, each with a certified prime witness, all
five verified independently (§1.1). Certificates are deterministic —
`audit.md:7-8`: "Four witnesses use complete-factor Pocklington certificates; M61
uses Lucas--Lehmer. No probabilistic primality test is part of the proof."

`statement.md:31-33` states the consequence plainly:

> "Therefore an unsigned census containing only the three `p=1 mod 4` types is
> not an all-admissible generating-row census."

### 4.9 `f2_admissible_degree_order_classification` — **ADOPT**

12 types, exhaustive, seven non-generating. The only nontrivial step —
excluding `e=6,k=2` — is done properly: `p^6 < 2^256 => p^3 < 2^128` bounds the
candidates to a finite list and **every** one is dispatched with a printed divisor.
All nine candidates, all nine divisors, and the `b >= 43` cutoff verified. Correct
and exhaustive. `audit.md:3`: "`k|e` is retained; generation is not assumed" —
which is what makes it the right base for the descent.

### 4.10 `f2_minus_branch_coupled_negacyclic_reduction` — **ADOPT-WITH-EDITS**

`(MINUS-ORDER)` verified: `v_2(p^{2^j}-1) = b+j` gives
`ord_{2^a}(p) = 2^{max(1,a-b)}`; `k in {2,4}` forces `b >= 39`. At `p = 2^61-1`,
`b = 61`, `k = 2` — matches my computed order. `(MINUS-RANK)` is structurally
right: `F_p` coefficients force Frobenius closure; `Omega` stable so
`G_W ∈ F_p[X]`; roots distinct so `K_W = G_W·F_p[X]_{<m-hR}`.

**Residual / EDIT.** Root **disjointness** (`|Omega| = hR`) is argued informally,
`proof.md:31-38`:

> "If `b` is at least the modulus exponent, Frobenius sends a small odd exponent
> to its negative. At the next modulus it sends it to its negative translated by
> the half-period; in the unique order-four case `b=39`, the four images occupy
> the four quarter-period bands. Their widths are below one eighth of the smallest
> modulus, so these bands are disjoint."

A band-separation argument leaning on `2R < 2^36` vs `2m >= 2^39`. Very likely
correct, and the verifier corroborates — but on **surrogates**, not at official
scale, and this is the weakest prose in the delta. Request a closed-form
inequality on exponent bands before it is quoted as PROVED downstream. Everything
above it (order law, code model, `(MINUS-L2)`, the `2R+1` distance) is independent
of the phrasing.

### 4.11 `f2_generated_field_ambient_invariance` — **ADOPT**

See §3.1. Elementary, exactly right, most board-relevant after §4.8.
`claim_contract.md:10-12` fences it properly.

### 4.12 `f2_fixed_weight_flatness_mass_bridge` — **ADOPT-WITH-EDITS**

`(FW-2)`/`(FW-3)` re-derived line by line; correct. Minkowski on `N = sum_b N_b`;
`sum_v N_b(v)^2 <= M_b B_b`; bad weights `<= B_b` each (total `T_G`); good weights
`<= sqrt(L)(sqrt(B_b)+B_b/sqrt(Q))`; `sum_b sqrt(B_b) <= sqrt((S+1)2^S)`; then
`(a+b+c)^2 <= 3(a^2+b^2+c^2)`, divide by `2^S`. Exact. Complementation `x -> 1-x`
shifts syndromes by `A1` and does not need `A1 = 0` (`audit.md:8-9`). Correct.

**EDIT — connect to the knife edge.** `statement.md:48` says "For the F2 branch
maps the natural value is `Q=p^d`", and the asymptotic clause needs
`2^S/Q = 2^{o(S)}`. Codex never evaluates this at its own banked witness.
Canonical has — `f2_z1_mass_knife_edge/statement.md:46-53`:

> "**THE KNIFE EDGE.** At k = e the Z-FLOOR is silent by 46.02 bits out of
> 2.75e11 under the banked R = ceil(t/2) reading — ONE Lambda condition, worth
> log2 p = 64 bits — and FIRES at +17.98 bits under the exact-balance reading
> (in which case ternary kernel vectors provably exist at the witness row:
> Z_1 >= 2^{17.98}, the EXACT-ZERO form of the terminal is dead, yet
> Z = 2^{o(n)} so the MASS form survives). The two defensible t-readings
> straddle zero."

Same object: canonical's `S = 2^40/e = 2^38` at `e=4` and its `2R+1 = 8,589,934,681`
(`:30`) are **Codex's exact witness parameters**. So the bridge's hypothesis at
the witness holds by **46.02 bits under one reading and fails by 17.98 under the
other** — and since `S = 2.75e11`, `2^{±46}` and `2^{17.98}` are both `2^{o(S)}`,
so **the bridge survives either way**. It is a true conditional and not a soundness
defect. But shipping it without printing the margin invites a reader to treat a
reading-dependent knife-edge hypothesis as free. Print the margin and cite the
knife-edge node.

*(Correcting my own working: computing at the ceiling `log2 p = 64` gives a 2816-bit
margin, but `p = 2^64` is not attainable — `p^4 < 2^256` forces `p < 2^64`.
Canonical's 46.02 bits, computed at the actual witness prime, is the real number.)*

### 4.13 `f2_antipodal_selector_prefix_transport` — **HOLD**

Math correct and rather elegant. Per-pair contribution
`x_s theta^{sl} + (1-x_s)(-theta^s)^l` is `theta^{sl}` for even `l` and
`(2x_s-1)theta^{sl}` for odd `l` (`proof.md:9-14`) — hence `(AS-1)`; `2` invertible
recovers `A(x)`; forgetting the transversal condition gives `(AS-2)`; Newton with
`2R < p` converts power-sum prefixes to elementary-symmetric prefixes.

The aperiodicity corollary is a genuinely nice observation (`statement.md:51-54`):
every nontrivial subgroup of a cyclic 2-group contains `-1`, but
`E_x ∩ (-E_x) = ∅`, so no selector image lands in the quotient-periodic bucket.

**SCOPE NOTE — this corollary is POST-PIN.** It is the only audited object that
drifted past `48fc9efcf`: added by `75b97465c` "Exclude periodic selectors from F2
transport", i.e. **wave-48 material**. The pinned version of this node did not have
it, and its nonclaim fence at the pin read "quotient/common-divisor removal"; the
post-pin edit narrows that to "common-divisor removal" on the strength of the new
corollary. I checked the corollary and the narrowing is legitimate — but the
coordinator should book it under wave 48, not wave 47. Everything else I audited
(including `f2_conditional_close/statement.md` and `verify.py`) is **byte-identical
to the pin**.

Nonclaims correct — `statement.md:60-65` and `audit.md:12-13` ("Forgetting the
transversal condition is an upper-bound injection. It is not equality with the
full split-locator fiber").

**HOLD, not ADOPT:** this is precisely the object the round-20 `f2_repose` pilot
exists to build. §5.3.

### 4.14 `rate_half_crossing_ideal_galois_multiplicity_exclusion` — **ADOPT**

Structure standard and correct: `p` odd hence unramified; decomposition group
`<sigma_p>`; `sigma_p(x_s) = x_{ps}` propagates containment around `p`-orbits; odd
`s` are units so `x_s = sigma_s(x_1)`; counting distinct primes modulo the
decomposition group and restoring residue degree yields exponent `|Z_w^odd(p)|`.
`(IG2)`'s orthogonality identity `sum_{c odd}|x_c|^2 = (n/2)(r - a_{n/2}(S))` is
right (odd-character sum is `n/2` at `d=0`, `-n/2` at `d=n/2`, `0` else), and AM-GM
over the `h = n/2` embeddings gives the ceiling. Benchmark reproduces exactly (§1.1).

The `audit.md:20-29` "Catches during transport" block is model practice — three
real defects in the imported material recorded and fixed (the `71.16%` headline was
not uniform in `q = p^e`; the tower display discarded floors; the source bisection
mislabelled the boundary). And commits `d157a7579`, `88c083661`, `30c41bce2`
preserve Codex's **own failed runs** rather than deleting them (`audit.md:33-34`).
That is the behaviour the campaign wants.

Note: this node is genuinely new to canonical — no id containing
`galois_multiplicity` exists there.

### 4.15 `critical/nodes/f2_conditional_close` — **HOLD**

Content is defensible: honest that the target is not refuted (`statement.md:28`),
does not assume `(O1)` (`claim_contract.md:15-16`), prints an attack surface
rather than a route. But it cannot land until §5.1 is adjudicated and `f2_repose`
banks.

---

## 5. WIRING, INTEGRATION, COLLISION

### 5.1 CATCH-47F-2 — the critical node is a rewrite, and it moved five nodes off the critical surface

**The mandate calls `f2_conditional_close` a NEW CRITICAL NODE. It is not.**
Canonical already has `critical/nodes/f2_conditional_close/` (node.json +
statement.md) at status CONDITIONAL, from the 2026-07-10 route commitment. Codex's
`6ab149e67` rewrote it and expanded it to a 7-file package.

What the rewrite actually did, beyond the disclosed Myerson removal:

| | canonical | worktree |
|---|---|---|
| status | CONDITIONAL | TARGET |
| incoming edges | **7, all `req`** | **21, all `ev`** |
| `requires` | 7 entries | `[]` |
| critical node dirs | **246** | **241** |

The seven demoted `req` edges were `f2_growing_order_myerson` (TARGET) **plus six
PROVED skeleton nodes**: `f2_newton_empty_extremes`, `f2_edge_lemma`,
`f2_full_ladder_dictionary`, `f2_k1_contraction_theorem`, `b2b_near_tail_bound`,
`b1_char0_giant_coset_theorem`. Canonical's own statement records that this wiring
was **deliberate**:

> "PROOF-SKELETON WIRING (2026-07-10, completing the route commitment): the
> assembly's proved inputs are now req-wired … so the committed chain's green
> skeleton is on the critical surface alongside its one red leaf (the summit)."

And **five node directories were moved from `critical/nodes/` to
`background/nodes/`**: `f2_edge_lemma`, `f2_full_ladder_dictionary`,
`f2_k1_contraction_theorem`, `f2_newton_empty_extremes`, `f2_growing_order_myerson`.

**Codex's `audit.md:31-33` discloses only one of these changes:**

> "This surgery does not mark the target false and does not delete the proved July
> suppliers. It changes `CONDITIONAL -> TARGET`, removes Myerson from `requires`,
> keeps it as evidence, and prints the all-row attack surface."

It says "removes Myerson from `requires`". It removed **seven** entries from
`requires` and relocated **five** nodes off the critical surface. Nothing is
deleted from disk and the six PROVED suppliers survive as `ev`, so this is
**under-disclosure, not destruction** — but a five-node critical-census change
recorded as "removes Myerson from requires" is exactly what the surfacing rule
exists to catch.

**Is the change defensible on the merits?** Partly. If the close is genuinely
re-posed as a bare TARGET, its former conditional suppliers arguably become
evidence. But (a) that is a board decision, (b) the critical census is a published
number, and (c) `req` -> `ev` on six PROVED nodes changes what the critical orbit
computes. **Surface for ratification; do not auto-apply.**

### 5.2 The package does not verify against canonical

`critical/nodes/f2_conditional_close/verify.py` asserts nine statuses and nine
edges. Against **canonical's** `dag.json`:

| assertion | canonical | worktree |
|---|---|---|
| `f2_conditional_close == TARGET` | **CONDITIONAL** | TARGET |
| `f2_admissible_direct_sum_grs_reduction == PROVED` | **ABSENT** | PROVED |
| `f2_growing_order_myerson == TARGET` | TARGET | TARGET |
| `f2_all_admissible_o1_mass_bound == REFUTED` | **ABSENT** | REFUTED |
| `f2_all_admissible_direct_sum_grs_reduction == REFUTED` | **ABSENT** | REFUTED |
| `f2_weighted_kernel_collision_floor == PROVED` | **ABSENT** | PROVED |
| `f2_minus_branch_coupled_negacyclic_reduction == PROVED` | **ABSENT** | PROVED |
| `f2_generated_field_ambient_invariance == PROVED` | **ABSENT** | PROVED |
| `f2_admissible_object == REFUTED` (`verify.py:35`) | **PROVED** | REFUTED |

Seven of eight asserted `ev`/`req` edges are absent from canonical, and the
`req` edge `f2_growing_order_myerson -> f2_conditional_close` that `verify.py:44`
asserts must **not** exist **does** exist there. All-or-nothing.

Census delta if adopted wholesale: canonical 1824 nodes / 5084 edges →
1838 / 5115. **15 worktree-only ids**: the 14 F2/crossing nodes audited here plus
`dli_wcl_weight5_squared_root_hypersurface_router` (the sibling auditor's stream).
Confirmed independently: none of the 12 new F2/crossing ids appears **anywhere** in
the canonical checkout.

**Only the `f2_admissible_object` row is a genuine contradiction.** The other eight
are "canonical hasn't seen these yet".

### 5.3 Collision with the running round-20 `f2_repose` pilot

**FIRST — the time-sensitive item.** `f2_repose/PREREG.md` briefs the pilot on the
census CATCH-47F-1 refutes, in three places:

- `:15` — "EXACTLY on the three generating classes"
- `:21` — "background/nodes/f2_admissible_object — the exact structure (ADM-2
  direct sum, dim L exact, **the three-class census**, C1)"
  *(line refs drift — the pilot is editing its own PREREG live; the quoted text is
  the stable anchor)*
- `:47-48` — "(i) the coset/class decomposition (**ADM-1/2 still holds** — dim L
  exact — only the BALANCE dies)"

ADM-1/2 holds **on the plus branch only**. A pilot that prices R3(i) on
minus-branch rows using ADM-1/2 will build on a false premise. **Recommend an
immediate correction to the pilot**, or accept that R3(i) will need re-doing.

**SECOND — the deliverable-by-deliverable overlap** (PREREG `:29-58`):

| deliverable | status against Codex's delta |
|---|---|
| **(R1) consumer contract** | **NOT built.** No node states what the downstream chain needs. `f2_weighted_mass_max_fiber_sandwich` is a *supplier-side* interface, not the consumer contract. Pilot owns this. |
| **(R2) re-posed intermediate at generating rows** | **Partially collided.** The PREREG asks to "test WEAKER candidates first … a quantile/median statement". Codex has **not** done a median version. But it *has* sharpened "generating rows" from three classes to five (§4.8) — which changes R2's domain. |
| **(R3) non-generating rows** | **HEAVILY COLLIDED.** `f2_generated_field_ambient_invariance` answers R3 essentially completely, and in a form the PREREG did not anticipate: not "a different lane" (option iii) but *the same lane at k=e*, by exact identity of the final objects. The pilot is running blind on a question Codex has largely closed. |
| **(R4) lane statement draft** | **NOT built** as a lane statement, though `f2_conditional_close/attack.md` is close in spirit. |

**Also already built (pilot may duplicate):**
1. The mass-form terminal, `M^2/2^m <= Z <= M` (`f2_weighted_mass_max_fiber_sandwich`).
2. The fixed-weight -> full-cube bridge with an explicit tail hypothesis
   (`f2_fixed_weight_flatness_mass_bridge`) — note §3.3: **a different tail** from
   canonical's criterion.
3. The upstream transport (`f2_antipodal_selector_prefix_transport`), which removes
   the weighted-map mismatch with `prob:capfr1-master-flatness` and correctly names
   the two obligations that remain (normalized-band scope; common-divisor /
   first-match owner decomposition).
4. The row surface cut, 12 types -> 5.

**NOT built by Codex — pilot still owns:** any **upper** bound on `Z` (every node
in the delta is a floor, identity, interface, or reduction); the normalized-band
placement and owner decomposition; **PP5.0**; reconciliation with the ruled slice
ensemble; and the median/quantile weakening the PREREG specifically asks for.

**Recommendation:** brief the pilot on items 1–4 at the earliest safe point, or
accept the duplication as independent replication and reconcile at bank. The
sandwich and the bridge are cheap and should agree exactly; disagreement would
itself be a catch. **The ADM-1/2 correction should not wait for the bank.**

---

## 6. SUBTRACTION CHECK

**Uncited re-derivation — ONE hit (CATCH-47F-3).** `(FLOOR-1)`,
`2^m Z(A) = sum_v N(v)^2`, is presented as new content of
`f2_weighted_kernel_collision_floor`. It is already banked in canonical, at
`background/nodes/f2_z1_mass_knife_edge/statement.md:19-21` ("the banked collision
identity sum_s |F_s|^2 = 2^m Z(L) (dli_c1_l1_block_owner_ledger:15,18)"), derived
in full at `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:139-155` — and canonical
marks it as **not even its own**:

> "**BANKED — the collision identity is NOT ours.**"
> — `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:31`

Codex cites Z-FLOOR (the inequality) but not the identity (its input). Add the
citation. Per the fifth-surface rule, this is exactly the case where our own
`background/` and `notes/` had to be grepped before claiming novelty.

**Related over-claim (§4.1):** "does not inherit its row classification" is
hollow — canonical's Z-FLOOR was already hypothesis-free
(`z1_ternary_mass/PROOFS.md:130-131`). Strike the distinction.

**Everywhere else, Codex cites canonical by name** —
`f2_weighted_kernel_collision_floor/audit.md:10-12` and `result.md:10-12`;
`f2_conditional_close/audit.md:20-22`;
`f2_minus_branch_coupled_negacyclic_reduction/audit.md:3-4`.

**Genuinely new (my assessment):**

1. **The five-type generating classification + the minus-branch order law.**
   Corrects canonical's minted three-class census. **Maintainer-level.**
2. **Generated-field ambient invariance** — 12 official types -> 5, with `(O1)`
   explicitly not restored. Board-moving if it survives.
3. **The `M^2/2^m <= Z <= M` sandwich** and the **fixed-weight -> full-cube bridge**.
4. **The antipodal-selector transport** and its aperiodicity corollary.
5. **The `e=6, k=2` exhaustive exclusion** with printed divisors.
6. **The whole crossing node** — no `galois_multiplicity` id exists in canonical —
   plus its three transport catches.
7. `(FLOOR-3)`'s `1+cos` form as a **PROVED node**: not new as a *fact* (canonical's
   CATCH-B1), but **independently and concurrently derived**, and canonical's
   erroneous `1+2cos` line still stands disclaimed at `z1_ternary_mass/PROOFS.md:394`.
   Convergent confirmation, not novelty — and worth recording as such.

**Reverse direction — canonical work Codex has not seen:** the 2026-08-06 rulings
(§3); the tail-count criterion in its exact Fourier form (§3.3); the knife-edge
constants (§4.12); THEOREM Z-NOGO, THEOREM 7, `tern_master_threshold`.

---

## 7. HONEST RESIDUALS

1. **Minus-branch root disjointness** (§4.10) is prose corroborated only on
   surrogates. Needs a closed-form inequality.
2. **All verifiers are self-referential on `dag.json`.** I cross-checked the wiring
   against canonical by hand (§5.2); no automated cross-tree check exists.
3. **Modal app ids unreplayed.** ~10 apps cited across audit/result files
   (`ap-gc4EOdiUFEghRR4qkIjUfX`, `ap-bMpQIqA5drSKk82JQgIgGa`,
   `ap-JNBoN1s1INvr1ovkHvbf8h`, …). I replayed local verifiers only.
4. **`(O1)` ensemble mismatch** (§3.2) — conclusion agrees, constant does not transfer.
5. **Knife-edge reading** (§4.12) — the bridge survives both readings, but which
   reading is of record still "belongs to the t-naming/ensemble maintainer stack"
   per canonical's own text.
6. **I did not audit the sibling WCL router** `dli_wcl_weight5_squared_root_hypersurface_router`,
   which is also worktree-only — other auditor's stream, flagged only so it is not
   lost in the census delta.
7. **Whether `refutes -> u2c_giant_tnull_dichotomy` survives** the narrowing of
   `f2_admissible_object` (§2.3) is a genuine open question I am not positioned to
   decide — it depends on which component of the composite carried that edge.
8. **Worktree is dirty** — modified `experiments/prize_resolution/verifier_replay.json`
   + untracked results, all in the `rate_half_kb_positive_433` lane, unrelated to F2.

### 7.1 Post-pin drift (for wave-48 booking, not wave-47)

Codex kept working during this audit; worktree HEAD moved `48fc9efcf` ->
`cf4699f77` -> `a16df47ef`. Per the coordinator's own pin (`f4143ab2f`: "audit head
pinned 48fc9efcf; Codex live, post-pin queues for wave 48"), the following are
**wave-48 items, deliberately outside this report's verdicts**:

- `75b97465c` "Exclude periodic selectors from F2 transport" — the aperiodicity
  corollary (§4.13). The only audited object that drifted.
- `e70368fe7`, `0c972e31f` "Reduce F2 selector fibers to primitive faces" — a **new
  background node `f2_selector_face_primitive_reduction`** (7 files + verifier).
  Not audited.
- `a16df47ef` merges canonical `master` into the Codex branch. **Consequence worth
  noting: as of that merge Codex HAS now seen the 2026-08-06 rulings**
  (`crossing_dsa_refutation` +14, `f2_o1_status_split` +16, `tern_master_threshold`
  minted, all present post-merge). The §3 reconciliation items should therefore be
  cheaper at wave 48 than they look here — Codex can do them itself.
