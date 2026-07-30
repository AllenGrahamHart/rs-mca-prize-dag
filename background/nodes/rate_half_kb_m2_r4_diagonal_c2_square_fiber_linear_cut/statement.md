# KoalaBear m2 r4 diagonal c2 square-fiber linear cut

- **status:** PROVED
- **scope:** the source-line branch of every saturated `c=2` diagonal row
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_branch_coefficient_compiler` and
  `rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction`
- **consumer:** `rate_half_band_closure`

Use the source-line coordinates and common sign of `(KBDC-1)--(KBDC-2)`:

```text
H(T,X)=U(T,W)+X V(T,W),       W=X^2,
G(T,W)=U(T,W)^2-WV(T,W)^2,    epsilon in {+1,-1}.
```

In either `(KBDM-8)` or the saturated cases of `(KBDM-9)`, let `w` be the
source quotient label of the forced square fiber and put
`q(T)=P_(J_1)(T)`. Thus

```text
G(T,w) ~ q(T)^2,                                      (KBC2-1)
```

and each reduced quadratic star over that source fiber is projectively
`q`.

## Unramified orbit

If the fiber of `W=X^2` over `w` is unramified, then
`w in K^x minus {+1,-1}` and

```text
U(T,w) in <q>,       V(T,w) in <q>.                 (KBC2-2)
```

Writing `U(T,w)=sum_i u_i(w)T^i`,
`V(T,w)=sum_i v_i(w)T^i`, `(KBC2-2)` is the six linear wedge equations

```text
u_i(w)q_j-u_j(w)q_i=0,
v_i(w)q_j-v_j(w)q_i=0             (0<=i<j<=2).      (KBC2-3)
```

They have total rank four on each reciprocal coefficient space. Hence the
affine source spaces of dimensions eight and seven cut exactly to

```text
epsilon=+1: dimension 4,       epsilon=-1: dimension 3. (KBC2-4)
```

There is also a quotient-free coefficient certificate. Put
`m_ij(W)=u_i(W)v_j(W)-u_j(W)v_i(W)` and normalize the source-orbit locator
as

```text
chi_w(W)=(W-w)(W-w^(-1))=W^2-sW+1.
```

Then for some scalars `A,B,C`,

```text
m_12= chi_w(AW+B),
m_01=-chi_w(BW+A),
m_02= C chi_w(W-1).                                (KBC2-5)
```

## Ramified orbit

If the forced source orbit is the deck-ramified orbit `{0,infinity}`, the
two stars coincide. At the finite member the exact condition is only

```text
U(T,0) in <q>;                                     (KBC2-6)
```

at infinity the analogous condition uses the leading `W^2` coefficient of
`U`. It has rank two, and the affine dimensions are respectively six and
five. No condition on the corresponding value of `V`, and no common-minor
factor `(KBC2-5)`, follows in this ramified branch.

This theorem is a linear reduction, not a contradiction. It does not delete
the ramified orbit, either `c=2` row, the source-line or biquadratic branch,
the diagonal orientation, an owner, payment, row, or Prize result.

## Falsifier

An actual saturated `c=2` source-line component whose unramified square
fiber violates `(KBC2-2)--(KBC2-5)` or has coefficient-space dimension
larger than `4/3`; or a ramified square fiber violating `(KBC2-6)` or the
`6/5` dimension count.
