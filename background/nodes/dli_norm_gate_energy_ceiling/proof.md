# Proof

`n = 2^s >= 4`, `h = phi(n) = n/2`, `zeta = zeta_n` a primitive complex
`n`-th root of unity. The roots of `x^h + 1` are the `zeta^j` for the `h`
odd residues `j (mod n)`, and

```text
Norm(alpha) = prod_{j odd mod n} alpha(zeta^j)                    (N-1)
```

for `alpha = sum_{i<h} a_i zeta^i`, `a_i in Z`.

## Claim 1 (LN4: energy ceiling)

This is the banked `dli_c1_ternary_relation_norm_sandwich` **Claim 2** with
the weight `w` replaced by the energy `E = sum_i a_i^2`. We do not re-derive
the banked argument; we record it and identify the single place where `w`
entered, showing that ternariness was never used.

**Step 1 — positivity by conjugate pairing.** Complex conjugation sends
`zeta^j` to `zeta^{n-j}`, and `j` is odd iff `n - j` is odd, with
`j != n - j` because `n = 2h` is even and `j` is odd. So the `h` factors of
`(N-1)` fall into `h/2` conjugate pairs, and since the `a_i` are real,

```text
Norm(alpha) = prod_{pairs} alpha(zeta^j) conj(alpha(zeta^j))
            = prod_{pairs} |alpha(zeta^j)|^2 >= 0.                 (N-2)
```

**Step 2 — negacyclic Parseval.** For odd `j != j'` mod `n`, `j - j'` is
even and `!= 0 (mod n)`, so `zeta^{j-j'}` is a nontrivial `h`-th root of
unity and `sum_{i<h} zeta^{(j-j')i} = 0`. Hence the `h x h` matrix
`(zeta^{ji})_{j odd, i<h}` is `sqrt(h)` times a unitary matrix, and

```text
sum_{j odd mod n} |alpha(zeta^j)|^2 = h * sum_{i<h} a_i^2 = h E.   (N-3)
```

**This is the ONLY step where the coefficients enter, and it enters as
`sum_i a_i^2` — never as "how many are nonzero".** For ternary `alpha` of
weight `w` one has `sum_i a_i^2 = w` and `(N-3)` reads `h w`, which is the
banked step verbatim. Nothing downstream sees the difference.

*(Exact-integer form of `(N-3)`, which is what the verifier checks: with
`alpha~ = sum_i a_i zeta^{-i}` (so `zeta^{-i} = -zeta^{h-i}` for
`0 < i < h`), one has `|alpha(zeta^j)|^2 = (alpha alpha~)(zeta^j)`, and
`sum_{j odd} beta(zeta^j) = h b_0` for `beta = sum_i b_i zeta^i` because
`Tr(zeta^i) = sum_{j odd} zeta^{ij} = 0` for `0 < i < h` and `= h` for
`i = 0`. The constant coefficient of `alpha alpha~ mod (x^h+1)` is exactly
`sum_i a_i^2 = E`.)*

**Step 3 — AM-GM.** Put `P_j = |alpha(zeta^j)|^2 >= 0`, one per conjugate
pair; by `(N-3)` the `h/2` values satisfy `sum P_j = hE/2`, so their
arithmetic mean is `E`. By AM-GM,

```text
Norm(alpha) = prod_{pairs} P_j <= E^{h/2}.                          (N-4)
```

**Step 4 — the lower bound.** `x^h + 1 = Phi_n(x)` is irreducible over `Q`,
and a nonzero `alpha` of degree `< h` is not divisible by it, so no
`alpha(zeta^j)` vanishes and `Norm(alpha)` is a nonzero integer; by `(N-2)`
it is non-negative, hence `>= 1`. QED (1).

**Honest scope of the generalization.** The generalization is *only* the
substitution `w -> E`. The banked node's other three claims (the doubling
embedding, the saturating family, the router threshold) are ternary
statements and are NOT generalized here; in particular the exact maxima
`maxnorm(N,w)` remain the banked exhaustive/ladder facts, and the stable-range
doubling law remains REFUTED in general.

## Claim 2 (LN5: junction router)

Fix a junction with root order `h_j`, degree `N_j = phi(h_j) = h_{j+1}`, and
constraint block `U_j` of size `L_j`; let `q` be odd with `h_j | q - 1` and
let `delta = sum_{i < N_j} d_i zeta_{h_j}^i != 0` be a junction-`j` skew
solution, i.e. `delta(zeta^u) = 0` in `F_q` for every `u in U_j`. The index
range `0 <= i < N_j = phi(h_j)` is exactly the basis range of
`Z[zeta_{h_j}]`, so `dli_norm_gate_forward_and_ofold` Claim 3 applies and

```text
q^{L_j} | Norm(delta),   Norm(delta) != 0   =>   q^{L_j} <= Norm(delta),
```

using `Norm(delta) >= 1` from Claim 1. Combining with the ceiling of
Claim 1 at `h = N_j`,

```text
q^{L_j} <= Norm(delta) <= E(delta)^{N_j/2}.                        (R-1)
```

Since `E -> E^{N_j/2}` is strictly increasing on positive integers, `(R-1)`
is equivalent to

```text
E(delta) >= E_min := min{ E in Z_{>0} : E^{N_j/2} >= q^{L_j} },     (R-2)
```

and the contrapositive of `(R-1)` is the router: **if
`E^{N_j/2} < q^{L_j}` then the junction admits no nonzero skew solution of
energy `<= E`.** At `j = 0` the skew domain is `{+-1}^{S_0}`, so
`E(delta) = |S_0|` exactly and `(R-2)` is a lower bound on the number of
unsaturated cells. At `j > 0` with `|d_i| <= c_i` one has
`E(delta) <= sum_{i in S_j} c_i^2`, so a state whose entire admissible skew
domain has `sum_i c_i^2 <= E` with `E^{N_j/2} < q^{L_j}` is killed. QED (2).

**Uniform-ratio corollary (used, and priced, downstream).** If
`N_j = 256 L_j` then `E^{N_j/2} = E^{128 L_j} = (E^{128})^{L_j}`, so `(R-1)`
reads `q^{L_j} <= (E^{128})^{L_j}`, i.e.

```text
q <= E^{128}                                                        (R-3)
```

independently of `j`. (Both sides are positive integers raised to the same
positive power `L_j`, and `t -> t^{L_j}` is strictly increasing.) The
official schedule has `N_j = 256 L_j` at all 33 junctions; the resulting
`E_min` table and the support-forcing theorem are
`dli_official_support_forcing`.

**What this does NOT give.** `(R-1)` is one-sided: energy `>= E_min` is
necessary, never sufficient, for a solution. The router therefore excludes;
it never certifies existence.
