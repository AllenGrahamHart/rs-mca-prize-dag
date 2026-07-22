# L1 exact-shell balanced shifted-lattice reduction

- **status:** PROVED
- **role:** remove the near-rational support mass and reduce band exact shells to one balanced split pencil
- **consumer:** `l1_mixed_petal_amplification`

## Shifted interpolation lattice

Let `H` be an `n`-point evaluation set with locator `Omega`, let `Uhat` be
the degree-below-`n` interpolant of a received word, and fix an agreement
level `m>k`.  Put

```text
w=m-k,       omega=n-m,
M_U={(W,N): N=W Uhat mod Omega},
sdeg(W,N)=max(deg W,deg N-(k-1)).                    (BL1)
```

The module `M_U` is free of rank two.  Any shifted weak-Popov basis
`g_1=(W_1,N_1),g_2=(W_2,N_2)` has predictable shifted degrees

```text
d_1<=d_2,       d_1+d_2=n-k+1=omega+w+1.            (BL2)
```

The unguarded level-`m` Pade/support census is exactly the set of monic
degree-`omega` divisors `W|Omega` for which some `(W,N) in M_U` has
`sdeg(W,N)<=omega`.  For split squarefree `W`, divisibility `W|N` is
automatic.

## Near-rational branch vanishes from the exact shell

Assume the band condition

```text
2m<=n+k-1,       equivalently w+1<=omega.            (BL3)
```

If `d_1<=w`, then either the unguarded support census is empty or it consists
of all `m`-subsets of the agreement set of one unique codeword `P_0`, whose
agreement size is exactly `n-d_1`.  In the nonempty case

```text
C_m(U)=binom(n-d_1,m),       n-d_1>=m+1.              (BL4)
```

Consequently the **exact** level-`m` shell is empty whenever `d_1<=w`.
The large near-rational binomial support mass is deleted by the complete-
agreement gcd guard rather than paid from the L1 reserve.

## Balanced split pencil

Every nonempty exact level-`m` shell therefore has

```text
w+1<=d_1<=d_2<=omega.                                (BL5)
```

Every unguarded census element, and hence every exact shell member, has a
unique representation

```text
(W,N)=A g_1+B g_2,
deg A<=omega-d_1,       deg B<=omega-d_2,             (BL6)
```

subject to monic normalization and `W=AW_1+BW_2` being a degree-`omega`
divisor of `Omega`.  The coefficient space in `(BL6)` has dimension exactly

```text
omega-w+1.                                           (BL7)
```

Writing `P=N/W`, `L=Omega/W`, and `Uhat-P=LQ`, the exact-shell guard is

```text
gcd(Q,W)=1.                                          (BL8)
```

Thus the band exact-shell problem is exactly a guarded balanced
two-generator split-pencil census.

## Scope

No row-sharp count of the balanced pencil, base-field normalization,
primitive/quotient priority map, or finite adjacent-row budget is proved.
The result applies to the band `(BL3)`; deeper shells require their existing
deep-list payment rather than this reduction.
