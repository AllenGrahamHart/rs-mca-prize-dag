# f2_antipodal_descent_lemma

- **status:** PROVED
- **closure:** proof
- **scope:** clauses (i)-(iii) are pure number theory (LTE + an order
  argument), exact at every rung and every prime of the stated shape,
  including the official KoalaBear prime. The CONSEQUENCE (parity
  homogeneity) is stated inside the banked F2 first-descent window model
  and is exact there; it is **not** a statement about any other window
  family.
- **provenance:** F2 deployed-windows pilot, statement and proof of
  record at
  `notes/pilots_20260802/f2_deployed_windows/tower.py:22-43`
  ("LEMMA (exact; verified in verify.py A1)" ... "QED"), prose twin at
  `notes/pilots_20260802/f2_deployed_windows/REPORT.md:23-33`, theorem-
  candidate status line at `REPORT.md:45` ("**(T1) the antipodal descent
  lemma — proved**"), independent coordinator hand-derivation at
  `notes/pilots_20260802/f2_deployed_windows/FABLE_AUDIT.md:27-33`
  ("Elementary and airtight"), theorem-of-record amendment at
  `notes/pro_briefs_20260801/responses/F2_SLICE_THEOREM_DRAFT.md:114-129`
  ("(proved, elementary)"). Cited as the statement of record downstream by
  `notes/pilots_20260802/f2_fixed_sector/core.py:20-22`.

## Setting

`p` an odd prime with `e := v_2(p-1) >= 2`. For `j >= 0` put

```text
n_j = 2^{e+j},        q_j = p^{2^j}.
```

`mu_N` denotes the group of `N`-th roots of unity in a fixed algebraic
closure of `F_p`. `v_2` is the 2-adic valuation.

**The banked first-descent window model** (`f2_carry_reachability/f2model.py`,
`f2_slice_coefficients/slicecore.py`, re-derived from scratch in `verify.py`):
`F_{p^2} = F_p(w)`, `w^2 = N_0` with `N_0` the least quadratic non-residue;
a frequency `c = (a_c, b_c) in F_{p^2}^*`; a subgroup order `n_ord` with
`n_ord | p^2-1`, `n_ord` even, `n_ord` not dividing `p-1`. The **window**
is the complete set of genuine Frobenius conjugate pairs `{y, y^p}` of
`mu_{n_ord}` — `m = (n_ord - gcd(n_ord, p-1))/2` coordinates, **no
selection**. Per coordinate:

```text
s_i^+ = Tr(c y_i),  s_i^- = Tr(c y_i^p)      (least residues in [0,p))
sigma_i^pm = s_i^pm + p*[2 s_i^pm > p]       (in Z/2p)
Delta_i    = sigma_i^+ - sigma_i^-           (in Z/2p)
```

With `omega = zeta_{2p}`, the mode weights of the lane are
`R_k = (1/m) sum_i omega^{k Delta_i}` and `flat := 1 - max_{k odd} |R_k|`.

## Statement (all PROVED)

1. **THEOREM (antipodal descent).** For `p` and `e >= 2` as above:
   - **(i)** `v_2(q_j - 1) = e + j` for every `j >= 0`;
   - **(ii)** `mu_{n_j} <= F_{q_j}^*`, and for `j >= 1`
     `mu_{n_j} ^ F_{q_{j-1}} = mu_{n_{j-1}}`;
   - **(iii)** every `y` of order exactly `n_j` (`j >= 1`) satisfies
     `y^{q_{j-1}} = -y`.
2. **COROLLARY A (antipodal pairs).** The rung-`j` descent pairs each
   genuine `y` with its Frobenius conjugate over `F_{q_{j-1}}`, and by
   (iii) that conjugate is `-y`: **the rung-`j` Frobenius conjugate pairs
   are exactly the ANTIPODAL pairs `{y, -y}`.**
3. **COROLLARY B (parity homogeneity of every deployed window).** In the
   model above, on a rung-`j` window (`j >= 1`; concretely `n_ord = n_j`,
   whose genuine elements are those of order exactly `n_j`), for **every**
   frequency `c` and **every** coordinate `i`:

   ```text
   s_i^- = -s_i^+  in F_p,   sigma_i^- = -sigma_i^+  in Z/2p,
   Delta_i = 2 sigma_i^+     ==  EVEN.
   ```

   The window is parity-homogeneous.
4. **COROLLARY C (the mode `k = p` is slice-dead; `flat = 0` exactly).**
   `p` is odd, and `omega^p = -1`, so under Corollary B
   `R_p = (1/m) sum_i (-1)^{Delta_i} = 1`. Hence `max_{k odd}|R_k| = 1`
   and **`flat = 0` exactly**, at every rung, every frequency, every `p`
   of the stated shape.
5. **COROLLARY D (no window selection can repair it).** "All `Delta_i`
   even" is a COORDINATEWISE property, so every non-empty sub-window of a
   rung-`j` window inherits it, and Corollary C applies to the sub-window
   verbatim. **Window selection is impossible in principle** — the
   degeneracy cannot be escaped inside coordinate space.

## Explicitly NOT claimed (context)

- **The degeneracy law is NOT claimed.** `n_ord/gcd(n_ord, p-1) == 2
  <=> all Delta even` is a CENSUS result (194 `(p, n_ord)` rows, 0
  violations, `notes/pilots_20260802/f2_deployed_windows/results/degeneracy_law.json`
  via `census.py:202-245`) — **measured, not proved**. This node proves
  only the `=>` direction for the rung subgroups, which is what the lane
  consumes.
- **The `-log2 rho_b <= log2 p + o(1)` corollary is NOT claimed.** The
  `1/p` ceiling ladder (`REPORT.md:39`, `results/E8_floor_ladder.json`)
  is exact-integer at toy scale with a measured saturation
  (`p=257`: 8.0054-8.0055 vs `log2 p = 8.0056`); the `o(1)` and the
  official-scale extrapolation are not proved here.
- **No generic-frequency flatness claim** (the pilot's T3, ~0.55-0.60,
  is OPEN — it needs an incomplete-character-sum bound over the 2-Sylow
  coset half-system, "not attempted", `REPORT.md:45`).
- **The K1 mass obligations (O1)-(O3) are OPEN and are not touched here.**
  `(O1)` `E_{c in K1}[exp S_c] <= 2^{n/2+o(n)}`, `(O2)` the same at fixed
  `b`, `(O3)` PP5.0 carrying the pullback ramification `2^d`
  (`notes/pilots_20260802/f2_fixed_sector/REPORT.md:33`) are a
  **constructive replacement obligation**, not a theorem. The measured
  first-moment constant behind (O1) is explicitly "banked as a labelled
  first-moment heuristic" (`f2_fixed_sector/REPORT.md:39,54`). Nothing in
  this node discharges any of them.
- **No claim that the fixed sector absorbs the parity-pure class** — that
  was REFUTED (`f2_fixed_sector` Theorem B, "no absorption, proved"); the
  refutation is the reason (O1)-(O3) exist.
- **Hypotheses are necessary, not cosmetic.** The law needs `n` a 2-power
  and the subgroup exactly one level above the fixed part; it **fails if
  `n` has an odd part** (`REPORT.md:70`). It also needs `e >= 2` (i.e.
  `p == 1 mod 4`); at `e = 1` clause (i) already fails.
- **Not a statement about the full-group window.** For
  `n_ord = p^2 - 1` the window is parity-INhomogeneous at generic
  frequencies — see `f2_parity_defect_certificate`. The two facts are
  complementary, not in tension.

## Falsifier

A prime `p` with `e = v_2(p-1) >= 2`, a rung `j >= 1` and an element `y`
of order exactly `2^{e+j}` with `y^{q_{j-1}} != -y`; or a value of `j`
with `v_2(p^{2^j}-1) != e+j`; or a rung-`j` deployed window and a
frequency `c` with some `Delta_i` odd; or a rung-`j` window with
`|R_p| != 1`.

## Verifier

`verify.py` in this node (profile: `tiny`; pure python integers,
deterministic, no third-party imports, no reads outside this directory —
the window model is re-implemented from scratch rather than imported).
Checks: (A) LTE at the official KoalaBear prime `p = 2^31-2^24+1`
(`e = 24`) for rungs `j = 0..16`, by two independent routes (exact big
integers up to `j = 6`, and a `2^64`-modular route valid because
`e+j <= 40 < 64`); (B) LTE at 8 further primes with `e = 2..8`;
(C) clause (iii) at rung 1 in `F_{p^2}` — every element of order exactly
`2^{e+1}` satisfies `y^p = -y` and `Tr(y) = 0`; (D) clause (ii) at rung 1
(`mu_{2^{e+1}} ^ F_p = mu_{2^e}`); (E) Corollary B EXHAUSTIVELY over
**every** frequency `c in F_{p^2}^*` at several primes — all `Delta_i`
even, 0 violations; (F) Corollary C — `R_p = 1` and `flat = 0` exactly,
by exact integer arithmetic (no floats); (G) Corollary D — sub-window
inheritance on random sub-windows; (H) NON-VACUITY — the full-group
window at the same primes has odd `Delta_i` and `flat > 0`, so the law
is a property of the rung subgroups, not of the model.
