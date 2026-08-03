# f2_parity_defect_certificate

- **status:** PROVED
- **closure:** proof
- **scope:** the certificate (Theorem 1) is an exact identity plus a
  triangle inequality inside the banked F2 first-descent window model,
  valid at every `p`, every admissible subgroup order and every
  frequency. The full-group evaluation (Theorem 2) is proved for the
  window `n_ord = p^2 - 1` under the **necessary** non-degeneracy
  condition `a_c != 0` and `b_c != 0`; the two excluded lines are
  identified exactly and shown to be genuinely exceptional.
- **provenance:** F2 deployed-windows pilot: derivation of record at
  `notes/pilots_20260802/f2_deployed_windows/deployed.py:37-56`
  (the `(DEF)`/`(FLAT)` block), reference implementation at
  `deployed.py:126-147` (`parity_classes`, `defect`, `flat_bound`),
  production implementation at
  `notes/pilots_20260802/f2_deployed_windows/census.py:65-75`
  (`defect_from_counts`), corollary check at
  `notes/pilots_20260802/f2_deployed_windows/verify.py:300-321`
  (`A8_crosscheck`), prose statement + status at
  `REPORT.md:37` ("a PROVED (H-flat) certificate") and `REPORT.md:45`
  ("**(T2) the parity-defect certificate — proved, exact**"), mint-queue
  entry at `FABLE_AUDIT.md:61-66`.

## Setting

Exactly the model of `f2_antipodal_descent_lemma` (restated so this node
is self-contained): `p` an odd prime, `F_{p^2} = F_p(w)`, `w^2 = N_0` the
least quadratic non-residue; an admissible subgroup order `n_ord`
(`n_ord | p^2-1`, even, not dividing `p-1`); a frequency
`c = (a_c, b_c) in F_{p^2}^*`. The window is the complete set of
`m = (n_ord - gcd(n_ord, p-1))/2` genuine Frobenius pairs, one
representative `y_i` per pair (convention: `w`-component in
`[1, (p-1)/2]`). Per coordinate:

```text
s_i^+ = Tr(c y_i),  s_i^- = Tr(c y_i^p)      (least residues in [0,p))
sigma_i^pm = s_i^pm + p*[2 s_i^pm > p]       (in Z/2p)
Delta_i    = sigma_i^+ - sigma_i^-           (in Z/2p)
```

With `omega = zeta_{2p}` a primitive `2p`-th root of unity,

```text
R_k = (1/m) sum_{i=1}^{m} omega^{k Delta_i},
flat := 1 - max_{k odd} |R_k|.
```

Because `Delta_i` lives in `Z/2p` and `2p` is even, the **parity** of
`Delta_i` is well defined.

## Statement

1. **THEOREM 1 (parity-defect certificate — PROVED).** For `d in Z/p`
   set

   ```text
   c_d := #{i : Delta_i == d (mod p), Delta_i EVEN}
        - #{i : Delta_i == d (mod p), Delta_i ODD}       (an integer),
   x_d := the EVEN element of {d, d+p} in Z/2p,
   D   := sum_{d in Z/p} |c_d|                            (a non-negative integer).
   ```

   Then for **every odd** `k`:

   ```text
   (ID)    R_k = (1/m) sum_{d in Z/p} c_d * omega^{k x_d},
   (DEF)   max_{k odd} |R_k| <= D/m,
   (FLAT)  flat >= 1 - D/m.
   ```

   `D` is computed from the exact `Delta` multiset by integer arithmetic
   alone; the bound is **mode-uniform** (one integer bounds all `p` odd
   modes at once). A residue class split exactly evenly between the two
   parities has `c_d = 0` and contributes nothing at any frequency —
   perfect local cancellation.
2. **THEOREM 2 (the full-group window — PROVED, with its exact scope).**
   Let `n_ord = p^2 - 1` (the FULL group `F_{p^2}^*`). Then
   `m = p(p-1)/2`, and for every frequency `c = (a_c, b_c)` with

   ```text
   a_c != 0   AND   b_c != 0
   ```

   the defect is **exactly** `D = ((p-1)/2)^2`, hence

   ```text
   flat(full group) >= 1 - ((p-1)/2)^2 / (p(p-1)/2) = (p+1)/(2p) > 1/2.
   ```

   The intermediate identity is sharp and is what makes the count exact:
   with `M := (p-1)/2` and `kappa(x) := (-1)^{centred representative of x mod p}`,

   ```text
   c_d = A(d),   A(t) := sum_{a in F_p} kappa(a) kappa(a+t) = (-1)^t (p - 2t)
                        for 0 <= t <= M, and A is even in t,
   ```

   and the support of `(c_d)` is a **half-system** of `F_p^*` (exactly one
   of each pair `{d, -d}`), so `|A|` runs over `p-2t`, `t = 1..M`, each
   value once, giving `D = sum_{t=1}^{M} (p-2t) = M^2`.
