# Proof

The harmonic-exclusion dependency gives `q_out!=-1`. Write the three
Mobius equations from the ratio-router dependency uniformly as

```text
a_j(1+q_out)^2=4q_out b_j.                            (1)
```

Every `a_j` is nonzero. Indeed, `r!=0`, while `r=1` or `r^2=-1` would give
`r^4=1`. Every `b_j` on a surviving branch is also nonzero: if `b_j=0`,
equation `(1)` and `a_j!=0` would force `q_out=-1`, which has been excluded.
Consequently `(1)` is equivalent to

```text
q_out/(1+q_out)^2=a_j/(4b_j).                         (2)
```

The remainder-square dependency says that the same pencil exists exactly
when

```text
deg S=2M-2,
T=q_out S^2/(1+q_out)^2,
S/(1+q_out) is a nonzero polynomial square.           (3)
```

Combining `(2)` and `(3)` gives `(NSR4)`.

Now put `y=q_out+q_out^(-1)`. Dividing `(1)` by `a_jq_out`
gives

```text
y+2=4b_j/a_j,                                        (4)
```

which is the initial value in `(NSR5)`. If
`y_m=q_out^(2^m)+q_out^(-2^m)`, then

```text
y_(m+1)=y_m^2-2.                                     (5)
```

Since `N=2^38`, every admitted `q_out in mu_N` therefore satisfies
`y_38=2`. Distinct outer factors give `q_out!=1`, and harmonic exclusion
gives `q_out!=-1`, so `y_0 notin {2,-2}`. This proves necessity.

Conversely, suppose `(NSR4)--(NSR6)` hold for one `j`. Let `q_out` be a root
of `(NSR7)` in an algebraic closure. Induction in `(5)` gives

```text
y_38=q_out^N+q_out^(-N)=2.
```

Hence `(q_out^N-1)^2/q_out^N=0`, so `q_out^N=1`. Because `N` divides
`p-1`, every `N`th root lies in `F_p`; the two roots of `(NSR7)` are the
base-field pair `q_out,q_out^(-1)`. The exclusion of `y_0=+/-2` makes them
distinct from `+/-1`.

Equation `(4)` now reverses to `(1)`, so the Mobius matching holds by the
ratio-router dependency. It also gives

```text
q_out/(1+q_out)^2=a_j/(4b_j).
```

Together with `(NSR4)`, this is the exact remainder identity in `(3)`.
The square test `(NSR6)` therefore invokes the converse of the
remainder-square router and reconstructs the complete square pencil.

It remains only to show that `(NSR6)` is well posed without choosing one of
the reciprocal roots. Since `4N` divides `p-1`, every element of `mu_N` is a
fourth power, hence a square, in `F_p`. Replacing `q_out` by its inverse
changes the candidate direction by

```text
S/(1+q_out^(-1))=q_out S/(1+q_out).                  (6)
```

Multiplication by the square `q_out` preserves both nonzeroness and the
polynomial square class. Thus either root gives the same verdict, completing
both directions. QED.
