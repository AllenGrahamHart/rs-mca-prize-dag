# Proof - L1 general polynomial-pullback interleaving descent

## 1. Free-module normal form

For existence in `(GP1)`, repeatedly remove the leading term of `f`. If its
degree is `d=as+j` with `0<=j<s`, subtract the same leading coefficient times
`X^j P(X)^a`. Monicity of `P` makes this cancel degree `d` and lowers the
residual degree. The process terminates and groups the selected powers by
`j`, producing `(GP1)`.

For uniqueness, the leading degree of a nonzero term `X^j g_j(P)` is

```text
j+s deg(g_j),
```

whose residue modulo `s` is `j`. Leading terms from distinct components
therefore cannot cancel. The zero polynomial has only the zero tuple. The
same degree formula proves that `deg f<k` is equivalent to `(GP2)`.

## 2. Fiberwise agreement

Fix `a in B` and order its `s` distinct roots as `x_0,...,x_(s-1)`. Evaluating
`(GP1)` gives

```text
f(x_i)=sum_(j=0)^(s-1) x_i^j g_j(a).                  (1)
```

The matrix in `(1)` is Vandermonde, with determinant
`product_(i<j)(x_j-x_i)`, and is invertible. Applying its inverse to the
received vector `(U(x_i))_i` defines `u(a)`. Equation `(1)` then proves
`(GP3)`.

## 3. Exact kernel charge

For component `j`, evaluation of degree-below-`k_j` polynomials on the `b`
distinct labels in `B` has kernel dimension

```text
max(0,k_j-b).
```

Indeed, when `k_j>b`, the kernel consists exactly of the multiples of the
monic locator `L_B` having degree below `k_j`; when `k_j<=b`, a nonzero
polynomial cannot vanish at all `b` labels. The product evaluation map on the
tuple `(g_j)_j` therefore has every nonempty fiber of size exactly `q^kappa`.

Every component code is contained in the evaluation code of degree-below
`K_0=max_j k_j=ceil(k/s)` polynomials on `B`. By `(GP3)`, agreeing on at least
`h` complete `P`-fibers maps into the common-support `s`-interleaved list at
agreement `h`. Multiplying its size by the exact evaluation-kernel charge
proves `(GP5)`.

Apply `list_subsqrt_interleaving_collapse` to that linear evaluation code.
Its proved bound is `L_s<=floor(L(q-1)/(q-L))` for `1<=L<q`, with equality
`L_s=L` when `L^2<q`. This proves `(GP6)`.

## 4. Full complete-fiber partition

If all of `D` is partitioned into degree-`s` fibers, then `s` divides `|D|`
and `b=|D|/s`. Since `k<|D|`,

```text
K_0=ceil(k/s)<=|D|/s=b.
```

Thus every term in `(GP4)` vanishes. The map from codeword polynomials to
quotient evaluation tuples is injective, proving the full-partition
corollary. No multiplicative stabilizer or monomial form for `P` was used.
