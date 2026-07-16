# PMA official-rate small-source degree sieve

- **status:** PROVED
- **role:** exact removal of impossible low-rate full-petal source scales
- **consumer:** `petal_mixed_amplification`, hence `imgfib`

## Statement

Let an official Reed-Solomon row have

```text
n=rk,       r in {2,4,8,16}.
```

Let a maximal sunflower source have a core of size `k-1`, petal size `ell`,
`M` full petals, and background size `b<ell`. Thus

```text
(r-1)k+1=n-k+1=Mell+b,       0<=b<ell.       (SRC)
```

Every exact core defect has size `d<=k-1`.

### 1. General source-scale sieve

If

```text
M<=r-2,
```

then

```text
ell>=k+1>d.
```

Consequently no strict full-petal branch with `d>ell` exists on those source
scales. In particular:

```text
rate 1/8:   M<=6 is empty in the strict branch,
rate 1/16:  M<=14 is empty in the strict branch.
```

The already-proved bounded root-excess ledger pays every remaining
`d<=ell` contribution on these scales.

### 2. Sharp rate-quarter `M=4,t=3` threshold

At rate `1/4` and `M=4`, equation (SRC) is

```text
3k+1=4ell+b.
```

For a three-touched-petal strict-strip contributor, write `d=ell+s`. The
upper mu-basis branch `s>=ell/2` is arithmetically possible exactly when

```text
2b>=ell+8.                                      (BG)
```

If `2b<ell+8`, every `M=4,t=3` contributor lies in the one-projective-point
lower mu-basis branch. For one carried source there are at most four touched
triples and at most `k` defect degrees, hence at most

```text
4k
```

such contributors. This is a uniform polynomial payment.

### 3. Remaining `M=4` scope

After this sieve and the three-petal mu-basis reduction:

- rates `1/8` and `1/16` have no strict `M=4` full-petal residual;
- rate `1/4`, `M=4,t=3` remains only in the upper branch with
  `2b>=ell+8`;
- rate `1/2`, `M=4,t=3` retains its upper mu-basis split-core-divisor count;
- `M=4,t=2` remains only at rates `1/2` and `1/4`;
- larger `M` and partial-petal branches are unchanged.

This sieve does not count either surviving upper branch and does not promote
`petal_mixed_amplification`.
