# Proof - PMA official-rate small-source degree sieve

## 1. The source equation

The source consists of a `(k-1)`-point core, `M` disjoint `ell`-point petals,
and `b` background points. Therefore

```text
n=(k-1)+Mell+b
```

and, since `n=rk`,

```text
(r-1)k+1=Mell+b.                                  (1)
```

Exact core defects are subsets of the core, so

```text
d<=k-1.                                           (2)
```

## 2. Small source scales

If `M<=r-2`, then `b<ell` and (1) give

```text
(r-1)k+1=Mell+b<(M+1)ell<=(r-1)ell.
```

Thus `ell>k+1/(r-1)`, and integrality gives `ell>=k+1`. Combining with (2)
yields `d<ell`. Hence no strict `d>ell` branch exists.

For `r=8`, this covers `M<=6`; for `r=16`, it covers `M<=14`. The residual
root-excess parameter is bounded when `d<=ell`, so these cases are already in
the proved petal-pattern payment.

## 3. The rate-quarter boundary

Now take `r=4` and `M=4`. Equation (1) becomes

```text
3k+1=4ell+b.                                      (3)
```

The upper three-petal mu-basis branch begins at

```text
s>=ell/2,
```

or equivalently at an integer defect satisfying

```text
2d>=3ell.                                         (4)
```

Such a defect is compatible with `d<=k-1` exactly when

```text
3ell<=2(k-1).                                     (5)
```

Substituting `k=(4ell+b-1)/3` from (3), condition (5) becomes

```text
9ell<=8ell+2b-8,
```

which is precisely `2b>=ell+8`. This proves the equivalence (BG), including
its endpoint.

If (BG) fails, the mu-basis theorem gives at most one projective contributor
for each exact defect and touched-petal triple. Monicity of the defect locator
fixes its scalar. There are `binom(4,3)=4` touched triples and fewer than `k`
possible nonzero defect sizes, so `4k` is a valid uniform bound.

## 4. Official-row consequences

At rates `1/8` and `1/16`, `M=4` lies in the general empty range. At rate
`1/4`, only the large-background upper branch from (BG) survives for `t=3`;
the two-touched branch is not covered by the three-petal theorem. Rate `1/2`
has `r-2=0`, so the general source-scale sieve removes no positive `M` and its
upper branch remains. No statement here concerns partial petals or larger
source scales.
