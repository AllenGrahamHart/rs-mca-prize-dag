# Proof

## 1. Exact row interpolation

Write a biform of bidegree at most `(2,4)` uniquely as

```text
H(T,X)=sum_(b=0)^4 X^b h_b(T),       deg(h_b)<=2.   (1)
```

Suppose first that `(KBSI-2)` holds. For each `b`, the twelve-vector

```text
(c_i q_(i,b))_i
```

is the evaluation vector of `h_b` at `alpha_1,...,alpha_12`. It is killed
by the parity-check matrix `P`. Stacking the five coefficient conditions is
exactly `Nc=0`. Every `c_i` is nonzero because both the actual row and its
projective representative are nonzero.

Conversely, let `c` be a full-support kernel vector of `N`. For each `b`,
the parity checks say that `(c_iq_(i,b))_i` lies in the evaluation code of
degree-at-most-two polynomials. There is therefore a unique polynomial
`h_b` of degree at most two with those twelve values. Substitution in `(1)`
gives `(KBSI-2)`. If two biforms gave the same rows, each difference
coefficient would be a degree-at-most-two polynomial vanishing at twelve
distinct points, hence zero. This proves existence and uniqueness.

The argument uses binary quartic coefficient vectors in projective charts;
changing a row representative merely rescales the corresponding coordinate
of `c`. Thus the full-support criterion is projectively well defined.

## 2. Complete-source resultant

The parent recurrence router imports the complete-source divisibility

```text
q_i=H(alpha_i,X) divides B/z_i divides B,
```

where the coordinate locators `z_i` are pairwise disjoint. Fix a geometric
root `x` of `B`. Since `H(T,x)` is nonzero of degree at most two, at most
two labels contribute at `x`, with multiplicity, and hence

```text
sum_i ord_x(q_i)<=2 ord_x(B).                       (2)
```

Both sides have total degree 48: there are twelve nonzero quartic rows and
`deg(B)=24`. Therefore every local inequality is an equality. Equivalently,

```text
q_i(X)=H(alpha_i,X),
sum_i div(q_i)=2 div(B).                            (3)
```

The divisor equality gives the binary-form identity `(KBSI-3)` up to a
nonzero constant. Scales in `(KBSI-2)` only modify that constant.

Because `A` is monic and has the twelve distinct roots `alpha_i`, the
standard product formula for the resultant gives

```text
Res_T(A,H)=product_i H(alpha_i,X).                  (4)
```

Equations `(3)--(4)` prove `(KBSI-4)`. This remains valid when `B` has
multiple roots because it is an equality of divisors, not a distinct-root
count.

In the source-line coordinates of the diagonal subfield dichotomy,
`psi(X)=X^2` and `B` is the pullback of the twelve-label divisor. Hence
`B(X)` is projectively `A(X^2)` as a binary form. Substitution in
`(KBSI-4)` proves `(KBSI-5)`. QED.
