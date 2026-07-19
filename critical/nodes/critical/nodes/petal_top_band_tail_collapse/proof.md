# Proof

The strict retained-remainder bound and the top-band pin give

```text
ell+d-r
  >= ell+ell(m-2)-(ell-1)
   = ell(m-2)+1.
```

Therefore

```text
ceil((ell+d-r)/ell) >= m-1.
```

The only possible touched-set sizes in the exact tail are `m-1` and `m`
(or none, if the lower endpoint exceeds `m`). Thus

```text
tail <= C(m,m-1)+C(m,m)=m+1.
```

The `m` petals, the core of size `k-1`, and the retained set are pairwise
disjoint subsets of the length-`n` domain, so

```text
m ell+(k-1)+r <= n.
```

Since `ell>=1`, `r>=0`, and official `k>=2`, this implies
`m<=n-k+1<=n-1`, hence `m+1<=n`. Combining this arithmetic with the proved
full-petal touched-set injection gives the complete-list bound `n`. The
primitive filter only decreases the count, proving K4 with `b4=1`.
