# xr_mc_depth_quantization

- **status:** PROVED
- **closure:** proof
- **scope:** the quantization and exclusion arguments are exact
  divisibility/parity arithmetic, valid at every scale; BP(2)'s slope
  confinement is proved on the SHIFT CLASS only (see NOT-claimed);
  structured-floor completeness (the Lam-Leung half of BP(1)) is char-0
  input, machine-checked at one large-`q` shape.
- **provenance:** occupancy-v2 pilot THEOREM 5
  (`notes/pilots_20260802/xr_occupancy_v2/{REPORT,FABLE_AUDIT}.md`,
  `mc.py`) MERGED with the band-adjudication pilot's THEOREM BP
  (`notes/pilots_20260802/band_adjudication/REPORT.md` section 2,
  `exp_band_proper.py`, 135 checks 0 fails) — BP(3)'s parity argument
  is STRICTLY STRONGER than the occupancy-v2 count where they overlap
  and is preferred here, per the occupancy-v2 REPORT's own section 6.
  MC construction inputs are `xr_band_key_lemma_pencil_mass` (MC-1/2/3)
  and the banked coset mechanism
  (`background/nodes/e22_tail_coset_locator_algebra`).

## Setting

Multiplicative-coset domain `H = x_0 mu_n` in `F_q^*` (`n | q-1`),
`C = RS_k` on `H`, `A = k + h`, band (proper) = depths `[1, h-2]`,
cascade tier = depth `h-1` (definitions items 2, 3). MC word
`u = X^{n-1} + c X^{k+w-1}`, `r' = n - k - w`; for `M | n`, `M | r'`,
`w <= M`, `N = n/M`, `m = r'/M`, the MC family is the set of unions `T`
of `m` cosets of `mu_M` with `prod T = gamma = (-1)^{r'+1} c`; each
member `P_T` agrees with `u` EXACTLY on `H \ T` (agreement exactly
`k + w`: MC-1/MC-2, consumed from `xr_band_key_lemma_pencil_mass`).
Shift pencil: `v = u / X^j mod (X^n - beta)`, `1 <= j <= M-1` — the
unique shift class keeping the whole family joint, because
`X^{M-1} | P_T`; the `v`-side members are `Q_T = P_T / X^j`.

## Statement (all PROVED)

1. **THEOREM 5 (MC depth quantization — diagonal at exactly `w`).**
   Distinct coset unions `T != T'` share at most `m - 1` cosets, so
   `|T ^ T'| <= r' - M`, hence the cross joint agreement is

   ```text
   |(H \ T) ^ (H \ T')| = n - |T u T'| <= n - r' - M = k + w - M <= k.
   ```

   So the only MC-family band pairs are DIAGONAL `(P_T, Q_T)`, with
   joint agreement exactly `H \ T`, i.e. depth exactly `w`. The
   two-live-slope profile of an MC pencil is supported on
   `{0, h-1}`-type depths only: `N_d = 0` at every band-proper depth
   (re-verified exhaustively at two shapes here; five in the pilot
   record — stray sub-band pairs occur but carry no live slopes).
2. **THEOREM BP(1) (structured => depth a power of two).** If a pair's
   core complement is a `mu_M`-coset union with
   `M = 2^ceil(log2 d)` (the structured/coset family, definitions
   item 10), then `M | d`; with `M >= d` this forces `M = d`, so `d`
   is a power of two. At the six-row shape (`n`, `k` powers of two,
   `h` ODD): the unique power of two in `[ceil(h/2), h]` is `h - 1`,
   so the band proper's upper window `[ceil(h/2), h-2]` contains NO
   structured depth, and excess `h` itself is not structured (`h`
   odd).
3. **THEOREM BP(3) (parity exclusion — the stronger argument,
   preferred).** On the shift class, the direction map of every
   depth-`d` pair is `zeta_P(i) = -x_i^j`, whose fibres on `H` are
   `mu_g`-cosets, `g = gcd(j, n)`; a forced ray at depth `d` has
   agreement `(k + d) + g`. It is LIVE iff `g = h - d`. At the six
   rows `g` is a power of two and `h` is odd, so `h - d` is odd for
   every even `d`; `d` is a power of two by BP(1), so `d >= 2` forces
   `g = h - d` impossible, and `d = 1` admits no shift
   (`j <= M - 1 = 0`). Hence

   ```text
   N_d^{coset} = 0   for EVERY band-proper depth d in [1, h-2],
   ```

   at all six rows. The band proper is unreachable by coset
   constructions; the occupancy lemma keeps its original scope
   `[1, h-2]` against this class, and the MC/coset class does not
   fire F1.
