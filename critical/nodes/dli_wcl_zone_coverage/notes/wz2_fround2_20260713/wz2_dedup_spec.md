# wz2_dedup_spec.md — canonical first-owner de-duplication (WCL-ZONE, F-round 2, PART 0)

- **Date:** 2026-07-13, F-round 2 against `dli_wcl_zone_coverage`. Written BEFORE
  the round-2 pre-registration and before any round-2 computation.
- **Object specified:** the phrase in the M3 CORRECTED POSE
  (`critical/nodes/dli_prime_weighted_large_block_support/notes/M3_ENDPOINT_EXCEPTION_COVERAGE.md`
  lines 103-106): W_cl is summed over the complete reduced primitive
  signed-shift orbit ledger "after generated-field normalization and
  **first-owner de-duplication of multiplier shadows and level lifts**."
  Round 1 established (wz-C2/wz-C8, catches #191/#197-adjacent) that NO repo
  script implements this and that it is material (observed W_cl 4 -> 1).
- **Method:** every clause below is grounded in a banked artifact where one
  exists (file + line cited); where the banked machinery is silent or two
  banked artifacts disagree, the clause is marked **RATIFY-n** with a stated
  default. The spec is normative for round 2's module; it is *proposed*
  normative for the node pending maintainer ratification of RATIFY-1..8.
- **Banked sources read for this spec:**
  - `notes/m2_c1prime_level_scaled_modal.py` (M2 enumerator: pinned embedding,
    orbit key, primitivity, ledger mass — NO dedup of any kind).
  - `notes/modal_dli_orbit_census.py` lines 194-235 (`ring_mult_shift`,
    `multiplier_edge` = weight-2 multipliers `1 +- z^b` both directions,
    `independent_components` union-find).
  - `notes/empirical_M_ledger.py` lines 6-11, 37-66 (union-find over
    ternary-multiplier edges "exactly the census convention"; each component
    charges its **minimal-weight orbit as the generator**).
  - `notes/ORBIT_CENSUS_SUMMARY.md` items 1 (weight-<=2 / weight-<=3
    multiplier closures), 5 (exponent-doubling lift is an identity, 57/57;
    "charge a coincidence once at its minimal level").
  - `notes/pro_reply_round7_fulfilment.md` section 4.2 (exact any-weight
    ternary-multiplier check by modular inversion + unique-solution ternarity
    + exact Z re-verification; section 4.3 level-lift parity screen).
  - Round-1 freeze: `background/nodes/dli_wcl_zone_coverage/notes/wz_fround1_20260713/wz_falsifiers.md`
    section 0.7-0.8 and `wz_census_modal.py` (`shadow_pairs`, `shadow_dedup`,
    `shard_band_c` lift dedup).

## 1. Ambient objects (pinned, no new choices)

1. **Row** `(q, n'=2N, L)`, `q ≡ 1 (mod n')`; ring `R_N = Z[z]/(z^N+1)`;
   pinned embedding `omega = g^((q-1)/n') mod q`, `g` = smallest primitive
   root (M2 script lines 31-45, 72; census header).
2. **Vector**: ternary, support in `[0,N)`, coefficients in `{+1,-1}`;
   normalized = lowest-position nonzero coefficient `+1`. Canonical sparse
   form: sorted tuple `((pos, coef), ...)` (round-1 `normalize`).
3. **Signed-shift action**: multiplication by `z^s`, `s in [0,2N)`, with fold
   `z^N = -1`, together with global `-1` (census `ring_mult_shift`; M2
   `orbit_key`; identical semantics).
4. **Orbit** `O`: closure of a vector under the action; **REP(O)** = the
   lexicographically minimal normalized sparse tuple among members (round-1
   `orbit_partition`). *Note:* M2's `orbit_key` (dense lex-min) is an equally
   canonical per-orbit key but induces a DIFFERENT cross-orbit order.
   **RATIFY-1**: canonical cross-orbit order = (weight asc, sparse REP lex
   asc). Default grounds: the only banked code that ever ordered orbits for
   ownership is the round-1 freeze, which used exactly this.
5. **Window ledger** at `(row, L)`: primitive orbits with
   `L+1 <= w(O) <= L+5`; primitive = no proper signed sub-vector vanishes at
   ALL levels `l = 1..L` (M2 lines 96-131).
6. **Mass**: literal `2N * 2^-w(O)` per orbit (pose text `2 N_L 2^(-w(O))`;
   M2 line 187 `Fraction(count*2*N, 2**weight)`), INCLUDING degenerate
   (small-stabilizer) orbits. At composite `n'` degenerate orbits are
   systematic: any vector divisible by `Phi_{n'}` lies in the 2-power-factor
   component where `z^{N/odd-part-period}` acts as the scalar `-1` (e.g.
   `n'=96`: `z^16 P = -P`, normalized orbit size 16 not 96). The literal
   charge overcounts their true member mass — conservative (upper) for the
   WCL-ZONE <= 1/32 direction, ANTI-conservative for the C1' allowance
   direction (see section 6). **RATIFY-2**: keep the literal charge (default:
   yes — it is the pose's and M2's letter).

## 2. Multiplier shadow

**D1 (shadow witness).** For orbits `O_i != O_j` in the SAME (row, level)
window: a witness from `O_i` to `O_j` is a ternary `m in R_N`
(coefficients in `{0,+1,-1}`, `m != 0`) with

```text
REP(O_i) * m = eps * z^s * REP(O_j)   in R_N,  eps in {+-1}, s in [0,2N).
```

*Representative-independence lemma:* replacing either REP by any other orbit
member only re-parametrizes `(eps, s)`; the existence of a witness is a
property of the ordered orbit pair. (One line: the action is exactly
multiplication by `eps' z^{s'}`, which commutes into the equation.)
Conformance-tested (T5).

**D2 (decision procedures, banked).**
- *(a) Bounded-weight sweep* (census convention): witnesses with
  `w(m) <= 3`, decided by exhaustive enumeration with exact integer
  arithmetic. Grounds: `multiplier_edge` (weight-2 form `1 +- z^b`,
  census lines 204-215) and the banked weight-<=3 closure of
  ORBIT_CENSUS item 1 which collapsed the config-B tails.
- *(b) Exact division* (round-7 convention): if the `N x N` left-multiplication
  matrix `M_i` of `REP(O_i)` is invertible modulo an auxiliary prime
  `p0 = 1000003` (fallback 1000033, 1000037, 1000039, 1000081), solve
  `M_i m = eps z^s REP(O_j)` mod `p0` for all `2*2N` signed shift targets;
  accept iff the unique modular solution is ternary AND the product identity
  re-verifies exactly over `Z`. This decides D1 for ANY-weight ternary `m`:
  a ternary integer solution reduces to the unique mod-p solution, and
  acceptance is gated by the exact Z check, so no false accepts and no false
  rejects (round-7 section 4.2; round-1 freeze 0.7).

**D3 (canonical relation).** A shadow LINK `{O_i, O_j}` exists iff a witness
exists in EITHER direction (symmetrized; grounds: `independent_components`
tests `multiplier_edge(vi,kj) or multiplier_edge(vj,ki)`). Shadow COMPONENTS
= connected components of the link graph within one (row, level) window.
The witness relation is not transitive by algebra; component closure is the
banked bookkeeping convention (ORBIT_CENSUS item 1 "modulo ... multiplier
closure"; `empirical_M_ledger` union-find). **RATIFY-3**: component-closure
semantics (default: components, per the two banked codes).

**D4 (singular sources — forced by composite n').** At 2-power `N`,
`z^N + 1` is irreducible, every nonzero `REP` is invertible in
`R_N (x) Q`, and D2(b) always applies — this covers ALL banked cells and
ALL round-1 cells (the aux fallback never fired on data). At composite `n'`
(analogue 96/192; OFFICIAL `n'_L = 512L` for every `L` with odd part > 1)
the ring splits, vectors divisible by a cyclotomic factor of `z^N+1` are
zero divisors, `det M_i = +-Res(REP, z^N+1) = 0` over `Z`, and D2(b) is
structurally inapplicable — this is not an edge case, it hits exactly the
forced/semi-forced orbits that make composite `n'` interesting.
**CANONICAL RULE**: for a singular source `O_i`, the witness search from
`O_i` is restricted to `w(m) <= 3` and decided by D2(a). The relation is
then the union over sources of the applicable procedure (any-weight when the
source is invertible, weight-<=3 when singular), symmetrized per D3.
**RATIFY-4**: this asymmetry. Default grounds: weight-<=3 closure is the
only banked bounded convention; Appendix A specifies the candidate upgrade
(factor-wise exact division with the annihilator component of `m` pinned to
zero) which restores any-weight detection at the cost of a new convention
with no banked precedent. Consistency control: on invertible sources, every
link found by (a) must also be found by (b) (a-witnesses are b-detectable);
tested (T8).

**D5 (first owner, shadow pass).** Sort the window orbits by the RATIFY-1
total order. Owner of each shadow component = its minimal element; all other
members are dropped. Grounds: `empirical_M_ledger` charges the
minimal-weight orbit of each component as the generator (lines 9-11, 66);
weight-ties broken by REP lex (round-1 freeze; the banked ledger never
needed the tie-break because it only counted). Properties: at least one
owner survives per component, so the shadow pass NEVER empties a nonempty
window (P4).

## 3. Level lift

**D6 (lift maps).** For an integer `k >= 2` with `k | N`, define
`D_k : R_{N/k} -> R_N`, `sum v_y z^y  |->  sum v_y z^{ky}`.
Pinned-embedding identity: with the same smallest primitive root `g`,
`omega_{2N}^k = g^{k(q-1)/(2N)} = omega_{2N/k}` EXACTLY, hence for every
level `l`: `(D_k v)(omega_{2N}^{2l-1}) = v(omega_{2N/k}^{2l-1})`.
Consequences (each conformance-tested):
  - `D_k` maps level-`1..L` vanishers to level-`1..L` vanishers, preserves
    weight, and maps orbits into orbits (`z`-shift at the source becomes the
    `k`-step shift at the target; fold signs agree since
    `z^{k(N/k)} = z^N = -1`).
  - Primitivity transfers at matched level depth: sub-vectors correspond
    bijectively and have EQUAL level values.
Banked grounds: `k=2` is the census lift identity (ORBIT_CENSUS item 5,
57/57; census header `omega_64^2 = omega_32`). `k > 2` follows from the same
one-line identity but has never been exercised on banked data.
**RATIFY-5**: include all `k >= 2, k | N` (default: yes; round 2 validates
`k=3` on data as a required-to-hold control).

**D7 (admissible source rows).** Source rows of target `(q, 2N, L)`:
`(q, 2N/k, L)` for each `k` of D6. `q ≡ 1 (mod 2N/k)` is automatic. The
source must be ADMISSIBLE in the C1' row-family sense: balance
`2^{N/k} >= q^L` and aspect `N/k >= 16L`. Ownership against inadmissible
rows is vacuous (round-1 freeze 0.8, stated per cell, never silently
skipped). **RATIFY-6**: admissibility (family membership) as the gate,
rather than mere well-definedness (default: round-1 freeze).

**D8 (lift ownership).** Target window orbit `O` is LIFT-OWNED iff for some
admissible source row and some `k`, there is a primitive level-`L` vanisher
`v` of the source row with `w(v) = w(O)` and `D_k(v)` a member of `O`.
First owner = the admissible source row with minimal `N/k` ("first owner =
minimal admissible N", round-1 freeze; "charge a coincidence once at its
minimal level", ORBIT_CENSUS item 5). Lift-owned orbits are dropped from the
target ledger; the lift pass CAN empty a window (by design — the mass is
charged at the owner row). Official-tower reading: rows are levels
`L | L'` with `k = L'/L` and `n'_{L'} = k n'_L`; the same `D_k` applies, the
source object must vanish at levels `1..L'` (evaluated in the source row via
the D6 identity), and windows differ across levels so cross-level ownership
bites only on the window intersection `[L'+1, L+5]`.
**RATIFY-7**: whether the source object must lie in the source row's OWN
window or merely be a primitive vanisher of the right weight (coincident at
fixed `L`, divergent cross-level; default: primitive vanisher whose weight
is in the TARGET window, which is the round-1 behavior read at fixed `L`).

## 4. Composition and output

**D9 (composition order).** Canonical dedup = **LIFT pass first** (D8), then
**SHADOW pass** (D5) on the surviving orbits. Rationale (grounding, not
proof): minimal-row ownership is the census's cross-row primitive rule
(item 5); shadows are within-row bookkeeping (item 1); round 1 computed the
two passes only separately (wz-C8), so the order is genuinely new content.
The order is MATERIAL: a lift-owned orbit may be the would-be shadow owner
of another orbit; lift-first re-assigns that component to its next-smallest
member, shadow-first would drop the other orbit entirely. **RATIFY-8**
(round 2 computes BOTH orders on its replay cells and reports every diff).

**Deduplicated ledger** = surviving orbits; `W_cl^dedup` = their literal
mass sum (exact rational). Reported alongside: `W_cl^raw`,
`W_cl^{shadow-only}`, `W_cl^{lift-only}`, and the owner list.

## 5. Worked micro-examples

(Values marked [R2] are computed by the round-2 conformance run; the spec
fixes the setup and the required qualitative outcome.)

- **E1 (banked accident row).** `(q, N, L) = (7937, 32, 1)`, raw banked
  ledger `0/2/8/31/126`, `W_cl^raw = 236` (M2). All sources invertible
  (2-power `N`). Round-1's M-2 control found ternary-multiplier links from
  the two `w=3` orbits into the window. Under this spec the two `w=3` orbits
  are the earliest owners; every `w=4..6` orbit in their components is
  dropped. Additionally the row has an ADMISSIBLE `N=16` companion
  (`2^16 >= 7937`, `16 >= 16`), so the lift pass is ACTIVE on this banked
  row — a fact no banked artifact ever priced. Deduped value [R2]: a
  FINDING, not a correction of M2 (M2's banked numbers are raw by
  construction, wz-C2).
- **E2 (synthetic shadow).** Any primitive `P` and the reduced ternary
  `(1+z)P`: `m = 1+z` is a witness; the pair must link (round-1 M-2
  synthetic; conformance T3).
- **E3 (composition order).** Round-1 cell `C/b21, q = 2100353, N=64, L=1`:
  raw `W_cl = 44`, round-1 shadow-only `34` (10 links), round-1 lift data
  banked in `wz_shard_band_c.json`. Both composition orders are computed
  [R2]; any owner-set difference is the RATIFY-8 exhibit.
- **E4 (singular source / forced orbit).** `n' = 96` (`N = 48`):
  `F = Phi_96(z) = z^32 - z^16 + 1` (weight 3, support `{0,16,32}`) is a
  level-1 vanisher at EVERY `q ≡ 1 (mod 96)` (it is the minimal polynomial
  of `omega`); it is primitive for all `q > 3` (its weight-1/2 sub-vectors
  evaluate to values of norm 1 or 3); its multiplication matrix is SINGULAR
  over Z (`F * Phi_32 = F * (z^16+1) = 0`), so only D2(a) applies to it; its
  normalized orbit has 16 members (`z^16 F = -F`), triggering the
  degenerate-orbit flag — expected, not an error. Moreover
  `F = D_2(Phi_48-vector)`: with `Phi_48(z) = z^16 - z^8 + 1` a primitive
  forced level-1 vanisher of the `(q, n'=48)` row, `F` is LIFT-OWNED
  whenever the `N = 24` row is admissible (`q <= 2^24`) — the forced mass is
  charged once at its minimal row, exactly the census principle.

## 6. Cross-node consistency consequence (recorded, not resolved here)

The C1' pose (`C1PRIME_LEVEL_SCALED_POSE.md` lines 20-29) defines `W_cl`
WITHOUT dedup (sum over primitive orbits); the M3 CORRECTED POSE defines
`W_cl` WITH first-owner dedup; the downstream assembly
`E_L <= 1 + 4 r_L (1 + W_cl) <= 41/8` uses ONE symbol for both. Dedup only
SHRINKS the ledger, so it helps `W_cl <= 1/32` but TIGHTENS the C1'
allowance: the banked M2 survival (raw ledgers) does NOT cover C1' with
deduped ledgers. This is a pose-level inconsistency risk that is exactly
testable on the banked rows (round 2 runs the exact deduped-C1' audit on the
eight banked rows with <= 350 window orbits; any `E - 1 > 4r(1 + W_cl^dedup)`
is a spec-level finding against the M3 interface, NOT a WCL-ZONE kill).

## 7. Invariance properties (normative)

- **P1** enumeration-order independence: output depends only on the SET of
  window orbits (canonical sort before the passes; union-find with
  min-element owners).
- **P2** representative independence (D1 lemma).
- **P3** idempotence: dedup(dedup(X)) = dedup(X).
- **P4** shadow pass preserves nonemptiness; lift pass need not.
- **P5** engine independence: identical output from direct- and
  mitm-enumerated hit sets.
- **P6** aux-prime independence of D2(b) (uniqueness + exact Z gate).
- **P7** determinism: no randomness; reruns bit-identical.

## 8. Conformance test suite (normative; implemented in wz2_census_modal.py)

- **T1** banked M2 replay: raw primitive counts and raw `W_cl` of the replay
  rows equal the banked values EXACTLY; deduped values reported as findings.
- **T2** round-1 replay: `A/b21 q=2107073` raw 4, round-1-convention shadow
  dedup 1 with 5 links; `B/b14 q=21569` single orbit with the recorded rep;
  `C/b21 q=2100353` raw 44, shadow-only 34 with 10 links. Exact match
  required for the round-1-convention path; canonical-path diffs reported.
- **T3** synthetic shadow trip (E2) — required to link.
- **T4** lift identity trip: every admissible-companion window orbit's
  `D_k` image found among target hits (`k=2`, and `k=3` where a `k=3`
  companion is admissible) — zero misses required.
- **T5** order-invariance: shuffled input order (3 permutations) gives the
  identical owner set (P1/P2).
- **T6** idempotence (P3).
- **T7** singular-source exercise: at an `n'=96` cell, the weight-<=3 sweep
  from `F` must find the witness `m = 1+z` to the reduced `(1+z)F` target
  (solver-level test; target need not be in the ledger).
- **T8** procedure consistency: on invertible sources, D2(a) links (weight
  <= 3) form a subset of D2(b) links.
- **T9** mutation controls (each deterministically required to trip):
  (M-A) primitivity filter off at `q=7937` changes `w=6` from 126 to 224
  (banked M1); (M-B) the D2(b) ternarity acceptance gate mutated to the
  empty coefficient set must LOSE the T3 synthetic link (verifies the gate
  is load-bearing on the accept path); (M-C) reversed owner order changes
  the owner SET on `A/b21 q=2107073` (its shadow component has >= 2
  members); (M-D) a non-ring lift map (`y -> 2y + (y mod 2)`, which no
  `z^s` shift can absorb) must produce >= 1 lift-control miss across the
  O96L1/b21 cells (every cell has a nonempty companion by the forced
  plant); (M-E) tag computed against the wrong cyclotomic factor breaks
  the forced-orbit control at an `n'=96` cell. NOTE: an earlier draft
  posed M-B as "widen ternarity to allow coefficient 2 and find a new
  link"; that variant is not deterministically trippable (existence of a
  coefficient-2 witness on a given cell is not guaranteed) and was
  replaced before any computation.
- **T10** nonemptiness guards per #137: every enumeration side nonempty;
  per-band candidate streams nonempty where the design lambda makes
  emptiness a failure (pre-registered per band in wz2_falsifiers.md).

## 9. Ratification list (maintainer decisions owed)

| id | question | default (this round) | banked tension |
|---|---|---|---|
| RATIFY-1 | cross-orbit total order: (w, sparse REP lex) vs (w, dense M2 orbit_key lex) | sparse | M2 never ordered; round-1 froze sparse |
| RATIFY-2 | literal 2N mass for degenerate orbits | literal | overcharge is anti-conservative for C1' side |
| RATIFY-3 | component closure vs direct-witness-only ownership | components | relation not transitive by algebra |
| RATIFY-4 | singular-source witness scope: weight-<=3 sweep vs factor-wise division (App. A) | weight-<=3 | round-7 method inapplicable; census bounded closure is the only precedent |
| RATIFY-5 | lift maps for all k >= 2 (not only k=2) | all k | only k=2 banked (57/57) |
| RATIFY-6 | lift gate = C1'-admissibility of the source row | admissibility | round-1 freeze; alternative = well-definedness |
| RATIFY-7 | lift source object: window-restricted vs any primitive vanisher of matching weight | any primitive vanisher, weight in target window | coincident at fixed L; divergent cross-level |
| RATIFY-8 | composition order lift->shadow | lift->shadow | opposite order changes owner sets |

## Appendix A — candidate upgrade for singular sources (not default)

Factor `z^N + 1 = prod_d Phi_d` over Q (composite `n'`). For singular
`P_i`, compute `P_i mod Phi_d` for each factor; on factors where it is
nonzero, `m mod Phi_d` is uniquely determined by exact division in
`Q[z]/Phi_d`; on null factors REQUIRE the target component zero and PIN
`m mod Phi_d = 0` (the canonical minimal solution). Accept iff the CRT
recombination is ternary and re-verifies over Z. This restores any-weight
detection for singular sources but undercounts witnesses whose annihilator
component is forced nonzero to achieve ternarity; no banked precedent
exists for either resolution. Needs ratification before it can replace
D4's default.
