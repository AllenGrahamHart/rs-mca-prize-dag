# Proof

The intermediate certifier starts from the exact norm identity

```text
Q=B^4+theta z^(3h)B C^3+phi z^(4h)C^4.               (1)
```

Subtract `B^4`, divide by `z^(3h)`, and put `u=phi/theta`. Since
`theta!=0`, this gives

```text
Rbar=theta C^3(B+u z^hC).                            (2)
```

The original pencil has `G_i=U+c_iV`, and two distinct `G_i` are coprime
factors of the squarefree polynomial `Y^d-1`. A common divisor of `U` and
`V` would divide every `G_i`; hence `gcd(U,V)=1`. Reversal and normalization
preserve every nonzero common root, while `B(0)=C(0)=1` excludes a new common
factor `z`. Therefore `gcd(B,C)=1`, and

```text
gcd(C,B+u z^hC)=gcd(C,B)=1.                           (3)
```

Equations `(2)--(3)` prove `(ICR1)`. If an irreducible `P` occurs in `C`
with multiplicity `e`, then it occurs in `Rbar` with multiplicity exactly
`3e`, because it does not divide `L`. This proves `C|Cube(Rbar)`.

The characteristic is zero or greater than `d`, hence greater than every
degree and multiplicity in `(2)`. Differentiation lowers the `P`-adic
multiplicity of `Rbar` from `3e` to `3e-1`, and a second differentiation
lowers it to at least `3e-2`. Thus `P^(2e)` divides
`gcd(Rbar,Rbar')`, and `P^e` divides
`gcd(Rbar,Rbar',Rbar'')`. Multiplying over the irreducible factors of `C`
proves `(ICR3)`.

For the converse, let a normalized `C` satisfy `(ICR4)--(ICR5)`. Multiplying
`(ICR5)` by `theta C^3` recovers `(2)`, and division by `theta B` recovers

```text
H=C^3(1+u z^hC/B).                                   (4)
```

The normalized formal solution of `(4)` is unique, so this polynomial is
exactly `C_u`. Conversely every polynomial `C_u` gives `(ICR4)--(ICR5)` by
`(2)`. The split and fractional-linear matching condition is precisely the
remaining necessary-and-sufficient reconstruction clause `(IHC9)`. This
proves the classifier and its stated scope. QED.
