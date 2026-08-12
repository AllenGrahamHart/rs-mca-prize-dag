# Proof

The two-jet theorem gives

```text
N(z)v(z)=z^2 kappa_2 nu(x_*)
          +z^3 kappa_3 nu(x_*)+O(z^4),
ord_z det N=4,                                     (1)
```

and the higher-corank hypothesis gives `r>=2`.
Every positive Smith exponent is at least one and their sum is the
determinant order four, so `r<=4`.

The full specialized Hankel kernel consists of one permanent primitive
line plus the `r` regular kernel directions, so it has dimension `r+1`.
The regular Hankel recurrence theorem for the specialized minimal
polynomial gives

```text
ker M_tau=P_tau F[X]_(<=d-deg P_tau).              (2)
```

Comparing dimensions in `(2)` gives `deg P_tau=d-r`. Both `U_tau` and
`Q_tau=(X-x_*)U_tau` lie in this kernel. Since `deg U_tau=d-1`, division
by `P_tau` gives a polynomial `L_tau` of degree `r-1` and the two
factorizations in `(HSR2)`. Evaluating the first factorization at `x_*`
gives `(HSR3)` without identifying the roots of `P_tau` with the original
fixed source.

It remains to classify the symmetric local block. We use the following
valuation lemma. Let a symmetric matrix over the local DVR have positive
Smith exponents `a_1,...,a_r` and an invertible complementary block. If

```text
Nv in z^s O^n,                                     (3)
```

then

```text
ord_z(v^T Nv)>=min(
  2s,
  min_i {a_i+2 max(0,s-a_i)}).                    (4)
```

Because the residue characteristic is odd, symmetric elimination
diagonalizes the singular block by congruence to
`diag(z^a_i u_i)`, with every `u_i` a unit. Equation `(3)` then forces
the corresponding coordinate of `v` to have order at least
`max(0,s-a_i)`; regular coordinates have order at least `s`. Summing the
diagonal self-pairings proves `(4)`.

The positive exponents sum to `ord det N=4`. The complete partition list
and the lower bounds from `(4)` are

```text
Smith profile    s=2 pairing order    s=3 pairing order
[4]                       4                    4
[1,3]                     3                    3
[2,2]                     2                    4
[1,1,2]                   2                    4
[1,1,1,1]                 3                    5.   (5)
```

Assume now that there is no quotient-root collision. Then
`U_tau(x_*)!=0`. The coefficient of order two in the self-pairing from
`(1)` is

```text
kappa_2 U_tau(x_*).                                (6)
```

For profiles `[1,3]` and `[1,1,1,1]`, the `s=2` column of `(5)` makes
this coefficient zero, so `kappa_2=0`. Equation `(1)` then has image order
at least three, and its order-three self-pairing coefficient is exactly

```text
kappa_3 U_tau(x_*).                                (7)
```

For `[1,1,1,1]`, the `s=3` column of `(5)` forces `(7)` to vanish as
well. Thus both jets vanish, contradicting `(HSR1)`. For `[1,3]`, only
`kappa_2` is forced to vanish, so `(HSR1)` gives `kappa_3!=0`.

For `[2,2]` and `[1,1,2]`, if `kappa_2` vanished then the `s=3` column
of `(5)` would also force `kappa_3=0`. Hence `(HSR1)` requires
`kappa_2!=0`. The corank-one profile `[4]` was already eliminated by the
preceding router. This leaves exactly `(HSR4)` and proves the theorem. QED.
