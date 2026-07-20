# Proof - L1 polarized petal-entropy ledger

Extend the exact support-size vector to all `M` petals by putting `a_i=0`
on untouched petals. Put

```text
s_i=min(a_i,ell-a_i),       p=sum_i s_i.
```

For a fixed vector `(s_i)`, every `a_i` has at most two possible
orientations, sparse `a_i=s_i` or dense `a_i=ell-s_i`. This harmlessly
overcounts the midpoint and also distinguishes an untouched petal from a full
petal when `s_i=0`. The number of nonnegative vectors `(s_i)` with
`sum_i s_i<=E` is `binom(M+E,E)`. Hence there are at most

```text
2^M binom(M+E,E)                                       (1)
```

support-size profiles with `p<=E`.

For one such profile, the number of exact petal support patterns is

```text
product_i binom(ell,a_i)
 = product_i binom(ell,s_i)
 <= ell^p.                                             (2)
```

Fix one exact pattern and a defect `d`. The fixed-pattern part of
`pma_petal_pattern_root_pinning_ledger` bounds the compatible monic split
locators, and hence listed words, by

```text
binom(k-1,e) <= (k-1)^e.                               (3)
```

There are at most `k<=n` possible defects. On `(PE2)`, equations (2) and (3)
give

```text
ell^p (k-1)^e <= n^(p+e) <= n^E.                       (4)
```

Multiplying (1), (4), and the defect count proves `(PE3)`.

Finally, maximality gives

```text
M=floor((n-k+1)/ell) <= n/ell <= log_2(n)/C_0,
```

so `2^M<=n^(1/C_0)`. With fixed `E`, the factor `binom(M+E,E)` is
polylogarithmic and therefore polynomial. This proves the lower-cutoff
claim.
