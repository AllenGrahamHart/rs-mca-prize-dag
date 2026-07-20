# HGE4 primitive swap odd-moment router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_primitive_shift_pair_near_square_union_router`

Fix an official row and a valid primitive near-square union of width `h` whose
nontrivial union stabilizer exchanges the reconstructed supports. Then:

1. `h` is odd;
2. the two supports are `P` and `-P`, with `P cap (-P)=empty`;
3. if `L_P(X)=sum_(j=0)^h (-1)^j e_j(P)X^(h-j)`, then

   ```text
   e_j(P)=0                 for every odd j<h;       (SOM1)
   ```

4. equivalently, since the official characteristic exceeds `h`,

   ```text
   sum_(x in P)x^j=0        for every odd j<h.       (SOM2)
   ```

The centered polynomial is odd and has zero constant term:

```text
L_P(X)=S(X)-e_h(P),       L_(-P)(X)=S(X)+e_h(P).
```

Conversely, any antipodal-free `h`-subset `P` with odd `h`, trivial common
scaling stabilizer for `(P,-P)`, and `(SOM1)` or `(SOM2)` gives a primitive
top shift pair with swap-stabilized union.

Let `A_h^swap` count anchored valid primitive unions in the swap class. Then

```text
A_h^swap=V_h^swap=0                         if h is even,
A_h^swap=h V_h^swap
          <=binom(n/2-1,h-1)                if h is odd.       (SOM3)
```

For odd `h`, the remaining generator chooses `h` of the `n/2` antipodal
pairs and seeks one sign vector, modulo global sign, in the odd Vandermonde
kernel

```text
sum_i epsilon_i r_i^(2m+1)=0,       0<=m<=(h-3)/2. (SOM4)
```

This removes the swap branch from every even width and removes every
`h|h` partition search from the odd swap branch. It does not bound the free
union class, prove the odd signed-moment fiber count, or close HGE4.
