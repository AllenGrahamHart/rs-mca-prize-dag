# Proof

Put `c=b_01`. The scroll atlas gives

```text
alpha=A_0/c,
beta=(A_1-hA_0)/c.                                  (1)
```

The block locators `A_0,A_1` have disjoint nonempty root sets, hence are
coprime. Since `c` is a nonzero field element,

```text
gcd(alpha,beta)=gcd(A_0,A_1-hA_0)=gcd(A_0,A_1)=1.  (2)
```

In both quadratic incidence types, `deg A_0=d-2`, so `(1)` gives
`deg alpha=d-2`.

For quadratic `K_4-e`, the edge `b_13` is linear and the balancing polynomial
is `h=0`. Also `deg A_1=d-2`, whence `deg beta=d-2`.

For a pendant chamber, `deg A_1=d-1` and `deg h<=1`, so initially
`deg beta<=d-1`. If `deg beta<=d-2`, then `(QPM1)` and the affine-linearity
of `U,V` would give

```text
deg A_i<=max(deg alpha+1,deg beta+1)<=d-1
```

for every `i`. This contradicts the pendant degree `deg A_3=d`. Therefore
`deg beta=d-1`, proving `(QPM2)`.

Suppose there were a base-field relation among the four module entries. It
would have the form

```text
(r_0+r_1X)alpha+(s_0+s_1X)beta=0.                  (3)
```

If either linear coefficient polynomial in `(3)` were zero, coprimality and
nonvanishing would make both zero. Otherwise `(2)` and Euclid's lemma imply
that `alpha` divides `s_0+s_1X`. But `deg alpha=d-2>=2`, while the latter
has degree at most one, a contradiction. This proves `(QPM3)`. Since `C` is
invertible, the same conclusion holds for the four `A_i`.

Finally, take `u_i,v_i` to be the coordinates of the two rows `U,V`.
Equation `(QPM1)` gives the first part of `(QPM4)`, while the parent
factorization `Lambda_D=EA_0A_1A_2A_3` gives the second. The coefficient
matrix of the four affine-linear pairs is exactly `C`, already proved
invertible, and the parent theorem gives the two exact exceptional degrees.
QED.
