# Proof certificate

## 1. Router and extra symmetry

The triple-cubic router normalizes a selected triple to `{1,x,y}` and writes
`d` for the product of the complementary triple. Put

```text
u=1+x+y,   A=x+y+xy,   B=xy,   C=(uA-B-d)/u.
```

The paid official weight-three exclusion makes `u` nonzero. The complement
is the root multiset of

```text
Q(T)=T^3+uT^2+CT-d.
```

With `w_i=uz_i`, the division-free doubling recurrences produce two
cyclotomic integers

```text
F=S_1024-3u^1024,       G=T_1024-3u^2048.             (1)
```

An official guarded relation kills both after evaluating `zeta_1024` at the
selected exact-order element.

There is a symmetry not used by the original `1,514*1,024` upper bound.
Rechoose `x` as the normalized root of the same selected triple and rescale
all six roots by `x^-1`. In exponent coordinates this sends

```text
(a,b,c) -> (-a,b-a,c-3a) mod 1024,                    (2)
```

where `(x,y,d)=(zeta^a,zeta^b,zeta^c)`. Rechoosing `y` gives the analogous
third presentation. Since the selected pair is unordered, these are the
three presentations of the normalized selected triple. Under (2),

```text
u -> u/x,   z_i -> z_i/x,   w_i -> w_i/x^2.
```

As `x^1024=1`, both expressions in (1) are unchanged. Odd Galois dilation
conjugates (1), so it preserves their absolute norms. Exact orbit
canonicalization gives

```text
521,220 legal unordered pairs,
1,514 odd-dilation pair orbits,
1,550,336 pair-product presentations,
404,740 combined dilation/rebasing candidate orbits.
```

The sorted representative digest is
`677871a774e3463b5f74b8c63578f9e075637745355599d682d7f9e0312747f2`.

## 2. Exact recursive norm

Generic resultants were the computational bottleneck. For `n` a power of two,
write

```text
f(X)=f_0(X^2)+X f_1(X^2).
```

Pairing every root `alpha` of `X^n+1` with `-alpha` gives

```text
f(alpha)f(-alpha)=f_0(alpha^2)^2-alpha^2 f_1(alpha^2)^2.
```

The squares of those pairs run once through the roots of `Y^(n/2)+1`.
Therefore

```text
Res(X^n+1,f)
 = Res(Y^(n/2)+1, f_0(Y)^2-Y f_1(Y)^2).                (3)
```

Reducing the right-hand polynomial modulo `Y^(n/2)+1` and iterating (3)
computes the exact integer norm using nine polynomial squares. Six independent
order-1024 controls agree exactly with FLINT's generic resultant, with observed
speedups from `190x` to `574x`.

For each candidate the certificate computes `Norm(F)`, `Norm(G)`, and
`Norm(u)`. Every official supporting characteristic divides both first norms.
It cannot divide `Norm(u)`: an odd conjugate with `u=0` would be an official
reduced weight-three relation. Repeatedly removing the gcd with `Norm(u)` is
therefore sound. Write the resulting integer as `g_sat`.

## 3. Nonzero obstruction branch

The exhaustive run contains `3,163` contiguous fail-closed batches covering
all `404,740` candidates. Every batch records candidate and factorization
digests; there are no worker errors or omitted ranges. Exactly `404,230`
candidates have nonzero `g_sat`. Their complete PARI factorizations multiply
back to the exact integers. The union consists of `443` distinct primes, the
largest saturated gcd has `16,986` bits, and

```text
max_p v_2(p-1)=18.
```

A separate 626-node recursive Pocklington graph proves every factor root
prime. Thus an official `q` dividing a nonzero `g_sat` would have
`v_2(q-1)<=18`, contradicting the required valuation at least `41`.

## 4. Identically zero branch

For the other `510` candidates, both `F` and `G` are zero as cyclotomic
integers. The converse part of the router now applies over characteristic
zero: the three roots of `Q` belong to `mu_1024`. Together with `{1,x,y}` they
form a six-term multiset of `1024`th roots whose sum is zero.

We use the following elementary power-of-two lemma.

**Lemma.** Every zero sum of a finite multiset of `2^m`th roots with all
coefficients equal to `+1` can be partitioned into antipodal pairs.

**Proof.** Induct on `m`. Write the sum uniquely as
`A(zeta^2)+zeta B(zeta^2)`. Since
`[Q(zeta):Q(zeta^2)]=2`, both `A(zeta^2)` and `B(zeta^2)` vanish. Apply the
induction hypothesis separately to the even- and odd-exponent submultisets.
The base case is `1+(-1)=0`. Each resulting pair is antipodal in the original
group. QED.

Hence every identically zero candidate has a repeated root or an antipodal
pair in its reconstructed union. It fails the router's distinct,
disjoint, antipodal-free guard. This pays all `510` structural candidates.

The two branches exhaust the representative file, proving the official
`(ell,w)=(2,6)` slot empty.

Production runs:

```text
recursive norm benchmark: ap-rugUuPBaWFaB9i8HKUfCPu
candidate orbit census:    ap-Fm6rWTfcN3oOkKIbq6kI7s
factor pilot:              ap-5OmIPnPF2ymy9GFXQa63Xv
full 404,740-row sweep:    ap-Sjm8psGJdvH8dchUcA5aUI
Pocklington graph:         ap-2igTaGtpVH5Ly9WimHRk6O
```
