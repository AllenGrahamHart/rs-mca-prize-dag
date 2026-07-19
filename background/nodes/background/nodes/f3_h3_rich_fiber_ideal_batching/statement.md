# C36' same-fiber cyclotomic ideal batching

- **status:** PROVED
- **consumer:** `f3_h3_mobius_excess_half`
- **dependency:** `f3_h3_shifted_product_sidon`

Let `n=2^s` with `s>=2`, let `zeta=zeta_n`, and put

```text
K=Q(zeta),       O=Z[zeta],       pi=1-zeta.
```

Let `p=1 mod n` be an odd prime, let `g in F_p` have order `n`, and let

```text
P=(p,zeta-g)
```

be the selected degree-one prime ideal of `O`. Take distinct unordered pairs
`E_i={a_i,b_i}`, `0<=i<=r`, of nonzero exponents modulo `n` whose shifted
products all have the same reduction modulo `P`. Write

```text
beta_i=(1-zeta^a_i)(1-zeta^b_i),
alpha_i=beta_i-beta_0,                 1<=i<=r,
J=(alpha_1,...,alpha_r) subset O.
```

Then every `alpha_i` is nonzero and

```text
0 != J subset (pi)^2 P,
4p divides N(J),
N(J) divides gcd_i |Norm_K/Q(alpha_i)|.                 (IB)
```

Here `N(J)=|O/J|` is the absolute ideal norm. In particular, if two of the
principal norms have gcd exactly `4p`, then those two obstructions generate
the minimal possible same-fiber ideal:

```text
(alpha_i,alpha_j)=(pi)^2 P.                           (SAT)
```

This theorem batches same-fiber collisions at the level of ideals. It gives
no uniform upper bound for the number or quotient weight of rich fibers and
does not prove the open C36' estimate.
