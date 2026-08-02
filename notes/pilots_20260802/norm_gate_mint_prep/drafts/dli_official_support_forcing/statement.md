# dli_official_support_forcing

- **status:** PROVED
- **closure:** proof plus exact integer ledger
- **scope:** the banked official DLI production schedule (`n = 2^41`,
  `t = 2^33`, 34 blocks / 33 junctions, `N_j = 256 L_j` uniformly), and any
  official-admissible modulus `q` (odd prime, `v_2(q-1) >= 41`, `q < 2^256`).
  The `|S_0| >= 4` form additionally requires `q > 3^128 = 2^202.87...`,
  which the production window satisfies with 53 bits to spare; the general
  `E >= E_min(q)` form holds for every admissible `q`.
- **provenance:** notes/pilots_20260802/dli_norm_gate/{REPORT,FABLE_AUDIT}.md
  §4 (LN5 at the official schedule). Official pins inlined from
  `notes/pilots_20260802/c2pp_nullity_structure/results/official_scale.json`.
  Tower validation of LN2/LN4/LN5 at real junctions `j = 0,1,2` in
  `notes/pilots_20260802/dli_norm_gate/results/tower.json`
  (`all_hold = true`; 2,453 states predicted empty by the router, 0 solutions
  found in them).

## Setting

The official C2''/DLI tower at `n = 2^41`, `t = 2^33`. Blocks
`B_j = {r <= t : v_2(r) = j}` for `j = 0..33`, so `L_j = |B_j| = 2^{32-j}`
for `j <= 32` and `L_33 = 1`, `sum_j L_j = t`. Junction `j` (`j = 0..32`,
33 junctions) works in `Z[zeta_{h_j}]` with `h_j = n/2^j`, degree
`N_j = phi(h_j) = h_{j+1} = 2^{40-j}`, and carries the `L_j` constraints
`sum_{i < N_j} d_i zeta_{h_j}^{u i} = 0`, `u in U_j`. Uniformly

```text
N_j = 256 L_j        for every j = 0, ..., 32.                       (OS-1)
```

The skew `d` has `|d_i| <= c_i` with `d_i == c_i (mod 2)` on the effective
(unsaturated) support `S_j`; its **energy** is `E = sum_i d_i^2`. At `j = 0`,
`c_i = 1` on `S_0` and the domain is `{+-1}^{S_0}`, so `E = |S_0|` exactly and
the domain contains no zero vector.

## Statement

1. **Uniform junction criterion (PROVED).** For every official junction
   `j` and every official-admissible `q`, a NONZERO junction-`j` skew
   solution of energy `E` satisfies

   ```text
   q^{L_j} <= Norm(delta) <= E^{N_j/2} = (E^{128})^{L_j},
   i.e.        q <= E^{128},                                          (OS-2)
   ```

   **independently of `j`**. Equivalently every junction solution has
   `E >= E_min(q) := min{ E in Z_{>0} : E^{128} >= q }`.
2. **The `E_min` ledger (PROVED, exact integers).**

   ```text
   E_min(q) = 2   for  q <= 2^128,
              3   for  2^128 < q <= 3^128 = 2^202.87...,
              4   for  3^128 < q <= 4^128 = 2^256   (EXACTLY the official cap).
   ```

   `4^128 = 2^256` is an exact identity, so `E_min <= 4` throughout the
   official range and `E_min = 4` on all of `3^128 < q < 2^256`.
3. **Official support forcing (PROVED).** For every official-admissible
   `q > 3^128`:

   ```text
   every t-null state satisfies  |S_0| = 0  or  |S_0| >= 4.           (OS-3)
   ```

   More generally, at any junction `j`, a state whose entire admissible skew
   domain satisfies `sum_{i in S_j} c_i^2 <= 3` admits NO nonzero skew
   solution — in particular (all `c_i = 1`) any state with at most 3
   unsaturated cells is killed.
4. **The exclusion is total at junction 0, not a small residual (PROVED
   given the banked definition of `rho_j`).** The junction-0 skew domain
   `{+-1}^{S_0}` contains no zero vector, so for an excluded state the
   solution count is `0` and hence `rho_0 = q^{L_0} * 0 / 2^{|S_0|} = 0`
   exactly; in the banked exact decomposition `rho_j = q^{delta_j} + Rem_j`
   (`notes/pilots_20260802/c2pp_nullity_structure/junctions.py`, certified in
   `Z[zeta_q]`, 24/24) this reads `Rem_0 = -q^{delta_0}` exactly. **The
   router kills states; it does not merely shrink a remainder.**