4. **BP(2) (slope confinement trichotomy — scope: the shift class).**
   `g < h - d`: agreement `< A`, no live slope (invisible to
   occupancy). `g = h - d`: live, and the forced slopes confine to
   `{-x^j : x in H}`, so `|Gamma| <= n / (h - d)` and, with k-packing
   exclusivity, `N_d <= n / (2(h - d))` — LINEAR in `n`.
   `g > h - d`: over-agreement — the tangent gate breaks (T2/P2
   fires) and the pair leaves the generic branch. The `h`-EVEN
   positive control (`n = 20, h = 6, d = 4, j = 2`) realizes the live
   case: the mechanism is REAL, and the official rows are protected by
   PARITY, not by impossibility.
5. **Cascade-tier population (context, load-bearing definition).** At
   the prize rows `w = M = h - 1` is the unique admissible power of
   two in `[ceil(h/2), h-1]`; the MC family then sits entirely at the
   cascade tier with `C(N,m)/N` members. Under the SELECTED-support
   reading of `L_P` (definitions item 8) each live slope serves at
   most one cascade-tier pair (k-packing exclusivity), so
   `N_{h-1} <= n/2`; under the un-banked "any exact-`A` ray" reading
   it would be `2^130`-`2^197` — the definition is load-bearing and
   pinned.

## Explicitly NOT claimed (context)

- **BP(2) covers the shift class only** (`v = u/X^j`) — the unique
  class keeping the whole family joint. General `v` against an MC `u`
  is heuristically empty but UNPROVED (band-adjudication caveat 4).
- **BP protects against COSET-type constructions** — the adjudicated
  question — not against all conceivable families; char-`p` accidental
  non-coset families occur outside the six-row shape (observed at
  `n = 18`); the structured-floor completeness input (MC-4) is char-0
  Lam-Leung, machine-checked here empirically at one shape
  (`(16,8,2,2)`, `q = 65537`: the structured window census equals the
  coset-union family exactly).
- **No claim that the MC pair reaches the generic branch**: it is
  quotient-periodic at `M = h-1`, `M | gcd(n,k)`, so P3 fires first
  under the banked strip order (band-adjudication section 1.5) —
  whether P3 FORMALLY fires depends on the quotient convention
  ("syndromes descend"), an open adjudication item (definitions
  item 6). The theorems above do not depend on it.
- **No claim about `|Gamma|` beyond the shift class at `j = 1`**: at
  `j = 1` `Gamma subset -H` is a THEOREM (adv_gamma_minus_h, banked
  coordinator amendment); at `j >= 2` the SET claim is refuted while
  the cardinality bound `|Gamma| <= n` stays — stated separately
  there, consumed here only through `|Gamma| <= n/(h-d)` on the live
  case.
- Nothing here proves or prices the occupancy lemma; this node
  removes one adversary class from the band proper.

## Falsifier

An MC pencil with a non-diagonal family pair of joint agreement
`> k`; a coset-union core complement at a non-2-power depth; a
productive shift `j` at a band-proper depth on a six-row-shape row; or
a live forced slope outside `{-x^j : x in H}` on the shift class.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers,
deterministic, no third-party imports, no reads outside this
directory). Checks: the coset-sharing integer `|T ^ T'| <= r' - M`
(exhaustive); MC diagonal quantization at `(16,4,2,2,q=97)` and
`(20,4,4,4,q=41)` by fresh exhaustive scan — agreement exactly `k+w`
per member, cross pairs `<= k`, `N_d = 0` at every band-proper depth,
cascade count = `C(N,m)/N`, line-cap saturation `L = n - A + 1` on the
diagonal pairs; BP(1)/BP(3) exact 2-adic arithmetic at all six rows
(unique 2-power in `[ceil(h/2), h]` is `h-1`; no structured depth in
the upper window; parity exclusion for every 2-power `d <= h-2`);
BP(3)/BP(2) fresh replication of the adjudication fixtures — `h = 6`
(even) control: `j = 2` productive with slopes inside `{-x^2}` and
`|Gamma| <= n/(h-d)`, `j in {1,3}` dead; `h = 7` (odd): NO productive
`j`; `h = 5`, `d = h-1`: `j = 1` productive (cascade tier, allowed);
and the structured-floor completeness census at `(16,8,2,2)`,
`q = 65537`.
