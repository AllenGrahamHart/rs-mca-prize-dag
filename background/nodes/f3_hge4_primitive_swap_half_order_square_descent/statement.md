# HGE4 primitive swap half-order square descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_primitive_swap_odd_moment_router`

Fix an official row, put `N=n/2`, and let `h=2d+1` be odd. For an `h`-subset
`Y` of `mu_N`, write

```text
L_Y(Z)=prod_(y in Y)(Z-y),       c_Y=prod_(y in Y)y=-L_Y(0).
```

Call `Y` a primitive half-order square support when

```text
(L_Y(Z)+c_Y)/Z=T_Y(Z)^2                         (HOS1)
```

for a monic degree-`d` polynomial `T_Y`, and the multiplicative scaling
stabilizer of `Y` in `mu_N` is trivial. The monic square root, if it exists,
is unique and is recovered coefficient by coefficient.

The map

```text
U -> Y={x^2:x in U}
```

is a bijection from primitive antipodal-swap near-square unions of width `h`
to primitive half-order square supports. Its inverse is

```text
U={x in mu_n:x^2 in Y}.
```

Indeed `c_Y` is automatically a square in `F_p`. For either `a^2=c_Y`, the
two reconstructed locators are

```text
X T_Y(X^2)-a,       X T_Y(X^2)+a.                (HOS2)
```

They split `U` into the primitive top shift pair `(P,-P)`; changing the sign
of `a` only exchanges the sides.

Equivalently, the half-order objects are the monic divisors

```text
Z T(Z)^2-c  divides  Z^N-1,       deg T=d, c in mu_N,          (HOS3)
```

whose root set has trivial `mu_N`-scaling stabilizer. Here `T` and `c` are
uniquely determined by the divisor.

Scaling orbits correspond through `mu_n/{+/-1}=mu_N`. Consequently, if
`W_h` counts scaling orbits of primitive half-order square supports, then

```text
V_h^swap=W_h,       A_h^swap=hW_h.                (HOS4)
```

An anchored swap generator therefore enumerates the
`binom(N-1,h-1)` subsets `Y` containing `1` and performs one deterministic
perfect-square test. It performs no sign search; compared with the signed
odd-moment generator it removes the factor `2^(h-1)` of side choices.

This theorem does not bound `W_h`, the free-union class, or the HGE4
aggregate. It also does not claim that enumerating all coefficient tuples
`(T,c)` is efficient.
