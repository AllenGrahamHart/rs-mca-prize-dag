# Refutation of the former fixed `(RH-SAFE)` claim

The former claim was

```text
epsilon_mca(C,1-(k+8,592,912,738+1)/n)<=2^-128.
```

It is refuted algebraically. In the proved cyclic rotated-prefix construction,
take

```text
c=2^22, d=2048, s=c-1.
```

The construction has the same pigeonhole list size for every `s<c`, so this
choice supplies the proved list at excess

```text
dc+s=8,594,128,895.
```

The proved quantitative simple-pole conversion gives MCA error greater than
`2^-83` at this excess and at every smaller positive excess. Since

```text
8,592,912,738+1 < 8,594,128,895,
```

the proposed point is unsafe, uniformly over the entire admissible field
range. No computation or unproved hypothesis enters the refutation.
