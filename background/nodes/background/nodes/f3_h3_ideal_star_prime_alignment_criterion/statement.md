# H3 ideal-star prime-alignment criterion

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependency:** `f3_h3_low_distance_ideal_star_router`

Use the normalized rooted ideal star `K_(E;F,G)` and admissibility conditions
from the ideal-star router. Let `p=1 mod n` be prime and fix any one element
`g in F_p` of exact order `n`. For a fixed rooted star,

```text
p divides N(K_(E;F,G))

iff there is an odd r mod n such that

beta_E(g^r)=beta_F(g^r)=beta_G(g^r).                (PAC1)
```

Equivalently, for the complete candidate union `D_n`, one fixed primitive
root is enough:

```text
p in D_n

iff there is an admissible rooted star (E;F,G) with

beta_E(g)=beta_F(g)=beta_G(g).                      (PAC2)
```

Thus candidate-prime screening does not require explicit ideal normal forms,
enumeration of every degree-one prime above `p`, or raw rooted-star
materialization. Group the admissible shifted products by their value at one
fixed `g` and test whether a fiber contains a center with two allowed leaves.

This criterion assumes that a complete relevant-prime list has already been
produced. It does not generate or factor that list and does not close C36'.
