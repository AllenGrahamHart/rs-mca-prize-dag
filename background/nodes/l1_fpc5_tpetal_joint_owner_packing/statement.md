# General t-petal fixed joint-owner packing

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Fix one nonempty full-petal cell surviving `(PF6)` and one exact anchor. Use

```text
N=|C|,       b=|Bkg|,       r=2d-t ell=e-1,
u=d-(t-1)ell,       v=max(0,u).                       (JP1)
```

Every exact candidate has a degree-`d` defect set in `C` and at least `v`
background roots in `Bkg`. For a distinct candidate with coordinate `H`,
let

```text
Q=gcd(H,F L_(R_0)),       q=deg Q.                    (JP2)
```

Fix one exact monic owner `Q`, and let `F_Q` be all distinct exact
candidates with owner `(JP2)`. Then `0<=q<=r`, and

```text
|F_Q| <= floor(
  binom(N+b-q,r-q+1) / binom(d+v-q,r-q+1)
).                                                    (JP3)
```

In particular, if `q=r-c`, then

```text
|F_Q|<=n^(c+1).                                       (JP4)
```

Thus every fixed joint-owner chamber of bounded co-deficiency `c` has a
uniform polynomial payment. At the top owner `q=r`, the sharper bound is

```text
|F_Q|<=floor((N+b-r)/(d+v-r)),                        (JP5)
```

where

```text
d+v-r = ell       if u>=0,
d+v-r = t ell-d  if u<0.                              (JP6)
```

The second denominator is at least `ell-b>=1` by the list threshold.

## Scope

This is a payment for one fixed exact joint owner. It does not bound the
number of realized divisors `Q`, sum owner chambers, provide first-owner
chronology, or pay the complete source cell. Summing `(JP3)` over all
divisors of the anchor owner polynomial can still be exponential.
