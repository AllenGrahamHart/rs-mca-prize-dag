# EXACT-QUOTE SWEEP — (ES), the round-17 collapse, regimes, catches, lemmas

Repo root: `/home/u2470931/smooth-read-solomin/prize`. The three quarantined dirs (`tern_master_statement`, `tern_route_b`, `tern_small_scale_laws`) were never opened or read.

**⚠️ ENCODING WARNING, load-bearing for verbatim quoting:** `notes/pilots_20260804/mun_anticoncentration/REPORT.md` and `.../PREREG.md`-adjacent recovered reports are stored **HTML-escaped**. The literal bytes on disk contain `&gt;` for `>`, `&lt;` for `<`, and `\|` for `|`. Below I give the **literal on-disk text** first where it matters. Do not silently un-escape when you claim "verbatim".

---

## (1) THE (ES) STATEMENT OF RECORD

### 1.1 The (ES) statement itself — the general form

**Primary source of record** (this is the line every downstream node and audit cites):

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/REPORT.md:40` — literal on-disk text:

```
&gt; **(ES) ENTROPIC SUPPRESSION OVER mu_n.** Let `n = 2^m`, `H = x_0 mu_n &lt;= F_q^*` split, `V` an affine subspace of codimension `c` in locator-coefficient space, `R(V) = {T &lt;= H : |T| = r', coeff(E_T) in V}`, and `R^per(V)` its `mu_M`-periodic members. If the row is **sub-balance**, `c·log2 q &gt;= log2 C(n,r') + sigma`, then `R(V) = R^per(V)` — **no accidental members**.
```

(un-escaped reading: *"Let `n = 2^m`, `H = x_0 mu_n <= F_q^*` split, `V` an affine subspace of codimension `c` in locator-coefficient space, `R(V) = {T <= H : |T| = r', coeff(E_T) in V}`, and `R^per(V)` its `mu_M`-periodic members. If the row is **sub-balance**, `c·log2 q >= log2 C(n,r') + sigma`, then `R(V) = R^per(V)` — **no accidental members**."*)

Abbreviated re-quote (clean, non-escaped) at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/PROOFS.md:34`:

```
> **(ES) ENTROPIC SUPPRESSION OVER mu_n.** … If the row is **sub-balance**, `c·log2 q >= log2 C(n,r') + sigma`, then `R(V) = R^per(V)` — **no accidental members**.
```

**Naming of record** at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md:14-20`:

```
- **(ES) ENTROPIC SUPPRESSION** as the terminal's name and unified
  statement (sub-balance codimension => no accidental members; the
  crossing instance is EXACT as a constant-weight slice, the band
  instance strictly finer). SHARED BY FOUR LANES: band fullrank,
  crossing, syzygy (via round-15's BC routing), and u2c/dli RES —
  whose own banked re-pose is (ES) verbatim. The wiring
  recommendation (one node all four consume) goes to mint-4.
```

### 1.2 "The (ES) crossing instance" — what it means

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/REPORT.md:42` (literal, escaped):

```
**Cyclic-code (prefix) instance — the crossing lane, exact.** With `V = {e_1 = .. = e_{w-1} = 0}` and `w &lt; p`, Newton makes this linear in the 0/1 indicator: `R(V) = {x in {0,1}^n : wt(x) = r', x in C(n,p,Z_w)}`. (ES) says the weight-`r'` coefficient of that code's 0/1 constant-weight enumerator equals its periodic value `C(n/M, r'/M)`, `M = 2^{ceil log2 w}`.
```

**The sharpest stand-alone form** ("the precise frontier"), `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/REPORT.md:125` (literal, escaped):

```
&gt; Let `C` be the `[2^41, 2^41−w+1, w]` Reed-Solomon code over `F_p` (`p ~ 2^256` prime, `2^41 | p−1`) with zeros `zeta,...,zeta^{w-1}`, `w in [2^34, 2^39]`. Show its **only 0/1 codewords of weight `r' = 2^40 − w` are the `mu_M`-periodic ones**, i.e. the count is exactly `C(n/M, r'/M)`, and `0` when `M` does not divide `r'`.
```

The pre-registered `(U1)` form of the same object, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/PREREG.md:55-61`:

