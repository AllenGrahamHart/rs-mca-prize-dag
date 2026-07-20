# H3 cutoff multiplicity-layer gcd compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half` (evidence/router)
- **dependencies:** `f3_h3_global_resultant_compression`,
  `f3_h3_cutoff18_double_accident_reduction`,
  `f3_h3_uniform_product_fiber_stepanov`

Let `n=2^s`, `s>=2`, let `p=1 mod n` be prime with `p>=n^2`, let `H` be
the order-`n` subgroup of `F_p^*`, and put `A=(1-H)\{0}` and `d=n-1`.
Define the two row polynomials

```text
Pcal(T)=product_(a,b in A)(T-ab),
Qcal(T)=product_(a,b in A,b/a!=1)(T-b/a).          (LGC1)
```

Thus a nonidentity target `t` has multiplicity `P(t)` in `Pcal` and
multiplicity `R(t)` in `Qcal`.

Fix an integer cutoff `0<=c<d`, and use Hasse derivatives. Put

```text
G=gcd(Pcal^[0],Pcal^[1],...,Pcal^[c]),
G_j=gcd(G^[0],G^[1],...,G^[j-1])       (j>=1),
Qcal_+=gcd(Qcal,Qcal^[1]).                         (LGC2)
```

Then the exact cutoff moments

```text
X_c=sum_(t!=1)(P(t)-c)_+ R(t),
Y_c=sum_(t!=1)(P(t)-c)_+ (R(t)-1)_+
```

are recovered without enumerating target fibers:

```text
X_c=sum_(j=1)^(d-c) deg gcd(Qcal,G_j^d),
Y_c=sum_(j=1)^(d-c) deg gcd(Qcal_+,G_j^d).         (LGC3)
```

The complete layer sum is load-bearing. The tempting one-gcd shortcut gives

```text
deg gcd(Qcal,G^d)=sum_(t:(P(t)-c)_+>0) R(t),       (LGC4)
```

which records rich support but discards the excess multiplicity.

At `c=18`, these are exactly the critical `X_18` and the proved
double-accident residual `Y_18`. By the global resultant compression,
`Pcal` and `Qcal` themselves are reductions of two resultants of
`F_n(X)=((1-X)^n-1)/X`. Hence `(LGC3)` is a quotient-lift-free exact row
compiler once those global polynomials are available.

On the 29 official orders, the proved uniform product-fiber bound truncates
both sums further to

```text
B_n=min(n-19,ceil(33n^(2/3))-19).                  (LGC5)
```

Every degree in `(LGC3)` is also the nullity of the corresponding Sylvester
matrix. An exact certificate first supplies sequential divisor-plus-Bezout
certificates for `G` and the nested `G_j`, then streams, for each live layer,
the monic terminal gcd `H`, both exact quotients, and a Bezout identity between
the two coprime quotients. The sum of the certified terminal gcd degrees is an
independently checkable row certificate for `X_18` or `Y_18`.

The formula does not bound either moment, construct the global polynomials at
official scale, or prove that dense polynomial gcds are cheaper than the
existing direct row evaluator.
