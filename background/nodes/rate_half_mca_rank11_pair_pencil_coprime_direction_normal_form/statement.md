# Pair-pencil coprime-direction normal form

- **status:** PROVED
- **scope:** the rank-at-most-two output of the quadratic quotient endgame

Choose distinct quotient pair types `p_0,p_1`. There are fixed coprime
polynomials `U,V` and a distinct scalar polynomial `R_p` for every quotient
type such that

```text
(a_p,b_p)=(a_0,b_0)+R_p(U,V),                        (NF1)
R_(p_0)=0.
```

The `R_p` lie in one `F`-linear polynomial space of dimension at most four.
If

```text
d=max(deg U,deg V),
```

with the zero component ignored, then

```text
deg R_p<=K-1-d.                                      (NF2)
```

For every two distinct types,

```text
H_p intersection H_q subset Z_D(R_p-R_q),
|Z_D(R_p-R_q)|>=2(m-2)-n=134940.                    (NF3)
```

Consequently `d<=913635`. Thus the open branch is exactly a family of at
least 520 points in a base-field vector space of dimension at most four,
whose every listed difference has at least 134940 distinct official-domain
roots. This node does not perform the required rank-one support or
split-pencil census.

## Falsifier

A rank-two pair family not admitting `(NF1)` over `F[X]`; scalar dimension
above four; a core-intersection point outside the corresponding
scalar-difference roots; or failure of the degree and root floors.
