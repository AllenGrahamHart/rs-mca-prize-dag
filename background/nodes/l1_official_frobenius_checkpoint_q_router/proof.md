# Proof - L1 official Frobenius-checkpoint Q router

## 1. At most 23 checkpoints

The order argument in `l1_official_reserve_tame_refinement_router` and the
strict cap give `(FQ1)`. By
`l1_official_newton_cofactor_window_router`, `p>=3583>2^11`. Therefore

```text
11n/(p+1)<256,
```

or `p+1>11n/256`. Since `n` is a power of two with `n>=2^13`, the right side
is an integer. Hence

```text
p>=11n/256.
```

Also `11/256>1/24`, proving `(FQ2)`. For `d<=n-1`, one obtains

```text
d/p<n/p<24,
```

which proves `(FQ3)`.

## 2. Forward coordinates

Newton identities compute every power sum successively from the elementary
coordinates:

```text
S_j-E_1S_(j-1)+E_2S_(j-2)-...+(-1)^j jE_j=0.         (1)
```

Thus `(E_1,...,E_d)` determines every `S_j`, and hence every `C_j` in
`(FQ4)`.

## 3. Inverse coordinates

Suppose `C_1,...,C_d` are given from a root set. Recover the coordinates in
increasing order. If `p` does not divide `j`, then `S_j=C_j`. If `p` divides
`j`, use Frobenius:

```text
S_j=S_(j/p)^p.                                        (2)
```

The power on the right was recovered at an earlier index. Hence all power
sums through `j` are known.

If `p|j`, set `E_j=C_j`. Otherwise `j` is invertible and the equivalent
Newton recursion

```text
jE_j=sum_(i=1)^j (-1)^(i-1) E_(j-i)S_i,       E_0=1 (3)
```

recovers `E_j` from earlier elementary coordinates and the known power sums.
At a divisible index, the omitted Newton equation is automatic: the monic
polynomial with the recovered elementary coefficients has a root multiset in
a splitting field, and its forward sums satisfy the universal identity
`S_(pj)=S_j^p`; induction identifies that value with `(2)`. Thus the
construction is triangular and inverse to the forward map. Equations
`(2)--(3)` prove `(FQ5)` and give the usual characteristic-`p` mixed
symmetric-function coordinates.

The locator coefficient `l_j` equals `(-1)^jE_j`, so fixing the first `d`
locator coefficients is equivalent to fixing the mixed vector. The
fixed-cofactor transport supplies exactly such a prefix cell at every exact
shell, with equality at scalar cofactor. This proves the shell consequence.

## 4. Coarse fibers and the exact cost of forgetting checkpoints

Projection from the mixed coordinate vector to its p-free power-sum
coordinates forgets only the `r` elementary checkpoints. Therefore a mixed
fiber is a subset of its projected coarse fiber, and the coarse fiber is the
disjoint union of the mixed fibers over the checkpoint vectors that are
actually attained. This proves `(FQ6)` and the zero-loss transfer from a
coarse p-free max-fiber theorem.

Each checkpoint lies in `F_q`, so there are at most `q^r` ambient vectors.
By the strict cap, `q^r<2^(256r)<=2^5888`. Since `n>=2^13`,
`n^453>=2^5889`, proving `(FQ7)`. Summing a uniform conditional bound over
the attained vectors proves `(FQ8)`.

Finally suppose `r>=1` and the conditional estimate is nontrivial, so its
numerical upper bound `M` is at least one. The raw all-vector union bound is
then `q^r M>=q`, whereas `q/2^128<q`. Hence this raw bound cannot establish
the finite prize inequality. This is a statement about what the union-bound
argument can certify, not a lower bound on the actual coarse fiber.
