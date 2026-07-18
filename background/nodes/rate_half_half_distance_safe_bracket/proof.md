# Proof

An `RS[F,D,k]` code has minimum weight `n-k+1`. At `r=(n-k)/2`,

```text
2r=n-k=w_min-1.
```

The proved MCA-from-CA half-distance theorem therefore gives

```text
epsilon_mca(C,r/n)<=max(epsilon_ca(C,r/n),r/q).
```

The published unique-decoding proximity-gap theorem, as imported and scoped
in `mca_from_ca_reduction`, gives `epsilon_ca(C,r/n)<=n/q`. Since `r<=n`,

```text
epsilon_mca(C,1/4)<=n/q.
```

Equivalently `B_mca(3n/4)<=n`. For `q>=2^169`,

```text
floor(q/2^128)>=2^41=n,
```

which proves `(HD1)`. The lower endpoint of `(HD2)` is the proved maximal
residual-prefix simple-pole floor. QED.
