# Proof

Put `M=m/2`. Use a primitive element `omega in F_p` of order `m`. For a
hypothetical primitive exact-level pair, write its constant-one reciprocal
locators as

```text
U(Y)=product_(i in I)(1-omega^i Y),
V(Y)=product_(j in J)(1-omega^j Y),
```

where `I,J` are disjoint `h`-subsets of `Z/mZ`. Top-shift equality says

```text
U-V=cY^h,       c!=0.                              (1)
```

Since `p>h`, Newton identities applied to the common coefficients below
degree `h` give

```text
sum_(i in I)omega^(ki)=sum_(j in J)omega^(kj),
1<=k<h.                                            (2)
```

## A nonzero cyclotomic integer with many prime divisors

Let `zeta` be a complex primitive `m`-th root, let

```text
f_t=1_(t in I)-1_(t in J),
z=sum_(t=0)^(m-1) f_t zeta^t in Z[zeta].           (3)
```

The integer `z` is nonzero. Indeed, if `z=0`, every odd Galois conjugate
also vanishes. Splitting the odd Fourier coefficients into antipodal pairs
gives

```text
0=sum_(t=0)^(M-1)(f_t-f_(t+M))zeta^((2b+1)t)
```

for every `0<=b<M`. Fourier inversion on `Z/MZ` then gives
`f_t=f_(t+M)` for every `t`. Both `I` and `J` are invariant under the
nontrivial scaling `-1`, contrary to primitivity.

Because `p=1 mod m`, the prime `p` splits completely in `Q(zeta)`. Fix the
prime ideal `P` induced by reduction `zeta -> omega`. For every odd
`1<=k<h`, equation `(2)` says

```text
sigma_k(z) in P,
```

where `sigma_k(zeta)=zeta^k`. Hence `(z)` is divisible by
`sigma_k^(-1)(P)`. These prime ideals are distinct, so, with

```text
r_h=floor(h/2),
```

one has

```text
p^r_h divides |Norm_Q(zeta)/Q(z)|.                 (4)
```

## Odd-frequency Parseval bound

For `0<=t<M` put `g_t=f_t-f_(t+M)`. The odd Fourier coefficients are the
length-`M` Fourier transform of `(g_t zeta^t)`. Parseval and AM--GM give

```text
sum_(a odd)|sigma_a(z)|^2=M sum_t g_t^2,
|Norm(z)|<=(sum_t g_t^2)^(m/4).                    (5)
```

Since `I,J` are disjoint and each has size `h`, termwise

```text
(f_t-f_(t+M))^2<=2(f_t^2+f_(t+M)^2),
```

and therefore

```text
sum_t g_t^2<=4h.                                   (6)
```

There is one delicate width. Write `a=m/4` and suppose `h=a+1`. Then `h`
is odd. Define the loss

```text
L=4h-sum_t g_t^2.
```

An antipodal pair occupied once contributes `1` to `L`; a pair occupied
twice on the same side contributes `4`; and an opposite `I/J` pair
contributes zero. Thus `L` is even. If `L=0`, all occupied antipodal pairs
are opposite, so `V(Y)=U(-Y)`. The midpoint `(U+V)/2` then has degree below
the odd number `h`. But here

```text
m=3h+e,       e=a-3,       0<e<h,
```

and the proved near-third Belyi theorem gives midpoint degree exactly `h`.
This is impossible.

If `L=2`, there are exactly two singleton antipodal pairs, one belonging to
each side, and every other occupied pair is opposite. Let their roots be
`alpha` and `beta`. The `k=2` case of `(2)` cancels every opposite pair and
gives `alpha^2=beta^2`. Hence `beta=+/-alpha`, contradicting that they are
distinct singleton antipodal pairs. Consequently

```text
sum_t g_t^2<=4h-4=m        when h=m/4+1.            (7)
```

## Numerical contradiction

The prime `p` is strictly greater than the composite integer `m^2`. Combine
`(4)--(6)`.

If `h=a`, then `h` is even and

```text
p^(a/2)>m^a>=(4h)^(m/4),
```

contradicting `(4)--(6)`. If `h=a+1`, equations `(4),(5),(7)` give the same
contradiction.

It remains to take `h=a+d` with `d>=2`. For even `h`, also `d` is even and
`2r_h=a+d`; for odd `h`, `d` is odd, `d>=3`, and `2r_h=a+d-1`. The elementary
estimate

```text
(1+d/a)^a<3^d                                      (8)
```

follows from `(1+1/a)^a<3` and Bernoulli's inequality. Therefore

```text
(4h)^(m/4)=m^a(1+d/a)^a<m^a 3^d.                  (9)
```

For even `h`, `m^d>3^d`; for odd `h`,
`m^(d-1)>3^d` because `m>=16` and `d>=3`. In either case `(9)` is strictly
below `m^(2r_h)`, while `(4)` and `p>m^2` put the nonzero norm strictly above
`m^(2r_h)`. This contradiction proves `(CNQ1)`.

The complement-third gate already makes every non-full exact-level pair
satisfy `h<m/3`. Removing all `h>=m/4` leaves `(CNQ2)`. QED.
