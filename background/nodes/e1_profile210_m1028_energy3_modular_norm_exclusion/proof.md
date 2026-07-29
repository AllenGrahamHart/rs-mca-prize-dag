# Proof

At energy three, integrality forces exactly three nonzero positive-half
autocorrelations, each in `{+1,-1}`. Thus

```text
y_u=18+sum_(j=1)^3 epsilon_j
              (zeta_256^(u d_j)+zeta_256^(-u d_j)), (1)
```

with `1<=d_1<d_2<d_3<=63`.

Modulo two, the signs disappear. The parity autocorrelation polynomial is

```text
sum_j (X^d_j+X^(128-d_j)).                          (2)
```

The singleton parity polynomial has local multiplicity two, so `(2)` has
multiplicity four at `X=1`. The verifier checks this by the exact Lucas
criterion for Hasse derivatives.

The factor `257` in the norm implies that `(1)` vanishes at a primitive
256-th root modulo `257`. Since `3` is such a root, diagonal Galois action
normalizes that root to `3`; multiplication and folding of the lags preserve
the family in `(1)`. It is therefore necessary and sufficient at the
autocorrelation level to screen

```text
18+sum_j epsilon_j(3^d_j+3^(-d_j))=0 mod 257.       (3)
```

The complete `C(63,3)*8` screen, after the multiplicity-four filter, leaves
exactly 329 signed lag triples.

For exact norms let `C_0=2`, `C_1=T`, and

```text
C_n=T C_(n-1)-C_(n-2).
```

Then `C_64` is the minimal polynomial of
`zeta_256+zeta_256^-1`, and the norm of `(1)` is

```text
Res_T(C_64,18+sum_j epsilon_j C_d_j).                (4)
```

The verifier computes `(4)` modulo nine distinct primes near `2^31`. It
proves each prime by trial division. Polynomial Euclidean reduction uses

```text
Res(A,B)=(-1)^(deg(A)deg(B))
         lc(B)^(deg(A)-deg(R)) Res(B,R),             (5)
```

where `R=A mod B`. Chinese remaindering is exact because the product of the
nine primes is larger than `18^64`, while AM-GM applied to the 64 positive
conjugate squares gives `Norm<=18^64`. Positivity picks the unique residue in
that interval. As an independent implementation cross-check, the same engine
reproduces all five degree-64 Bareiss norms from the proved cofactor-`1538`
node.

Every reconstructed norm is divisible by `1028`. The 329 sorted
type/quotient rows have digest

```text
d462adc241981e2e3aa9747a5ba582808d8ebf505e2df6a86fdad2df52a7d3cc
```

and quotient range

```text
110037709021719095415927105791028375912712994655842773868558710185217329606913
..
120963671460232983862280624800699787448990635276721201666721603772949806841601.
```

The lower endpoint is strictly above `p_max`. Hence no official row prime can
equal `Norm/1028`, excluding energy three. The separate proved leaves already
exclude energies two, five, and six; therefore only energy four remains. QED.
