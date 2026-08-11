# Proof

Let `z` be a local base parameter at the shared root. The specialized
locator has

```text
Q_tau=(X-x_*)U_tau,                                (1)
```

where `U_tau` is the minimal locator of the contracted actual source. The
source consists of distinct points with nonzero weights, so among
polynomials of degree at most `d`,

```text
ker M_tau=U_tau F[X]_(<=1).                         (2)
```

The primitive kernel line is spanned by `Q_tau`; after removing it, the
regular symmetric block `N(z)` therefore has corank exactly one. Its
determinant has order three at the shared root.

We use the following elementary symmetric local lemma.

> If a symmetric matrix `N(z)` has corank one at `z=0` and determinant
> order three, if `v_0` spans its kernel, and if `N(z)v(z)` is divisible by
> `z^2`, then `v(z)^T N(z)v(z)` is divisible by `z^3`.

To prove the lemma, choose a basis with `v_0` first and write

```text
N=[a  b^T]
  [b   C ],       C(0) invertible.                 (3)
```

The Schur complement `s=a-b^TC^(-1)b` has order three. The canonical kernel
lift `w=(1,-C^(-1)b)` obeys `Nw=(s,0)`. Write
`v=lambda w+(0,r)`, where `lambda` is a unit and `r(0)=0`. Divisibility of
`Nv` by `z^2` and invertibility of `C` force `z^2|r`. Orthogonality of the
two summands gives

```text
v^TNv=lambda^2s+r^TCr,                             (4)
```

whose terms have orders at least three and four. This proves the lemma.

Apply it to the regular class of the divided row `U(t,X)`. The shared-jet
gate gives

```text
M(t)u(t)=z^2 kappa_tau nu(x_*)+O(z^3).              (5)
```

The permanent primitive kernel contributes nothing to the symmetric
pairing, so the lemma implies

```text
u(t)^T M(t)u(t)=O(z^3).                             (6)
```

On the other hand, taking the coefficient of `z^2` in `(5)` gives

```text
[z^2](u^TMu)=kappa_tau nu(x_*)^T u_tau
            =kappa_tau U_tau(x_*).                 (7)
```

The root `x_*` of `Q_tau` is simple in the specialized locator: the
minimum-gap root normal form makes every excess root squarefree. Hence

```text
U_tau(x_*)=Q_X(tau,x_*)!=0.                         (8)
```

Equations `(6)--(8)` force `kappa_tau=0`, proving `(HSV1)`. The equivalence
in the shared third-jet gate gives `(HSV2)`, the cubic recurrence, and Smith
type `[3]`. QED.
