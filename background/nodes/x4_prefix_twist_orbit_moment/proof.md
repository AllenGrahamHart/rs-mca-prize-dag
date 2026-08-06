# Proof

If

```text
Q_S(X)=X^A+c_1(S)X^(A-1)+...+c_A(S),
```

then direct scaling of the roots gives

```text
c_i(zeta S)=zeta^i c_i(S).
```

Because multiplication by `zeta` is a bijection of `D`, it is a bijection
between the two displayed fibers. A group element stabilizes `z` exactly when
`zeta^i=1` for every `i in I(z)`. In a cyclic group of order `N`, this
subgroup has order `gcd(N,I(z))`; every element stabilizes the zero prefix.
Orbit-stabilizer proves the orbit size.

The equal fibers in this orbit contribute

```text
Q^(r-1) (N/s(z)) (|F_z|/binom(N,A))^r
  =(N/s(z)) R(z)^r/Q
```

to `Gamma_r`. All other terms are nonnegative, proving `(TO-1)`; rearranging
under `Gamma_r<=G` proves `(TO-2)`.

Finally, every divisor of `2^ell` is a power of two and

```text
gcd(2^ell,I(z))=2^min(ell,min_{i in I(z)} v_2(i)).
```

Since `1<=i<=t<N=2^ell`, the cap at `ell` is inactive for nonzero prefixes.
QED.
