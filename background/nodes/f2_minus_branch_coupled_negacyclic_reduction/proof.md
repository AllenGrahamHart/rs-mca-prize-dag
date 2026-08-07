# Proof

For odd `p=3 mod 4`, the standard order law at `a>=2` is

```text
ord_(2^a)(p)=2^max(1,a-v_2(p+1)).                       (1)
```

The official field cap and `2^41|p^e-1` give `e<=6`, while the order in
`(1)` divides `e`. Hence `k in {2,4}` and `(1)` gives `b>=39`, proving
`(MINUS-ORDER)`.

For a nested window choose `y` of order `2^a`; its antipodal
representatives are `y^s`, `0<=s<m`, and take `omega=y`. For an exact-order
window the representatives are `y^(2s+1)` with `y` of order `2^a`; take
`omega=y^2`. In both cases `ord(omega)=2m`, and the `ell`-th moment is,
up to the nonzero factor `y^ell` in the exact-order case,

```text
P_eps(omega^ell).
```

This proves `(MINUS-K)` and also shows that a domain coset only contributes
another nonzero row factor.

Because the coefficients of `P_eps` lie in `F_p`, a root
`omega^ell` forces every Frobenius conjugate `omega^(p^i ell)`. Conversely
the original roots are included. The relevant Frobenius order is
`ord_(2m)(p)`, which is exactly the printed `h` by `(1)`.

It remains to check that the conjugate roots do not collide. The smallest
frequency modulus here is `2m=2^39`, while every selected exponent is less
than `2R<2^36`. If `b` is at least the modulus exponent, Frobenius sends a
small odd exponent to its negative. At the next modulus it sends it to its
negative translated by the half-period; in the unique order-four case
`b=39`, the four images occupy the four quarter-period bands. Their widths
are below one eighth of the smallest modulus, so these bands are disjoint.
Thus `|Omega|=hR`.

The set `Omega` is Frobenius-stable, so its monic root polynomial `G_W`
lies in `F_p[X]`. Since its roots are distinct, a polynomial of degree less
than `m` satisfies `(MINUS-K)` exactly when it is divisible by `G_W`.
Multiplication by `G_W` is injective on polynomials of degree less than
`m-hR`, proving `(MINUS-RANK)`. Equivalently, scalarizing the extension-field
moment matrix stacks its Frobenius-conjugate Fourier rows, and those `hR`
distinct rows are independent.

The weighted collision identity and floor `(MINUS-L2)` are the proved
`f2_weighted_kernel_collision_floor` theorem with rank `hR`.

Finally `p>m` on this branch. If `b=39` or `40`, the coefficient-one
candidates `2^39-1` and `2^40-1` are composite, so primality forces the
next odd coefficient and gives `p>2^40>=m`; if `b>=41`, the same inequality
is immediate. Apply the proved DLI Newton short-window exclusion to
`P_eps`, `N=m`, and `omega` of order `2m`. A nonzero ternary word of weight
at most `2R` is impossible, so its weight is at least `2R+1`. QED.
