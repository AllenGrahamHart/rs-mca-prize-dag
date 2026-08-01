# Proof

Write `X=t^2`.  The resultant of the two product minors in `X`, after
removing only source and target guards, is

```text
G=b(c+1)(r^4+1)+2r^2(b^2c+1).                                  (KB433AB-4)
```

Hence

```text
c=-[b(r^4+1)+2r^2]/[b(r^4+1+2br^2)].                           (KB433AB-5)
```

The denominator cannot vanish on a solution: if its core and the numerator
both vanished, their difference would give `2r^2(1-b^2)=0`, a guard.

Substitute `(KB433AB-5)` in the two q welds.  Each is linear in `t`; their
compatibility is the printed polynomial `H_{epsilon_1,epsilon_2}(b,r)` in
the finite router.  The first row's coefficient and constant cannot both
vanish because their `b`-resultant is

```text
4r^6(r-1)^4(r+1)^4(r-i)^2(r+i)^2.
```

The product row remains linear in `X`: its coefficient and constant cores
have resultant

```text
4r^4(r-1)^2(r+1)^2(r^2+1)^6.
```

Equating the q value of `t^2` with the product value factors into guards,
the two branches `b=-r^2,-r^-2`, and a quartic-in-`b` polynomial
`K_{epsilon_1}(b,r)`.  Substitution in `H` deletes both linear branches by
the guards `r+/-1,r+/-i`.  After those guards are removed,

```text
Res_b(H,K)=C3(r)^2 C4(r)^2,                                    (KB433AB-6)
```

where `C3` is an irreducible cubic in every sign row and `C4` is one linear
factor times an irreducible cubic.  Its unique base-field root is the `r`
printed in `(KB433AB-3)`.  At each root,

```text
gcd_b(H,K)=b^2+278278958b+1,
```

whose two roots are the printed `b` values.  Formula `(KB433AB-5)` then
gives the printed `c`, and either linear q row gives the printed `t`.

The finite router substitutes all eight tuples into all four original
equations and all guards.  The independent audit reconstructs the original
determinants and denominator-cleared q welds directly from the packet table
and obtains zero.  This proves completeness and converse for cell `3`.
The explicit target exchange gives a bijection with cell `6`, proving the
sixteen-packet classification. QED.
