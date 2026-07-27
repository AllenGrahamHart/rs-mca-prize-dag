# Proof

Put `K=Q(zeta)` and choose `r=min T`. If

```text
d=gcd(256,{i-r:i in T})>1,
```

then every support exponent is `r+d j`. Set `eta=zeta^d`, whose order is
`M=256/d`. Since `d` is a nontrivial divisor of a power of two,

```text
M<=128,        [Q(eta):Q]=phi(M)=M/2<=64.
```

We can write

```text
alpha=zeta^r beta,       beta=sum_(i in T) c_i eta^((i-r)/d).
```

Because `0<=i-r<128`, the polynomial defining `beta` has degree strictly
less than `128/d=M/2=phi(M)`. It is nonzero, so `beta` is a nonzero element
of `L=Q(eta)`.

The two first-band profiles have folded square mass

```text
S=sum_i c_i^2=18       for (4,2,0),
S=sum_i c_i^2=16       for (3,4,0).
```

Odd-character orthogonality in the order-`M` field gives

```text
(1/phi(M)) sum_(u mod M, u odd) |B(eta^u)|^2=S,
```

where `B(eta)=beta` and `deg B<phi(M)`. AM-GM therefore yields

```text
0<|Norm_(L/Q)(beta)|<=S^(phi(M)/2)<=18^32<2^250.       (1)
```

The extension degree is `[K:L]=d`. Since `beta` belongs to `L` and the
absolute norm of the root of unity `zeta^r` is one,

```text
|Norm_(K/Q)(alpha)|=|Norm_(L/Q)(beta)|^d.              (2)
```

Thus every rational prime dividing the full norm also divides the nonzero
small-field norm. Equation (1) rules out every pair-feasible row prime,
because those primes satisfy `p>=2^250`. By the collision-norm criterion,
no proper-conductor vector in either profile can collide.

The condition cannot be strengthened to say that every low-variance vector
has proper conductor. The folded vector with nonzero coefficients

```text
(0,2),(16,-2),(32,-1),(48,1),(65,1),(80,-1),(96,-2)
```

has profile `(3,4,0)`, support-difference gcd one, and exact negacyclic
autocorrelation variance `36`. This counterexample only fences the stronger
classification; it does not challenge the proved exclusion above.
