# Proof - HGE4 multiscale Haar norm product and `m=64` close

## 1. One energy budget for all even moments

Retain the signed support notation from the ambient norm theorem. Newton's
identities give

```text
sum_t f_t omega^(kt)=0,       0<=k<h.                (1)
```

The odd moments produce the nonzero cyclotomic integer
`z=F(zeta_m)`. With `u=floor(h/2)`, the inherited norm packet gives

```text
p^u divides |Norm_m(z)|,       |Norm_m(z)|<=D^(m/4),
D+L=4h.                                               (2)
```

Fix `a<ell`. Folding `q` modulo `N_a` gives `Q_a`. Folding once more gives

```text
Q_(a+1)(u)=Q_a(u)+Q_a(u+N_a/2).
```

If `E_a=sum_u Q_a(u)^2`, the parallelogram identity is

```text
E_(a+1)=2E_a-Delta_a.                                (3)
```

Divide `(3)` by `2^(a+1)` and telescope. Since `E_0=L` and every terminal
energy is nonnegative,

```text
sum_(a<ell)Delta_a/2^(a+1)
 =L-E_ell/2^ell<=L.                                  (4)
```

This proves `(MHN4)`.

## 2. The norm at each Haar scale

Put

```text
alpha_a=F(zeta_(N_a))=sum_(u<N_a)Q_a(u)zeta_(N_a)^u.
```

The minimal polynomial of `zeta_(N_a)` is
`Phi_(N_a)(X)=X^(N_a/2)+1`. Hence

```text
alpha_a=0
 iff Q_a(u)=Q_a(u+N_a/2) for every u<N_a/2
 iff Delta_a=0.                                      (5)
```

If `Delta_a>0`, the even moments `k=2^(a+1)b`, with odd
`b<=H/2^a`, put `alpha_a` in `r_a` distinct primes above `p`. Therefore

```text
p^r_a divides |Norm_(N_a)(alpha_a)|.                (6)
```

Odd-frequency Parseval at order `N_a` is exact:

```text
sum_(b odd)|sigma_b(alpha_a)|^2=(N_a/2)Delta_a.
```

AM--GM over the `N_a/2` conjugates gives

```text
|Norm_(N_a)(alpha_a)|<=Delta_a^(N_a/4).             (7)
```

Every positive integer `j<=H` has a unique form `2^a b` with `b` odd, so
`sum_a r_a=H`. This accounts for every even moment below `h` exactly once.

## 3. The structural zero factors

If `a in Z`, equation `(5)` and Gauss's lemma give
`Phi_(N_a)|F` in `Z[X]`. The distinct dyadic cyclotomic factors are coprime,
so their product divides `F`.

Let `O` be either `m` or one of the nonzero evaluation orders `N_j`. For
`O!=N_a`, direct evaluation of `X^(N_a/2)+1` gives

```text
|Norm_(Q(zeta_O)/Q)(Phi_(N_a)(zeta_O))|
 =2^(min(O,N_a)/2).                                  (8)
```

Indeed, if `O>N_a`, the displayed value is `1+xi` for a primitive
`2O/N_a`-th root and its norm is `2^(N_a/2)`. If `O<N_a`, the value is the
rational integer `2`, whose norm is `2^(O/2)`.

Multiplying `(2)`, `(6)--(8)` over all nonzero evaluations proves the
divisibility and upper bound `(MHN6)`. The prime exponent is `R_S`; the
known power of two is exactly `T_2(S)`.

Put `x_a=Delta_a/2^(a+1)`. Equations `(2),(4)` give

```text
D+sum_(a in S)x_a<=4h.                               (9)
```

Weighted AM--GM with weights `A` and `B_a` maximizes the right side of
`(MHN6)` at

```text
D=4h A/W_S,       x_a=4h B_a/W_S.
```

This gives `(MHN7)`. Since the row prime is strictly greater than the
composite integer `n^2`, `(MHN8)` contradicts `(MHN6)`, including equality.

## 4. The sharp width-four endpoint

Now put `m=64`, `h=4`, and first suppose `Delta_0=0`. Then
`Phi_32|F`, so `(8)` contributes `2^16` to `Norm_64(z)`. Equations `(2)`
give

```text
2^16 p^2<=|Norm_64(z)|<=D^16<=16^16.
```

But `p>n^2>=2^26`, making the left side greater than `2^68`, while the
right side is `2^64`. This is impossible.

Suppose `Delta_0>0`. The moments `k=1,2,3` give

```text
p^3 divides |Norm_64(F(zeta_64)) Norm_32(F(zeta_32))|. (10)
```

Let `nu` be the multiplicity of `X-1` in `F mod 2`, truncated at nine.
Since `F(1)=0`, `nu>=1`. At the unique primes above two,
`1-zeta_64` and `1-zeta_32` are uniformizers of norm two. The truncation is
strictly below both ramification degrees, so the Taylor expansion proves that
each norm in `(10)` is divisible by `2^nu`. Parseval gives the upper bound
`D^16 Delta_0^8`.

It remains only to prove `(MHN9)`. Split the 64 coefficients into the sixteen
quarter-orbits

```text
(f_j,f_(j+16),f_(j+32),f_(j+48)).                  (11)
```

Each entry is in `{-1,0,1}` and the global counts of `+1` and `-1` are both
four. One orbit contributes

```text
(f_j-f_(j+32))^2+(f_(j+16)-f_(j+48))^2
```

to `D`, and

```text
(f_j+f_(j+32)-f_(j+16)-f_(j+48))^2
```

to `Delta_0`. Modulo two, the signs disappear, so the parity of the first
eight Taylor coefficients at `1` depends only on the occupied coordinates.
The recurrence in `verify.py` processes `(11)` one orbit at a time and keeps
exactly

```text
(number of +1, number of -1, D, Delta_0,
 parities of Taylor coefficients 1,...,8).
```

After sixteen steps there are 28,171 reachable aggregate states. If all
first eight parities vanish, using `nu=9` is a valid lower bound. Exhausting
the states with four signs of each kind and `D Delta_0!=0` proves

```text
4D^16 Delta_0^8<=10^24 2^(2nu),                    (12)
```

with equality at `(D,Delta_0,nu)=(10,10,1)`. This is `(MHN9)`. Equations
`(10)--(12)` imply

```text
p^3<=10^24/4<2^78,
```

contrary to `p>2^26`. Thus `h=4` is empty.

## 5. Width five and the complete level

For `h=5`, the two scales have `(N_0,N_1)=(32,16)`,
`(B_0,B_1)=(8,4)`, and `(r_0,r_1)=(1,1)`. The four subsets `S` in `(MHN8)`
are exact integer comparisons. Their worst positive margin occurs at
`S={0}` and is still positive; `verify.py` checks all four without floating
point. Hence `h=5` is empty already at `n=2^13`, and therefore at every
larger ambient order.

For `6<=h<16`, the exact ambient predicate from
`f3_hge4_ambient_norm_level_contraction` holds at the smallest ambient order;
the verifier checks both parity starts and all ten widths. The quarter-width
theorem deletes `16<=h<64/3`, and the complement-third theorem deletes
`3h>=64`. Together with the two endpoint arguments, every `4<=h<=32` is
empty. This proves `(MHN10)`. QED.
