# Proof

The Hasse Taylor identity gives `(TCS1)` over `Z[T,X]`. Since `q_O` is monic
over `R`, its resultant with `F_35` lies in `R[X]` and commutes with reduction
at every odd prime.

Fix an odd prime `p` and work over an algebraic closure `k` of `F_p`. List
the roots of the reduced monic polynomial `q_O` with multiplicity as
`alpha_1,...,alpha_d`. The evaluation formula for the resultant gives

```text
C_O,35(X) mod p
 =product_(r=1)^d F_35(alpha_r,X).                    (1)
```

The polynomial ring `k[X]` is an integral domain. Hence the right side of
`(1)` is the zero polynomial exactly when at least one factor is zero. For a
fixed root `alpha`,

```text
F_35(alpha,X)
 =sum_(i=0)^35 Pcal_n^[i](alpha)X^i                  (2)
```

is zero exactly when all thirty-six coefficients in `(2)` vanish. Therefore

```text
C_O,35 mod p=0
 iff q_O,Pcal_n^[0],...,Pcal_n^[35]
     have a common root over k.                       (3)
```

By definition, `C_O,35 mod p=0` exactly when `p` divides every coefficient,
equivalently when `p|c_O,35`. The quotient-algebra Fitting support compiler
identifies the right side of `(3)` with `p|s_O,35`. This proves `(TCS5)` and
the radical identity `(TCS4)`.

The same argument in characteristic zero proves `C_O,35` is nonzero. If it
were zero, one root of the irreducible `q_O` would make the first thirty-six
Hasse derivatives vanish, so it would be a shifted-product root of
multiplicity at least thirty-six. Dyadic shifted-product Sidonicity bounds
that multiplicity by two.

Finally every factor in `(1)` has `X`-degree at most `35`, so

```text
deg_X(C_O,35)<=35 deg(q_O).
```

The canonical orbit decomposition gives maximum block degree `4,096` and
total block degree `67,084,290` at `n=8192`. Multiplying by `35` gives the
two degree values in `(TCS6)` and the printed total. QED.
