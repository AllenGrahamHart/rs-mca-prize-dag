# `A=1` core-one middle-Hankel adjugate factorization

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger`

Retain the `A=1`, `s=1`, maximal-degree face

```text
e=2m-1,       d=4m-1=2e+1,       Delta=1.             (MAF1)
```

After contracting the one fixed domain factor, the residual divided-power
binary form has degree `2d`. Its degree-`d` middle catalecticant is a symmetric
Hankel pencil

```text
M(U,V)=U M_0+V M_1,       size (d+1) x (d+1),
rank_(F(U/V)) M=d.                                      (MAF2)
```

Let

```text
q(U,V)=(q_0(U,V),...,q_d(U,V))^T                       (MAF3)
```

be the primitive coefficient vector of the residual apolar generator
`Qbar(U,V;X)`. Every `q_j` is homogeneous of degree `e`, their gcd is one,
and `M q=0`. There is a nonzero homogeneous linear form `lambda(U,V)`, unique
up to a nonzero scalar, such that

```text
adj M=lambda*q*q^T.                                    (MAF4)
```

The scalar ambiguity is absorbed into `lambda`, so equality is literal.
Consequently:

1. every `d x d` cofactor of the middle Hankel pencil is
   `lambda q_i q_j`, with the usual cofactor sign included in `adj M`;
2. the gcd of all nonzero maximal minors is exactly `lambda`;
3. `lambda` is the determinant of the unique size-one regular Kronecker
   block;
4. `rank M(gamma)=d` when `lambda(gamma)!=0`, while the unique projective root
   of `lambda` has rank exactly `d-1`.

The residual root-omission budget is therefore supported at only that one
projective slope. In particular, for the finite supported set,

```text
O in {0,1},                                             (MAF5)
```

and `O=0` unless the exceptional root of `lambda` is supported and actually
omits one residual domain root. On the sharp-cap face, the norm residual has

```text
C=e-1+O in {e-1,e}.                                    (MAF6)
```

Identity `(MAF4)` is an exact coefficient-chain interface for the remaining
rank-at-least-five dominant component. It does not by itself exclude that
component or close the stratum.
