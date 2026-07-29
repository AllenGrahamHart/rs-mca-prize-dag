# Proof

For odd `a`, the quotient

```text
b_a=(1-zeta^a)/(1-zeta)=1+zeta+...+zeta^(a-1)
```

is an algebraic integer. Both numerator and denominator have absolute norm
two, so `b_a` has norm one and is a unit. Complex conjugation gives

```text
bar(b_a)=zeta^(1-a)b_a.
```

Thus `eta_a=zeta^((1-a)/2)b_a` is fixed by conjugation and belongs to the
real unit group of `K+`. This proves the elementary part of `(CUB1)`.

For prime-power conductor, the Kummer-Sinnott unit-index theorem says that
the circular-unit group `C` in the full cyclotomic field satisfies

```text
[R^x:C]=h(K+).                                       (1)
```

The same theorem's standard prime-power generators are the roots of unity
and the units `b_a` for `a` prime to 256. John C. Miller proves
unconditionally that

```text
h(Q(zeta_256+zeta_256^(-1)))=1.                      (2)
```

Specifically, this is Theorem 2.1 of *Class numbers of totally real fields
and applications to the Weber class number problem*, Acta Arith. 164.4
(2014), 381-397. Equations (1) and (2) give `R^x=C`.

Modulo roots of unity, `b_a` and `eta_a` have the same class. Also
`b_1=1`, and replacing `a` by `-a mod 256` changes `b_a` only by a root of
unity. Hence the 63 indices

```text
a=3,5,...,127
```

generate `R^x/mu_256`. Dirichlet's unit theorem gives this quotient rank 63,
and it is torsion-free. A surjection from `Z^63` onto a free abelian group of
rank 63 is an isomorphism. Therefore these 63 classes form a basis, proving
`(CUB2)` and the uniqueness in `(CUB3)`.

Under the embedding `zeta -> zeta^b`, the root-of-unity factor in `eta_a`
has modulus one, while

```text
|1-zeta^(ab)|/|1-zeta^b|
  =|sin(pi*a*b/256)|/|sin(pi*b/256)|.
```

Taking the logarithm of the squared modulus gives `(CUB4)`. The logarithmic
map kills exactly `mu_256`, so the uniqueness in `(CUB3)` makes the columns
of `(CUB4)` an integer basis of the full unit log lattice. QED.
