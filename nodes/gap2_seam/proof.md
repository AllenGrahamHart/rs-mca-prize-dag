# proof: gap2_seam

- **status:** PROVED
- **closure:** proof

## Statement (this node)

GAP-2 seam. In the normal-form / residue framework (`thm:normalform`,
`def:residue`, banked), a bad-slope datum on a residue line carries a
**denominator polynomial** `E in F[X]` of degree `t_denom` with
`1 <= t_denom <= r`, where `r = n - k`. Say the datum is a **pullback** if
`E = g(X^M)` for some `g in F[X]` and integer `M >= 2`. Claim:

1. **(Divisibility.)** A pullback denominator forces `M | t_denom`.
2. **(Strip coincidence.)** If moreover `M | gcd(n,k)`, then the line-side
   aperiodic strip (`rem:aper`: remove pullback denominators) coincides with
   the support-side **rate-preserving** quotient strip (the `Q_M = Q_1(H_{n/M})`
   recursion, banked): on every exact-agreement bucket `A`,
   `M | j  <=>  M | t_win`, where `j = n - A`, `t_win = A - k`.
3. **(Residual seam classified.)** The only strata that are periodic on the
   support side but *not* pulled back rate-preservingly are those with
   `M | gcd(n,j)` but `M !| k`: these are **non-rate-preserving folds** — the
   quotient row `(n/M, k/M)` is not integral, the syndrome conditions do not
   descend to a valid RS row, so they stay on the aperiodic side and carry no
   alignment boost (checker convention `rem:aper`).

Parts 1–2 are the load-bearing divisibility content and are proved here in full.
Part 3's classification is proved; its "no boost" clause is the banked
`rem:aper` convention, cited (not re-derived), and flagged as such.

## 1. Divisibility: pullback => `M | t_denom` [complete]

Let `E = g(X^M)` with `g` of degree `e = deg g >= 1` and leading coefficient
`c != 0`. Every monomial of `E` is `c_i X^{M i}` for a coefficient `c_i` of `g`,
so `E` is supported on exponents that are multiples of `M`. In particular the
top exponent is `deg E = M * deg g = M e`. Hence

```
t_denom = deg E = M e,     so     M | t_denom.                            (1)
```

This is exact and unconditional: the degree of a polynomial in `X^M` is a
multiple of `M`. (Conversely any `E` all of whose exponents are multiples of `M`
is literally `g(X^M)` with `g(Y) = sum_i c_{Mi} Y^i`; so "pullback by `X^M`"
`<=>` "support of `E` contained in `M Z`", a clean characterisation used in
Part 3.) ∎(1)

## 2. Strip coincidence under `M | gcd(n,k)` [complete]

Assume `M | gcd(n,k)`, i.e. `M | n` **and** `M | k`. Then

```
M | n,  M | k   =>   M | (n - k) = r.                                     (2)
```

On any exact-agreement bucket `A` set `j = n - A` (co-support size) and
`t_win = A - k` (syndrome-window length). These satisfy the identity

```
j + t_win = (n - A) + (A - k) = n - k = r.                                (3)
```

Since `M | r` by (2), reducing (3) mod `M` gives `j ≡ -t_win (mod M)`, hence

```
M | j   <=>   M | t_win.                                                  (4)
```

**Interpretation as strip coincidence.** The support-side strip removes
supports that are `mu_M`-periodic (unions of cosets of the order-`M` subgroup
`mu_M <= mu_n`, which exists because `M | n`); on the co-support side this is
`M | j`. Such a periodic support descends under `x |-> x^M` to a support in
`mu_{n/M}`, and — because `M | k` makes `k/M` an integer — the quotient datum is
a genuine RS row `(n/M, k/M)` of the **same rate** `k/n = (k/M)/(n/M)`. This is
exactly the hypothesis of the banked recursion `Q_M = Q_1(H_{n/M})`
(`rate-preserving` fold). The line-side strip removes pullback denominators
`E = g(X^M)`; by (1) these are precisely the data with `M | t_denom`, and the
alignment (harmonic-window) conditions of such a datum are `mu_M`-invariant, so
they descend to the same quotient row. By (4), "co-support periodic" (`M | j`)
and "window-length compatible" (`M | t_win`) are the *same* condition once
`M | r`; the two strips act on the same set of buckets. Hence, when
`M | gcd(n,k)`, the `rem:aper` line-side strip and the `Q_M` support-side strip
coincide bucket-by-bucket. ∎(2)

## 3. The residual seam [classified]

The seam is the set of strata that are periodic on one side but not both. By (3),
`M | j <=> M | t_win` requires only `M | r`; but a *rate-preserving* descent
additionally needs `M | k` (so that `k/M in Z`). Consider `M | gcd(n,j)` with
`M !| k`:

- `M | n` and `M | j` give, via (3) rearranged as `t_win = r - j` and
  `r = n - k`, that `t_win ≡ (n - k) - j ≡ -k (mod M)`, so `M | t_win <=> M | k`.
  Since `M !| k`, here `M !| t_win`: the window length is **not** a multiple of
  `M`. Equivalently `k/M not in Z`: the fold `x |-> x^M` sends the row
  `(n, k)` to `(n/M, k/M)` with `k/M` **non-integral**.
- A non-integral target dimension is not an RS row; the syndrome/alignment
  conditions therefore do not descend to a valid quotient datum. These strata
  are exactly the "`M | gcd(n,j)` but `M !| k`" folds.

**Conclusion of the classification.** The `mu_M`-periodic supports split cleanly:

```
M | gcd(n,k)          => rate-preserving fold  => stripped by BOTH sides (Part 2);
M | gcd(n,j), M !| k  => non-rate-preserving fold => descends to no valid row.
```

The second class carries **no alignment boost** and remains on the aperiodic
side — this is the checker convention `rem:aper` (banked). *Honesty flag:* the
"no boost" statement for the non-rate-preserving folds is a **cited convention**,
justified in the source by the observation that the syndrome conditions have no
valid quotient target; it is not re-proved from scratch here. The seam's
*arithmetic* — that these are exactly the `M | gcd(n,j), M !| k` strata and that
they are disjoint from the rate-preserving ones — is proved above (Parts 1–3).

## 4. Why this closes GAP-2

GAP-2 (of `s3b_ii`) was the worry that the *line-side* aperiodic strip
(`rem:aper`, phrased via pullback denominators) and the *support-side* quotient
recursion might disagree, double-counting or missing periodic strata. Parts 1–2
show they agree exactly on the rate-preserving class `M | gcd(n,k)`, and Part 3
accounts for every remaining periodic stratum as a non-rate-preserving fold that
both conventions leave aperiodic. The two bookkeeping systems are thus a single
partition of the periodic strata, indexed by `M | gcd(n,k)` — GAP-2 closed at the
divisibility level, which is precisely this node's scope.

## Verifier

`verify.py` (stdlib only, <1s) checks, by exhaustive small enumeration:
(a) every pullback `g(X^M)` has `M | deg`; (b) for all `(n,k)` with
`M | gcd(n,k)` and all `A`, identity (4) `M|j <=> M|t_win` holds; (c) the seam
classification: `M | gcd(n,j)` with `M !| k` forces `M !| t_win` (non-integral
`k/M`), disjoint from the rate-preserving class. All checks PASS.
