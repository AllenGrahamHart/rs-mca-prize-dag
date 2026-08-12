# Proof

The source contract pins the strict upstream manifest, schema, and four
verifier implementations at exact `#1159` head `e603e0ced`.  A fresh local
replay at that head reports

```text
PASS ... d1=67473 ... actual_owner=not-established actual_record=1
PASS tamper-selftest: 62 semantic and 3 parser mutations rejected
```

Here is an independent reconstruction of the load-bearing mathematics.

The recorded Pocklington witnesses prove the base modulus prime.  Rabin's
test proves `X^6+X+6` irreducible over the base field, so `alpha` has degree
six and cannot equal any carrier point.  Exact modular powers prove that
`zeta` has order `n=2^21`.

The exponent intervals defining `E` and `S` are disjoint because

```text
67473+1116048=1183521<2097152.
```

For every carrier point, direct cancellation gives

```text
u+alpha v = 1_E.
```

This word is zero on `S`, so `(alpha,S,0)` is an explanation with degree
below `k`.

If a polynomial `g` of degree below `k` agreed with `v` on `S`, then

```text
(X-alpha)g(X)+1
```

would have `m` roots and degree at most `k<m`, impossible.  The same proof
holds for degree below `k+1`, since `k+1<m`.  Thus the pair is not
simultaneously explained on the identical support.

Let `W_S` be the monic locator of `D\S` and put `N=0`.  Its degree is
`n-m=981104`; `(W_S,0)` lies in the slope-word lattice because the word is
zero on `S` and `W_S` is zero off `S`.  Its quotient is zero, so the guarded
adapter reconstructs the actual explanation without the extra degree-`k`
coefficient.

Finally, `(Lambda_E,0)` gives shifted degree `e=67473` under both shifts.
If a nonzero `(W,N)` had shifted degree at most `e-1`, then `N` would vanish
on all `n-e=2029679` points outside `E`, while its degree would be at most
`1116047` under `K=k` or `1116048` under `K=k+1`.  Hence `N=0`.  On `E`, the
lattice identity would then make `W` vanish at `e` points despite degree at
most `e-1`, so `W=0`, a contradiction.  The minimum is therefore exactly
`e` under both shifts.  Substitution of `m-k=67472` and
`m-(k+1)=67471` gives the two numerical profile labels.  No owner conclusion
is used.  QED.
