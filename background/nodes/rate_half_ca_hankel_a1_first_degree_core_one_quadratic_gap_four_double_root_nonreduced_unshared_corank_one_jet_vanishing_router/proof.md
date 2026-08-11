# Proof

The nonreduced two-jet theorem gives, in the regular quotient,

```text
N(z)v(z)
 =z^2 kappa_2 nu(x_*)+z^3 kappa_3 nu(x_*)+O(z^4),  (1)
ord det N=4.                                        (2)
```

We first show that corank one supplies the simple-root evaluation. The full
specialized Hankel kernel has dimension two: one permanent primitive line
and one regular line. If `P_tau` is the minimal locator of the nonzero
contracted source weights, the distinct-source Vandermonde representation
gives

```text
ker M_tau=P_tau F[X]_(<=d-deg P_tau).              (3)
```

Hence `deg P_tau=d-1`. Every source point lies in `U_0`, while the fixed
heavy point lies outside `U_0`; therefore `P_tau(x_*)!=0`. The primitive
degree-`d` kernel polynomial vanishes at `x_*`, so `(3)` forces

```text
Q(tau,X)=c(X-x_*)P_tau(X),       c!=0.              (4)
```

Thus `U_tau=cP_tau` and `U_tau(x_*)!=0`, proving `(HCR2)`.

We first record the required symmetric local lemma.

> Let `N(z)` be symmetric, with `corank N(0)=1` and determinant order four.
> If `N(z)v(z)` is divisible by `z^2`, then
> `v(z)^T N(z)v(z)` is divisible by `z^4`.

Choose a basis whose first vector spans the specialized kernel and write

```text
N=[a  b^T]
  [b   C ],       C(0) invertible.                 (5)
```

The Schur complement `s=a-b^TC^(-1)b` has order four. Its canonical kernel
lift `w=(1,-C^(-1)b)` satisfies `Nw=(s,0)`. Write

```text
v=lambda w+(0,r),       lambda(0)!=0.              (6)
```

Divisibility of `Nv` by `z^2` and invertibility of `C` force `z^2|r`.
The two summands in `(4)` are orthogonal for the form `N`, so

```text
v^TNv=lambda^2s+r^TCr.                             (7)
```

Both terms have order at least four, proving the lemma.

Apply it to `(1)`. The permanent primitive kernel contributes nothing to
the symmetric pairing. Moreover `v(0)` is nonzero in the regular quotient:
adding a primitive-kernel multiple does not change evaluation at `x_*`
because `Q(tau,x_*)=0`, whereas `(HCR2)` gives `U_tau(x_*)!=0`. Thus
`v(0)` spans the corank-one kernel as required by the lemma. The coefficient
of `z^2` in `v^TNv` is

```text
kappa_2 nu(x_*)^T v(0)=kappa_2 U_tau(x_*).         (8)
```

By `(HCR1)` this last evaluation is nonzero, while the lemma makes `(6)`
zero. Hence `kappa_2=0`. Equation `(1)` now starts in order three, and the
coefficient of `z^3` in the same pairing is

```text
kappa_3 U_tau(x_*).                                (9)
```

The lemma again makes it zero, so `kappa_3=0`. This proves `(HCR3)`.

The equivalence in the two-jet theorem now gives local divisibility by
`D_1`, extension of the degree-at-most-three quotient, and Smith type
`[4]`. Taking the contrapositive of `(HCR3)` gives `(HCR4)`. QED.
