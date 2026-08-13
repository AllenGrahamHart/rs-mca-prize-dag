# Support-local transversality compiler

- **status:** PROVED
- **source:** upstream PR #1166 at `af0e7c63b`
- **scope:** one supplied same-support pair-noncontained MCA family

Let `C=RS[F,D,K]`, `|D|=n`, `m=K+w`, `w>0`. Suppose selected
explanations lie in an affine space `c_0+C'` of dimension `s`, where
`1<=s<=K`. For every selected slope `gamma`, retain an exact `m`-set
`S_gamma` and same-support pair noncontainment. Define

```text
theta_0 = min_(gamma,b in C')
          |{x in S_gamma : r_1(x) != b(x)}|,
theta   = min(theta_0,w+1).
```

Then `theta>=1` and

```text
|Z| <= floor(max{
  n_fall_(s+1)/(m theta (w+1)_rise_(s-1)),
  (n-K+s)_fall_(s+1)/(theta (w+1)_rise_s)
}).                                                     (ST1)
```

For a complete shortened KoalaBear row

```text
(n,K,m)=(R+s,s,d+s),  (R,d)=(1048576,67472),
```

the automatic margin `theta>=1` pays full explanation rank through `s=9`.
At `s=10,11,12,13`, the least paying margins are respectively

```text
4, 49, 757, 11748.
```

Thus an over-budget family at those ranks emits an actual selected support
with at most `3,48,756,11747` direction exceptions. Rank `s>=14` remains
unpaid by this compiler.

## Nonclaims

This theorem does not select a v4 owner, move a deployed ledger atom, or
sum bounds over different record-local cores. Its `theta` is recomputed
after every gauge or shortening; it is not inherited from another
presentation.
