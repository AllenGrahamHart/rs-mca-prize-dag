# Proof

Every root of `B=L_Q` lies in `S0`, so `B|L0`.  Every root of `A=L_P` lies
in `D\S0`, so `A|U`.  Both locators are monic of degree `e`, and `S!=S0`
gives `H=A-B!=0` with `deg H<e`.

The full locators factor as

```text
L_S=L_C A,                 L_(S0)=L_C B.
```

Therefore

```text
L_S-L_(S0)=L_C H.                                  (1)
```

The two monic degree-`m` locators have the same first `t` sub-leading
coefficients exactly when the right side of `(1)` has degree at most
`m-t-1`.  Since `deg L_C=m-e`, this is equivalent to
`deg H<=e-t-1`, proving the forward direction of `(TD-1)`.

Conversely, let `(B,H)` satisfy `(TD-1)`.  Because `L0` and `U` are
squarefree with disjoint root sets, `B` and `A=B+H` have unique disjoint
root sets `Q subset S0` and `P subset D\S0`, each of size `e`.  Put
`C=S0\Q` and `S=C union P`.  Then `|S|=m`, and `(1)` together with the
degree bound proves equality of the first `t` locator coefficients.  Both
constructions recover `P,Q,B,H`, so they are inverse.

For the cyclic-coset consequence, the coefficient-scale quotient sieve
proves that every common quotient scale `c` divides `deg(A-B)`.  At `d=1`
this forces `c=1`.

For `(TD-3)`, the three reduced locator pairs, in ascending coefficient
order over `F_17`, are

```text
A1=(2,16,2,1),     B1=(9,10,2,1),
A2=(1,14,0,1),     B2=(8, 8,0,1),
A3=(13,5,14,1),    B3=(3,16,14,1).
```

Each difference is `(10,6,0,0)`, namely `6X+10`.  Direct multiplication
gives the base locator

```text
L_(S0)=(10,11,9,5,15,1),
```

and each displayed full neighbour locator has the same coefficient `15`
of `X^4`.  Their supports are distinct, so the fixed base and fixed linear
difference have multiplicity at least three.  QED.
