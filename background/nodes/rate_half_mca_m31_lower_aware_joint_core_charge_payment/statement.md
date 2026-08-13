# Mersenne lower-aware joint-core charge payment

- **status:** PROVED
- **scope:** Mersenne-31 full-lift supports `e=130220,130221`
- **adjacent route wall:** `e=130222`

Let `r` distinct parameterized affine explanation lines have actual total
core sizes `g_i` and certified lower bounds `ell_i<=g_i`.  Put

```text
S_r=min(r(m-1),e+C(r+1,2)c),
f(g)=(N-g)/(m-g),
```

where `m=D+K` and `c=K-1`.  Sort the lower bounds decreasingly and spend the
available excess `S_r-sum ell_i` by filling the first coordinate to `m-1`,
then the second, and so on.  If the resulting vector is `x`, then

```text
sum_i f(g_i) <= sum_i f(x_i).
```

Thus the floor of the right side is a valid joint charge for all previously
peeled lines.  Substituting it into the exact line-bank recursion proves

```text
epsilon_mca(C,e/N) <= 2^-24
```

for `e=130220,130221` in the integer budget normalization used by the parent
Mersenne route.  Both rows terminate after 38 forced lines by pairwise
inside-core packing.  The same compiler reaches only a residual-base wall at
`e=130222`; no unsafe conclusion is claimed there.
