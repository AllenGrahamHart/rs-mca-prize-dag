# H3 line-star moment identity

- **status:** see `dag.json` (single source of truth)

Let `A=(1-H)\{0}` and, for `m in F_p^*`, put

```text
C_m={a in A:ma in A}.
```

Then `|C_m|=R(m)`. If

```text
Q(t)=P(t)(P(t)-2)+D(t),
```

the exact non-swap product-collision multiplicity, then

```text
Q(t)=#{(m,a,a'):
        m!=1, a!=a', a,a' in C_m, m*a*a'=t}.       (LS1)
```

Consequently the critical sufficient moment has the exact line-star form

```text
S_ns=sum_(m!=1) sum_(a!=a' in C_m, m*a*a'!=1) R(m*a*a').  (LS2)
```

Thus the missing estimate is a directed correlation between a populated
source line and the population of the slope emitted by each ordered chord.
It is not a marginal product-energy or quotient-energy estimate.

