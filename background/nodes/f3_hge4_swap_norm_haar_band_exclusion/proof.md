# Proof

Let `P` be the `h`-point reciprocal root support on one side of a primitive
antipodal-swap pair. The proved swap router gives

```text
P cap (-P)=empty,
sum_(x in P)x^j=0       for j=1,3,...,h-2.           (1)
```

Choose `omega in F_p` of order `m`, label `P` by an exponent set `I`, and put

```text
z=sum_(i in I) zeta_m^i in Z[zeta_m].               (2)
```

This cyclotomic integer is nonzero. If it vanished, all its odd Galois
conjugates would vanish. Odd Fourier inversion would then make the indicator
of `I` invariant under translation by `m/2`, contrary to
`P cap (-P)=empty` and `h>0`.

There are `(h-1)/2` odd exponents in `(1)`. Since `p=1 mod m`, their
congruences place `(h-1)/2` distinct primes above `p` in `(z)`. Hence

```text
p^((h-1)/2)<=|Norm_Q(zeta_m)/Q(z)|.                 (3)
```

For `0<=t<m/2`, let `a_t` be the indicator of `I` and put
`g_t=a_t-a_(t+m/2)`. Antipodal freeness gives

```text
sum_t g_t^2=h.                                      (4)
```

The odd conjugates of `z` are the length-`m/2` Fourier transform of
`(g_t zeta_m^t)`. Parseval and AM--GM therefore give the exact norm ceiling

```text
|Norm(z)|<=h^(m/4).                                 (5)
```

The compatible prime is strictly greater than the composite integer `m^2`.
Equations `(3)--(5)` imply

```text
m^(h-1)<h^(m/4),
```

which is `(SNH1)` and proves `(SNH2)`.

Now retain odd `h` and write `m=2^s`, `a=m/4`, and `h=a-d`. Since `h<=a`,

```text
h^a<=a^a=(m/4)^a=m^a/4^a.                          (6)
```

Condition `(SNH3)` is exactly

```text
m^(d+1)=2^(s(d+1))<=2^(m/2)=4^a.                   (7)
```

Combining `(6)--(7)` gives

```text
m^(h-1)=m^(a-d-1)>=m^a/4^a>=h^a,
```

so `(SNH2)` excludes every odd swap pair in the band. The swap dependency
already excludes even widths, hence the whole swap class is empty there.
Integer `d>=1` converts `(SNH3)` to `(SNH4)`.

Finally, `(SNH5)`, `B>=X`, and its strict upper inequality give

```text
X^2<=BX<m,
d+1<sqrt(m)/(4 log m)=sqrt(m)/(4s log 2)<m/(2s)
```

for `m>=16`. Thus the full Haar band lies inside the swap-exclusion band.
The Haar dependency routes every primitive pair there to the swap class, and
the theorem just proved makes that class empty. This is `(SNH6)`. QED.
