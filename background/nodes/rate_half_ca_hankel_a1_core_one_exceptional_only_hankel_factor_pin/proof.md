# Proof

The middle-adjugate theorem gives

```text
adj M=lambda q q^T,                                 (1)
```

where `lambda` is a nonzero projective linear form. Its unique root is the
only slope at which residual root omission can occur, and the total omission
budget is `O<=1`.

On the exceptional-only face, `P=P_clE`, so the root `gamma_0` of `E` is a
supported slope. The exceptional factor descent proves that

```text
Q(gamma_0;X) is squarefree of degree r-1.            (2)
```

The nominal supported-fiber degree is `r`. Thus `(2)` contributes one to
the omission count. Consequently `O=1`, and the unique omission slope is
`gamma_0`. By `(1)`, this is the unique root of `lambda`. Two nonzero
projective linear forms with the same root are associates, so

```text
lambda=c_H E                                        (3)
```

for one nonzero field scalar `c_H`. Substitution into `(1)` proves `(HFP1)`.
The middle-adjugate theorem also proves that `lambda` is the exact gcd of all
nonzero maximal minors, so `(3)` proves `(HFP2)`.

Every coordinate of `q` is homogeneous of degree `e`, and their gcd is one.
They therefore cannot all vanish at the projective point `gamma_0`: otherwise
`E` would divide every coordinate. Divide `(HFP1)` by `E` and specialize at
`gamma_0`. The resulting outer product is nonzero and has rank one, proving
`(HFP3)`.

On this `b=0` face the residual generator in the adjugate theorem is the same
degree-`r` biform `Q` used by the exceptional descent. The infinity theorem
gives its top coefficient `(HFP4)`. Inserting it into `(HFP1)` gives
`(HFP5)`. At `E=0`, the top coordinate of `q` vanishes, so the corresponding
row and column in `(HFP3)` vanish. Some other coordinate is nonzero by
primitivity, so the quotient matrix itself remains nonzero. QED.
