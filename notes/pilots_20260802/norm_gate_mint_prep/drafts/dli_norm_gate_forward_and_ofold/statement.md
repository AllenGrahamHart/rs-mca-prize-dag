# dli_norm_gate_forward_and_ofold

- **status:** PROVED
- **closure:** proof
- **scope:** `n = 2^s >= 4`, `q` an odd prime with `n | q - 1` (the DLI
  admissibility condition), any coefficient vector supported in the
  **basis range** `[0, phi(n))`. Official C2'' instantiation: every
  junction `j` of the DLI tower, root order `h_j = n/2^j`, constraint
  block `U_j`, `o = L_j = |U_j|`.
- **provenance:** notes/pilots_20260802/dli_norm_gate/{REPORT,FABLE_AUDIT}.md
  (lemmas LN0-LN3), coordinator audit alongside. Formalizes the
  C2'' pilot's measured law L13
  (`notes/pilots_20260802/c2pp_nullity_structure/REPORT.md` §5) and
  identifies it, at junction 0, with the banked C1 relation-side router.

## Setting

`n = 2^s` with `s >= 2`, `h = phi(n) = n/2`, and

```text
Z[zeta_n] = Z[x]/(Phi_n(x)) = Z[x]/(x^h + 1),
Norm(alpha) = det( multiplication by alpha on Z[zeta_n] )
            = prod_{j odd mod n} alpha(zeta_n^j)                   (over C),
```

the field norm `N_{Q(zeta_n)/Q}`. `q` is an odd prime with `n | q - 1`;
`zeta in F_q^*` has exact order `n`. For `alpha = sum_{i < h} a_i zeta_n^i`
with `a_i in Z` put

```text
Z(alpha) = { j odd mod n : alpha(zeta^j) = 0 in F_q },   m(alpha) = |Z(alpha)|.
```

A **skew/relation solution for the block `U`** (`U` a set of `o` odd
residues mod `n`) is such an `alpha`, supported in `[0, h)`, with
`alpha(zeta^u) = 0` in `F_q` for every `u in U`. In the C2'' tower at
junction `j` the skew element is `delta = sum_{i < h_{j+1}} d_i zeta_{h_j}^i`
and the index range `0 <= i < h_{j+1} = phi(h_j)` is exactly the basis
range, so the basis-range hypothesis holds BY CONSTRUCTION.

## Statement (all four claims PROVED)

1. **LN0 (splitting).** `x^h + 1 = prod_{j odd mod n} (x - zeta^j)` in
   `F_q[x]` with the `h` roots pairwise distinct; consequently
   `Z[zeta_n]/(q) ~ prod_{j odd} F_q`, `q` is unramified, and the `h`
   primes `p_j = ker(pi_j)` above it — where `pi_j : Z[zeta_n] -> F_q`,
   `zeta_n -> zeta^j` — are distinct, of residue degree 1 and norm `q`.
   The Galois group `(Z/n)^*` acts on them by `sigma_a^{-1}(p_j) = p_{ja}`,
   **simply transitively**.
   *Ramification caveat (load-bearing for the count in Claim 3):* `q` odd
   and `n` a power of two is exactly what makes the `h` factors squarefree
   and distinct; `n | q - 1` is what makes each residue degree `1`, hence
   each norm exactly `q` rather than `q^f`.
2. **LN1 (forward gate).** Let `G subset [0, h)`, `eps in {+-1}^G`,
   `alpha = sum_{i in G} eps_i zeta_n^i`. If `sum_{i in G} eps_i zeta^i = 0`
   in `F_q`, then

   ```text
   Norm(alpha) != 0   and   q | Norm(alpha).
   ```

   **The basis-range hypothesis `G subset [0, h)` is essential and load
   bearing**: for a support meeting an opposite pair `{i, i+h}` the formal
   sum can be the zero element of `Z[zeta_n]` (`zeta_n^{i+h} = -zeta_n^i`),
   whose norm is `0`, and the conclusion is vacuous. This is the banked C1
   "no opposite pairs / reduced signed support" clause.
3. **LN2 (`o`-fold upgrade).** If in addition `alpha(zeta^u) = 0` for every
   `u in U` with `|U| = o`, then

   ```text
   q^o | Norm(alpha),   Norm(alpha) != 0.
   ```

   More generally `v_q(Norm(alpha)) >= m(alpha)` for every nonzero `alpha`
   supported in the basis range. In the official C2'' schedule the junction
   block `U_j = { odd u : u*2^j <= t }` has `|U_j| = L_j`, so every
   junction-`j` skew solution satisfies `q^{L_j} | Norm(delta) != 0`.
4. **LN3 (computational / evaluation form).** For every `alpha` supported
   in `[0, h)`,

   ```text
   Norm(alpha) = prod_{j odd mod n} alpha(zeta^j)   in F_q,
   q | Norm(alpha)  <=>  m(alpha) >= 1,
   v_q(Norm(alpha)) >= m(alpha).
   ```

   This makes every norm-divisibility measurement determinant-free: `h`
   modular evaluations instead of an `h x h` exact determinant.

## Bridge to the banked C1 lane (context, not a new claim)

At `t = 2` the junction-0 block is `U_0 = {1}` and the junction matrix
columns are `v_i = zeta^i`, `i in Z/(n/2)` — so a **junction-0 C2'' skew
solution IS a C1 ternary relation at `2N = n`**, verbatim (same
admissibility `q == 1 mod n`, same half-section index range, same `Norm`).
Claims 2-4 at `o = 1` are therefore the banked C1 relation-side resultant
router, re-proved here in the C2'' coordinates; the census agreement is
recorded in `notes/pilots_20260802/dli_norm_gate/REPORT.md` §3 (three
independent code paths, byte-identical censuses at `2N = 16, 32`).

## Explicitly NOT claimed (context)

- **No converse at the level of blocks.** `q^o | Norm(alpha)` does NOT
  imply that `alpha` is a `U`-solution: the `o` primes dividing `alpha`
  need not be the block `a.U` for `a = 1`. The exact counting relation
  between the two counts is the separate splitting law
  (`dli_norm_gate_splitting_law`), not this node.
- **No claim about `Norm(alpha) = 0`.** Outside the basis range the
  statement is false as written; see Claim 2's caveat.
- **No bound on `Norm(alpha)`.** The upper bound `Norm <= E^{h/2}` — the
  other half of the router — is `dli_norm_gate_energy_ceiling`, which this
  node does not use or assert.
- **No claim at `j > 0` about the C1 census identification.** The *shape*
  (Claims 1-4) is proved for every junction; the identification of the
  C2'' census with the C1 census is a junction-0 statement.

## Falsifier

A prime `q == 1 (mod n)`, a vector supported in `[0, phi(n))` with
`alpha(zeta^u) = 0` for `o` distinct odd `u`, and `q^o` not dividing the
exact integer `Norm(alpha)`; or such an `alpha` with `Norm(alpha) = 0`.

## Verifier

`verify.py` in this node (profile: `tiny`; uses `sympy` for the third leg of
the norm triple check). Exhaustive LN3 criterion and valuation checks at
`h = 4, 8` and weights `1-3` at `h = 16` over `(n,q)` in
`{(8,17), (16,17), (16,97), (16,113), (32,97), (32,193)}`; simple
transitivity at `n = 8,16,32,64`; the complete splitting of `x^h+1` mod `q`;
the load-bearing basis-range counterexample; LN2 with the banked solution
counts at `(16,17,U={1,3})` and `(32,97,U={1,3})` reproduced exactly; and
the Bareiss / `sympy.resultant` / LN3-evaluation triple check on 72 samples.