```
  ```text
  W_w = { x in {0,1}^n <= F_p^n : wt(x) = r',  x in C(n, p, Z_w) }
  ```
  where `C(n,p,Z_w)` is the cyclic code of length `n` over `F_p` with
  defining zero set `Z_w` = the p-cyclotomic closure of `{1,...,w-1}`
  mod `n`; `dim C = n - |Z_w|`, `w-1 <= |Z_w| <= delta (w-1)`.
```

Line `:61` continues: `  This is LEMMA Y, BANKED round 14 — cited, not claimed.`

### 1.3 The parameters (n, w, r', p, q) it quantifies over

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/PREREG.md:9-18` (the object block, "Crossing consumer (mystery 4)"):

```
n = 2^41,  k = 2^40,  q < 2^256,  log2 q in (255.900, 256),
a_L >= k + 2^34            (RHL-LB, proved floor)
a_IJ = floor(sqrt(n(k-1))) + 1 = 1554944255988    (Johnson anchor)
w := a_L - k  in  [2^34, 2^39]   (bracket as recorded in
                                  crossing_w2_opening/verify3_prizerow.py:49)
r' = n - k - w = 2^40 - w
```

(`w := a_L - k in [2^34, 2^39]` is line **:16**; `r' = n - k - w = 2^40 - w` is line **:18**.)

Characteristic arithmetic, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/PREREG.md:39-44`:

```
**Characteristic arithmetic (proved, verify3_prizerow.py R3).** `n = 2^41`,
`n | p^e - 1`, `p^e = q < 2^256` force `delta := ord_n(p) = 2^j` with
`j <= 2`, so `delta in {1,2,4}` and `p >= 2^39 + 1`. Consequently
`p > w` on the whole crossing bracket and `p > 2^33 > d` on every band
depth: **Newton's identities are invertible at every one of the four
rows**...
```

Row table, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/REPORT.md:48` (literal, escaped):

```
| crossing razor | `F_p`, `p &gt;= 2^39+1`; recorded rows `q = p` PRIME ~2^256, `delta = 1` | `2^41` | `Z_w = {1..w-1}`, `\|Z_w\| = w-1` | `[2^41, 2^41-w+1, w]` **MDS = Reed-Solomon** | `r' = 2^40-w`, `w in [2^34,2^39]` | `B* = floor(q/2^128) &lt; 2^128` |
```

### 1.4 The "bracket" for w, and w*

Two distinct things are called "bracket". Both are pinned:

**(a) The w-bracket** (the crossing lane's range of `w`): `w in [2^34, 2^39]`.
- Definition: `notes/pilots_20260804/mun_anticoncentration/PREREG.md:16` (above).
- Machine source of record: `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/crossing_w2_opening/verify3_prizerow.py:49` — `    wlo, whi = 2 ** 34, 2 ** 39`
- Size: `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/crossing_w2_opening/REPORT.md:65` says `w` is a power of two for *"6 values out of the 532,575,944,705 integers in the open bracket."*
- Cap re-affirmed at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/PROOFS.md:562`: ``  SP-COVER needs `w >= 2^42` while the bracket caps at `w = 2^39` ``

**(b) The |Z_w| bracket**: `notes/pilots_20260804/mun_anticoncentration/PREREG.md:60` — ``  mod `n`; `dim C = n - |Z_w|`, `w-1 <= |Z_w| <= delta (w-1)`.`` — and its round-17 correction, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/REPORT.md:35`:

```
**CATCH-B.** The banked bracket `w-1 <= |Z_w| <= delta(w-1)` (`mun PREREG.md:60`) is correct but **its top is never attained at delta = 4** — the maximum is `3(w−1)`, i.e. `0.75·delta(w−1)`. Pricing a `delta = 4` row at the bracket top over-credits it by 33%.
```

**w\* (the CS-EXCL threshold) = 170,752,922,588 = 2^37.3131.** Verbatim, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_coprimality/REPORT.md:79`:

```
> **UNCONDITIONAL (no conjecture used).** At crossing rows `n = 2^41`, `r' = 2^40 − w`, `log2 p = 256`: if `ceil((w−1)/2)·log2 p > (n/4)·log2 r'` then the (ES) crossing instance HOLDS — the count equals the structural count. Exact threshold `w* = 170,752,922,588 = 2^37.3131`; **every w > w\* is excluded**, i.e. **71.16% of the bracket [2^34, 2^39]**, including **2 of the 6 power-of-two w** (2^38, 2^39). By field size: 128 bits → 39.57%, 208 → 63.83%, 256 → 71.16%, 512 → 87.14%.
```

Node-level pin, `/home/u2470931/smooth-read-solomin/prize/background/nodes/es_ternary_suppression_instruments/statement.md:20-23`:

```
CONSEQUENCE (unconditional): the (ES) crossing instance HOLDS
wherever ceil((w-1)/2)·log2 p > (n/4)·log2 r' — at 256-bit p,
71.16% of the bracket (every w > w* = 2^37.3131, incl. 2^38, 2^39);
scaling with log2 p (39.57% at 128 bits).
```

### 1.5 (ES-G) — the surviving global re-pose (round 16)

There is **no node named `es_*` that states (ES) itself**; the statement of record lives in the pilot report above. What *is* a node is the **re-pose** and the **re-scope**:

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_boundary_adversary/FABLE_AUDIT.md:21-25`:

```
- **(ES-G)**: the terminal's statement of record is the GLOBAL-balance
  form (2^n <= p^{|Z_w|} with the TRUE cyclotomic-closure size), with
  balance imposed STRATUM-BY-STRATUM (C4-a: T a union of mu_{2^a}-
  cosets sees only the surviving conditions of the n/2^a instance;
  the binding stratum is not always a = 0).
```
and `:26-28`:
```
- The per-weight form (round-15's Lam) is REFUTED and retired as a
  statement; it survives only as a heuristic with a measured thin
  boundary band [-8.3, +0.1] bits.
```

The two functionals side by side, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/PROOFS.md:39-40`:

```
PER-WEIGHT (retired):  c*log2 V  >=  log2 C(n,r')
GLOBAL     ((ES-G)):   c*log2 V  >=  n
```
(line `:42` adds: ``GLOBAL => PER-WEIGHT` since `C(n,r') <= 2^n`.  No third functional is used.``)

**THEOREM Q** (why the base is `p`, not `q`) — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/crossing_w2_opening/REPORT.md:69`:

```
&gt; Fix `n,r',w`. For every `q` with `n | q−1`, `W_w` and its entire sig-profile depend on `q` only through `p = char F_q` — never through `e` in `q=p^e`. Changing `ζ` only permutes the profile by `S→aS`.
```

---

## (2) THE ROUND-17 (ES) UNIFICATION COLLAPSE — VERBATIM WITHDRAWAL

### 2.1 The claim that was withdrawn

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/REPORT.md:53` (literal, escaped):

```
**(ES) discharges all four consumers.** Band: `xr_mc_depth_quantization` proves `N_d^coset = 0` at band-proper depths, so (ES) gives `|R_d| = 0`. Crossing: (ES) gives `X_w = C(N,m)/N &lt; B*`. **u2c**: its own re-pose is (ES) verbatim — *"zero accidents when the expected count is &lt; 1 uniformly — an entropic-suppression / anti-concentration statement"*. **dli RES**: same file, *"the SAME hard shape as the dli RES count."* The round-14 merge verdict understated its own result: the terminal is shared by **four** lanes.
```

### 2.2 Source of record #1 — the withdrawal

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/FABLE_AUDIT.md:3-12` (the verdict):

```
**Auditor:** Fable, 2026-08-06. **Verdict: BANKED, MAINTAINER-LEVEL —
the FOUR-LANE UNIFICATION IS BROKEN AS WIRED. Only u2c can cite
(ES-G) (its pin is the global form verbatim); the rate-1/16 band row
and the dli RES row are above global balance at EVERY admissible
parameter (routing BROKEN); the crossing lane fails at w = 2^34 at
all 19 admissible (p-class, e) pairs under the adopted stratum
clause; and the four lanes' field requirements are MUTUALLY
UNSATISFIABLE — no single row satisfies all four. The "unified
terminal" framing is WITHDRAWN of record and replaced by a
regime-split terminal family.**
```

`.../es_g_lanes/FABLE_AUDIT.md:23-47` (the adjudication, all four lanes):

```
ADOPTED — THE TERMINAL RE-SCOPE OF RECORD (coordinator adjudication;
statement-level; wiring changes to mint-4):
- The round-15/16 claim "(ES)/(ES-G) is the unified terminal of four
  lanes" is WITHDRAWN. The statement of record becomes:
  (a) **u2c**: (ES-G) verbatim — the lane's own pin; the five
      round-16 witnesses confirmed excluded by independent
      recomputation (P5).
  (b) **crossing**: (ES-G) applies at w >= 2^37 (19/19 admissible
      pairs, deep strata included); at w in {2^34, 2^35, 2^36} the
      DEEP STRATA are a separate named obligation — the n_a = 256
      one-condition instance, small enough for direct attack. At
      w = 2^34 no admissible row clears the binding stratum (the
      requirement log2 p >= 256 IS the rules cap).
  (c) **band (both nodes)**: (ES-G) is NOT available at rate 1/16 at
      any (d, q) (deficit >= 512 bits at the cap), nor at the
      low-depth 22.5% of rates 1/4-1/8 scope at the banked pin. The
      band lanes need either a re-posed weight-aware balance form
      (the retired per-weight heuristic does predict suppression
      there but is refuted as a theorem) or a non-balance argument.
  (d) **dli RES**: (ES-G) is UNWIRED — the lane is above global
      balance by its own proved scoping hypothesis (H2/A2); its
      above-balance flatness instruments (C1'/C2''/WCL-ZONE) are the
      route of record, as they already were. The round-15 "discharges
      all four consumers" claim is REFUTED for this lane (mun
      FABLE_AUDIT addendum #2 written this bank).
```

**The exact reason (mutual unsatisfiability), `.../es_g_lanes/FABLE_AUDIT.md:60-67`:**

```
- CATCH-E: the u2c node carries three different bases in one
  statement (q^t / |B0| / p^{|Z_w|}) — pin to one (THEOREM Q says p,
  the least favourable, for the crossing instance); the "~2%" prose
  corrected to the 0.089-bit sliver; and the MUTUAL UNSATISFIABILITY
  of the four lanes' field regimes — the reading of record: each
  lane's obligation ranges over ALL admissible rows in its scope
  (rules quantifier), so no shared-row discharge was ever available;
  the unification was of STATEMENT SHAPE, not of regime.
```

**The numeric field requirements** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/REPORT.md:174`:

```
3. **The four lanes' field requirements are mutually unsatisfiable.** u2c needs `log2 Q >= 255.9113`; band 1/4, 1/8 at low depth need `>= 255.99999994`; band 1/16 needs `>= 256`; dli RES needs the *opposite* inequality (`< 256` strictly, by H2). **No single row satisfies all four.** (ES-G) cannot be a shared terminal for the four lanes as currently wired.
```

Same in node form — `/home/u2470931/smooth-read-solomin/prize/background/nodes/esg_lane_rescope/statement.md:12-18`:

```
THE (ES-G) TERMINAL RE-SCOPE OF RECORD: the round-15 "unified
terminal of four lanes" is WITHDRAWN — the four lanes' field
regimes are MUTUALLY UNSATISFIABLE (u2c needs log2 Q >= 255.9113;
band 1/4-1/8 low depth >= 255.99999994; band 1/16 >= 256 exactly,
i.e. NEVER — deficit >= 512 bits even at the cap; dli RES needs
< 256 STRICTLY by its own proved H2/A2). No single row satisfies
all four; the unification was of statement SHAPE, not regime.
```

**The four consumers, named:** `u2c` (`u2c_giant_tnull_dichotomy`), `crossing` (`rate_half_list_adjacent_crossing`), `band full-rank` + `band syzygy` (`xr_band_fullrank_window_divisor_count`, `xr_band_forced_commonroot_syzygy_count` — counted as "band (both nodes)"), `dli RES` (`dli_prime_weighted_large_block_support`). The per-lane obligation table is `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/REPORT.md:113-118`.

**CATCH-F (dli RES), verbatim** — `.../es_g_lanes/REPORT.md:134-136`:

```
`2^N >= q^L` is **exactly the negation of global balance** `q^L >= 2^N`, proved strict at every one of the 34 levels for every admissible `q`. The lane's object is a **flatness** statement (mean ≥ 1 ⇒ above balance); (ES-G) is a **zero-count** statement conditioned on sub-balance. **Same shape, disjoint regimes.**

This **refutes the round-15 discharge claim** at `mun REPORT.md:53` — *"**(ES) discharges all four consumers.** … **dli RES**: same file, *"the SAME hard shape as the dli RES count."*"* — "same hard shape" was read as "discharged by". It is not.
```

Underlying pins: `/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/DLI_CLOSE_PINNED.md:164-165`:
```
    2^N >= q^L    (balanced-volume / matched-alpha; automatic at production:
                   N = 256L and q < 2^256).
```
and `/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_c1r3_gated_envelope_bound/statement.md:12`:
```
(H2)  2^N >= q^L,  N >= 16L,
```
and `/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/notes/m4_report.md:107-108`:
```
- **A2** balance: `r_L = q^L / 2^{256L} < 1` for every admissible
  `q < 2^256` — exact integer inequality at L = 1, 2, 34.
```

### 2.3 Source of record #2 — the mun_anticoncentration FABLE_AUDIT addendum

**Path (asked for):** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/FABLE_AUDIT.md`

**ADDENDUM 2, verbatim, lines 76-87:**

```
## ADDENDUM 2 (2026-08-06, coordinator, from round-17 es_g_lanes)

REPORT.md §1's "(ES) discharges all four consumers" is REFUTED for
the dli RES lane: that lane is ABOVE global balance by its own proved
scoping hypothesis (2^N >= q^L, H2/A2 — exact strict inequality at
every admissible q), so "the SAME hard shape" never meant "discharged
by". (ES-G) is unwired from dli RES; its above-balance flatness
instruments remain the route of record. The four-lane unification is
re-scoped per notes/pilots_20260806/es_g_lanes/FABLE_AUDIT.md — the
lanes' field regimes are mutually unsatisfiable, so the shared
terminal was a shape identification, not a shared discharge.
```

(There is also **ADDENDUM 1** at `.../mun_anticoncentration/FABLE_AUDIT.md:56-74`, from round-16 CATCH-16C, which repairs the report persistence and reprices the "1-2 orders EARLY" evidence.)

### 2.4 Round-19's own summary of the collapse (useful one-liner)

`/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/tern_unification_adversary/PREREG.md:4-9`:

```
own registrations BEFORE any computation. MANDATE: attack the round-18
unification candidate BEFORE it becomes load-bearing. The campaign has
already had one unification collapse — (ES), which died in round 17
because it was a SHAPE identification, not a shared regime (mutually
unsatisfiable field requirements; "discharges all four consumers"
never checked per lane). Your falsifiers ARE that collapse's failure
modes. If this unification is a pun, kill it now.
```

---

## (3) OFFICIAL ROW / REGIME PARAMETERS

### 3(a) The F2 terminal lane (`f2_*`, `u2c_giant_tnull_dichotomy`, `dli_*`)

**Object of record**, `/home/u2470931/smooth-read-solomin/prize/background/nodes/f2_z1_mass_knife_edge/statement.md:12-15`:

```
THE F2 TERMINAL OF RECORD (SL-1b' pinned to the MASS form) AND ITS
PROVED CONSTRAINTS, on the admissible object (the [S, S-R, R+1]_p
negacyclic GRS code on the half-system of mu_{2^{e_p}},
S = 2^40/e, R/S = 1/log2 p, p >= 2^39; Z(L) = Z_1^C, C <= 4).
```

- **S = 2^40/e** — literally `S = 2^40/e` at `background/nodes/f2_z1_mass_knife_edge/statement.md:15`; equivalently `S = 2^{e_p-1}`. Instantiations: `e=1 → S=2^40`, `e=2 → S=2^39`, `e=4 → S=2^38`.
- **k = e** — the *generating* condition. `/home/u2470931/smooth-read-solomin/prize/background/nodes/f2_o1_status_split/statement.md:16-17`: `**Non-generating rows (k = ord_n(p) < e): (O1) IS FALSE by` / `2^{Theta(n)}, twice over.**`; and `:33-34`: `**Generating rows (k = e, exactly three classes): (O1)'s truth is` / `decided by two unpinned conventions — THEOREM Z2 (the ensemble dichotomy).**`
- **m** — `m = n/2 = 2^40`. `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/PROOFS.md:261-262`: ``Write the nested reading of `f2_adm`'s ladder: `m = n/2`, `C = k`,`` / ``  `S = m/C`, `dim L = C·min(S,R) = C·R`, `L = log2 q = e·log2 p`, and``. `Z(L) >= 2^m / p^{dim L}` uses this `m` (`f2_z1_mass_knife_edge/statement.md:17-19`).
- **Range of p** — `p >= 2^39` (`f2_z1_mass_knife_edge/statement.md:15`); the admissible classes are `(e_p, e) ∈ {(≥41,1),(40,2),(39,4)}` with `e·log2 p < 256`. Verbatim, `/home/u2470931/smooth-read-solomin/prize/background/nodes/f2_o1_status_split/statement.md:50-54`:
```
E_{c in K1(Lambda)}[T_W(c)] = 2^{n/2}·Z_1^e EXACTLY, on
(e_p, e) in {(>=41,1), (40,2), (39,4)} with e·log2 p < 256, coset
droppable by C1, Z_1 the ternary mass of the negacyclic prime-field
GRS code [S, S-R, R+1]_p on the half-system of mu_{2^{e_p}}
(S = 2^40/e, R/S = 1/log2 p, min ternary weight >= 2R+1). (O1)
holds iff Z_1 <= 2^{o(n)/e}
```
- Round-19 restatement with p-range: `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/tern_unification_adversary/PREREG.md:18-21`, and `:60-62`: `I1 lives at k = e generating rows, p ~ 2^39-2^64; I2's open part` / `lives at e = 1 prime rows, p ~ 2^129+; I3 lives at the official q` / `in the SP/CS gap.`
- **The witness row (concrete)**: `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/f2_adm/REPORT.md:10` — ``(`p = 18446735827372343297`, `e_p = v_2(p-1) = 39`, `q = p^4`, `L = 255.999997420`, `k = ord_n(p) = 4`, `t = n/L = 8,589,934,678.6`, `R = 4,294,967,340`)``. `S = 2^38 = 274,877,906,944` at `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:319`.
- **The dli/H-gates**: `(H1) q prime, q = 1 mod n'`, `(H2) 2^N >= q^L, N >= 16L`, `(H3) OFFICIAL-ADMISSIBILITY GATE: v_2(q-1) >= 41 [analogue scale: >= 20].` — `/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_c1r3_gated_envelope_bound/statement.md:11-13`.

**NOT FOUND:** the specific string "`S = 2^40/e`" is never expanded into a per-`e` numeric table in a node; and there is no F2-lane statement of a *range* of `p` narrower than `p >= 2^39` together with `e·log2 p < 256` (the upper end `2^64` appears only in the round-19 PREREG prose at `tern_unification_adversary/PREREG.md:61`).

### 3(b) The crossing lane (`rate_half_list_adjacent_crossing`)

**The row.** `/home/u2470931/smooth-read-solomin/prize/critical/nodes/rate_half_list_adjacent_crossing/statement.md:25-29`:

```
At the prize-max razor row

```text
n=2^41,    k=2^40,    q<2^256,
```
```
and `:5-11`:
```
For every admissible official rate-`1/2` row `C=RS[F,D,k]`, put

```text
q=|F|,
B*=floor(q/2^128),
L_1(a)=max_u #{c in C: agr(c,u)>=a}.
```
```

**Admissible rows / the 19 (class, e) pairs.** Rule of record, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/PROOFS.md:143-144`:

```
Admissible `(delta, e)` pairs: `delta | e`, `e <= 6`, `v_2(e) <= 2`, giving
19 `(p-class, e)` combinations; `p ∈ [p_min(class), floor((2^256−1)^{1/e})]`.
```

Machine form, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/full_run.txt:48-50`:

```
Admissible (delta,e): delta | e, e <= 6, v_2(e) <= 2, e*log2 p < 256,
p >= 2^(41-log2 delta) - 1.  For each class+e, p ranges over
[p_min(class), floor((2^256-1)^(1/e))].
```

The **enumeration** (19 rows, `full_run.txt:53-71` at `w=2^34`) is:
- class `1` (δ=1): `e = 1,2,3,4,5,6` → **6 pairs**
- class `1099511627775` (= 2^40−1, δ=2): `e = 2,4,6` → **3**
- class `1099511627777` (= 2^40+1, δ=2): `e = 2,4,6` → **3**
- class `2199023255551` (= 2^41−1, δ=2): `e = 2,4,6` → **3**
- classes `549755813887`, `549755813889`, `1649267441663`, `1649267441665` (the four δ=4 classes, i.e. `2^39±1`, `3·2^39±1`): `e = 4` each → **4**
Total **19**. The eight p-classes are described at `full_run.txt:5`: `The eight residue classes of p mod 2^41 with ord_n(p) | 4 (all admissible`.

**"e = 1 prime rows"** — the sub-family with `q = p` prime (no tower), `delta = 1`. Its meaning is fixed by the dichotomy, `/home/u2470931/smooth-read-solomin/prize/background/nodes/crossing_dsa_refutation/statement.md:52-56`:

```
**THE DICHOTOMY.** e = 1 prime rows are NEVER in the DSA regime:
B* >= 3 forces log2 p >= 129.585 > 126. The recorded prize rows are
untouched and RE-PRICED (HEURISTIC, labelled): expected relation
count 3^128/p = 2^{-53.1}, orbit-corrected 2^{-61.1} — a 53-61 bit
margin replacing the 0.089-bit global-functional cliff.
```
and `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/PROOFS.md:306-307`:
```
> **`e = 1` rows are NEVER in the provable regime.** `B* >= 3` forces
> `q = p >= 3·2^128`, i.e. `log2 p >= 129.585 > 126 = L−2`.
```

**Tower rows** (e ≥ 2) — the adversary's best choice. `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/REPORT.md:184`:

```
- **Mechanism finding (new).** Because of THEOREM Q, **tower rows (`e >= 2`) get no balance credit from the extension degree while `e` divides the available `log2 p`.** This is the single mechanism behind every crossing-lane flip, and it makes extension rows — proved admissible by `axis8_generating` — the adversary's best choice against (ES-G).
```
and `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/PROOFS.md:309-311`:
```
So THEOREM DSA kills **tower rows only** — exactly the rows
`es_g_lanes/REPORT.md:184` identified as *"the adversary's best choice against
(ES-G)"* — and leaves the recorded prime rows `q = p ~ 2^256` untouched.
```

**B\* ≥ 3.** `B* = floor(q/2^128)` (`crossing/statement.md:8`). The `B* ∈ {1,2}` branches are closed exactly (`statement.md:57-70`, `(RHL-B12)`); `B* >= 3` is the live branch. Scope clause, `/home/u2470931/smooth-read-solomin/prize/background/nodes/crossing_dsa_refutation/statement.md:58-63`:
```
**SCOPE (load-bearing, honest):** the refutation applies under the
campaign's adopted reading that tower rows are in the crossing
lane's obligation (axis8_generating PROVED + the es_g_lanes bank +
B* >= 3). If the official family excludes towers (MAINTAINER
question), CATCH-18A shrinks to nothing and the lemma kit +
re-pricing survive.
```

**The official q for this lane.** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/mun_anticoncentration/REPORT.md:48` (escaped): ``recorded rows `q = p` PRIME ~2^256, `delta = 1```; re-quoted at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/PROOFS.md:317-318`: ``At the recorded rows (`mun REPORT.md:48`: *"recorded rows `q = p` PRIME`` / ``~2^256, `delta = 1`"*), `log2 p ≈ 256`.`` The lane's *live* exhibit tower row is `p = 6597069766657 = 3·2^41 + 1, e = 6, q = p^6, log2 q = 255.509775` (`notes/pilots_20260806/es_g_lanes/PROOFS.md:175-178`).

Global-balance verdicts across the bracket, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_g_lanes/REPORT.md:48-50`:
```
w=2^34: ALWAYS sub-balance  0, FLIPS  8, NEVER 11
w=2^35: ALWAYS sub-balance 10, FLIPS  5, NEVER  4
w=2^36 .. 2^39: ALWAYS 19, FLIPS 0, NEVER 0
```
Binding-stratum table, `.../es_g_lanes/REPORT.md:96-101` (`2^34` → required `log2 p` **256 / 128**, **0 of 19**; `2^35` → 128/64, 3 of 19; `2^36` → 64/32, 12 of 19; `2^37..2^39` → ≤32, 19 of 19).

### 3(c) The sparsity / (ES) lane

**Official q + the gate.** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/PROOFS.md:545-550`:

```
> **THE CONVERSION STATEMENT.** The 1440-trial credit becomes mathematics
> if and only if one proves, at the official row parameters
> (`n = 2^41`, `r' = 2^40 - w`, `q` prime with `v_2(q-1) >= 41`):
> ```text
> (CONV)  for every S <= Z/n with strat(S) = 0,  q does not divide N(I_S).
> ```
```

**The gate `v_2(q-1) >= 41` is SP-COVER's blind spot; the bracket caps at 2^39.** `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/REPORT.md:77`:

```
- **CATCH E-3 (campaign-relevant).** The official row gate `v_2(q-1) >= 41` — *required* by the construction — forces `j_q >= 42`, so SP-COVER needs `w >= 2^42` while the bracket caps at `w = 2^39`. **The row primes are the worst possible primes for the mechanism that works.** CS-EXCL closes `w > 2^37.3131` (independently reproduced); the gap to SP-COVER is `2^4.6869` in `w` and the two exclusions do not meet.
```

Machine-checked summary line, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/PROOFS.md:566-568`:

```
v_2(q-1)=41 -> SP-COVER needs w >= 2^42 ; bracket caps at 2^39  -> VACUOUS
CS-EXCL threshold w* = 170752922588 = 2^37.3131  (reproduces round 17)
UNCOVERED segment w in [2^34, 2^37.3131];  GAP to SP-COVER = 2^4.6869 in w
```

Node form, `/home/u2470931/smooth-read-solomin/prize/background/nodes/es_ternary_suppression_instruments/statement.md:57-62`:
```
(E-3) the official row gate v_2(q-1) >= 41 is exactly
SP-COVER's blind spot (needs w >= 2^42 vs bracket cap 2^39) — the
official primes sit PROVABLY in the gap between the two closed ends
(2^4.69 wide in w); the SPD union-bound shape is PROVED VACUOUS in
every regime (character sums + BCH cannot reach the middle).
```

Two-sided range for bad primes, `.../efloor_sparsity/REPORT.md:71`:
```
How far this pilot gets: SP-UNIFORM proves (CONV) for all `q <= sqrt(w+1)` (i.e. `q <= 2^17.00` at `w=2^34`, up to `2^19.50` at `w=2^39`); CS-EXCL proves it above the CS3 floor. **The official `q` sits in neither end, provably.**
```

### 3(d) "The official row" of the prize — exact q, n, k, and where pinned

**There is no single pinned (q, n, k) triple; the repo proves there cannot be one.** `/home/u2470931/smooth-read-solomin/prize/background/nodes/official_row_primes_pinning/statement.md:8-18` (status PROVED, closure proof):

```
The grand challenges quantify over every admissible choice of `F`, `L`, and
`k`, subject to the printed bounds and sufficiently-large-field proviso. They
do not specify a hidden finite list of official row primes.

Consequently, a prize-facing certificate must be either:

- uniform over the complete admissible family; or
- explicitly scoped only to the exact exhibit field it names.

A stand-in or named exhibit does not certify the universal family without a
proved transport theorem.
```

**What IS pinned is the admissible family / caps** — `/home/u2470931/smooth-read-solomin/prize/critical/nodes/rules_freeze/statement.md:9` (quoted verbatim as the campaign's cap line by `notes/pilots_20260806/crossing_low_w/PROOFS.md:70-72`):

```
THE RULES-FACT (closed by citation, not proof): the operative prize rules are exactly — smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16} (no dither latitude); the m-quantifier per rules_m_reading (family-per-constant-m). Certificate = quote + hash of proximityprize.org and ePrint 2026/680 with a drift detector; on any residual ambiguity the campaign plans against the stricter reading. (Reworded 2026-07-04 from task form to propositional form — node-kind hygiene.)
```

**The "prize-max razor row"** (the standing rate-1/2 instantiation, `n = 2^41`, `k = 2^40`, `q < 2^256`) is pinned at `/home/u2470931/smooth-read-solomin/prize/critical/nodes/rate_half_list_adjacent_crossing/statement.md:25-29` (quoted in 3(b)) and re-instantiated at `notes/pilots_20260804/mun_anticoncentration/PREREG.md:9-12`. The **admissible-sliver** of `q` at prize-max is `log2 Q in [255.9113, 256)`, width 0.089 bits — `/home/u2470931/smooth-read-solomin/prize/background/nodes/u2c_giant_tnull_dichotomy/statement.md:16-17`:

```
2. The "~2% sub-balance" prose is corrected: the exact admissible
   prize-max sliver is log2 Q in [255.9113, 256), width 0.089 bits.
```

(Its source, verbatim, inside `background/nodes/u2c_giant_tnull_dichotomy/node.json:8`: *"the '~2% sub-balance' prose is wrong in both directions: the exact admissible prize-max sliver is log2 Q in [255.9113, 256), width 0.089 bits, and the official factorization q = p^k is pinned nowhere (upstream r2's 'prize band underdetermined', made quantitative — maintainer-level pin required for any verbatim prize-max instantiation)"*.)

**So: the exact q is deliberately NOT pinned** (`"the official factorization q = p^k is pinned nowhere"`, `u2c_giant_tnull_dichotomy/node.json:8`); `n = 2^41`, `k = 2^40` are the prize-max razor row (`rate_half_list_adjacent_crossing/statement.md:27`); `|F| < 2^256`, `k <= 2^40` are the rules caps (`rules_freeze/statement.md:9`).

---

## (4) CATCH RECORDS — VERBATIM

### CATCH-Z1 (mass form vs exact-zero form)

**Pilot report form** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/REPORT.md:30`:

```
1. **CATCH-Z1 (against this brief's §0 and `f2_sl1b/REPORT.md:62`).** "`Z_1 ≤ 2^{o(m)}` (equivalently `L^⊥ ∩ T = {0}` or nearly)" — **the equivalence is false.** `Z` is *weighted*; the forms differ by `log2 3` (as `f2_sl1_powersums/PROOFS.md:304-307` itself says), and at the admissible object the mass form is heuristically TRUE while the exact-zero form is heuristically FALSE by `≈ (3/2)^{2^38}`. Measured: 67 configurations with ≥16 ternary kernel vectors but `Z < 3`; extreme 1,184 vectors with `Z_1 = 2.59`.
```

**PROOFS form** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/PROOFS.md:482-491`:

```
1. **CATCH-Z1 (against this brief's §0, and `f2_sl1b/REPORT.md:62`).** The
   equivalence *"`Z_1 <= 2^{o(m)}` (equivalently `L^perp ∩ T = {0}` or
   nearly)"* is **false**. `Z` is weighted; the two forms differ by
   `log2 3` in the exponent — `f2_sl1_powersums/PROOFS.md:304-307` says so
   itself (*"the two differ by exactly `log2 3 = 1.58496`"*) — and at the
   admissible object the mass form is heuristically TRUE (`Z_1 ≈ 1`) while
   the exact-zero form is heuristically FALSE by `≈ (3/2)^S =
   2^{0.585·2^38}`. Measured separation: 67 configurations with `>= 16`
   ternary kernel vectors but `Z < 3`; the extreme is 1,184 ternary vectors
   with `Z_1 = 2.59`.
```

**Audit adoption** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/FABLE_AUDIT.md:46-52`:

```
- **CATCH-Z1 (MY brief defect, accepted)**: the mass form and the
  exact-zero form are NOT equivalent (they differ by log2 3 per
  vector); at the admissible object the MASS form survives at k = e
  while the exact-zero form dies heuristically. THE TERMINAL OF
  RECORD is hereby pinned to the MASS form: prove Z_1 <= 2^{o(m)}
  at k = e. (The f2_sl1b REPORT's "equivalently" gloss carried into
  my brief — addendum to that audit written this bank.)
```

**Node form** — `/home/u2470931/smooth-read-solomin/prize/background/nodes/f2_z1_mass_knife_edge/node.json:13` (inside the `statement` string) and the same text in `.../f2_z1_mass_knife_edge/statement.md` is split across lines; the DAG copy reads verbatim: `CATCH-Z1: mass form != exact-zero form (differ by log2 3 per vector) — the terminal of record is the MASS form: prove Z_1 <= 2^{o(m)} at k = e.` Also present at `/home/u2470931/smooth-read-solomin/prize/dag.json:28181`.

**The corrected upstream line** it fires against: `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/f2_sl1b/REPORT.md:62` — ``**Renamed residual — SL-1b′:** at rungs 14-16, bound the ternary mass of the *deployed* alternant code, `Z(L) ≤ 2^{o(m)}` (equivalently `L^perp ∩ T = {0}`).…`` and the addendum repairing it at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/f2_sl1b/FABLE_AUDIT.md:65-71`.

### CATCH-Z6 (2-power vs composite-length parasitic relations)

**Report form** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/REPORT.md:35`:

```
6. **CATCH-Z6 (self-caught, methodological).** My own registered grid was **contaminated**: composite `2N` carries `p`-independent cyclotomic ternary relations (`2N=12` → 8 common vectors of min weight 3; `2N=20` → 8; `2N=24` → 80) which the official 2-power object structurally cannot have (`2N=8,16` → 0, the `Z`-basis property). Only 2-power `2N` rows are valid miniatures.
```

**PROOFS form** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/PROOFS.md:510-514`:

```
6. **CATCH-Z6 (self-caught, methodological).** My registered calibration
   grid was contaminated by composite `2N`, which carries `p`-independent
   cyclotomic ternary relations the official 2-power object cannot have
   (§7(v)). Any future calibration of this terminal must be restricted to
   2-power `2N`.
```
(The measurement section is at `.../z1_ternary_mass/PROOFS.md:441`: `**(v) CATCH-Z6 — my own registered grid was contaminated.** At composite`)

**Audit adoption** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/FABLE_AUDIT.md:60-63`:

```
- CATCH-Z6 (self-caught grid contamination: only 2-power 2N rows
  are valid miniatures — a scope rule all future toy grids must
  carry) and the Z-A10 partial self-falsification (packing constant
  corrected) — the discipline working.
```

**Node form** — `/home/u2470931/smooth-read-solomin/prize/background/nodes/f2_z1_mass_knife_edge/statement.md:63-69`:

```
**Calibration (honest):** on all valid miniatures (2-power 2N ONLY —
composite 2N carries p-independent cyclotomic ternary relations the
official object structurally cannot have, CATCH-Z6; a standing grid
rule) the deployed code sits at or below the random-ensemble median;
the deficit is exactly the excluded low-weight mass; "better than
random" is NOT established. No toy is evidence about Z_1 at the
official row.
```

**Standing grid rule carried forward** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/tern_unification_adversary/PREREG.md:97`: `  2-POWER LENGTHS ONLY (the CATCH-Z6 rule) unless deliberately`

### CATCH E-2 (CC-sparsity IS (ES) again)

**Report form** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/REPORT.md:76`:

```
- **CATCH E-2 (structural).** LEMMA AB shows `E_floor`-sparsity = counting **{0,±1} vectors in a `p`-ary cyclic code of length `n/2`**, while (ES) is counting **{0,1} vectors in a `p`-ary cyclic code of length `n`**. Same shape. **CC-sparsity is not a lemma below (ES) — it is (ES) again, at half length over a ternary alphabet.** Anyone planning to close the residual 28.84% of the crossing bracket via CC-sparsity should read this first.
```

**PROOFS §6** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/PROOFS.md:348-363`:

```
## §6. CATCH E-2 — `E_floor` sparsity is a SELF-SIMILAR copy of (ES)

LEMMA AB + THEOREM SP-TERNARY identify the object that must be counted:

```text
(ES)                : # 0/1 vectors of length n   in a cyclic F_p-code    -> conjectured structural
E_floor sparsity    : # {0,+-1} vectors of length n/2 in a cyclic F_p-code -> conjectured 0/sparse
```

They are the **same shape**: constant-alphabet vectors in a `p`-ary cyclic
code with a consecutive defining set. So the conjecture invoked to close
(ES) is a copy of (ES) itself at half the length over a ternary alphabet.
**CC-sparsity is not a lemma below (ES); it is (ES) again.** That is the
structural reason the round-17 conditional (K5) could not be discharged by
elementary means, and it is a scope warning for anyone planning to close
the residual 28.84% of the crossing bracket by proving CC-sparsity.
```

**Audit adoption** (with the coordinator's convergence note) — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/FABLE_AUDIT.md:55-66`:

```
- **CATCH E-2 (structural, the round's second unification signal)**:
  CC-sparsity = ternary vectors in a p-ary cyclic code at half
  length; (ES) = binary vectors in a p-ary cyclic code. COORDINATOR
  CONVERGENCE NOTE: this is the THIRD independent appearance of
  "ternary vectors in a p-ary code" as the primitive object this
  round — crossing_low_w's LEMMA TC (the deep stratum's primitive is
  epsilon in {0,±1}^L), this pilot's LEMMA AB, and the z1 pilot's
  entire mandate (ternary mass of a GRS code). The true shared
  terminal of the campaign may be the TERNARY-IN-CODE question, not
  (ES) — to be tested against the z1 report at its bank, then posed
  as the round-19 unification candidate if it survives.
```

**Node form** — `/home/u2470931/smooth-read-solomin/prize/background/nodes/es_ternary_suppression_instruments/statement.md:56-58`:
```
(E-2) CC-sparsity IS the (ES) shape
again, at half length over the ternary alphabet — not a smaller
lemma;
```

Also in the es_coprimality audit addendum — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_coprimality/FABLE_AUDIT.md:92`: `2. **CATCH E-2**: CC-sparsity is structurally (ES) again — ternary`

### CATCH-18A — **IT EXISTS**

**Report form** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/REPORT.md:101`:

```
- **CATCH-18A (the campaign-critical one).** The (ES) crossing instance is **FALSE at admissible tower rows** — proved unconditionally by pigeonhole and exhibited explicitly at `n = 2^41`. The deep stratum is not empty "for a reason invisible to balance"; it is **full**, and balance was right to fail there. Round-17's `es_g_lanes` P4 ("no admissible row clears the deep-stratum requirement, 19/19") was not a pricing artefact — it was detecting a real refutation.
```

**Audit adoption / statement of record** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/FABLE_AUDIT.md:38-43`:

```
- **THEOREM DSA + the witness** (CATCH-18A). STATEMENT OF RECORD
  after this bank: the (ES) crossing instance is FALSE at admissible
  tower rows in the DSA regime (p^{delta_a} < 2^{L-2}); at e = 1
  prime rows DSA provably cannot apply — a clean dichotomy. The
  round-17 es_g_lanes P4 balance failure was DETECTING A REAL
  REFUTATION, not a pricing artefact.
```

**Scope clause** — `.../crossing_low_w/REPORT.md:112`:
```
- **The refutation's scope depends on the campaign's own adopted reading** that tower rows are in the crossing lane's obligation (`axis8_generating` PROVED + `es_g_lanes` FABLE_AUDIT adoption + `B* ≥ 3`). If the official family were later shown to exclude towers, CATCH-18A shrinks to nothing and only the re-pricing (CATCH-18C/D) survives.
```
and the node echo, `/home/u2470931/smooth-read-solomin/prize/background/nodes/crossing_dsa_refutation/statement.md:61-63`:
```
question), CATCH-18A shrinks to nothing and the lemma kit +
re-pricing survive.
```
(sibling catches 18B/18C/18D/18E are at `crossing_low_w/REPORT.md:102`, `:103`, `:104`, `:105`.)

---

## (5) LEMMA / THEOREM STATEMENTS AND HYPOTHESES

### LEMMA AB — proved at `notes/pilots_20260806/efloor_sparsity/PROOFS.md:86-108`

Statement, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/PROOFS.md:88-97`:

```
> **LEMMA AB.** Write `f_S = A + X^h B` with `deg A, deg B < h = n/2`, i.e.
> `A` is the indicator of `S n [0,h)` and `B` that of `S n [h,n)` shifted.
> Put `v := A - B in {-1,0,1}^h`. Then
>
> 1. `f_S = v (mod Phi_n)`, so for every **odd** `s`,
>    `f_S(xi^s) = v(xi^s)` for any primitive `n`-th root `xi` in char `p`;
> 2. `v = 0  <=>  S + n/2 = S  <=>  strat(S) >= 1`, for every odd `p`;
> 3. the number of `S` with a given `v` is exactly `2^{z(v)}`, where
>    `z(v) = #{i : v_i = 0}`.
```

**Hypotheses:** `n = 2^m` (2-power length; used via `Phi_n(X) = X^h + 1`), `p` odd (clause 2 needs `p >= 3`), `S <= Z/n`. Proof at `:99-108`. Machine check `:110-114` (56 cells, 112 checks, 0 failures). Node form: `/home/u2470931/smooth-read-solomin/prize/background/nodes/es_ternary_suppression_instruments/statement.md:38-39`.

### LEMMA TC — proved at `notes/pilots_20260806/crossing_low_w/PROOFS.md:167-187`

Statement, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/PROOFS.md:169-178`:

```
> **LEMMA TC.** The single deep-stratum condition depends on `S'` only through
> `eps in {0,±1}^L`. The fibre over `eps` has size
> `C(L−U, (r'_a−U)/2)` where `U = |supp(eps)|`, nonempty iff `U ≡ r'_a (mod 2)`
> and `U <= r'_a`; and
>
> ```text
> sum_{eps} C(L−U(eps), (r'_a−U(eps))/2)  =  C(2L, r'_a).
> ```
>
> `eps = 0` is exactly the structural fibre, of size `C(L, r'_a/2)`.
```

**Hypotheses:** the LEMMA DS setting — `n = 2^41`, `w = 2^v`, `r' = 2^40 − w`, `a = v−1` (the deepest stratum), `n_a = 2^{42−v}`, `L = n_a/2 = 2^{41−v}`, `r'_a = L−2`; proof is "LEMMA OE at `t = 1`" (`:180`). Node form: `/home/u2470931/smooth-read-solomin/prize/background/nodes/crossing_dsa_refutation/statement.md:28-33`. Pricing table at `PROOFS.md:191-196` (GLOBAL 256 / PER-WEIGHT 251.628 / TERNARY 202.875 / orbit-corrected 194.875).

### LEMMA ROT — proved at `notes/pilots_20260806/crossing_low_w/PROOFS.md:328-336`

Statement, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/PROOFS.md:330-332`:

```
> **LEMMA ROT.** The relation set is closed under `eps -> −eps` and under the
> twisted rotation `(R eps)_0 = −eps_{L−1}`, `(R eps)_j = eps_{j−1}`; `R` has
> order `2L`. Hence relations come in orbits of size dividing `2L`.
```

**Hypotheses:** the same deep-stratum object (`eps in {0,±1}^L`, `theta` of order `2L`, relation = `sum_j eps_j theta^j = 0`). Proof `:334-336`; machine check `toy_gate.py orbit`, 66 checks (`:338`). Node form: `crossing_dsa_refutation/statement.md:32-33` (`LEMMA ROT: relations come in orbits of size 2L; Poisson estimates over-predict by 2L`).

### THEOREM DSA — proved at `notes/pilots_20260806/crossing_low_w/PROOFS.md:205-233`

Statement, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/crossing_low_w/PROOFS.md:207-222`:

```
> **THEOREM DSA (unconditional).** Let `delta_a = ord_{2L}(p)`, so
> `theta = zeta_n^{2^{v-1}}` generates `F_{p^{delta_a}}` over `F_p`. If
>
> ```text
> p^{delta_a} < 2^{L−2}
> ```
>
> then there is `eps in {0,±1}^L`, `eps != 0`, with `sum_j eps_j theta^j = 0`,
> `U(eps)` even and `2 <= U(eps) <= L−2 = r'_a`. Consequently (LEMMA DS +
> LEMMA TC) `W_w` contains a **non-structural** member, so
>
> ```text
> |W_w|  >=  C(n/M, r'/M) + C(L−U, (r'_a−U)/2)   >   C(n/M, r'/M),
> ```
>
> i.e. **the (ES) crossing instance is FALSE at that row.**
```

**Hypotheses:** exactly one — `p^{delta_a} < 2^{L−2}` — plus the LEMMA DS/TC setting. Proof is pigeonhole, `:224-233`; explicitly *no balance functional* (`:236`). Node form: `/home/u2470931/smooth-read-solomin/prize/background/nodes/crossing_dsa_refutation/statement.md:35-41`. Witness `:43-50`; coverage `ALL = 10, PART = 6, NONE = 3` at `w = 2^34` (`statement.md:39-41`).

### THEOREM CS — proved at `notes/pilots_20260806/es_coprimality/PROOFS.md:198-…`

Statement, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_coprimality/PROOFS.md:202-225`:

```
> **THEOREM CS.** Let `n = 2^m`, `p` an odd prime, `delta = ord_n(p)`,
> `S <= Z/n` with `|S| = r'` and `x_1 != 0`. If `p | N(I_S)` then
>
> ```text
> p^{|Z_w^odd|}  divides  |N_{K/Q}(x_1)|                            (CS1)
> ```
>
> and, unconditionally,
>
> ```text
> |N_{K/Q}(x_1)|^2  <=  ( r' - a_{n/2}(S) )^h ,   h = n/2.          (CS2)
> ```
>
> Hence
>
> ```text
> |Z_w^odd| * log2 p  <=  (n/4) * log2( r' - a_{n/2}(S) ).          (CS3)
> ```
>
> Moreover `|Z_w^odd| >= ceil((w-1)/2)` **uniformly in `delta`**, so
>
> ```text
> ceil((w-1)/2) * log2 p  <=  (n/4) * log2 r'.                      (CS4)
> ```
```

**Exact hypotheses:** `n = 2^m`; `p` an odd prime; `S <= Z/n` with `|S| = r'`; **`x_1 != 0`**; and `p | N(I_S)` for (CS1). (CS2) is unconditional.

**Window structure / notation** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/es_coprimality/PROOFS.md:11-22`:

```
`n = 2^m`, `h = n/2 = phi(n) = [K:Q]`, `K = Q(zeta_n)`, `O_K = Z[zeta_n]`,
`Phi_n(X) = X^h + 1`. `S <= Z/n`, `|S| = r'`. For `s in Z/n`

```text
x_s = sum_{i in S} zeta^{s i}  in  O_K,      I_S = (x_1,...,x_{w-1}) <= O_K,
N(I_S) = [O_K : I_S]   (N(0) = 0, N(O_K) = 1).
```

`delta = ord_n(p)`; `Z_w` = the `p`-cyclotomic closure of `{1,...,w-1}` mod
`n`; `Z_w^odd = {s in Z_w : s odd}`; `a_{n/2}(S) = #{(i,j) in SxS :
i-j = n/2 mod n}`; `strat(S) = max{a >= 0 : S + n/2^a = S}`.
```

Node form (with the `w*` consequence) — `/home/u2470931/smooth-read-solomin/prize/background/nodes/es_ternary_suppression_instruments/statement.md:16-26`.

Scope caveats: `w = 3` degenerates to the banked M3 (`es_coprimality/PROOFS.md:435`, `REPORT.md:88`); band rows are outside CS's window hypotheses (`es_ternary_suppression_instruments/statement.md:74-75`).

### THEOREM SP-COVER / LEMMA COS / THEOREM SP-UNIFORM

**SP-COVER**, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/PROOFS.md:122-129`:

```
> **THEOREM SP-COVER.** Let `n = 2^m`, `p` odd, and suppose **every coset of
> `<p>` in `(Z/n)^*` contains an odd `s` with `1 <= s <= w-1`.** Then for
> every `S <= Z/n` with `strat(S) = 0`,
> ```text
> p  does not divide  N(I_S).
> ```
> Equivalently: `p | N(I_S)` forces `S + n/2 = S`.
```
**Hypotheses:** `n = 2^m`; `p` odd; **full `<p>`-coset coverage of the odd window** `{1,…,w−1}`; conclusion for all `S` with `strat(S) = 0`. Proof `:131-145`. One-line report form at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/REPORT.md:23`.

**LEMMA COS**, `.../efloor_sparsity/PROOFS.md:152-160`:
```
> **LEMMA COS.** Put `j_p := v_2(p^2 - 1) (>= 3)`. For `m >= j_p`,
> `<p>` contains `U_{j_p} := {s : s = 1 mod 2^{j_p}}`, so the coset of `s`
> in `(Z/2^m)^*/<p>` depends only on `s mod 2^{j_p}`. Consequently
> ```text
> w_cov(p, 2^m)  is independent of m for m >= j_p,   and
> w_cov(p, 2^m)  <=  2^{j_p}  <=  p^2 - 1.
> ```
```

**SP-UNIFORM**, `.../efloor_sparsity/PROOFS.md:174-180`:
```
> **THEOREM SP-UNIFORM.** If `w >= 2^{v_2(p^2-1)}` then `p` divides no
> `N(I_S)` with `strat(S) = 0`. Contrapositive — **the small-prime end of
> the bad-prime range, which was previously unbounded below:**
> ```text
> p | N(I_S)  and  strat(S) = 0   ==>   2^{v_2(p^2-1)} > w   ==>   p > sqrt(w+1).
> ```
```
**Hypotheses:** `w >= 2^{v_2(p^2-1)}`, `p` odd, `n = 2^m`, `strat(S) = 0`. Report form at `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/efloor_sparsity/REPORT.md:29`. Two-sided range at `PROOFS.md:184-186`:
```
```text
sqrt(w+1)  <  p  <=  r'^{ n / (4 ceil((w-1)/2)) }.
```
```

**SP-TERNARY** (a stronger, certified criterion), `.../efloor_sparsity/PROOFS.md:304-310`:
```
> **THEOREM SP-TERNARY.** If `C_odd(n,p,w)` contains **no nonzero vector
```
(full statement `:304-310`; proof `:312-313`; honest scope — "no `n`-uniform form" — `:335-337` and `:591`).

Node form of all three: `/home/u2470931/smooth-read-solomin/prize/background/nodes/es_ternary_suppression_instruments/statement.md:36-44`.

### THEOREM Z-FLOOR

**Node statement**, `/home/u2470931/smooth-read-solomin/prize/background/nodes/f2_z1_mass_knife_edge/statement.md:17-24`:

```
**THEOREM Z-FLOOR (pointwise first-moment floor).** For EVERY
F_p-subspace, Z(L) = sum_{eps in L^perp cap T} 2^{-wt(eps)} >=
2^m / p^{dim L}. One Cauchy-Schwarz from the banked collision
identity sum_s |F_s|^2 = 2^m Z(L)
(dli_c1_l1_block_owner_ledger:15,18) — the identity was banked, the
inequality never drawn. Tight within a factor 2 of the ensemble
mean (no subspace beats random by more than 2x). 696 configurations,
exact rationals, 0 violations.
```

**Proof-level statement + hypotheses**, `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/PROOFS.md:130-136`:

```
**THEOREM Z-FLOOR.** For **every** `F_p`-subspace `L ⊆ F_p^m` (no MDS, no
GRS, no genericity, no randomness),

```text
        Z(L)  =  sum_{eps in L^perp ∩ T} 2^{-wt(eps)}   >=   2^m / p^{dim L} ,
```

with equality iff the syndrome map is exactly balanced on `{0,1}^m`.
```
**Hypotheses: none beyond `L` an `F_p`-subspace of `F_p^m`** — explicitly "no MDS, no GRS, no genericity, no randomness". Proof `:138-…` (double counting + Cauchy–Schwarz). Corollaries: `Z-FLOOR.1` (tightness) at `:180`, `Z-FLOOR.2` (LEMMA 3 re-derived) at `:188`.

### THEOREM Z-1 / THEOREM D1 (the same law, blind-convergent)

**Z-1, node form** — `/home/u2470931/smooth-read-solomin/prize/background/nodes/f2_z1_mass_knife_edge/statement.md:26-33`:

```
**THEOREM Z-1 (the DLI transport; = the adversary's THEOREM D1,
blind convergence).** dli_wcl_newton_short_window_exclusion's
hypothesis char > w HOLDS on every admissible row (p > m always, by
the e_p case split — the tower verdict is REVERSED by the field
cap), so the min ternary weight is >= 2R+1 = 8,589,934,681, double
SL-1's characteristic-free R+1. SCOPE: shift-0 windows only — 43
shifted counterexamples exist; the transport is legitimate because
the official window starts at l = 1.
```

**Z-1, proof form** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/z1_ternary_mass/PROOFS.md:96-100`:
```
**THEOREM Z-1.** On the admissible object every nonzero ternary vector of
`L^perp` has

```text
        wt  >=  2R + 1  =  8,589,934,681 ,
```
```
Its four hypotheses are tabulated (verified row by row) at `.../z1_ternary_mass/PROOFS.md:87-93`:
```
`e_p = 39`, `S = 2^38`, `R = 4,294,967,340`):
…
| `char F > w` | `p = 1.845e19`, `w <= S = 2.749e11` | **HOLDS**, margin `6.71e7` |
| `omega` of exact order `2N` | `2N = 2^{e_p} = 2^39`, `v_2(p-1) = 39` exactly | **HOLDS** |
| `e_i` distinct in `{0..N-1}` | `N = 2^38 = S`; the half-system IS `{omega^e : 0<=e<N}` | **HOLDS** |
| `P(omega^{2j-1}) = 0`, `j = 1..ell` | `Lambda = {odd l : l <= t}` starts at `l = 1` (`f2_sl1_powersums/PROOFS.md:121`) | **HOLDS**, `ell = R` |
```
**Load-bearing scope** (`.../z1_ternary_mass/PROOFS.md:114-124`): the run must start at `l = 1`; 43 shifted configurations violate `2R+1`.

**D1 (the independent, blind-convergent statement)** — `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/o1_generating_adversary/PROOFS.md:225-232`:

```
> **THEOREM D1.** On EVERY admissible row `p > m >= w`, so the hypothesis
> *"characteristic greater than `w`"* HOLDS, and every nonzero ternary
> relation on a window `W <= mu_n` with `Lambda` a run of `R` consecutive
> odd exponents starting at 1 satisfies
>
> ```
>            wt(eps)  >=  2R + 1        (twice SL-1's R+1).
> ```
```
Proof of the hypothesis (the `e_p` case split) at `.../o1_generating_adversary/PROOFS.md:234-243`. The imported banked node it transports is quoted verbatim at `.../o1_generating_adversary/PROOFS.md:214-224` from `background/nodes/dli_wcl_newton_short_window_exclusion/statement.md:8-22`.

**THEOREM Z-2 and Z-NOGO** (for completeness): node form `background/nodes/f2_z1_mass_knife_edge/statement.md:35-44`; proof forms `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:200` (Z-2) and `:366` (Z-NOGO). The knife edge at `k = e` is `.../f2_z1_mass_knife_edge/statement.md:46-53`.

---

## NOT FOUND / caveats you should not paper over

1. **No node named with an `es_` prefix states (ES) itself.** The three `es_*` nodes are `background/nodes/es_regularity` (an unrelated 2026-era TARGET about Tao's algebraic regularity lemma — `node.json` only, no statement.md), `background/nodes/es_ternary_suppression_instruments` (the *instruments*), and `background/nodes/esg_lane_rescope` (the *re-scope*). The statement of record for (ES) lives only in `notes/pilots_20260804/mun_anticoncentration/REPORT.md:40`.
2. **The exact official `q` is deliberately NOT pinned** — `u2c_giant_tnull_dichotomy/node.json:8` states *"the official factorization q = p^k is pinned nowhere"* and `official_row_primes_pinning/statement.md:10` states the challenges *"do not specify a hidden finite list of official row primes."* Any report claiming a single official `q` is misquoting the repo.
3. **The 19 (class, e) pairs are never printed as a labelled list in a `.md` node**; the enumeration exists only as the machine table at `notes/pilots_20260806/es_g_lanes/full_run.txt:53-71` (plus the generating rule at `es_g_lanes/PROOFS.md:143-144` / `full_run.txt:48-50`). I reconstructed the 6+3+3+3+4 breakdown from that table.
4. **`log2 S(2^34) = 117.149` vs `log2 C(128,63) = 124.149`** — these are *not* interchangeable; see the correction at `notes/pilots_20260806/es_g_lanes/FABLE_AUDIT.md:96-98` and `notes/pilots_20260806/crossing_low_w/REPORT.md:107`.
5. **The mun_anticoncentration REPORT.md is a recovered artefact** — header line `:1` reads: `(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)` Cite it as recovered, and prefer the FABLE_AUDIT for adjudications.
6. The three quarantined `tern_*` dirs were **not** opened; anything they contain about the round-19 ternary unification is outside this sweep. The only round-19 material I read is `notes/pilots_20260806/tern_unification_adversary/PREREG.md` (not on the exclusion list).