## Named instance (context)

The C2'' named 256-bit exhibit
`q = 2^256 - 191,315,023,233,023` has `v_2(q-1) = 41`, `q.bit_length() = 256`,
and `3^128 < q < 2^256`, so `E_min(q) = 4`: **at that modulus every t-null
state has `|S_0| = 0` or `|S_0| >= 4`.** Its primality is the banked C2''
BPSW claim and is NOT re-certified here (the verifier runs only a 12-base
strong-probable-prime test and says so); **no claim above depends on the
exhibit being prime** — it is an illustration of the pricing, and the theorem
quantifies over admissible `q`.

## Explicitly NOT claimed (context)

- **Not** `|S_0| >= 4` for every formally admissible official `q`. The
  official constraints (`v_2(q-1) >= 41`, `q < 2^256`) permit `q` as small as
  about `2^41`, where `E_min = 2` and only `|S_0| = 1` is excluded. The
  `>= 4` form is a statement about `q > 3^128`, which covers the production
  window (`q ~ 2^255.9`).
- **Not** a bound on states with `|S_0| >= 4`. The gate is one-sided:
  `E >= E_min` is necessary, never sufficient. What happens at `|S_0| >= 4`
  is exactly the open territory (count bounds, not max-norm bounds).
- **Not** a `j > 0` census statement. Claims 1-3 are proved for every
  junction; the identification of the C2'' junction census with the banked
  C1 census is a junction-0 result
  (`dli_norm_gate_forward_and_ofold`, bridge section).
- **Not** the `rho_j = 0` conclusion at `j > 0` in general: when some
  `c_i` is even the skew domain contains `d = 0`, which trivially solves, so
  the solution count is `>= 1` and `rho_j > 0`. Claim 4 is stated at
  junction 0 (and holds verbatim at any junction all of whose `c_i` are odd).
- **Not** the 34th-block reading. Using a final block with ratio `128`
  instead of `256` would give `q <= E^{64}` and `E_min = 16` at the exhibit.
  The pinned schedule (`official_scale.json`: 33 junctions, ratio `256`
  uniformly) is what is used; the alternative reading is recorded in the
  verifier and NOT relied on.
- **Not** the WCL fence. The associated law "no open WCL slot (`w >= 5`) is
  reachable by a max-norm gate, since `23^64 = 2^289.5 > 2^256`" is the same
  arithmetic applied to a different banked family; it is recorded in the
  provenance pilot §5 as a decisive negative and is a candidate SEPARATE
  node, not asserted here.

## Falsifier

An official-admissible `q > 3^128` together with a `t`-null state whose
level-1 unsaturated cell count `|S_0|` lies in `{1,2,3}`; or a junction-`j`
skew solution with `q > E^{128}`; or an arithmetic error in the `E_min`
ledger (all entries are exactly bracketed integers).

## Verifier

`verify.py` in this node (profile: `tiny`, pure python integers, no floats,
no logarithms; runs in well under a second). Checks: the banked schedule pins
inlined from `official_scale.json` plus the independent derivation
`L_j = #{r <= t : v_2(r) = j}` (exhaustive for `t = 2..2^11`); `N_j = 256 L_j`
and `N_j/2 = 128 L_j` at all 33 junctions; the `q^L <= E^{128L} <=> q <= E^128`
collapse on 120 exact-integer triples; the full `E_min` ledger with every
entry bracketed by `(E_min-1)^128 < q <= E_min^128`; `4^128 = 2^256` and
`3^128` to the digit with `bit_length = 203`; the `2^53`-bit production
margin; the exhibit's admissibility shape and `E_min = 4` (with the explicit
BPSW/non-certificate caveat); the support-forcing exclusion `{1,2,3}` and the
general `sum c_i^2 <= 3` cell profile test; and the two honest-scope items
(small admissible `q` gives `E_min = 2`; a single constraint at junction 0
excludes only `E = 1`) plus the recorded, unused 34th-block reading.