3. **THEOREM 3 (the two exceptional lines — PROVED).** The hypothesis of
   Theorem 2 is necessary, and the failure is total on both excluded
   lines:
   - `b_c = 0` (i.e. `c in F_p^*`): then `s_i^+ = s_i^-` and
     `Delta_i = 0` for every `i`; `D = m`, `(FLAT)` degenerates to
     `flat >= 0`.
   - `a_c = 0` (i.e. `c in w F_p^*`): then `s_i^- = -s_i^+`, every
     `Delta_i` is EVEN (the same mechanism as
     `f2_antipodal_descent_lemma` Corollary B), so every `c_d >= 0`,
     `D = m`, and again `(FLAT)` degenerates.

   These are exactly the two parity-pure lines the pilot names; on both
   of them `D = m` and the certificate carries no information.
4. **COROLLARY (the degenerate branch — PROVED).** If a window is
   parity-homogeneous (every `Delta_i` even — the conclusion of
   `f2_antipodal_descent_lemma` at every deployed rung window), then
   `c_d = #{i : Delta_i == d} >= 0`, so `D = sum_d c_d = m` and `(FLAT)`
   gives only `flat >= 0`. **The certificate is informative exactly to
   the extent that the window is parity-INHOMOGENEOUS.** For deployed
   rung windows the true value is `flat = 0` (that node's Corollary C),
   so nothing is lost: the certificate is tight there.

## Explicitly NOT claimed (context)

- **This is NOT an (H-flat) certificate for any DEPLOYED window.**
  Theorem 2 is about `n_ord = p^2-1`, a window "the tower does NOT
  deploy" (`REPORT.md:37`). Its value is as the TEMPLATE for certifying
  whatever windows the frequency-space case split actually sends to the
  slice theorem (`FABLE_AUDIT.md:61-66`) — not as a discharge of
  anything.
- **`(DEF)` is an upper bound on `max_{k odd}|R_k|`, not an identity.**
  It can be lossy; no claim of sharpness is made except in the degenerate
  branch (Corollary 4) where it is tight.
- **No claim about even modes `k`.** The whole certificate rests on
  `omega^{k(x+p)} = -omega^{kx}` for `k` ODD; for even `k` the two
  parities do not cancel and the grouping fails.
- **No generic-frequency flatness claim** (the pilot's T3, ~0.55-0.60,
  is OPEN; `REPORT.md:45`).
- **The multiplicity law is NOT claimed as a theorem.** "the sorted
  non-zero `Delta`-counts over `Z/2p` are `[1, 2, ..., p-1]`" is part of
  the pilot's A8 check; here it is machine-VERIFIED (exhaustively over
  all frequencies with `a_c b_c != 0` at `p = 11..31`, and at the pilot's
  `p = 41`) and labelled MEASURED. It is not used in the proof of
  Theorem 2.
- **No claim about the K1 mass obligations (O1)-(O3)** — those are OPEN
  constructive obligations (`f2_fixed_sector/REPORT.md:33`), untouched
  here.
- **Convention dependence, inherited and made precise.** `REPORT.md:71`
  records that "all `Delta` even" is invariant under orientation flips
  while `max_{k != p}|R_k|` is NOT. For `D` the exact statement (proved
  in `proof.md`, Claim 6) is: `D` is invariant under the **global**
  orientation reversal (`Delta_i -> -Delta_i` for all `i`, which
  preserves parity and permutes the classes by `d -> -d`), but **NOT**
  under partial flips — the verifier exhibits partial flips that change
  `D`. Theorem 2 is stated at the banked half-system labelling; do not
  quote `D` as label-free.

## Falsifier

A window (`p`, `n_ord`, `c`) and an odd `k` with `|R_k| > D/m`; or a
frequency `c` of the full group with `a_c b_c != 0` and
`D != ((p-1)/2)^2`; or an exhibit of `A(t) != (-1)^t (p-2t)` for some
`0 <= t <= (p-1)/2`; or a support of `(c_d)` at the full group that is
not a half-system.

## Verifier

`verify.py` in this node (profile: `tiny`; pure python integers,
deterministic, no third-party imports, no reads outside this directory —
the model is re-implemented from scratch). Checks: (A) the grouping
identity `(ID)` against a DIRECT exact evaluation of `R_k` in the
cyclotomic ring `Z[zeta_p]` (no floats) at every odd `k`, over many
windows; (B) `(DEF)` against the same exact `|R_k|^2` values; (C) the
autocorrelation formula `A(t) = (-1)^t (p-2t)`; (D) the half-system
property of the support; (E) Theorem 2 EXHAUSTIVELY over **every**
frequency of `F_{p^2}^*` at `p = 11,13,19,23,31` — `D = ((p-1)/2)^2` at
every one with `a_c b_c != 0`, and the pilot's own row (`p = 11..41`,
`c = (1,1),(2,3)`) reproduced; (F) Theorem 3 — the two excluded lines
give `D = m` and are the ONLY exceptions; (G) the multiplicity law
(labelled MEASURED); (H) Corollary 4 on rung-1 deployed windows
(`D = m`, and the true `flat = 0`); (I) flip-robustness of `D` under a
random orientation relabelling.
