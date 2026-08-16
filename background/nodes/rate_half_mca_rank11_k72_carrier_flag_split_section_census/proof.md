# Proof

Let `D=D_45`, so `|D|=36`, and let `W` be the five-dimensional correction
subspace vanishing on `D`.  Divide every member of `W` by the squarefree
locator of `D`.  The residual space has dimension five and consists of
polynomials of degree at most `72-1-36=35`.

Restrict its evaluation matroid to the `N=m-36=67508` points outside `D`.
A rank-three flat has a two-dimensional annihilator in the residual space.
Two independent degree-at-most-35 polynomials have at most 34 common roots,
so every rank-three flat has size at most 34.  A rank-four flat is the zero
set of one nonzero residual polynomial and has size at most 35.  The
rank-five flat-circuit coupling theorem therefore gives, for entirely-outside
circuits,

```text
5 C_5 <= 31 C(N,4) - (N-34) C_4.                  (1)
```

The global completion maxima `M_4=M_5=31` also give

```text
C_4 <= floor(31 C(N,3)/4)=397371647886059.        (2)
```

For support `d` and exactly `j<d` outside points, ordinary fixed-union
exposure bounds the circuit count by

```text
C(36,d),                                             j=0,
floor(C(36,d-j) C(N,j-1) 31/j),                    1<=j<d.   (3)
```

No parallel-class refinement is used.

Put `S_4=C(m-4,7)` and `S_5=C(m-5,6)`.  One additional entirely-outside
four-circuit can reduce the integer upper bound for `C_5` in `(1)` by at
most `ceil((N-34)/5)=13495`.  Since

```text
21 S_4 - 15*13495 S_5
 = (3(m-4)-15*13495) S_5
 = 195 S_5 > 0,                                    (4)
```

the weighted upper envelope is increasing in `C_4`.  It is therefore
maximized at the endpoint `(2)`, where `(1)` gives

```text
C_5 <= 2463704216893565.                            (5)
```

Add the lower strata `(3)` and multiply by the selected eleven-set extension
factors `S_4,S_5`.  Exact integer arithmetic gives

```text
I_4 <= 506389674857089789010503158660245768712830400,
I_5 <=   2212036714331204501716306860191372678671248.
```

Consequently

```text
21 I_4 + 15 I_5
 <= 10667363722713853636746310934768031733149507120
 <  20552964203529559475043545396584734873674935990.
```

The difference is
`9885600480815705838297234461816703140525428870`, proving `(K72-SC)`.
QED.
