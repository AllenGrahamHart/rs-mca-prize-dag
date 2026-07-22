# Proof

The element `6` is primitive in `F_151`, and `zeta=6^10=38` has order 15.
Translation of exponent sets therefore acts transitively on `Z=mu_15`.
Both `S` and `T` have full translation orbit of size 15, those orbits are
disjoint, and `U` has orbit size three disjoint from both. This gives 33
distinct blocks. A full orbit of a five-set contains every point five times;
the three translates of `U` partition `Z`. Hence every point occurs
`5+5+1=11` times, proving `(SCRF3)`.

We compute the quadratic rank by characters. The two seed locators are

```text
G_S=149+46z+150z^2+2z^3+105z^4+z^5,
G_T= 75+135z+92z^2+32z^3+118z^4+z^5.              (1)
```

Up to one common scalar, translation by `t` multiplies coefficient `i` by
`zeta^(-it)`. A quadratic coefficient indexed by `(i,j)` therefore has
character `i+j`. For sums `0,...,10`, exact row reduction of the two seed
vectors in each character space, after adding the three `U`-orbit rows,
gives

```text
sum i+j       0 1 2 3 4 5 6 7 8 9 10
rank          1 1 1 2 2 2 2 2 1 1  1.             (2)
```

The sum is 16. Distinct characters are independent because 15 is nonzero
in `F_151`, proving `(SCRF4)`.

For the complements, direct division by the two seed locators gives

```text
H_S=76+87z+108z^3+68z^4+42z^6+60z^7+46z^9+z^10,
H_T= 2+87z+130z^3+68z^4+17z^6+60z^7+33z^9+z^10.
                                                               (3)
```

The `U` orbit has seed locator `z^5-1` and complement
`1+z^5+z^10`. Translation orbits and Fourier inversion show that the
complement span is exactly the coordinate space supported on

```text
Omega={0,1,3,4,5,6,7,9,10}.                        (4)
```

It has dimension nine, proving `(SCRF5)`.

Finally let `I` have degree five and nonzero constant term. Reduction modulo
`I` on the nine-dimensional space `W=span{H_E}` has kernel

```text
W intersect I F[z]_(<=5).                           (5)
```

Multiplication by `I` is injective, so the second space in `(5)` has
dimension six. If the residue image had dimension at most three, rank-nullity
would force the kernel to have dimension at least six. It would therefore
equal `I F[z]_(<=5)`, placing every `z^jI`, `0<=j<=5`, in `W`.

But `z^2I` has a nonzero coefficient at degree two, namely the nonzero
constant coefficient of `I`, whereas degree two is absent from `Omega` in
`(4)`. Thus `z^2I` is not in `W`, a contradiction. The residue image has
dimension at least four, proving `(SCRF6)` and the route fence. QED.
