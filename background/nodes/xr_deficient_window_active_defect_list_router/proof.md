# Proof

Write the errors of the parameter `tau` as

```text
E_tau=E_*-Q tau,       E_tau'=E_*'+P tau.                   (1)
```

Consequently

```text
P E_tau+Q E_tau'=P E_*+Q E_*'=rho,                          (2)
```

so the residual and its support are independent of the base member. The
primitive Pade router gives `P E_*+Q E_*'=0` outside `G_d`; hence
`D subset G_d`. Its bound `ell+|G_d|<=d-1` proves `(AD2)`. If both errors
of any member vanished at `x in D`, equation `(2)` would give `rho(x)=0`,
a contradiction. Thus `D` is a fixed joint-mismatch set.

## Punctured word and scalar factorization

Fix `x notin D`. Equation `(2)` vanishes there, and coprimality ensures
that `P(x),Q(x)` are not both zero. Define

```text
w(x)=E_*(x)/Q(x)          if Q(x)!=0,
w(x)=-E_*'(x)/P(x)        otherwise.
```

The two definitions agree when both denominators are nonzero. They give
`E_*=Qw` and `E_*'=-Pw`, so `(1)` proves `(AD3)`. Since `D` contains no
joint-core point and `P,Q` have no common root,

```text
Z_tau={x in H\D:tau(x)=w(x)}.                               (3)
```

Maximal exact depth makes `|Z_tau|=k+d`, while the primitive router gives
`deg tau<k-ell`. Moreover

```text
(n-e)-(k-ell)>=R-d+2ell+1>0,
```

so evaluation of these polynomials on `H\D` is injective. This proves the
exact-list embedding `(AD4)` as an ordinary Reed--Solomon list.

For `lambda=[alpha:beta]`, equations `(AD3)` give

```text
alpha E_tau+beta E_tau'
  =(alpha Q-beta P)(w-tau).
```

The factor `L_lambda=alpha Q-beta P` cannot vanish identically: that would
make the coprime nonproportional pair `P,Q` constant-proportional. Its degree
is at most `ell`, proving `(AD5)`.

Now let the selected ray be `D`-local. Since its support contains the
`k+d>=k` point joint core, the ray-rigidity interpolation in
`xr_band_ledger_theorems` identifies its codeword with
`alpha f_tau+beta g_tau`. Its agreement support is therefore exactly the
zero set of the scalar error in `(AD5)`. Every root of `L_lambda` in `H\D`
is such an agreement point. If it were not in `(3)`, it would be an off-core
point outside `D`, contrary to locality. The selected ray is exact-`A`;
after its `k+d` core points, exactly `h-d` scalar agreements remain.
Locality and the fact that `D` contains no core point identify them with
`(AD6)`.

If a point of `D` lay in the blocks of two distinct projective slopes, the
two independent scalar equations would force both errors to vanish there,
contrary to `(2)`. The blocks are disjoint.

## Outside payment

Let `N_d^out` count pairs with a selected off-core point `x notin D`. By
`(AD3)`, the nonzero error vector at `x` has the fixed projective annihilator
determined by `[P(x):Q(x)]`; equivalently its selected slope lies in an
image of `H\D` having at most `n-e` elements. Assign one such slope to each
pair. The global first-match convention makes equal assigned slopes the same
selected ray. The high-depth interaction strip excludes two distinct pairs
on that ray because `2d>=h`. The assignment is injective, proving
`N_d^out<=n-e`.

A pair counted by `N_d^D` has at least two selected slopes. Their disjoint
blocks from `(AD6)` each have `h-d` points in `D`, proving
`e>=2(h-d)`. The same disjointness over all selected slopes gives
`L_(f_tau,g_tau)(h-d)<=e`. This is `(AD7)`. QED.
