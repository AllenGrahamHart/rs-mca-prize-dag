# L1 Mersenne-checkpoint cyclotomic normal form

- **status:** PROVED
- **role:** replace the nine surviving first-checkpoint Fourier closures by
  an exact residue-chamber formula
- **dependency:** `l1_official_broad_checkpoint_frobenius_periodicity_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

Let `N=p+1`, let `m=2^A` with `m in {4,8,16}`, assume `m|N`, and put
`n=mN`. Let `zeta` have order `n`. For a balanced signed exponent word

```text
B(T)=sum_(i in I) T^i-sum_(j in J) T^j in F_p[T]/(T^n-1),
|I|=|J|=p,
```

assume `B(zeta^a)=0` for `0<=a<=p-1=N-2`. Write each frequency uniquely as

```text
k=qN+b,       0<=q<m,       0<=b<N.                    (MCN1)
```

Then multiplication by `p=N-1` acts by

```text
(q,0) -> (-q,0),
(q,b) -> (b-q-1,N-b)                 (b>0),             (MCN2)
```

and its square sends `(q,b)` to `(q-2b,b)` modulo `m`.

Let `S` be the `p`-cyclotomic closure of `[0,p-1]`, and for `b>0` put
`g_b=gcd(2b,m)`. The closure is exactly

```text
(q,0) in S       iff q=0,
(q,b) in S       iff q=0 or q=b-1 (mod g_b),  b>0.     (MCN3)
```

Consequently the Fourier complement has size

```text
m=4:       2N+1,
m=8:       9N/2+1,
m=16:      37N/4+1.                                  (MCN4)
```

In particular all `N` consecutive frequencies `0,...,N-1` vanish. A
Vandermonde argument therefore gives

```text
|supp(B)|>=N+1.                                      (MCN5)
```

For a first-checkpoint pair the support has exact size `2p=2N-2`, so every
survivor lies in the explicit low-weight window

```text
N+1<=|supp(B)|=2N-2<2(N+1).                          (MCN6)
```

This is an exact normal form and a strict search compression. It does not
exclude the nine rows, prove a low-weight BCH classification, bound lower
split-value degrees, treat widths above `p`, or close L1.

The complete nonofficial analogue `(n,p,m)=(32,7,4)` has 16 two-fiber
pencils and no `h>=3` pencil; this is evidence only, recorded in
`experiments/prize_resolution/l1_mersenne_checkpoint_analog_result.md`.
