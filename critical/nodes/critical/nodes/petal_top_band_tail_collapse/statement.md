# Top-band full-petal tail collapse

- **status:** PROVED
- **consumer:** `petal_k4_primitive_bound`

Let a full-petal sunflower chart have petal size `ell>=1`, petal count `m>=2`,
missed degree `d`, and canonical retained remainder size `0<=r<ell`. If the
pinned top-band inequality

```text
d >= ell(m-2)
```

holds, then the exact touched-set tail from
`petal_full_touched_set_injection` satisfies

```text
sum_(t=ceil((ell+d-r)/ell))^m C(m,t) <= m+1.
```

If the chart lives in a length-`n` official row with core size `k-1` and
`k>=2`, then `m+1<=n`. Hence every such complete full-petal chart list, and
therefore its stabilizer-primitive part, has size at most `n`; K4 holds with
the printed exponent `b4=1`.
