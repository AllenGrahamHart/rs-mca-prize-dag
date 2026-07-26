# Proof - L1 Mersenne HNF m=8 order-zero reciprocal elimination

Retain the notation of the Frobenius reciprocal dependency. Thus

```text
Q_s(Z)=Res_W(P_s(W),Z-W^8)
      =sum_(j=0)^7 q_j(s)Z^(7-j),
C(s)=q_7(s)=-binom(s+6,7)^8.                        (1)
```

Every survivor gives `t=s^p` satisfying

```text
F_j(s,t):=C(s)q_j(t)-q_(7-j)(s)=0,       0<=j<=7.  (2)
```

We use only `F_1,F_2,F_3`.

## 1. Two eliminants

Define

```text
R_12(s)=Res_t(F_1(s,t),F_2(s,t)),
R_13(s)=Res_t(F_1(s,t),F_3(s,t)).                   (3)
```

Any common solution of `(2)` is a common zero of `(3)`. Weighted
homogeneity of the root resultant gives

```text
deg q_j=8j,       j=0,...,7.                        (4)
```

Hence every coefficient of `F_j`, viewed as a polynomial in `t`, has
`s`-degree at most 56. The raw resultant degree bounds are therefore

```text
deg R_12<=8*56+16*56=1344,
deg R_13<=8*56+24*56=1792.                          (5)
```

These bounds make exact evaluation/interpolation a proof certificate rather
than a heuristic sample.

For each official characteristic, evaluate the fixed-degree resultants in
`(3)` at 1345 and 1793 consecutive base-field points that avoid
`C(s)=0`, and interpolate under `(5)`. One additional point independently
checks each interpolation. The actual degrees are

```text
deg R_12=1320,       deg R_13=1760.                 (6)
```

Exact Euclidean gcd in `F_p[s]` then gives, on every one of the four rows,

```text
gcd(R_12,R_13)
 =s^176(s-1)^4(s+1)^176(s+2)^168(s+3)^162
  (s+4)^152(s+5)^128(s+6)^64(s+7)^2.               (7)
```

The monic factor in `(7)` has degree 1032. Every root belongs to `F_p`.

## 2. Independent construction

The primary verifier constructs the rational polynomials `q_j` from the
symbolic resultant `(1)`, reduces coefficients exactly modulo each official
prime, and performs the bounded interpolation above.

The independent audit does not use a symbolic resultant. At 57 values of
`s`, it forms the seven-by-seven companion matrix for multiplication by `W`
in `F_p[W]/(P_s)`, raises it to the eighth power, and obtains `Q_s` as its
characteristic polynomial using Newton traces. Since `(4)` bounds every
`q_j` by degree 56, interpolation reconstructs all eight coefficient
polynomials exactly. A standalone resultant, interpolation, and polynomial-
gcd implementation then reproduces `(6)--(7)` on every row.

If an HNF survivor existed, its parameter `s` would be a common root of
`R_12,R_13` and hence a root of `(7)`. This would put `s` in `F_p`, contrary
to the HNF condition. Thus the complete printed order-zero chamber is empty.
QED.
